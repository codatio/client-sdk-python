# Sync for Commerce version 1

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for POS and eCommerce platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-sync-for-commerce-version-1
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [sync_flow_preferences](docs/sdks/syncflowpreferences/README.md)

* [get_config_text_sync_flow](docs/sdks/syncflowpreferences/README.md#get_config_text_sync_flow) - Retrieve preferences for text fields on sync flow
* [get_sync_flow_url](docs/sdks/syncflowpreferences/README.md#get_sync_flow_url) - Retrieve sync flow url
* [get_visible_accounts](docs/sdks/syncflowpreferences/README.md#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](docs/sdks/syncflowpreferences/README.md#update_config_text_sync_flow) - Update preferences for text fields on sync flow
* [update_visible_accounts_sync_flow](docs/sdks/syncflowpreferences/README.md#update_visible_accounts_sync_flow) - Update the visible accounts on sync flow

### [companies](docs/sdks/companies/README.md)

* [delete_company](docs/sdks/companies/README.md#delete_company) - Delete a company
* [get_company](docs/sdks/companies/README.md#get_company) - Get company
* [update_company](docs/sdks/companies/README.md#update_company) - Update company

### [connections](docs/sdks/connections/README.md)

* [delete_connection](docs/sdks/connections/README.md#delete_connection) - Delete connection
* [get_connection](docs/sdks/connections/README.md#get_connection) - Get connection
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [accounting_bank_accounts](docs/sdks/accountingbankaccounts/README.md)

* [get_accounting_bank_account](docs/sdks/accountingbankaccounts/README.md#get_accounting_bank_account) - Get bank account
* [list_accounting_bank_accounts](docs/sdks/accountingbankaccounts/README.md#list_accounting_bank_accounts) - List bank accounts

### [commerce_customers](docs/sdks/commercecustomers/README.md)

* [get_commerce_customer](docs/sdks/commercecustomers/README.md#get_commerce_customer) - Get customer
* [list_commerce_customers](docs/sdks/commercecustomers/README.md#list_commerce_customers) - List customers

### [commerce_company_info](docs/sdks/commercecompanyinfo/README.md)

* [get_commerce_company_info](docs/sdks/commercecompanyinfo/README.md#get_commerce_company_info) - Get company info

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

### [accounting_accounts](docs/sdks/accountingaccounts/README.md)

* [create_accounting_account](docs/sdks/accountingaccounts/README.md#create_accounting_account) - Create account
* [get_accounting_account](docs/sdks/accountingaccounts/README.md#get_accounting_account) - Get account
* [list_accounting_accounts](docs/sdks/accountingaccounts/README.md#list_accounting_accounts) - List accounts

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

### [refresh_data](docs/sdks/refreshdata/README.md)

* [all](docs/sdks/refreshdata/README.md#all) - Refresh all data
* [by_data_type](docs/sdks/refreshdata/README.md#by_data_type) - Refresh data type
* [get_company_data_status](docs/sdks/refreshdata/README.md#get_company_data_status) - Get data status
* [get_pull_operation](docs/sdks/refreshdata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/refreshdata/README.md#list_pull_operations) - List pull operations

### [accounting_company_info](docs/sdks/accountingcompanyinfo/README.md)

* [get_accounting_company_info](docs/sdks/accountingcompanyinfo/README.md#get_accounting_company_info) - Get company info
* [refresh](docs/sdks/accountingcompanyinfo/README.md#refresh) - Refresh company info

### [push_data](docs/sdks/pushdata/README.md)

* [get_operation](docs/sdks/pushdata/README.md#get_operation) - Get push operation
* [list_operations](docs/sdks/pushdata/README.md#list_operations) - List push operations

### [sync](docs/sdks/sync/README.md)

* [get_sync_status](docs/sdks/sync/README.md#get_sync_status) - Get status for a company's syncs
* [request_sync](docs/sdks/sync/README.md#request_sync) - Sync new
* [request_sync_for_date_range](docs/sdks/sync/README.md#request_sync_for_date_range) - Sync range

### [configuration](docs/sdks/configuration/README.md)

* [get_configuration](docs/sdks/configuration/README.md#get_configuration) - Retrieve config preferences set for a company
* [set_configuration](docs/sdks/configuration/README.md#set_configuration) - Create or update configuration

### [integrations](docs/sdks/integrations/README.md)

* [get_integration_branding](docs/sdks/integrations/README.md#get_integration_branding) - Get branding for an integration
* [list_integrations](docs/sdks/integrations/README.md#list_integrations) - List integrations

### [company_management](docs/sdks/companymanagement/README.md)

* [create_company](docs/sdks/companymanagement/README.md#create_company) - Create sync for commerce company
* [create_connection](docs/sdks/companymanagement/README.md#create_connection) - Create connection
* [list_companies](docs/sdks/companymanagement/README.md#list_companies) - List companies
* [list_connections](docs/sdks/companymanagement/README.md#list_connections) - List data connections
* [update_connection](docs/sdks/companymanagement/README.md#update_connection) - Update data connection
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from codatsynccommerce.utils import BackoffStrategy, RetryConfig

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.localization_info is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared
from codatsynccommerce.utils import BackoffStrategy, RetryConfig

s = codatsynccommerce.CodatSyncCommerce(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401,402,403,429,500,503 | application/json        |
| errors.SDKError         | 400-600                 | */*                     |

### Example

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = None
try:
    res = s.sync_flow_preferences.get_config_text_sync_flow(req)
except errors.ErrorMessage as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatsynccommerce
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatsynccommerce.CodatSyncCommerce(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `auth_header` | apiKey        | API key       |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_preferences.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
### Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->