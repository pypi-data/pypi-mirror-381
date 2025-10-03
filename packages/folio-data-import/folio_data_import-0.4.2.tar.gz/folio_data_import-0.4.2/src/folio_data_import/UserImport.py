import asyncio
import datetime
import json
import logging
import sys
import time
import uuid
from datetime import datetime as dt
from enum import Enum
from pathlib import Path
from typing import List, Tuple

import aiofiles
import folioclient
import httpx
import typer
from aiofiles.threadpool.text import AsyncTextIOWrapper
from rich.logging import RichHandler
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from typing_extensions import Annotated

from folio_data_import._progress import ItemsPerSecondColumn, UserStatsColumn

try:
    utc = datetime.UTC
except AttributeError:
    import zoneinfo

    utc = zoneinfo.ZoneInfo("UTC")

logger = logging.getLogger(__name__)

# Mapping of preferred contact type IDs to their corresponding values
PREFERRED_CONTACT_TYPES_MAP = {
    "001": "mail",
    "002": "email",
    "003": "text",
    "004": "phone",
    "005": "mobile",
}


class PreferredContactType(Enum):
    MAIL = "001"
    EMAIL = "002"
    TEXT = "003"
    PHONE = "004"
    MOBILE = "005"
    _001 = "mail"
    _002 = "email"
    _003 = "text"
    _004 = "phone"
    _005 = "mobile"


class UserMatchKeys(Enum):
    USERNAME = "username"
    EMAIL = "email"
    EXTERNAL_SYSTEM_ID = "externalSystemId"


class UserImporter:  # noqa: R0902
    """
    Class to import mod-user-import compatible user objects
    (eg. from folio_migration_tools UserTransformer task)
    from a JSON-lines file into FOLIO
    """

    logfile: AsyncTextIOWrapper
    errorfile: AsyncTextIOWrapper
    http_client: httpx.AsyncClient

    def __init__(
        self,
        folio_client: folioclient.FolioClient,
        library_name: str,
        batch_size: int,
        limit_simultaneous_requests: asyncio.Semaphore,
        user_file_path: Path = None,
        user_match_key: str = "externalSystemId",
        only_update_present_fields: bool = False,
        default_preferred_contact_type: str = "002",
        fields_to_protect: List[str] = [],
        no_progress: bool = False,
    ) -> None:
        self.limit_simultaneous_requests = limit_simultaneous_requests
        self.batch_size = batch_size
        self.folio_client: folioclient.FolioClient = folio_client
        self.library_name: str = library_name
        self.user_file_path: Path = user_file_path
        self.patron_group_map: dict = self.build_ref_data_id_map(
            self.folio_client, "/groups", "usergroups", "group"
        )
        self.address_type_map: dict = self.build_ref_data_id_map(
            self.folio_client, "/addresstypes", "addressTypes", "addressType"
        )
        self.department_map: dict = self.build_ref_data_id_map(
            self.folio_client, "/departments", "departments", "name"
        )
        self.service_point_map: dict = self.build_ref_data_id_map(
            self.folio_client, "/service-points", "servicepoints", "code"
        )
        self.only_update_present_fields: bool = only_update_present_fields
        self.default_preferred_contact_type: str = default_preferred_contact_type
        self.match_key = user_match_key
        self.lock: asyncio.Lock = asyncio.Lock()
        self.logs: dict = {"created": 0, "updated": 0, "failed": 0}
        self.fields_to_protect = set(fields_to_protect)
        self.no_progress = no_progress

    @staticmethod
    def build_ref_data_id_map(
        folio_client: folioclient.FolioClient, endpoint: str, key: str, name: str
    ) -> dict:
        """
        Builds a map of reference data IDs.

        Args:
            folio_client (folioclient.FolioClient): A FolioClient object.
            endpoint (str): The endpoint to retrieve the reference data from.
            key (str): The key to use as the map key.

        Returns:
            dict: A dictionary mapping reference data keys to their corresponding IDs.
        """
        return {x[name]: x["id"] for x in folio_client.folio_get_all(endpoint, key)}

    @staticmethod
    def validate_uuid(uuid_string: str) -> bool:
        """
        Validate a UUID string.

        Args:
            uuid_string (str): The UUID string to validate.

        Returns:
            bool: True if the UUID is valid, otherwise False.
        """
        try:
            uuid.UUID(uuid_string)
            return True
        except ValueError:
            return False

    async def setup(self, error_file_path: Path) -> None:
        """
        Sets up the importer by initializing necessary resources.

        Args:
            log_file_path (Path): The path to the log file.
            error_file_path (Path): The path to the error file.
        """
        self.errorfile = await aiofiles.open(error_file_path, "w", encoding="utf-8")

    async def close(self) -> None:
        """
        Closes the importer by releasing any resources.

        """
        await self.errorfile.close()

    async def do_import(self) -> None:
        """
        Main method to import users.

        This method triggers the process of importing users by calling the `process_file` method.
        """
        async with httpx.AsyncClient() as client:
            self.http_client = client
            if self.user_file_path:
                with open(self.user_file_path, "r", encoding="utf-8") as openfile:
                    await self.process_file(openfile)
            else:
                raise FileNotFoundError("No user objects file provided")

    async def get_existing_user(self, user_obj) -> dict:
        """
        Retrieves an existing user from FOLIO based on the provided user object.

        Args:
            user_obj: The user object containing the information to match against existing users.

        Returns:
            The existing user object if found, otherwise an empty dictionary.
        """
        match_key = "id" if ("id" in user_obj) else self.match_key
        try:
            existing_user = await self.http_client.get(
                self.folio_client.gateway_url + "/users",
                headers=self.folio_client.okapi_headers,
                params={"query": f"{match_key}=={user_obj[match_key]}"},
            )
            existing_user.raise_for_status()
            existing_user = existing_user.json().get("users", [])
            existing_user = existing_user[0] if existing_user else {}
        except httpx.HTTPError:
            existing_user = {}
        return existing_user

    async def get_existing_rp(self, user_obj, existing_user) -> dict:
        """
        Retrieves the existing request preferences for a given user.

        Args:
            user_obj (dict): The user object.
            existing_user (dict): The existing user object.

        Returns:
            dict: The existing request preferences for the user.
        """
        try:
            existing_rp = await self.http_client.get(
                self.folio_client.gateway_url
                + "/request-preference-storage/request-preference",
                headers=self.folio_client.okapi_headers,
                params={
                    "query": f"userId=={existing_user.get('id', user_obj.get('id', ''))}"
                },
            )
            existing_rp.raise_for_status()
            existing_rp = existing_rp.json().get("requestPreferences", [])
            existing_rp = existing_rp[0] if existing_rp else {}
        except httpx.HTTPError:
            existing_rp = {}
        return existing_rp

    async def get_existing_pu(self, user_obj, existing_user) -> dict:
        """
        Retrieves the existing permission user for a given user.

        Args:
            user_obj (dict): The user object.
            existing_user (dict): The existing user object.

        Returns:
            dict: The existing permission user object.
        """
        try:
            existing_pu = await self.http_client.get(
                self.folio_client.gateway_url + "/perms/users",
                headers=self.folio_client.okapi_headers,
                params={
                    "query": f"userId=={existing_user.get('id', user_obj.get('id', ''))}"
                },
            )
            existing_pu.raise_for_status()
            existing_pu = existing_pu.json().get("permissionUsers", [])
            existing_pu = existing_pu[0] if existing_pu else {}
        except httpx.HTTPError:
            existing_pu = {}
        return existing_pu

    async def map_address_types(self, user_obj, line_number) -> None:
        """
        Maps address type names in the user object to the corresponding ID in the address_type_map.

        Args:
            user_obj (dict): The user object containing personal information.
            address_type_map (dict): A dictionary mapping address type names to their ID values.

        Returns:
            None

        Raises:
            KeyError: If an address type name in the user object is not found in address_type_map.

        """
        if "personal" in user_obj:
            addresses = user_obj["personal"].pop("addresses", [])
            mapped_addresses = []
            for address in addresses:
                try:
                    if (
                        self.validate_uuid(address["addressTypeId"])
                        and address["addressTypeId"] in self.address_type_map.values()
                    ):
                        logger.debug(
                            f"Row {line_number}: Address type {address['addressTypeId']} is a UUID, "
                            f"skipping mapping\n"
                        )
                        mapped_addresses.append(address)
                    else:
                        address["addressTypeId"] = self.address_type_map[
                            address["addressTypeId"]
                        ]
                        mapped_addresses.append(address)
                except KeyError:
                    if address["addressTypeId"] not in self.address_type_map.values():
                        logger.error(
                            f"Row {line_number}: Address type {address['addressTypeId']} not found"
                            f", removing address\n"
                        )
            if mapped_addresses:
                user_obj["personal"]["addresses"] = mapped_addresses

    async def map_patron_groups(self, user_obj, line_number) -> None:
        """
        Maps the patron group of a user object using the provided patron group map.

        Args:
            user_obj (dict): The user object to update.
            patron_group_map (dict): A dictionary mapping patron group names.

        Returns:
            None
        """
        try:
            if (
                self.validate_uuid(user_obj["patronGroup"])
                and user_obj["patronGroup"] in self.patron_group_map.values()
            ):
                logger.debug(
                    f"Row {line_number}: Patron group {user_obj['patronGroup']} is a UUID, "
                    f"skipping mapping\n"
                )
            else:
                user_obj["patronGroup"] = self.patron_group_map[user_obj["patronGroup"]]
        except KeyError:
            if user_obj["patronGroup"] not in self.patron_group_map.values():
                logger.error(
                    f"Row {line_number}: Patron group {user_obj['patronGroup']} not found in, "
                    f"removing patron group\n"
                )
                del user_obj["patronGroup"]

    async def map_departments(self, user_obj, line_number) -> None:
        """
        Maps the departments of a user object using the provided department map.

        Args:
            user_obj (dict): The user object to update.
            department_map (dict): A dictionary mapping department names.

        Returns:
            None
        """
        mapped_departments = []
        for department in user_obj.pop("departments", []):
            try:
                if (
                    self.validate_uuid(department)
                    and department in self.department_map.values()
                ):
                    logger.debug(
                        f"Row {line_number}: Department {department} is a UUID, skipping mapping\n"
                    )
                    mapped_departments.append(department)
                else:
                    mapped_departments.append(self.department_map[department])
            except KeyError:
                logger.error(
                    f'Row {line_number}: Department "{department}" not found, '  # noqa: B907
                    f"excluding department from user\n"
                )
        if mapped_departments:
            user_obj["departments"] = mapped_departments

    async def update_existing_user(
        self, user_obj, existing_user, protected_fields
    ) -> Tuple[dict, dict]:
        """
        Updates an existing user with the provided user object.

        Args:
            user_obj (dict): The user object containing the updated user information.
            existing_user (dict): The existing user object to be updated.
            protected_fields (dict): A dictionary containing the protected fields and their values.

        Returns:
            tuple: A tuple containing the updated existing user object and the API response.

        Raises:
            None

        """

        await self.set_preferred_contact_type(user_obj, existing_user)
        preferred_contact_type = {
            "preferredContactTypeId": existing_user.get("personal", {}).pop(
                "preferredContactTypeId"
            )
        }
        if self.only_update_present_fields:
            new_personal = user_obj.pop("personal", {})
            existing_personal = existing_user.pop("personal", {})
            existing_preferred_first_name = existing_personal.pop(
                "preferredFirstName", ""
            )
            existing_addresses = existing_personal.get("addresses", [])
            existing_user.update(user_obj)
            existing_personal.update(new_personal)
            if (
                not existing_personal.get("preferredFirstName", "")
                and existing_preferred_first_name
            ):
                existing_personal["preferredFirstName"] = existing_preferred_first_name
            if not existing_personal.get("addresses", []):
                existing_personal["addresses"] = existing_addresses
            if existing_personal:
                existing_user["personal"] = existing_personal
        else:
            existing_user.update(user_obj)
        if "personal" in existing_user:
            existing_user["personal"].update(preferred_contact_type)
        else:
            existing_user["personal"] = preferred_contact_type
        for key, value in protected_fields.items():
            if type(value) is dict:
                try:
                    existing_user[key].update(value)
                except KeyError:
                    existing_user[key] = value
            else:
                existing_user[key] = value
        create_update_user = await self.http_client.put(
            self.folio_client.gateway_url + f"/users/{existing_user['id']}",
            headers=self.folio_client.okapi_headers,
            json=existing_user,
        )
        return existing_user, create_update_user

    async def create_new_user(self, user_obj) -> dict:
        """
        Creates a new user in the system.

        Args:
            user_obj (dict): A dictionary containing the user information.

        Returns:
            dict: A dictionary representing the response from the server.

        Raises:
            HTTPError: If the HTTP request to create the user fails.
        """
        response = await self.http_client.post(
            self.folio_client.gateway_url + "/users",
            headers=self.folio_client.okapi_headers,
            json=user_obj,
        )
        response.raise_for_status()
        async with self.lock:
            self.logs["created"] += 1
        return response.json()

    async def set_preferred_contact_type(self, user_obj, existing_user) -> None:
        """
        Sets the preferred contact type for a user object. If the provided preferred contact type
        is not valid, the default preferred contact type is used, unless the previously existing
        user object has a valid preferred contact type set. In that case, the existing preferred
        contact type is used.
        """
        if "personal" in user_obj and "preferredContactTypeId" in user_obj["personal"]:
            current_pref_contact = user_obj["personal"].get(
                "preferredContactTypeId", ""
            )
            if mapped_contact_type := dict(
                [(v, k) for k, v in PREFERRED_CONTACT_TYPES_MAP.items()]
            ).get(
                current_pref_contact,
                "",
            ):
                existing_user["personal"]["preferredContactTypeId"] = (
                    mapped_contact_type
                )
            else:
                existing_user["personal"]["preferredContactTypeId"] = (
                    current_pref_contact
                    if current_pref_contact in PREFERRED_CONTACT_TYPES_MAP
                    else self.default_preferred_contact_type
                )
        else:
            logger.warning(
                f"Preferred contact type not provided or is not a valid option: {PREFERRED_CONTACT_TYPES_MAP} "
                f"Setting preferred contact type to {self.default_preferred_contact_type} or using existing value"
            )
            mapped_contact_type = (
                existing_user.get("personal", {}).get("preferredContactTypeId", "")
                or self.default_preferred_contact_type
            )
            if "personal" not in existing_user:
                existing_user["personal"] = {}
            existing_user["personal"]["preferredContactTypeId"] = (
                mapped_contact_type or self.default_preferred_contact_type
            )

    async def create_or_update_user(
        self, user_obj, existing_user, protected_fields, line_number
    ) -> dict:
        """
        Creates or updates a user based on the given user object and existing user.

        Args:
            user_obj (dict): The user object containing the user details.
            existing_user (dict): The existing user object to be updated, if available.
            logs (dict): A dictionary to keep track of the number of updates and failures.

        Returns:
            dict: The updated or created user object, or an empty dictionary an error occurs.
        """
        if existing_user:
            existing_user, update_user = await self.update_existing_user(
                user_obj, existing_user, protected_fields
            )
            try:
                update_user.raise_for_status()
                self.logs["updated"] += 1
                return existing_user
            except Exception as ee:
                logger.error(
                    f"Row {line_number}: User update failed: "
                    f"{str(getattr(getattr(ee, 'response', str(ee)), 'text', str(ee)))}\n"
                )
                await self.errorfile.write(
                    json.dumps(existing_user, ensure_ascii=False) + "\n"
                )
                self.logs["failed"] += 1
                return {}
        else:
            try:
                new_user = await self.create_new_user(user_obj)
                return new_user
            except Exception as ee:
                logger.error(
                    f"Row {line_number}: User creation failed: "
                    f"{str(getattr(getattr(ee, 'response', str(ee)), 'text', str(ee)))}\n"
                )
                await self.errorfile.write(
                    json.dumps(user_obj, ensure_ascii=False) + "\n"
                )
                self.logs["failed"] += 1
                return {}

    async def process_user_obj(self, user: str) -> dict:
        """
        Process a user object. If not type is found in the source object, type is set to "patron".

        Args:
            user (str): The user data to be processed, as a json string.

        Returns:
            dict: The processed user object.

        """
        user_obj = json.loads(user)
        user_obj["type"] = user_obj.get("type", "patron")
        return user_obj

    async def get_protected_fields(self, existing_user) -> dict:
        """
        Retrieves the protected fields from the existing user object,
        combining both the customFields.protectedFields list *and*
        any fields_to_protect passed on the CLI.

        Args:
            existing_user (dict): The existing user object.

        Returns:
            dict: A dictionary containing the protected fields and their values.
        """
        protected_fields = {}
        protected_fields_list = (
            existing_user.get("customFields", {}).get("protectedFields", "").split(",")
        )
        cli_fields = list(self.fields_to_protect)
        # combine and dedupe:
        all_fields = list(dict.fromkeys(protected_fields_list + cli_fields))
        for field in all_fields:
            if "." in field:
                fld, subfld = field.split(".", 1)
                val = existing_user.get(fld, {}).pop(subfld, None)
                if val is not None:
                    protected_fields.setdefault(fld, {})[subfld] = val
            else:
                val = existing_user.pop(field, None)
                if val is not None:
                    protected_fields[field] = val
        return protected_fields

    async def process_existing_user(self, user_obj) -> Tuple[dict, dict, dict, dict]:
        """
        Process an existing user.

        Args:
            user_obj (dict): The user object to process.

        Returns:
            tuple: A tuple containing the request preference object (rp_obj),
                   the existing user object, the existing request preference object (existing_rp),
                   and the existing PU object (existing_pu).
        """
        rp_obj = user_obj.pop("requestPreference", {})
        spu_obj = user_obj.pop("servicePointsUser", {})
        existing_user = await self.get_existing_user(user_obj)
        if existing_user:
            existing_rp = await self.get_existing_rp(user_obj, existing_user)
            existing_pu = await self.get_existing_pu(user_obj, existing_user)
            existing_spu = await self.get_existing_spu(existing_user)
            protected_fields = await self.get_protected_fields(existing_user)
        else:
            existing_rp = {}
            existing_pu = {}
            existing_spu = {}
            protected_fields = {}
        return (
            rp_obj,
            spu_obj,
            existing_user,
            protected_fields,
            existing_rp,
            existing_pu,
            existing_spu,
        )

    async def create_or_update_rp(self, rp_obj, existing_rp, new_user_obj):
        """
        Creates or updates a requet preference object based on the given parameters.

        Args:
            rp_obj (object): A new requet preference object.
            existing_rp (object): The existing resource provider object, if it exists.
            new_user_obj (object): The new user object.

        Returns:
            None
        """
        if existing_rp:
            await self.update_existing_rp(rp_obj, existing_rp)
        else:
            await self.create_new_rp(new_user_obj)

    async def create_new_rp(self, new_user_obj):
        """
        Creates a new request preference for a user.

        Args:
            new_user_obj (dict): The user object containing the user's ID.

        Raises:
            HTTPError: If there is an error in the HTTP request.

        Returns:
            None
        """
        rp_obj = {"holdShelf": True, "delivery": False}
        rp_obj["userId"] = new_user_obj["id"]
        response = await self.http_client.post(
            self.folio_client.gateway_url
            + "/request-preference-storage/request-preference",
            headers=self.folio_client.okapi_headers,
            json=rp_obj,
        )
        response.raise_for_status()

    async def update_existing_rp(self, rp_obj, existing_rp) -> None:
        """
        Updates an existing request preference with the provided request preference object.

        Args:
            rp_obj (dict): The request preference object containing the updated values.
            existing_rp (dict): The existing request preference object to be updated.

        Raises:
            HTTPError: If the PUT request to update the request preference fails.

        Returns:
            None
        """
        existing_rp.update(rp_obj)
        response = await self.http_client.put(
            self.folio_client.gateway_url
            + f"/request-preference-storage/request-preference/{existing_rp['id']}",
            headers=self.folio_client.okapi_headers,
            json=existing_rp,
        )
        response.raise_for_status()

    async def create_perms_user(self, new_user_obj) -> None:
        """
        Creates a permissions user object for the given new user.

        Args:
            new_user_obj (dict): A dictionary containing the details of the new user.

        Raises:
            HTTPError: If there is an error while making the HTTP request.

        Returns:
            None
        """
        perms_user_obj = {"userId": new_user_obj["id"], "permissions": []}
        response = await self.http_client.post(
            self.folio_client.gateway_url + "/perms/users",
            headers=self.folio_client.okapi_headers,
            json=perms_user_obj,
        )
        response.raise_for_status()

    async def process_line(
        self,
        user: str,
        line_number: int,
    ) -> None:
        """
        Process a single line of user data.

        Args:
            user (str): The user data to be processed.
            logs (dict): A dictionary to store logs.

        Returns:
            None

        Raises:
            Any exceptions that occur during the processing.

        """
        async with self.limit_simultaneous_requests:
            user_obj = await self.process_user_obj(user)
            (
                rp_obj,
                spu_obj,
                existing_user,
                protected_fields,
                existing_rp,
                existing_pu,
                existing_spu,
            ) = await self.process_existing_user(user_obj)
            await self.map_address_types(user_obj, line_number)
            await self.map_patron_groups(user_obj, line_number)
            await self.map_departments(user_obj, line_number)
            new_user_obj = await self.create_or_update_user(
                user_obj, existing_user, protected_fields, line_number
            )
            if new_user_obj:
                try:
                    if existing_rp or rp_obj:
                        await self.create_or_update_rp(
                            rp_obj, existing_rp, new_user_obj
                        )
                    else:
                        logger.debug(
                            f"Row {line_number}: Creating default request preference object"
                            f" for {new_user_obj['id']}\n"
                        )
                        await self.create_new_rp(new_user_obj)
                except Exception as ee:  # noqa: W0718
                    rp_error_message = (
                        f"Row {line_number}: Error creating or updating request preferences for "
                        f"{new_user_obj['id']}: "
                        f"{str(getattr(getattr(ee, 'response', ee), 'text', str(ee)))}"
                    )
                    logger.error(rp_error_message)
                if not existing_pu:
                    try:
                        await self.create_perms_user(new_user_obj)
                    except Exception as ee:  # noqa: W0718
                        pu_error_message = (
                            f"Row {line_number}: Error creating permissionUser object for user: "
                            f"{new_user_obj['id']}: "
                            f"{str(getattr(getattr(ee, 'response', str(ee)), 'text', str(ee)))}"
                        )
                        logger.error(pu_error_message)
                await self.handle_service_points_user(
                    spu_obj, existing_spu, new_user_obj
                )

    async def map_service_points(self, spu_obj, existing_user):
        """
        Maps the service points of a user object using the provided service point map.

        Args:
            spu_obj (dict): The service-points-user object to update.
            existing_user (dict): The existing user object associated with the spu_obj.

        Returns:
            None
        """
        if "servicePointsIds" in spu_obj:
            mapped_service_points = []
            for sp in spu_obj.pop("servicePointsIds", []):
                try:
                    if self.validate_uuid(sp) and sp in self.service_point_map.values():
                        logger.debug(
                            f"Service point {sp} is a UUID, skipping mapping\n"
                        )
                        mapped_service_points.append(sp)
                    else:
                        mapped_service_points.append(self.service_point_map[sp])
                except KeyError:
                    logger.error(
                        f'Service point "{sp}" not found, excluding service point from user: '
                        f"{self.service_point_map}"
                    )
            if mapped_service_points:
                spu_obj["servicePointsIds"] = mapped_service_points
        if "defaultServicePointId" in spu_obj:
            sp_code = spu_obj.pop("defaultServicePointId", "")
            try:
                if (
                    self.validate_uuid(sp_code)
                    and sp_code in self.service_point_map.values()
                ):
                    logger.debug(
                        f"Default service point {sp_code} is a UUID, skipping mapping\n"
                    )
                    mapped_sp_id = sp_code
                else:
                    mapped_sp_id = self.service_point_map[sp_code]
                if mapped_sp_id not in spu_obj.get("servicePointsIds", []):
                    logger.warning(
                        f'Default service point "{sp_code}" not found in assigned service points, '
                        "excluding default service point from user"
                    )
                else:
                    spu_obj["defaultServicePointId"] = mapped_sp_id
            except KeyError:
                logger.error(
                    f'Default service point "{sp_code}" not found, excluding default service '
                    f"point from user: {existing_user['id']}"
                )

    async def handle_service_points_user(self, spu_obj, existing_spu, existing_user):
        """
        Handles processing a service-points-user object for a user.

        Args:
            spu_obj (dict): The service-points-user object to process.
            existing_spu (dict): The existing service-points-user object, if it exists.
            existing_user (dict): The existing user object associated with the spu_obj.
        """
        if spu_obj:
            await self.map_service_points(spu_obj, existing_user)
            if existing_spu:
                await self.update_existing_spu(spu_obj, existing_spu)
            else:
                await self.create_new_spu(spu_obj, existing_user)

    async def get_existing_spu(self, existing_user):
        """
        Retrieves the existing service-points-user object for a given user.

        Args:
            existing_user (dict): The existing user object.

        Returns:
            dict: The existing service-points-user object.
        """
        try:
            existing_spu = await self.http_client.get(
                self.folio_client.gateway_url + "/service-points-users",
                headers=self.folio_client.okapi_headers,
                params={"query": f"userId=={existing_user['id']}"},
            )
            existing_spu.raise_for_status()
            existing_spu = existing_spu.json().get("servicePointsUsers", [])
            existing_spu = existing_spu[0] if existing_spu else {}
        except httpx.HTTPError:
            existing_spu = {}
        return existing_spu

    async def create_new_spu(self, spu_obj, existing_user):
        """
        Creates a new service-points-user object for a given user.

        Args:
            spu_obj (dict): The service-points-user object to create.
            existing_user (dict): The existing user object.

        Returns:
            None
        """
        spu_obj["userId"] = existing_user["id"]
        response = await self.http_client.post(
            self.folio_client.gateway_url + "/service-points-users",
            headers=self.folio_client.okapi_headers,
            json=spu_obj,
        )
        response.raise_for_status()

    async def update_existing_spu(self, spu_obj, existing_spu):
        """
        Updates an existing service-points-user object with the provided service-points-user object.

        Args:
            spu_obj (dict): The service-points-user object containing the updated values.
            existing_spu (dict): The existing service-points-user object to be updated.

        Returns:
            None
        """
        existing_spu.update(spu_obj)
        response = await self.http_client.put(
            self.folio_client.gateway_url
            + f"/service-points-users/{existing_spu['id']}",
            headers=self.folio_client.okapi_headers,
            json=existing_spu,
        )
        response.raise_for_status()

    async def process_file(self, openfile) -> None:
        """
        Process the user object file.

        Args:
            openfile: The file or file-like object to process.
        """
        with Progress(  # Set up the progress bar
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            MofNCompleteColumn(),
            UserStatsColumn(),
            "[",
            TimeElapsedColumn(),
            "<",
            TimeRemainingColumn(),
            "/",
            ItemsPerSecondColumn(),
            "]",
        ) as progress:
            with open(openfile.name, "rb") as f:
                total_lines = sum(
                    buf.count(b"\n") for buf in iter(lambda: f.read(1024 * 1024), b"")
                )
            self.progress = progress
            self.task_progress = progress.add_task(
                "Importing users: ", total=total_lines, created=0, updated=0, failed=0, visible=not self.no_progress
            )  # Add a task to the progress bar
            openfile.seek(0)
            tasks = []
            for line_number, user in enumerate(openfile):
                tasks.append(self.process_line(user, line_number))
                if len(tasks) == self.batch_size:
                    start = time.time()
                    await asyncio.gather(*tasks)
                    duration = time.time() - start
                    async with self.lock:
                        progress.update(
                            self.task_progress,
                            advance=len(tasks),
                            created=self.logs["created"],
                            updated=self.logs["updated"],
                            failed=self.logs["failed"],
                        )
                        message = (
                            f"{dt.now().isoformat(sep=' ', timespec='milliseconds')}: "
                            f"Batch of {self.batch_size} users processed in {duration:.2f} "
                            f"seconds. - Users created: {self.logs['created']} - Users updated: "
                            f"{self.logs['updated']} - Users failed: {self.logs['failed']}"
                        )
                        logger.info(message)
                    tasks = []
            if tasks:
                start = time.time()
                await asyncio.gather(*tasks)
                duration = time.time() - start
                async with self.lock:
                    progress.update(
                        self.task_progress,
                        advance=len(tasks),
                        created=self.logs["created"],
                        updated=self.logs["updated"],
                        failed=self.logs["failed"],
                    )
                    message = (
                        f"{dt.now().isoformat(sep=' ', timespec='milliseconds')}: "
                        f"Batch of {len(tasks)} users processed in {duration:.2f} seconds. - "
                        f"Users created: {self.logs['created']} - Users updated: "
                        f"{self.logs['updated']} - Users failed: {self.logs['failed']}"
                    )
                    logger.info(message)


def set_up_cli_logging():
    """
    This function sets up logging for the CLI.
    """
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Set up file and stream handlers
    file_handler = logging.FileHandler(
        "folio_user_import_{}.log".format(dt.now().strftime("%Y%m%d%H%M%S"))
    )
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    if not any(
        isinstance(h, logging.StreamHandler) and h.stream == sys.stderr
        for h in logger.handlers
    ):
        stream_handler = RichHandler(
            show_level=False,
            show_time=False,
            omit_repeated_times=False,
            show_path=False,
        )
        stream_handler.setLevel(logging.WARNING)
        stream_formatter = logging.Formatter("%(message)s")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    # Stop httpx from logging info messages to the console
    logging.getLogger("httpx").setLevel(logging.WARNING)


app = typer.Typer()


@app.command()
def main(
    gateway_url: Annotated[
        str,
        typer.Option(
            ...,
            prompt="Please enter the FOLIO API Gateway URL",
            help="The FOLIO API Gateway URL",
            envvar="FOLIO_GATEWAY_URL",
        ),
    ],
    tenant_id: Annotated[
        str,
        typer.Option(
            ...,
            prompt="Please enter the FOLIO tenant id",
            help="The tenant id",
            envvar="FOLIO_TENANT_ID",
        ),
    ],
    username: Annotated[
        str,
        typer.Option(
            ...,
            prompt="Please enter your FOLIO username",
            help="The FOLIO username",
            envvar="FOLIO_USERNAME",
        ),
    ],
    password: Annotated[
        str,
        typer.Option(
            ...,
            prompt="Please enter your FOLIO Password",
            hide_input=True,
            help="The FOLIO password",
            envvar="FOLIO_PASSWORD",
        ),
    ],
    library_name: Annotated[
        str,
        typer.Option(
            ...,
            prompt="Please enter the library name",
            help="The name of the library",
            envvar="FOLIO_LIBRARY_NAME",
        ),
    ],
    user_file_path: Annotated[
        Path, typer.Option(..., help="The path to the user file")
    ],
    member_tenant_id: Annotated[
        str,
        typer.Option(
            help="The FOLIO ECS member tenant id (if applicable)",
            envvar="FOLIO_MEMBER_TENANT_ID",
        ),
    ] = "",
    fields_to_protect: Annotated[
        str,
        typer.Option(
            help="Comma-separated list of top-level or nested (dot-notation) fields to protect"
        ),
    ] = "",
    update_only_present_fields: bool = typer.Option(
        False,
        "--update-only-present-fields",
        help="Only update fields that are present in the new user object",
    ),
    limit_async_requests: Annotated[
        int,
        typer.Option(
            help="Limit how many http requests can be made at once",
            envvar="FOLIO_LIMIT_ASYNC_REQUESTS",
        ),
    ] = 10,
    batch_size: Annotated[
        int,
        typer.Option(
            help="How many user records to process before logging statistics",
            envvar="FOLIO_USER_IMPORT_BATCH_SIZE",
        ),
    ] = 250,
    report_file_base_path: Annotated[
        Path, typer.Option(help="The base path for the log and error files")
    ] = Path.cwd(),
    user_match_key: UserMatchKeys = typer.Option(
        UserMatchKeys.EXTERNAL_SYSTEM_ID.value, help="The key to use to match users"
    ),
    default_preferred_contact_type: PreferredContactType = typer.Option(
        PreferredContactType.EMAIL.value,
        case_sensitive=False,
        help="The default preferred contact type to use if the provided value is not valid or not present",
    ),
    no_progress: bool = typer.Option(
        False,
        "--no-progress",
        help="Disable progress bar display during user import",
    ),
) -> None:
    """
    Command-line interface to batch import users into FOLIO
    """
    set_up_cli_logging()
    protect_fields = [f.strip() for f in fields_to_protect.split(",") if f.strip()]

    library_name = library_name

    # Semaphore to limit the number of async HTTP requests active at any given time
    limit_async_requests = asyncio.Semaphore(limit_async_requests)
    batch_size = batch_size

    folio_client = folioclient.FolioClient(gateway_url, tenant_id, username, password)

    # Set the member tenant id if provided to support FOLIO ECS multi-tenant environments
    if member_tenant_id:
        folio_client.okapi_headers["x-okapi-tenant"] = member_tenant_id

    user_file_path = user_file_path
    report_file_base_path = report_file_base_path
    error_file_path = (
        report_file_base_path
        / f"failed_user_import_{dt.now(utc).strftime('%Y%m%d_%H%M%S')}.txt"
    )
    try:
        importer = UserImporter(
            folio_client,
            library_name,
            batch_size,
            limit_async_requests,
            user_file_path,
            user_match_key.value,
            update_only_present_fields,
            default_preferred_contact_type.value,
            fields_to_protect=protect_fields,
            no_progress=no_progress
        )
        asyncio.run(run_user_importer(importer, error_file_path))
    except Exception as ee:
        logger.critical(f"An unknown error occurred: {ee}")
        raise typer.Exit(1)


async def run_user_importer(importer: UserImporter, error_file_path: Path):
    try:
        await importer.setup(error_file_path)
        await importer.do_import()
    except Exception as ee:
        logger.critical(f"An unknown error occurred: {ee}")
        typer.Exit(1)
    finally:
        await importer.close()


def _main():
    typer.run(main)


# Run the main function
if __name__ == "__main__":
    app()
