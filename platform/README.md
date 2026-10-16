# Platform

Manage the building blocks of Codat, including companies, connections, and more.

## Summary

Platform API: An API for the common components of all of Codat's products.

These end points cover creating and managing your companies, data connections, and integrations.

[Explore solution](https://docs.codat.io/core-concepts/companies) | [See OpenAPI spec](https://github.com/codatio/oas)

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

## Table of Contents

* [Summary](#summary)
* [Endpoints](#endpoints)
* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Resource Management](#resource-management)
* [Support](#support)

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

## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)

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

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
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

        res = await cp_client.companies.list_async(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
        })

        # Handle response
        print(res)

asyncio.run(main())
```

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
* [rotate_zapier_key](docs/sdks/webhooks/README.md#rotate_zapier_key) - Rotate Zapier key

</details>

## Retries

Every operation in this SDK retries failed requests with a default backoff strategy. By default it retries connection errors and responses with status 408, 429 or 5XX, starting at 500 ms and backing off by a factor of 1.5 up to 60 s between attempts, for at most an hour. You can override the retry strategy for a single call, or across the entire SDK.

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

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations, you can use the `retry_config` optional parameter when initializing the SDK:
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

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Error Handling

[`CodatPlatformError`](./src/codat_platform/models/errors/codatplatformerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type                  | Description                                                                             |
| ------------------ | --------------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`                 | Error message                                                                           |
| `err.status_code`  | `int`                 | HTTP response status code eg `404`                                                      |
| `err.headers`      | `Mapping[str, str]`   | HTTP response headers, looked up case-insensitively                                     |
| `err.body`         | `str`                 | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `Any`                 | The SDK exception or response the error was built from; prefer the properties above     |
| `err.data`         |                       | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

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

        res = cp_client.companies.list(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
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
  * [`ErrorMessage`](./src/codat_platform/models/errors/errormessage.py): A Codat API error response. Its structured fields are on `err.data`.

<details><summary>Less common errors (2)</summary>

<br />

**Inherit from [`CodatPlatformError`](./src/codat_platform/models/errors/codatplatformerror.py)**:
* [`SDKError`](./src/codat_platform/models/errors/sdkerror.py): The fallback error class if no more specific error class is matched.
* [`ResponseValidationError`](./src/codat_platform/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

Network failures, such as a refused connection or a timeout, are raised by the underlying HTTP library: `urllib3` by default, or `httpx` when you pass `client`.

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

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Custom HTTP Client

The Python SDK can make its API calls through an [httpx](https://www.python-httpx.org/) client you provide. This is a convenient way to configure cookies, proxies, custom headers, and other low-level settings. Pass an `httpx.Client` instance as the `client` parameter when initializing the SDK. It carries every request, including those made by the `_async` methods. The `async_client` parameter is accepted for compatibility with earlier SDK versions but is not used.

The SDK sets the timeout of every request itself, so a timeout configured on the `httpx.Client` is overridden. Use the `timeout_ms` parameter instead, when initializing the SDK or on a single call. The default is 5000 ms.

For example, you could specify a header for every request that this SDK makes as follows:
```python
from codat_platform import CodatPlatform
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatPlatform(client=http_client)
```

or you could subclass `httpx.Client` to wrap each request in your own custom logic:
```python
from codat_platform import CodatPlatform
import httpx


class CustomClient(httpx.Client):
    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"
        return super().send(request, **kwargs)


s = CodatPlatform(client=CustomClient())
```

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

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Resource Management

The `CodatPlatform` class implements the context manager protocol, so existing code that uses it in a `with` or `async with` block keeps working. Leaving the context does not close any HTTP connections: if you pass your own `client`, close it yourself when you are done. In longer-lived programs, create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

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
        pass


# Or when using async:
async def amain():

    async with CodatPlatform(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as cp_client:
        # Rest of application here...
        pass
```

## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
