# Sync for Expenses version 1

<!-- Start Codat Library Description -->
Push expenses to accounting platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-sync-for-expenses-version-1
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

res = s.companies.create_company(req)

if res.company is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [companies](docs/sdks/companies/README.md)

* [create_company](docs/sdks/companies/README.md#create_company) - Create company
* [delete_company](docs/sdks/companies/README.md#delete_company) - Delete a company
* [get_company](docs/sdks/companies/README.md#get_company) - Get company
* [list_companies](docs/sdks/companies/README.md#list_companies) - List companies
* [update_company](docs/sdks/companies/README.md#update_company) - Update company

### [connections](docs/sdks/connections/README.md)

* [create_connection](docs/sdks/connections/README.md#create_connection) - Create connection
* [create_partner_expense_connection](docs/sdks/connections/README.md#create_partner_expense_connection) - Create partner expense connection
* [delete_connection](docs/sdks/connections/README.md#delete_connection) - Delete connection
* [get_connection](docs/sdks/connections/README.md#get_connection) - Get connection
* [list_connections](docs/sdks/connections/README.md#list_connections) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [configuration](docs/sdks/configuration/README.md)

* [get_company_configuration](docs/sdks/configuration/README.md#get_company_configuration) - Get company configuration
* [save_company_configuration](docs/sdks/configuration/README.md#save_company_configuration) - Set company configuration

### [expenses](docs/sdks/expenses/README.md)

* [create_expense_dataset](docs/sdks/expenses/README.md#create_expense_dataset) - Create expense-transactions
* [update_expense_dataset](docs/sdks/expenses/README.md#update_expense_dataset) - Update expense transactions
* [upload_attachment](docs/sdks/expenses/README.md#upload_attachment) - Upload attachment

### [mapping_options](docs/sdks/mappingoptions/README.md)

* [get_mapping_options](docs/sdks/mappingoptions/README.md#get_mapping_options) - Mapping options

### [sync](docs/sdks/sync/README.md)

* [initiate_sync](docs/sdks/sync/README.md#initiate_sync) - Initiate sync

### [sync_status](docs/sdks/syncstatus/README.md)

* [get_last_successful_sync](docs/sdks/syncstatus/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/syncstatus/README.md#get_latest_sync) - Latest sync status
* [get_sync_by_id](docs/sdks/syncstatus/README.md#get_sync_by_id) - Get sync status
* [list_syncs](docs/sdks/syncstatus/README.md#list_syncs) - List sync statuses

### [transaction_status](docs/sdks/transactionstatus/README.md)

* [get_sync_transaction](docs/sdks/transactionstatus/README.md#get_sync_transaction) - Get sync transaction
* [list_sync_transactions](docs/sdks/transactionstatus/README.md#list_sync_transactions) - Get sync transactions
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

res = s.companies.create_company(req,
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

res = s.companies.create_company(req)

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
    res = s.companies.create_company(req)
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

res = s.companies.create_company(req)

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

res = s.companies.create_company(req)

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

res = s.companies.create_company(req)

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