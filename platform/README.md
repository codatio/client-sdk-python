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
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Support](#support)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add codat-platform
```

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

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-platform python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "codat-platform",
# ]
# ///

from codat_platform import CodatPlatform

sdk = CodatPlatform(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
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


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from codat_platform import CodatPlatform
from codat_platform.models import shared

async def main():

    async with CodatPlatform(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cp_client:

        res = await cp_client.settings.create_api_key_async(request={
            "name": "azure-invoice-finance-processor",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Companies](docs/sdks/companies/README.md)

* [add_product](docs/sdks/companies/README.md#add_product) - Add product
* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [get_access_token](docs/sdks/companies/README.md#get_access_token) - Get company access token
* [get_company_sync_settings](docs/sdks/companies/README.md#get_company_sync_settings) - Get company sync settings
* [list](docs/sdks/companies/README.md#list) - List companies
* [refresh_product_data](docs/sdks/companies/README.md#refresh_product_data) - Refresh product data
* [remove_product](docs/sdks/companies/README.md#remove_product) - Remove product
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [set_company_sync_settings](docs/sdks/companies/README.md#set_company_sync_settings) - Set company sync settings
* [update](docs/sdks/companies/README.md#update) - Update company

### [~~ConnectionManagement~~](docs/sdks/connectionmanagement/README.md)

* [~~get~~](docs/sdks/connectionmanagement/README.md#get) - Get access token (old) :warning: **Deprecated** Use [get_access_token](docs/sdks/companies/README.md#get_access_token) instead.

### [Connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection
* [update_authorization](docs/sdks/connections/README.md#update_authorization) - Update authorization

### [~~Cors~~](docs/sdks/cors/README.md)

* [~~get~~](docs/sdks/cors/README.md#get) - Get CORS settings (old) :warning: **Deprecated** Use [get](docs/sdks/settings/README.md#get) instead.
* [~~set~~](docs/sdks/cors/README.md#set) - Set CORS settings (old) :warning: **Deprecated** Use [set](docs/sdks/settings/README.md#set) instead.

### [CustomDataType](docs/sdks/customdatatype/README.md)

* [configure](docs/sdks/customdatatype/README.md#configure) - Configure custom data type
* [get_configuration](docs/sdks/customdatatype/README.md#get_configuration) - Get custom data configuration
* [list](docs/sdks/customdatatype/README.md#list) - List custom data type records
* [refresh](docs/sdks/customdatatype/README.md#refresh) - Refresh custom data type

### [Integrations](docs/sdks/integrations/README.md)

* [get](docs/sdks/integrations/README.md#get) - Get integration
* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding
* [list](docs/sdks/integrations/README.md#list) - List integrations

### [PushData](docs/sdks/pushdata/README.md)

* [get_model_options](docs/sdks/pushdata/README.md#get_model_options) - Get push options
* [get_operation](docs/sdks/pushdata/README.md#get_operation) - Get push operation
* [list_operations](docs/sdks/pushdata/README.md#list_operations) - List push operations

### [ReadData](docs/sdks/readdata/README.md)

* [get_validation_results](docs/sdks/readdata/README.md#get_validation_results) - Get validation results

### [RefreshData](docs/sdks/refreshdata/README.md)

* [all](docs/sdks/refreshdata/README.md#all) - Refresh all data
* [by_data_type](docs/sdks/refreshdata/README.md#by_data_type) - Refresh data type
* [get](docs/sdks/refreshdata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/refreshdata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/refreshdata/README.md#list_pull_operations) - List pull operations

### [Settings](docs/sdks/settings/README.md)

* [create_api_key](docs/sdks/settings/README.md#create_api_key) - Create API key
* [delete_api_key](docs/sdks/settings/README.md#delete_api_key) - Delete API key
* [get](docs/sdks/settings/README.md#get) - Get CORS settings
* [get_profile](docs/sdks/settings/README.md#get_profile) - Get profile
* [get_sync_settings](docs/sdks/settings/README.md#get_sync_settings) - Get sync settings
* [list_api_keys](docs/sdks/settings/README.md#list_api_keys) - List API keys
* [set](docs/sdks/settings/README.md#set) - Set CORS settings
* [update_profile](docs/sdks/settings/README.md#update_profile) - Update profile
* [update_sync_settings](docs/sdks/settings/README.md#update_sync_settings) - Update all sync settings

### [SupplementalData](docs/sdks/supplementaldata/README.md)

* [configure](docs/sdks/supplementaldata/README.md#configure) - Configure
* [get_configuration](docs/sdks/supplementaldata/README.md#get_configuration) - Get configuration

### [Webhooks](docs/sdks/webhooks/README.md)

* [create_consumer](docs/sdks/webhooks/README.md#create_consumer) - Create webhook consumer
* [delete_consumer](docs/sdks/webhooks/README.md#delete_consumer) - Delete webhook consumer
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
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

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
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`CodatPlatformError`](./src/codat_platform/models/errors/codatplatformerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from codat_platform import CodatPlatform
from codat_platform.models import errors, shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:
    res = None
    try:

        res = cp_client.settings.create_api_key(request={
            "name": "azure-invoice-finance-processor",
        })

        # Handle response
        print(res)


    except errors.CodatPlatformError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorMessage):
            print(e.data.can_be_retried)  # Optional[str]
            print(e.data.correlation_id)  # Optional[str]
            print(e.data.detailed_error_code)  # Optional[int]
            print(e.data.error)  # Optional[str]
            print(e.data.service)  # Optional[str]
```

### Error Classes
**Primary errors:**
* [`CodatPlatformError`](./src/codat_platform/models/errors/codatplatformerror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](./src/codat_platform/models/errors/errormessage.py): Your API request was not properly authorized.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CodatPlatformError`](./src/codat_platform/models/errors/codatplatformerror.py)**:
* [`ResponseValidationError`](./src/codat_platform/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

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
) as cp_client:

    res = cp_client.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CodatPlatform` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_platform import CodatPlatform
from codat_platform.models import shared
def main():

    with CodatPlatform(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cp_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CodatPlatform(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cp_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

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