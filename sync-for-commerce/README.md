# Sync for Commerce

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for POS and eCommerce platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install codat-sync-for-commerce
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

res = s.sync_flow_settings.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [sync_flow_settings](docs/sdks/syncflowsettings/README.md)

* [get_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#get_config_text_sync_flow) - Get preferences for text fields
* [get_visible_accounts](docs/sdks/syncflowsettings/README.md#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#update_config_text_sync_flow) - Update preferences for text fields
* [update_visible_accounts_sync_flow](docs/sdks/syncflowsettings/README.md#update_visible_accounts_sync_flow) - Update visible accounts

### [advanced_controls](docs/sdks/advancedcontrols/README.md)

* [create_company](docs/sdks/advancedcontrols/README.md#create_company) - Create company
* [get_configuration](docs/sdks/advancedcontrols/README.md#get_configuration) - Get company configuration
* [list_companies](docs/sdks/advancedcontrols/README.md#list_companies) - List companies
* [set_configuration](docs/sdks/advancedcontrols/README.md#set_configuration) - Set configuration

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [get_sync_flow_url](docs/sdks/connections/README.md#get_sync_flow_url) - Start new sync flow
* [list](docs/sdks/connections/README.md#list) - List connections
* [update_authorization](docs/sdks/connections/README.md#update_authorization) - Update authorization
* [update_connection](docs/sdks/connections/README.md#update_connection) - Update connection

### [sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [get_status](docs/sdks/sync/README.md#get_status) - Get sync status
* [list](docs/sdks/sync/README.md#list) - List sync statuses
* [request](docs/sdks/sync/README.md#request) - Initiate new sync
* [request_for_date_range](docs/sdks/sync/README.md#request_for_date_range) - Initiate sync for specific range

### [integrations](docs/sdks/integrations/README.md)

* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding for an integration
* [list](docs/sdks/integrations/README.md#list) - List integrations
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
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

res = s.sync_flow_settings.get_config_text_sync_flow(req,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.localization_info is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
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

res = s.sync_flow_settings.get_config_text_sync_flow(req)

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
| errors.SDKError         | 4x-5xx                  | */*                     |

### Example

```python
import codatsynccommerce
from codatsynccommerce.models import errors, operations, shared

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
    res = s.sync_flow_settings.get_config_text_sync_flow(req)
except errors.ErrorMessage as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
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

res = s.sync_flow_settings.get_config_text_sync_flow(req)

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

res = s.sync_flow_settings.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

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

res = s.sync_flow_settings.get_config_text_sync_flow(req)

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