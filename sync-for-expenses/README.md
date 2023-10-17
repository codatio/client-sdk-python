# Sync for Expenses

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for corporate card providers.
<!-- End Codat Library Description -->

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-sync-for-expenses
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared
from decimal import Decimal

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountRequest(
    account=shared.Account(
        currency='USD',
        current_balance=Decimal('0'),
        description='Invoices the business has issued but has not yet collected payment on.',
        fully_qualified_category='Asset.Current',
        fully_qualified_name='Cash On Hand',
        id='1b6266d1-1e44-46c5-8eb5-a8f98e03124e',
        metadata=shared.AccountMetadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Accounts Receivable',
        nominal_code='610',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.AccountStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "Money": {
                    "blue": 'shred',
                },
            },
        ),
        type=shared.AccountType.ASSET,
        valid_datatype_links=[
            shared.AccountValidDataTypeLinks(
                links=[
                    'abnormally',
                ],
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounts.create(req)

if res.create_account_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [configuration](docs/sdks/configuration/README.md)

* [get](docs/sdks/configuration/README.md#get) - Get company configuration
* [get_mapping_options](docs/sdks/configuration/README.md#get_mapping_options) - Mapping options
* [set](docs/sdks/configuration/README.md#set) - Set company configuration

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [create_partner_expense_connection](docs/sdks/connections/README.md#create_partner_expense_connection) - Create partner expense connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [get](docs/sdks/customers/README.md#get) - Get customer
* [list](docs/sdks/customers/README.md#list) - List customers
* [update](docs/sdks/customers/README.md#update) - Update customer

### [expenses](docs/sdks/expenses/README.md)

* [create](docs/sdks/expenses/README.md#create) - Create expense transaction
* [update](docs/sdks/expenses/README.md#update) - Update expense-transactions
* [upload_attachment](docs/sdks/expenses/README.md#upload_attachment) - Upload attachment

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [push_operations](docs/sdks/pushoperations/README.md)

* [get](docs/sdks/pushoperations/README.md#get) - Get push operation
* [list](docs/sdks/pushoperations/README.md#list) - List push operations

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [initiate_sync](docs/sdks/sync/README.md#initiate_sync) - Initiate sync
* [list](docs/sdks/sync/README.md#list) - List sync statuses

### [transaction_status](docs/sdks/transactionstatus/README.md)

* [get](docs/sdks/transactionstatus/README.md#get) - Get sync transaction
* [list](docs/sdks/transactionstatus/README.md#list) - List sync transactions
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:


<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)