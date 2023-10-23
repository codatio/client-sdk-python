# Sync for Commerce version 1

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for POS and eCommerce platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-sync-for-commerce-version-1
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingAccountRequest(
    accounting_account=shared.AccountingAccount(
        currency='GBP',
        current_balance=Decimal('0'),
        description='Invoices the business has issued but has not yet collected payment on.',
        fully_qualified_category='Asset.Current',
        fully_qualified_name='Cash On Hand',
        id='1b6266d1-1e44-46c5-8eb5-a8f98e03124e',
        metadata=shared.AccountingAccountMetadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        name='Accounts Receivable',
        nominal_code='610',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.AccountStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
        type=shared.AccountType.ASSET,
        valid_datatype_links=[
            shared.AccountingAccountValidDataTypeLinks(
                links=[
                    'string',
                ],
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounting_accounts.create_accounting_account(req)

if res.accounting_create_account_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [accounting_accounts](docs/sdks/accountingaccounts/README.md)

* [create_accounting_account](docs/sdks/accountingaccounts/README.md#create_accounting_account) - Create account
* [get_accounting_account](docs/sdks/accountingaccounts/README.md#get_accounting_account) - Get account
* [list_accounting_accounts](docs/sdks/accountingaccounts/README.md#list_accounting_accounts) - List accounts

### [accounting_bank_accounts](docs/sdks/accountingbankaccounts/README.md)

* [get_accounting_bank_account](docs/sdks/accountingbankaccounts/README.md#get_accounting_bank_account) - Get bank account
* [list_accounting_bank_accounts](docs/sdks/accountingbankaccounts/README.md#list_accounting_bank_accounts) - List bank accounts

### [accounting_company_info](docs/sdks/accountingcompanyinfo/README.md)

* [get_accounting_company_info](docs/sdks/accountingcompanyinfo/README.md#get_accounting_company_info) - Get company info
* [refresh](docs/sdks/accountingcompanyinfo/README.md#refresh) - Refresh company info

### [accounting_credit_notes](docs/sdks/accountingcreditnotes/README.md)

* [create_accounting_credit_note](docs/sdks/accountingcreditnotes/README.md#create_accounting_credit_note) - Create credit note

### [accounting_customers](docs/sdks/accountingcustomers/README.md)

* [create_accounting_customer](docs/sdks/accountingcustomers/README.md#create_accounting_customer) - Create customer

### [accounting_direct_incomes](docs/sdks/accountingdirectincomes/README.md)

* [create_accounting_direct_income](docs/sdks/accountingdirectincomes/README.md#create_accounting_direct_income) - Create direct income

### [accounting_invoices](docs/sdks/accountinginvoices/README.md)

* [create_accounting_invoice](docs/sdks/accountinginvoices/README.md#create_accounting_invoice) - Create invoice

### [accounting_journal_entries](docs/sdks/accountingjournalentries/README.md)

* [create_accounting_journal_entry](docs/sdks/accountingjournalentries/README.md#create_accounting_journal_entry) - Create journal entry

### [accounting_payments](docs/sdks/accountingpayments/README.md)

* [create_accounting_payment](docs/sdks/accountingpayments/README.md#create_accounting_payment) - Create payment

### [commerce_company_info](docs/sdks/commercecompanyinfo/README.md)

* [get_commerce_company_info](docs/sdks/commercecompanyinfo/README.md#get_commerce_company_info) - Get company info

### [commerce_customers](docs/sdks/commercecustomers/README.md)

* [get_commerce_customer](docs/sdks/commercecustomers/README.md#get_commerce_customer) - Get customer
* [list_commerce_customers](docs/sdks/commercecustomers/README.md#list_commerce_customers) - List customers

### [commerce_locations](docs/sdks/commercelocations/README.md)

* [get_commerce_location](docs/sdks/commercelocations/README.md#get_commerce_location) - Get location
* [list_commerce_locations](docs/sdks/commercelocations/README.md#list_commerce_locations) - List locations

### [commerce_orders](docs/sdks/commerceorders/README.md)

* [get_commerce_order](docs/sdks/commerceorders/README.md#get_commerce_order) - Get order
* [list_commerce_orders](docs/sdks/commerceorders/README.md#list_commerce_orders) - List orders

### [commerce_payments](docs/sdks/commercepayments/README.md)

* [get_commerce_payment](docs/sdks/commercepayments/README.md#get_commerce_payment) - Get payment
* [get_method](docs/sdks/commercepayments/README.md#get_method) - Get payment method
* [list_commerce_payments](docs/sdks/commercepayments/README.md#list_commerce_payments) - List payments
* [list_methods](docs/sdks/commercepayments/README.md#list_methods) - List payment methods

### [commerce_products](docs/sdks/commerceproducts/README.md)

* [get_commerce_product](docs/sdks/commerceproducts/README.md#get_commerce_product) - Get product
* [list_commerce_products](docs/sdks/commerceproducts/README.md#list_commerce_products) - List products

### [commerce_transactions](docs/sdks/commercetransactions/README.md)

* [get_commerce_transaction](docs/sdks/commercetransactions/README.md#get_commerce_transaction) - Get transaction
* [list_commerce_transactions](docs/sdks/commercetransactions/README.md#list_commerce_transactions) - List transactions

### [companies](docs/sdks/companies/README.md)

* [delete_company](docs/sdks/companies/README.md#delete_company) - Delete a company
* [get_company](docs/sdks/companies/README.md#get_company) - Get company
* [update_company](docs/sdks/companies/README.md#update_company) - Update company

### [company_management](docs/sdks/companymanagement/README.md)

* [create_company](docs/sdks/companymanagement/README.md#create_company) - Create sync for commerce company
* [create_connection](docs/sdks/companymanagement/README.md#create_connection) - Create connection
* [list_companies](docs/sdks/companymanagement/README.md#list_companies) - List companies
* [list_connections](docs/sdks/companymanagement/README.md#list_connections) - List data connections
* [update_connection](docs/sdks/companymanagement/README.md#update_connection) - Update data connection

### [configuration](docs/sdks/configuration/README.md)

* [get_configuration](docs/sdks/configuration/README.md#get_configuration) - Retrieve config preferences set for a company
* [set_configuration](docs/sdks/configuration/README.md#set_configuration) - Create or update configuration

### [connections](docs/sdks/connections/README.md)

* [delete_connection](docs/sdks/connections/README.md#delete_connection) - Delete connection
* [get_connection](docs/sdks/connections/README.md#get_connection) - Get connection
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [integrations](docs/sdks/integrations/README.md)

* [get_integration_branding](docs/sdks/integrations/README.md#get_integration_branding) - Get branding for an integration
* [list_integrations](docs/sdks/integrations/README.md#list_integrations) - List integrations

### [push_data](docs/sdks/pushdata/README.md)

* [get_operation](docs/sdks/pushdata/README.md#get_operation) - Get push operation
* [list_operations](docs/sdks/pushdata/README.md#list_operations) - List push operations

### [refresh_data](docs/sdks/refreshdata/README.md)

* [all](docs/sdks/refreshdata/README.md#all) - Refresh all data
* [by_data_type](docs/sdks/refreshdata/README.md#by_data_type) - Refresh data type
* [get_company_data_status](docs/sdks/refreshdata/README.md#get_company_data_status) - Get data status
* [get_pull_operation](docs/sdks/refreshdata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/refreshdata/README.md#list_pull_operations) - List pull operations

### [sync](docs/sdks/sync/README.md)

* [get_sync_status](docs/sdks/sync/README.md#get_sync_status) - Get status for a company's syncs
* [request_sync](docs/sdks/sync/README.md#request_sync) - Sync new
* [request_sync_for_date_range](docs/sdks/sync/README.md#request_sync_for_date_range) - Sync range

### [sync_flow_preferences](docs/sdks/syncflowpreferences/README.md)

* [get_config_text_sync_flow](docs/sdks/syncflowpreferences/README.md#get_config_text_sync_flow) - Retrieve preferences for text fields on sync flow
* [get_sync_flow_url](docs/sdks/syncflowpreferences/README.md#get_sync_flow_url) - Retrieve sync flow url
* [get_visible_accounts](docs/sdks/syncflowpreferences/README.md#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](docs/sdks/syncflowpreferences/README.md#update_config_text_sync_flow) - Update preferences for text fields on sync flow
* [update_visible_accounts_sync_flow](docs/sdks/syncflowpreferences/README.md#update_visible_accounts_sync_flow) - Update the visible accounts on sync flow
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)