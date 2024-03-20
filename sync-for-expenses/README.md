# Sync for Expenses

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for corporate card providers.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-sync-for-expenses
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [create_partner_expense_connection](docs/sdks/connections/README.md#create_partner_expense_connection) - Create partner expense connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model

### [customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [get](docs/sdks/customers/README.md#get) - Get customer
* [list](docs/sdks/customers/README.md#list) - List customers
* [update](docs/sdks/customers/README.md#update) - Update customer

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [push_operations](docs/sdks/pushoperations/README.md)

* [get](docs/sdks/pushoperations/README.md#get) - Get push operation
* [list](docs/sdks/pushoperations/README.md#list) - List push operations

### [configuration](docs/sdks/configuration/README.md)

* [get](docs/sdks/configuration/README.md#get) - Get company configuration
* [get_mapping_options](docs/sdks/configuration/README.md#get_mapping_options) - Mapping options
* [set](docs/sdks/configuration/README.md#set) - Set company configuration

### [expenses](docs/sdks/expenses/README.md)

* [create](docs/sdks/expenses/README.md#create) - Create expense transaction
* [update](docs/sdks/expenses/README.md#update) - Update expense transactions
* [upload_attachment](docs/sdks/expenses/README.md#upload_attachment) - Upload attachment

### [sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [initiate_sync](docs/sdks/sync/README.md#initiate_sync) - Initiate sync
* [list](docs/sdks/sync/README.md#list) - List sync statuses

### [transaction_status](docs/sdks/transactionstatus/README.md)

* [get](docs/sdks/transactionstatus/README.md#get) - Get sync transaction
* [list](docs/sdks/transactionstatus/README.md#list) - List sync transactions
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import codatsyncexpenses
from codatsyncexpenses.models import shared
from codatsyncexpenses.utils import BackoffStrategy, RetryConfig

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.company is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import codatsyncexpenses
from codatsyncexpenses.models import shared
from codatsyncexpenses.utils import BackoffStrategy, RetryConfig

s = codatsyncexpenses.CodatSyncExpenses(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

### Example

```python
import codatsyncexpenses
from codatsyncexpenses.models import errors, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = None
try:
    res = s.companies.create(req)
except errors.ErrorMessage as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.company is not None:
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
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatsyncexpenses
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatsyncexpenses.CodatSyncExpenses(client: http_client)
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
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
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