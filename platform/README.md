# Platform

<!-- Start Codat Library Description -->
Manage the building blocks of Codat, including companies, connections, and more.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-platform
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [settings](docs/sdks/settings/README.md)

* [create_api_key](docs/sdks/settings/README.md#create_api_key) - Create API key
* [delete_api_key](docs/sdks/settings/README.md#delete_api_key) - Delete API key
* [get_profile](docs/sdks/settings/README.md#get_profile) - Get profile
* [get_sync_settings](docs/sdks/settings/README.md#get_sync_settings) - Get sync settings
* [list_api_keys](docs/sdks/settings/README.md#list_api_keys) - List API keys
* [update_profile](docs/sdks/settings/README.md#update_profile) - Update profile
* [update_sync_settings](docs/sdks/settings/README.md#update_sync_settings) - Update all sync settings

### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [connection_management](docs/sdks/connectionmanagement/README.md)

* [get_access_token](docs/sdks/connectionmanagement/README.md#get_access_token) - Get access token

### [connection_management.cors_settings](docs/sdks/corssettings/README.md)

* [get](docs/sdks/corssettings/README.md#get) - Get CORS settings
* [set](docs/sdks/corssettings/README.md#set) - Set CORS settings

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection
* [update_authorization](docs/sdks/connections/README.md#update_authorization) - Update authorization

### [custom_data_type](docs/sdks/customdatatype/README.md)

* [configure](docs/sdks/customdatatype/README.md#configure) - Configure custom data type
* [get_configuration](docs/sdks/customdatatype/README.md#get_configuration) - Get custom data configuration
* [list](docs/sdks/customdatatype/README.md#list) - List custom data type records
* [refresh](docs/sdks/customdatatype/README.md#refresh) - Refresh custom data type

### [push_data](docs/sdks/pushdata/README.md)

* [get_model_options](docs/sdks/pushdata/README.md#get_model_options) - Get push options
* [get_operation](docs/sdks/pushdata/README.md#get_operation) - Get push operation
* [list_operations](docs/sdks/pushdata/README.md#list_operations) - List push operations

### [refresh_data](docs/sdks/refreshdata/README.md)

* [all](docs/sdks/refreshdata/README.md#all) - Refresh all data
* [by_data_type](docs/sdks/refreshdata/README.md#by_data_type) - Refresh data type
* [get](docs/sdks/refreshdata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/refreshdata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/refreshdata/README.md#list_pull_operations) - List pull operations

### [groups](docs/sdks/groups/README.md)

* [add_company](docs/sdks/groups/README.md#add_company) - Add company
* [create](docs/sdks/groups/README.md#create) - Create group
* [list](docs/sdks/groups/README.md#list) - List groups
* [remove_company](docs/sdks/groups/README.md#remove_company) - Remove company

### [integrations](docs/sdks/integrations/README.md)

* [get](docs/sdks/integrations/README.md#get) - Get integration
* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding
* [list](docs/sdks/integrations/README.md#list) - List integrations

### [supplemental_data](docs/sdks/supplementaldata/README.md)

* [configure](docs/sdks/supplementaldata/README.md#configure) - Configure
* [get_configuration](docs/sdks/supplementaldata/README.md#get_configuration) - Get configuration

### [webhooks](docs/sdks/webhooks/README.md)

* [~~create~~](docs/sdks/webhooks/README.md#create) - Create webhook :warning: **Deprecated**
* [create_consumer](docs/sdks/webhooks/README.md#create_consumer) - Create webhook consumer
* [delete_consumer](docs/sdks/webhooks/README.md#delete_consumer) - Delete webhook consumer
* [~~get~~](docs/sdks/webhooks/README.md#get) - Get webhook :warning: **Deprecated**
* [~~list~~](docs/sdks/webhooks/README.md#list) - List webhooks :warning: **Deprecated**
* [list_consumers](docs/sdks/webhooks/README.md#list_consumers) - List webhook consumers
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import codatplatform
from codatplatform.models import shared
from codatplatform.utils import BackoffStrategy, RetryConfig

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.api_key_details is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import codatplatform
from codatplatform.models import shared
from codatplatform.utils import BackoffStrategy, RetryConfig

s = codatplatform.CodatPlatform(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

### Example

```python
import codatplatform
from codatplatform.models import errors, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = None
try:
    res = s.settings.create_api_key(req)
except errors.ErrorMessage as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.api_key_details is not None:
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
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import codatplatform
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = codatplatform.CodatPlatform(client=http_client)
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
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
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