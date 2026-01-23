# Bank Feeds

<!-- Start Codat Library Description -->
﻿Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Bank Feeds: Bank Feeds solution enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.

A bank feed is a connection between a source bank account in your application and a target bank account in a supported accounting software.

[Explore solution](https://docs.codat.io/bank-feeds-api/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

---
<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Source accounts | Provide and manage lists of source bank accounts. |
| Account mapping | Extra functionality for building an account management UI. |
| Company information | Get detailed information about a company from the underlying platform. |
| Transactions | Create new bank account transactions for a company's connections, and see previous operations. |
<!-- End Codat Tags Table -->
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Bank Feeds](#bank-feeds)
  * [Endpoints](#endpoints)
  * [SDK Installation](#sdk-installation)
  * [Example Usage](#example-usage)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
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
uv add codat-bankfeeds
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-bankfeeds
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-bankfeeds
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-bankfeeds python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "codat-bankfeeds",
# ]
# ///

from codat_bankfeeds import CodatBankFeeds

sdk = CodatBankFeeds(
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
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared

async def main():

    async with CodatBankFeeds(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_bank_feeds:

        res = await codat_bank_feeds.companies.create_async(request={
            "name": "Technicalium",
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

### [AccountMapping](docs/sdks/accountmapping/README.md)

* [create](docs/sdks/accountmapping/README.md#create) - Create bank feed account mapping
* [get](docs/sdks/accountmapping/README.md#get) - List bank feed accounts

### [BankAccounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_model](docs/sdks/bankaccounts/README.md#get_create_model) - Get create/update bank account model
* [list](docs/sdks/bankaccounts/README.md#list) - List bank accounts

### [Companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [get_access_token](docs/sdks/companies/README.md#get_access_token) - Get company access token
* [list](docs/sdks/companies/README.md#list) - List companies
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [update](docs/sdks/companies/README.md#update) - Update company

### [CompanyInformation](docs/sdks/companyinformation/README.md)

* [get](docs/sdks/companyinformation/README.md#get) - Get company information

### [Connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [ManagedBankFeeds](docs/sdks/managedbankfeeds/README.md)

* [get_latest_sync](docs/sdks/managedbankfeeds/README.md#get_latest_sync) - Get latest sync
* [get_sync](docs/sdks/managedbankfeeds/README.md#get_sync) - Get sync
* [run_ad_hoc_sync](docs/sdks/managedbankfeeds/README.md#run_ad_hoc_sync) - Run ad-hoc sync

### [SourceAccounts](docs/sdks/sourceaccounts/README.md)

* [create](docs/sdks/sourceaccounts/README.md#create) - Create single source account
* [create_batch](docs/sdks/sourceaccounts/README.md#create_batch) - Create source accounts
* [delete](docs/sdks/sourceaccounts/README.md#delete) - Delete source account
* [delete_credentials](docs/sdks/sourceaccounts/README.md#delete_credentials) - Delete all source account credentials
* [generate_credentials](docs/sdks/sourceaccounts/README.md#generate_credentials) - Generate source account credentials
* [list](docs/sdks/sourceaccounts/README.md#list) - List source accounts
* [update](docs/sdks/sourceaccounts/README.md#update) - Update source account

### [Transactions](docs/sdks/transactions/README.md)

* [create](docs/sdks/transactions/README.md#create) - Create bank transactions
* [get_create_model](docs/sdks/transactions/README.md#get_create_model) - Get create bank transactions model
* [get_create_operation](docs/sdks/transactions/README.md#get_create_operation) - Get create operation
* [list_create_operations](docs/sdks/transactions/README.md#list_create_operations) - List create operations

</details>
<!-- End Available Resources and Operations [operations] -->





<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.source_accounts.generate_credentials(request={
        "request_body": open("example.file", "rb"),
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared
from codat_bankfeeds.utils import BackoffStrategy, RetryConfig


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared
from codat_bankfeeds.utils import BackoffStrategy, RetryConfig


with CodatBankFeeds(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->



<!-- Start Error Handling [errors] -->
## Error Handling

[`CodatBankFeedsError`](./src/codat_bankfeeds/models/errors/codatbankfeedserror.py) is the base class for all HTTP error responses. It has the following properties:

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
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import errors, shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:
    res = None
    try:

        res = codat_bank_feeds.companies.create(request={
            "name": "Technicalium",
        })

        # Handle response
        print(res)


    except errors.CodatBankFeedsError as e:
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
* [`CodatBankFeedsError`](./src/codat_bankfeeds/models/errors/codatbankfeedserror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](./src/codat_bankfeeds/models/errors/errormessage.py): Your `query` parameter was not correctly formed.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`CodatBankFeedsError`](./src/codat_bankfeeds/models/errors/codatbankfeedserror.py)**:
* [`ResponseValidationError`](./src/codat_bankfeeds/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
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
from codat_bankfeeds import CodatBankFeeds
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatBankFeeds(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.httpclient import AsyncHttpClient
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

s = CodatBankFeeds(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CodatBankFeeds` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared
def main():

    with CodatBankFeeds(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_bank_feeds:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CodatBankFeeds(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_bank_feeds:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from codat_bankfeeds import CodatBankFeeds
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatBankFeeds(debug_logger=logging.getLogger("codat_bankfeeds"))
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