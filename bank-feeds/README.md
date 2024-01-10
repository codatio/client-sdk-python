# Bank Feeds

<!-- Start Codat Library Description -->
﻿Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-bankfeeds
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
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
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [account_mapping](docs/sdks/accountmapping/README.md)

* [create](docs/sdks/accountmapping/README.md#create) - Create bank feed account mapping
* [get](docs/sdks/accountmapping/README.md#get) - List bank feed account mappings

### [source_accounts](docs/sdks/sourceaccounts/README.md)

* [create](docs/sdks/sourceaccounts/README.md#create) - Create source account
* [delete](docs/sdks/sourceaccounts/README.md#delete) - Delete source account
* [delete_credentials](docs/sdks/sourceaccounts/README.md#delete_credentials) - Delete all source account credentials
* [generate_credentials](docs/sdks/sourceaccounts/README.md#generate_credentials) - Generate source account credentials
* [list](docs/sdks/sourceaccounts/README.md#list) - List source accounts
* [update](docs/sdks/sourceaccounts/README.md#update) - Update source account

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [list](docs/sdks/bankaccounts/README.md#list) - List bank accounts

### [transactions](docs/sdks/transactions/README.md)

* [create](docs/sdks/transactions/README.md#create) - Create bank transactions
* [get_create_operation](docs/sdks/transactions/README.md#get_create_operation) - Get create operation
* [list_create_operations](docs/sdks/transactions/README.md#list_create_operations) - List create operations

### [configuration](docs/sdks/configuration/README.md)

* [get](docs/sdks/configuration/README.md#get) - Get configuration
* [set](docs/sdks/configuration/README.md#set) - Set configuration
<!-- End Available Resources and Operations [operations] -->





<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```python
import codatbankfeeds
from codatbankfeeds.models import shared
from codatbankfeeds.utils import BackoffStrategy, RetryConfig

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
)

res = s.companies.create(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.company is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```python
import codatbankfeeds
from codatbankfeeds.models import shared
from codatbankfeeds.utils import BackoffStrategy, RetryConfig

s = codatbankfeeds.CodatBankFeeds(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
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
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
)

res = None
try:
    res = s.companies.create(req)
except errors.ErrorMessage as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
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
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
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
import codatbankfeeds
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatbankfeeds.CodatBankFeeds(client: http_client)
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
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
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