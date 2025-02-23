# Sync for Commerce

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for POS and eCommerce software.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Sync for Commerce: The API for Sync for Commerce. 

Sync for Commerce automatically replicates and reconciles sales data from a merchant’s source PoS, Payments, and eCommerce systems into their accounting software. This eliminates manual processing by merchants and transforms their ability to run and grow their business.
  
[Explore solution](https://docs.codat.io/commerce/overview) | [See our OpenAPI spec](https://github.com/codatio/oas)

Not seeing the endpoints you're expecting? We've [reorganized our products](https://docs.codat.io/updates/230901-new-products), and you may be using a [different version of Sync for Commerce](https://docs.codat.io/sync-for-commerce-v1-api#/).

---

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Connections | Create new and manage existing data connections for a company. |
| Sync | Initiate data syncs and monitor their status. |
| Sync flow settings | Control text and visibility settings for the Sync Flow. |
| Integrations | Get a list of integrations supported by Sync for Commerce and their logos. |
| Advanced controls | View and manage mapping configured for a company's commerce sync. |
<!-- End Codat Tags Table -->
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Sync for Commerce](#sync-for-commerce)
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

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-sync-for-commerce
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-sync-for-commerce
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-sync-for-commerce python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "codat-sync-for-commerce",
# ]
# ///

from codat_sync_for_commerce import CodatSyncCommerce

sdk = CodatSyncCommerce(
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
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

with CodatSyncCommerce() as codat_sync_commerce:

    codat_sync_commerce.connection_deleted(request={
        "event_type": "connection.created",
        "generated_date": "2022-10-23T00:00:00Z",
        "id": "ba29118f-5406-4e59-b05c-ba307ca38d01",
        "payload": {
            "connection": {
                "created": "2022-10-23T00:00:00Z",
                "id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
                "integration_id": "fd321cb6-7963-4506-b873-e99593a45e30",
                "integration_key": "dfxm",
                "link_url": "https://link-api.codat.io/companies/86bd88cb-44ab-4dfb-b32f-87b19b14287f/connections/2e2eb431-c1fa-4dc9-93fa-d29781c12bcd/start",
                "platform_name": "Basiq",
                "source_id": "35b92968-9851-4095-ad60-395c95cbcba4",
                "source_type": shared.SourceType.ACCOUNTING,
                "status": shared.DataConnectionStatus.LINKED,
                "data_connection_errors": [
                    {
                        "errored_on_utc": "2022-10-23T00:00:00Z",
                        "resolved_on_utc": "2022-10-23T00:00:00Z",
                    },
                    {
                        "errored_on_utc": "2022-10-23T00:00:00Z",
                        "resolved_on_utc": "2022-10-23T00:00:00Z",
                    },
                ],
                "last_sync": "2022-10-23T00:00:00Z",
            },
            "reference_company": {
                "description": "Requested early access to the new financing scheme.",
                "id": "8a210b68-6988-11ed-a1eb-0242ac120002",
                "name": "Codat Ltd.",
            },
        },
    })

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

async def main():
    async with CodatSyncCommerce() as codat_sync_commerce:

        await codat_sync_commerce.connection_deleted_async(request={
            "event_type": "connection.created",
            "generated_date": "2022-10-23T00:00:00Z",
            "id": "ba29118f-5406-4e59-b05c-ba307ca38d01",
            "payload": {
                "connection": {
                    "created": "2022-10-23T00:00:00Z",
                    "id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
                    "integration_id": "fd321cb6-7963-4506-b873-e99593a45e30",
                    "integration_key": "dfxm",
                    "link_url": "https://link-api.codat.io/companies/86bd88cb-44ab-4dfb-b32f-87b19b14287f/connections/2e2eb431-c1fa-4dc9-93fa-d29781c12bcd/start",
                    "platform_name": "Basiq",
                    "source_id": "35b92968-9851-4095-ad60-395c95cbcba4",
                    "source_type": shared.SourceType.ACCOUNTING,
                    "status": shared.DataConnectionStatus.LINKED,
                    "data_connection_errors": [
                        {
                            "errored_on_utc": "2022-10-23T00:00:00Z",
                            "resolved_on_utc": "2022-10-23T00:00:00Z",
                        },
                        {
                            "errored_on_utc": "2022-10-23T00:00:00Z",
                            "resolved_on_utc": "2022-10-23T00:00:00Z",
                        },
                    ],
                    "last_sync": "2022-10-23T00:00:00Z",
                },
                "reference_company": {
                    "description": "Requested early access to the new financing scheme.",
                    "id": "8a210b68-6988-11ed-a1eb-0242ac120002",
                    "name": "Codat Ltd.",
                },
            },
        })

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

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

### [integrations](docs/sdks/integrations/README.md)

* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding for an integration
* [list](docs/sdks/integrations/README.md#list) - List integrations

### [sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [get_status](docs/sdks/sync/README.md#get_status) - Get sync status
* [list](docs/sdks/sync/README.md#list) - List sync statuses
* [request](docs/sdks/sync/README.md#request) - Initiate new sync
* [request_for_date_range](docs/sdks/sync/README.md#request_for_date_range) - Initiate sync for specific range

### [sync_flow_settings](docs/sdks/syncflowsettings/README.md)

* [get_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#get_config_text_sync_flow) - Get preferences for text fields
* [get_visible_accounts](docs/sdks/syncflowsettings/README.md#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#update_config_text_sync_flow) - Update preferences for text fields
* [update_visible_accounts_sync_flow](docs/sdks/syncflowsettings/README.md#update_visible_accounts_sync_flow) - Update visible accounts

</details>
<!-- End Available Resources and Operations [operations] -->



<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared
from codat_sync_for_commerce.utils import BackoffStrategy, RetryConfig

with CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:

    res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
        "locale": shared.Locale.EN_US,
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared
from codat_sync_for_commerce.utils import BackoffStrategy, RetryConfig

with CodatSyncCommerce(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:

    res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
        "locale": shared.Locale.EN_US,
    })

    assert res is not None

    # Handle response
    print(res)

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_config_text_sync_flow_async` method may raise the following exceptions:

| Error Type          | Status Code        | Content Type     |
| ------------------- | ------------------ | ---------------- |
| errors.ErrorMessage | 401, 402, 403, 429 | application/json |
| errors.ErrorMessage | 500, 503           | application/json |
| errors.SDKError     | 4XX, 5XX           | \*/\*            |

### Example

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import errors, shared

with CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:
    res = None
    try:

        res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
            "locale": shared.Locale.EN_US,
        })

        assert res is not None

        # Handle response
        print(res)

    except errors.ErrorMessage as e:
        # handle e.data: errors.ErrorMessageData
        raise(e)
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

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

with CodatSyncCommerce(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:

    res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
        "locale": shared.Locale.EN_US,
    })

    assert res is not None

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
from codat_sync_for_commerce import CodatSyncCommerce
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatSyncCommerce(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.httpclient import AsyncHttpClient
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

s = CodatSyncCommerce(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

with CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:

    res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
        "locale": shared.Locale.EN_US,
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CodatSyncCommerce` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared
def main():
    with CodatSyncCommerce(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_commerce:
        # Rest of application here...


# Or when using async:
async def amain():
    async with CodatSyncCommerce(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_commerce:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_sync_for_commerce import CodatSyncCommerce
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatSyncCommerce(debug_logger=logging.getLogger("codat_sync_for_commerce"))
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