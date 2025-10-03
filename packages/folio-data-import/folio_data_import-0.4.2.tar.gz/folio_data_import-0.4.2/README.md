# folio_data_import

## Description

This project is designed to import data into the FOLIO LSP. It provides a simple and efficient way to import data from various sources using FOLIO's REST APIs.

## Features

- Import MARC records using FOLIO's Data Import system
- Import User records using FOLIO's User APIs

## Installation

## Installation

Using `pip`
```shell
pip install folio_data_import
```
or `uv pip`
```shell
uv pip install folio_data_import
```

To install the project from the git repo using Poetry, follow these steps:

1. Clone the repository.
2. Navigate to the project directory: `$ cd /path/to/folio_data_import`.
3. Install Poetry if you haven't already: `$ pip install poetry`.
4. Install the project and its dependencies: `$ poetry install`.
6. Run the application using Poetry: `$ poetry run python -m folio_data_import --help`.

Make sure to activate the virtual environment created by Poetry before running the application.

## Usage

1. Prepare the data to be imported in the specified format.
2. Run the application and follow the prompts to import the data.
3. Monitor the import progress and handle any errors or conflicts that may arise.

### folio-data-import
This command provides access to subcommands for importing user and marc data. To import users:
```shell
folio-data-import users --help
```
(for more information, see [folio-user-import](#folio-user-import), below)

For MARC data:
```shell
folio-data-import marc --help
```
(for more information, see [folio-marc-import](#folio-marc-import), below)

As an added convenience, this script can also install tab-completions for itself in your shell:
```shell
folio-data-import --install-completion
```
Once installed, you can `[tab][tab]` after typing `--` and be presented with a list of availabl command options.

### folio-user-import
When this package is installed via PyPI or using `poetry install` from this repository, it installs a convenience script in your `$PATH` called `folio-user-import`. To view all command line options for this script, run `folio-user-import --help`. In addition to supporting `mod-user-import`-style JSON objects, this script also allows you to manage service point assignments for users by specifying a `servicePointsUser` object in the JSON object, using service point codes in place of UUIDs in the `defaultServicePointId` and `servicePointIds` fields:
```
{
    "username": "checkin-all",
    "barcode": "1728439497039848103",
    "active": true,
    "type": "patron",
    "patronGroup": "staff",
    "departments": [],
    "personal": {
        "lastName": "Admin",
        "firstName": "checkin-all",
        "addresses": [
          {
            "countryId": "HU",
            "addressLine1": "Andrássy Street 1.",
            "addressLine2": "",
            "city": "Budapest",
            "region": "Pest",
            "postalCode": "1061",
            "addressTypeId": "Home",
            "primaryAddress": true
          }
        ],
        "preferredContactTypeId": "email"
    },
    "requestPreference": {
        "holdShelf": true,
        "delivery": false,
        "fulfillment": "Hold Shelf"
    }
    "servicePointsUser": {
        "defaultServicePointId": "cd1",
        "servicePointsIds": [
            "cd1",
            "Online",
            "000",
            "cd2"
        ]
    }
}
```
#### Matching Existing Users

Unlike mod-user-import, this importer does not require `externalSystemId` as the match point for your objects. If the user objects have `id` values, that will be used, falling back to `externalSystemId`. However, you can also specify `username` or `barcode` as the match point if desired, using the `--user_match_key` argument.

#### Preferred Contact Type Mapping

Another point of departure from the behavior of `mod-user-import` is the handling of `preferredContactTypeId`. This importer will accept either the `"001", "002", "003"...` values stored by FOLIO, or the human-friendly strings used by `mod-user-import` (`"mail", "email", "text", "phone", "mobile"`). It will also __*set a customizable default for all users that do not otherwise have a valid value specified*__ (using `--default_preferred_contact_type`), unless a (valid) value is already present in the user record being updated.

#### Per-record Field Protection (*experimental*)

This script offers a rudimentary field protection implementation using custom fields. To enable this functionality, create a text custom field that has the field name `protectedFields`. In this field, you can specify a comma-separated list of User schema field names, using dot-notation for nested fields. This protection should support all standard fields except addresses within `personal.addresses`. If you include `personal.addresses` in a user record, any existing addresses will be replaced by the new values.

##### Example

```
{
    "protectedFields": "customFields.protectedFields,personal.preferredFirstName,barcode,personal.telephone,personal.addresses"
}
```

Would result in `preferredFirstName`, `barcode`, and `telephone` remaining unchanged, regardless of the contents of the incoming records.

#### Job-level field protection

To protect fields for all records in a particular import job, you can pass a list of field paths with the `--fields-to-protect` flag. These protections will be applied in combination with any record-level protections specified.

##### Example
```Shell
folio-user-import ... --fields-to-protect "personal.preferredFirstName,customFields.exampleCustomField"
```

#### How to use:
1. Generate a JSON lines (one JSON object per line) file of FOLIO user objects in the style of [mod-user-import](https://github.com/folio-org/mod-user-import)
2. Run the script and specify the required arguments (and any desired optional arguments), including the path to your file of user objects
3. Watch the pretty progress bars...

### folio-marc-import
`folio-marc-import` provides direct access to the MARC import functionality of FOLIO. It can be used to import any file (or files) of binary MARC records via FOLIO's Data Import system using the [change-manager](https://github.com/folio-org/mod-source-record-manager?tab=readme-ov-file#data-import-workflow) APIs directly.

#### How to use:
1. Have a binary MARC21 file (or directory of files)
2. Have a [Data Import Job Profile](https://docs.folio.org/docs/metadata/additional-topics/jobprofiles/) that you want to use to import your records already set up in FOLIO
3. Run the script and specify the required arguments. (`folio-marc-import --help` for more details)
4. Select the job profile you want to use
5. Watch the pretty progress bars...

#### A note on logging
The import logs and job summaries provided by FOLIO can be unreliable in certain circumstances. The scripts have been written to balance the need to retrieve job summary information at the end of each job with the the need to move on to the next import job. If you don't see a job summary when your job completes, check Data Import in FOLIO (Data Import > Actions > View all logs...)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
