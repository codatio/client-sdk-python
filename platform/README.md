# Platform

<!-- Start Codat Library Description -->
Manage the building blocks of Codat, including companies, connections, and more.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Platform API: Platform API

An API for the common components of all of Codat's products.

These end points cover creating and managing your companies, data connections, and integrations.

[Read about the building blocks of Codat...](https://docs.codat.io/core-concepts/companies) | [See our OpenAPI spec](https://github.com/codatio/oas) 

---
<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Connection management | Configure connection management UI and retrieve access tokens for authentication. |
| Webhooks | Create and manage webhooks that listen to Codat's events. |
| Integrations | Get a list of integrations supported by Codat and their logos. |
| Refresh data | Initiate data refreshes, view pull status and history. |
| Settings | Manage company profile configuration, sync settings, and API keys. |
| Push data | Initiate and monitor Create, Update, and Delete operations. |
| Supplemental data | Configure and pull additional data you can include in Codat's standard data types. |
| Custom data type | Configure and pull additional data types that are not included in Codat's standardized data model. |
<!-- End Codat Tags Table -->
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Platform](#platform)
  * [Endpoints](#endpoints)
  * [SDK Installation](#sdk-installation)
  * [Example Usage](#example-usage)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Debugging](#debugging)
  * [Support](#support)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-platform
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-platform
```
<!-- End SDK Installation [installation] -->

## Example Usage
<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform() as codat_platform:
    codat_platform.company_data_connection_status_changed(request={
        "alert_id": "a9367074-b5c3-42c4-9be4-be129f43577e",
        "client_id": "bae71d36-ff47-420a-b4a6-f8c9ddf41140",
        "client_name": "Bank of Dave",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "data": {
            "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
            "new_status": shared.DataConnectionStatus.LINKED,
            "old_status": shared.DataConnectionStatus.PENDING_AUTH,
            "platform_key": "gbol",
        },
        "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "message": "Data connection for SandBox status changed from PendingAuth to Linked",
        "rule_id": "70af3071-65d9-4ec3-b3cb-5283e8d55dac",
        "rule_type": "DataConnectionStatusChanged",
    })

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_platform import CodatPlatform
from codat_platform.models import shared

async def main():
    async with CodatPlatform() as codat_platform:
        await codat_platform.company_data_connection_status_changed_async(request={
            "alert_id": "a9367074-b5c3-42c4-9be4-be129f43577e",
            "client_id": "bae71d36-ff47-420a-b4a6-f8c9ddf41140",
            "client_name": "Bank of Dave",
            "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
            "data": {
                "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
                "new_status": shared.DataConnectionStatus.LINKED,
                "old_status": shared.DataConnectionStatus.PENDING_AUTH,
                "platform_key": "gbol",
            },
            "data_connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
            "message": "Data connection for SandBox status changed from PendingAuth to Linked",
            "rule_id": "70af3071-65d9-4ec3-b3cb-5283e8d55dac",
            "rule_type": "DataConnectionStatusChanged",
        })

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [companies](docs/sdks/companies/README.md)

* [add_product](docs/sdks/companies/README.md#add_product) - Add product
* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [get_access_token](docs/sdks/companies/README.md#get_access_token) - Get company access token
* [list](docs/sdks/companies/README.md#list) - List companies
* [remove_product](docs/sdks/companies/README.md#remove_product) - Remove product
* [update](docs/sdks/companies/README.md#update) - Update company

### [connection_management](docs/sdks/connectionmanagement/README.md)

* [get_access_token](docs/sdks/connectionmanagement/README.md#get_access_token) - Get access token

#### [connection_management.cors_settings](docs/sdks/corssettings/README.md)

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

### [integrations](docs/sdks/integrations/README.md)

* [get](docs/sdks/integrations/README.md#get) - Get integration
* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding
* [list](docs/sdks/integrations/README.md#list) - List integrations

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

### [settings](docs/sdks/settings/README.md)

* [create_api_key](docs/sdks/settings/README.md#create_api_key) - Create API key
* [delete_api_key](docs/sdks/settings/README.md#delete_api_key) - Delete API key
* [get_profile](docs/sdks/settings/README.md#get_profile) - Get profile
* [get_sync_settings](docs/sdks/settings/README.md#get_sync_settings) - Get sync settings
* [list_api_keys](docs/sdks/settings/README.md#list_api_keys) - List API keys
* [update_profile](docs/sdks/settings/README.md#update_profile) - Update profile
* [update_sync_settings](docs/sdks/settings/README.md#update_sync_settings) - Update all sync settings

### [supplemental_data](docs/sdks/supplementaldata/README.md)

* [configure](docs/sdks/supplementaldata/README.md#configure) - Configure
* [get_configuration](docs/sdks/supplementaldata/README.md#get_configuration) - Get configuration

### [webhooks](docs/sdks/webhooks/README.md)

* [~~create~~](docs/sdks/webhooks/README.md#create) - Create webhook (legacy) :warning: **Deprecated**
* [create_consumer](docs/sdks/webhooks/README.md#create_consumer) - Create webhook consumer
* [delete_consumer](docs/sdks/webhooks/README.md#delete_consumer) - Delete webhook consumer
* [~~get~~](docs/sdks/webhooks/README.md#get) - Get webhook (legacy) :warning: **Deprecated**
* [~~list~~](docs/sdks/webhooks/README.md#list) - List webhooks (legacy) :warning: **Deprecated**
* [list_consumers](docs/sdks/webhooks/README.md#list_consumers) - List webhook consumers

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared
from codat_platform.utils import BackoffStrategy, RetryConfig

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:
    res = codat_platform.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    if res is not None:
        # handle response
        pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared
from codat_platform.utils import BackoffStrategy, RetryConfig

with CodatPlatform(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:
    res = codat_platform.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    if res is not None:
        # handle response
        pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_api_key_async` method may raise the following exceptions:

| Error Type          | Status Code                            | Content Type     |
| ------------------- | -------------------------------------- | ---------------- |
| errors.ErrorMessage | 400, 401, 402, 403, 409, 429, 500, 503 | application/json |
| errors.SDKError     | 4XX, 5XX                               | \*/\*            |

### Example

```python
from codat_platform import CodatPlatform
from codat_platform.models import errors, shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:
    res = None
    try:
        res = codat_platform.settings.create_api_key(request={
            "name": "azure-invoice-finance-processor",
        })

        if res is not None:
            # handle response
            pass

    except errors.ErrorMessage as e:
        # handle e.data: errors.ErrorMessageData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:
    res = codat_platform.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    if res is not None:
        # handle response
        pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from codat_platform import CodatPlatform
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatPlatform(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_platform import CodatPlatform
from codat_platform.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CodatPlatform(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type   | Scheme  |
| ------------- | ------ | ------- |
| `auth_header` | apiKey | API key |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_platform:
    res = codat_platform.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    if res is not None:
        # handle response
        pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_platform import CodatPlatform
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatPlatform(debug_logger=logging.getLogger("codat_platform"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

<!-- Start Codat Support Notes -->
## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
<!-- End Codat Support Notes -->

<!-- Start Codat Generated By -->
### Library generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
<!-- End Codat Generated By -->