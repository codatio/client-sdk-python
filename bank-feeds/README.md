# Bank Feeds

<!-- Start Codat Library Description -->
﻿Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Bank Feeds API: Bank Feeds API enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.

A bank feed is a connection between a source bank account in your application and a target bank account in a supported accounting software.

[Explore product](https://docs.codat.io/bank-feeds-api/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

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
  * [Debugging](#debugging)
  * [Support](#support)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

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
from decimal import Decimal

with CodatBankFeeds() as codat_bank_feeds:

    codat_bank_feeds.bank_feeds_source_account_connected(request={
        "event_type": "bankFeeds.sourceAccount.connected",
        "generated_date": "2022-10-23T00:00:00Z",
        "id": "ba29118f-5406-4e59-b05c-ba307ca38d01",
        "payload": {
            "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
            "reference_company": {
                "description": "Requested early access to the new financing scheme.",
                "id": "0498e921-9b53-4396-a412-4f2f5983b0a2",
                "links": {
                    "portal": "https://app.codat.io/companies/0498e921-9b53-4396-a412-4f2f5983b0a2/summary",
                },
                "name": "Toft stores",
            },
            "source_account": {
                "id": "acc-002",
                "account_name": "account-081",
                "account_number": "12345678",
                "balance": Decimal("99.99"),
                "currency": "GBP",
                "modified_date": "2023-01-09T14:14:14.105Z",
                "sort_code": "040004",
                "status": shared.Status.PENDING,
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
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared
from decimal import Decimal

async def main():
    async with CodatBankFeeds() as codat_bank_feeds:

        await codat_bank_feeds.bank_feeds_source_account_connected_async(request={
            "event_type": "bankFeeds.sourceAccount.connected",
            "generated_date": "2022-10-23T00:00:00Z",
            "id": "ba29118f-5406-4e59-b05c-ba307ca38d01",
            "payload": {
                "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
                "reference_company": {
                    "description": "Requested early access to the new financing scheme.",
                    "id": "0498e921-9b53-4396-a412-4f2f5983b0a2",
                    "links": {
                        "portal": "https://app.codat.io/companies/0498e921-9b53-4396-a412-4f2f5983b0a2/summary",
                    },
                    "name": "Toft stores",
                },
                "source_account": {
                    "id": "acc-002",
                    "account_name": "account-081",
                    "account_number": "12345678",
                    "balance": Decimal("99.99"),
                    "currency": "GBP",
                    "modified_date": "2023-01-09T14:14:14.105Z",
                    "sort_code": "040004",
                    "status": shared.Status.PENDING,
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

### [account_mapping](docs/sdks/accountmapping/README.md)

* [create](docs/sdks/accountmapping/README.md#create) - Create bank feed account mapping
* [get](docs/sdks/accountmapping/README.md#get) - List bank feed accounts

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_model](docs/sdks/bankaccounts/README.md#get_create_model) - Get create/update bank account model
* [list](docs/sdks/bankaccounts/README.md#list) - List bank accounts


### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [get_access_token](docs/sdks/companies/README.md#get_access_token) - Get company access token
* [list](docs/sdks/companies/README.md#list) - List companies
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [update](docs/sdks/companies/README.md#update) - Update company

### [company_information](docs/sdks/companyinformation/README.md)

* [get](docs/sdks/companyinformation/README.md#get) - Get company information

### [configuration](docs/sdks/configuration/README.md)

* [get](docs/sdks/configuration/README.md#get) - Get configuration
* [set](docs/sdks/configuration/README.md#set) - Set configuration

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [source_accounts](docs/sdks/sourceaccounts/README.md)

* [create](docs/sdks/sourceaccounts/README.md#create) - Create single source account
* [create_batch](docs/sdks/sourceaccounts/README.md#create_batch) - Create source accounts
* [delete](docs/sdks/sourceaccounts/README.md#delete) - Delete source account
* [delete_credentials](docs/sdks/sourceaccounts/README.md#delete_credentials) - Delete all source account credentials
* [generate_credentials](docs/sdks/sourceaccounts/README.md#generate_credentials) - Generate source account credentials
* [list](docs/sdks/sourceaccounts/README.md#list) - List source accounts
* [update](docs/sdks/sourceaccounts/README.md#update) - Update source account

### [sync](docs/sdks/sync/README.md)

* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Get last successful sync

### [transactions](docs/sdks/transactions/README.md)

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

    assert res is not None

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

    assert res is not None

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type          | Status Code             | Content Type     |
| ------------------- | ----------------------- | ---------------- |
| errors.ErrorMessage | 400, 401, 402, 403, 429 | application/json |
| errors.ErrorMessage | 500, 503                | application/json |
| errors.SDKError     | 4XX, 5XX                | \*/\*            |

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

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
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

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

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