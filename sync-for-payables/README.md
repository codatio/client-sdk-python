# Sync for Payables

<!-- Start Codat Library Description -->
Streamline your customers' accounts payable workflow.
<!-- End Codat Library Description -->

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-sync-for-payables
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared
from decimal import Decimal

s = codatsyncpayables.CodatSyncPayables(
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
        metadata=shared.Metadata(),
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
* [get](docs/sdks/accounts/README.md#get) - Get account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model
* [list](docs/sdks/accounts/README.md#list) - List accounts

### [bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [create](docs/sdks/billcreditnotes/README.md#create) - Create bill credit note
* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [get_create_update_model](docs/sdks/billcreditnotes/README.md#get_create_update_model) - Get create/update bill credit note model
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes
* [update](docs/sdks/billcreditnotes/README.md#update) - Update bill credit note

### [bill_payments](docs/sdks/billpayments/README.md)

* [create](docs/sdks/billpayments/README.md#create) - Create bill payments
* [delete](docs/sdks/billpayments/README.md#delete) - Delete bill payment
* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [get_create_model](docs/sdks/billpayments/README.md#get_create_model) - Get create bill payment model
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

### [bills](docs/sdks/bills/README.md)

* [create](docs/sdks/bills/README.md#create) - Create bill
* [delete](docs/sdks/bills/README.md#delete) - Delete bill
* [delete_attachment](docs/sdks/bills/README.md#delete_attachment) - Delete bill attachment
* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [get_create_update_model](docs/sdks/bills/README.md#get_create_update_model) - Get create/update bill model
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments
* [update](docs/sdks/bills/README.md#update) - Update bill
* [upload_attachment](docs/sdks/bills/README.md#upload_attachment) - Upload bill attachment

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [company_info](docs/sdks/companyinfo/README.md)

* [get_accounting_profile](docs/sdks/companyinfo/README.md#get_accounting_profile) - Get company accounting profile

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [journal_entries](docs/sdks/journalentries/README.md)

* [create](docs/sdks/journalentries/README.md#create) - Create journal entry
* [get_create_model](docs/sdks/journalentries/README.md#get_create_model) - Get create journal entry model

### [journals](docs/sdks/journals/README.md)

* [create](docs/sdks/journals/README.md#create) - Create journal
* [get](docs/sdks/journals/README.md#get) - Get journal
* [get_create_model](docs/sdks/journals/README.md#get_create_model) - Get create journal model
* [list](docs/sdks/journals/README.md#list) - List journals

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [push_operations](docs/sdks/pushoperations/README.md)

* [get](docs/sdks/pushoperations/README.md#get) - Get push operation
* [list](docs/sdks/pushoperations/README.md#list) - List push operations

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_create_update_model](docs/sdks/suppliers/README.md#get_create_update_model) - Get create/update supplier model
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [tax_rates](docs/sdks/taxrates/README.md)

* [get](docs/sdks/taxrates/README.md#get) - Get tax rate
* [list](docs/sdks/taxrates/README.md#list) - List all tax rates

### [tracking_categories](docs/sdks/trackingcategories/README.md)

* [get](docs/sdks/trackingcategories/README.md#get) - Get tracking categories
* [list](docs/sdks/trackingcategories/README.md#list) - List tracking categories
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.
