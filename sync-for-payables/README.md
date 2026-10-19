# Sync for Payables

Streamline your customers' accounts payable workflow.

## Summary

Bill pay (synchronous solution): The API reference for the synchronous Bill Pay solution.

The synchronous Bill Pay solution is an API and a set of supporting tools designed to integrate a bill pay flow into your app as quickly as possible. It's ideal for facilitating essential bill payment processes within your SMB's accounting software.

[Explore solution](https://docs.codat.io/payables/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

## Supported Integrations

| Integration       | Supported |
|-------------------|-----------|
| FreeAgent         | Yes       |
| QuickBooks Online | Yes       |
| Oracle NetSuite   | Yes       |
| Sage Intacct      | Yes       |
| Xero              | Yes       |
| Zoho Books        | Yes       |

## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Company information | View company profile from the source platform. |
| Bills | Get, create, and update Bills. |
| Bill payments | Get, create, and update Bill payments. |
| Suppliers | Get, create, and update Suppliers. |
| Bank accounts | Create a bank account for a given company's connection. |

## Table of Contents

* [Summary](#summary)
* [Supported Integrations](#supported-integrations)
* [Endpoints](#endpoints)
* [SDK Installation](#sdk-installation)
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
uv add codat-sync-for-payables
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-sync-for-payables
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-sync-for-payables
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-sync-for-payables python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "codat-sync-for-payables",
# ]
# ///

from codat_sync_for_payables import CodatSyncPayables

sdk = CodatSyncPayables(
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
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.companies.list(request={
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
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared

async def main():

    async with CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_payables:

        res = await codat_sync_payables.companies.list_async(request={
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

### [BankAccounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account

### [BillPayments](docs/sdks/billpayments/README.md)

* [get_payment_options](docs/sdks/billpayments/README.md#get_payment_options) - Get payment mapping options
* [create](docs/sdks/billpayments/README.md#create) - Create bill payment

### [Bills](docs/sdks/bills/README.md)

* [get_bill_options](docs/sdks/bills/README.md#get_bill_options) - Get bill mapping options
* [list](docs/sdks/bills/README.md#list) - List bills
* [create](docs/sdks/bills/README.md#create) - Create bill
* [update](docs/sdks/bills/README.md#update) - Update bill
* [upload_attachment](docs/sdks/bills/README.md#upload_attachment) - Upload bill attachment
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments
* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment

### [Companies](docs/sdks/companies/README.md)

* [list](docs/sdks/companies/README.md#list) - List companies
* [create](docs/sdks/companies/README.md#create) - Create company
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [update](docs/sdks/companies/README.md#update) - Update company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company

### [CompanyInformation](docs/sdks/companyinformation/README.md)

* [get](docs/sdks/companyinformation/README.md#get) - Get company information

### [Connections](docs/sdks/connections/README.md)

* [list](docs/sdks/connections/README.md#list) - List connections
* [create](docs/sdks/connections/README.md#create) - Create connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [Suppliers](docs/sdks/suppliers/README.md)

* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

</details>

## File uploads

Certain SDK methods accept files as part of a multi-part request. Pass each file as its name and its contents in bytes. The following example demonstrates how to attach a file to a request.

```python
from pathlib import Path
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.upload_attachment(request={
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "attachment_upload": {
            "file": {
                "file_name": "example.file",
                "content": Path("example.file").read_bytes(),
            },
        },
    })

    # Handle response
    print(res)
```

## Retries

Every operation in this SDK retries failed requests with a default backoff strategy. By default it retries connection errors and responses with status 408, 429 or 5XX, starting at 500 ms and backing off by a factor of 1.5 up to 60 s between attempts, for at most an hour. You can override the retry strategy for a single call, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from codat_sync_for_payables.utils import BackoffStrategy, RetryConfig


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from codat_sync_for_payables.utils import BackoffStrategy, RetryConfig


with CodatSyncPayables(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Error Handling

[`CodatSyncPayablesError`](./src/codat_sync_for_payables/models/errors/codatsyncpayableserror.py) is the base class for all HTTP error responses. It has the following properties:

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
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import errors, shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:
    res = None
    try:

        res = codat_sync_payables.companies.list(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
        })

        # Handle response
        print(res)

    except errors.CodatSyncPayablesError as e:
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
* [`CodatSyncPayablesError`](./src/codat_sync_for_payables/models/errors/codatsyncpayableserror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](./src/codat_sync_for_payables/models/errors/errormessage.py): A Codat API error response. Its structured fields are on `err.data`.

<details><summary>Less common errors (2)</summary>

<br />

**Inherit from [`CodatSyncPayablesError`](./src/codat_sync_for_payables/models/errors/codatsyncpayableserror.py)**:
* [`SDKError`](./src/codat_sync_for_payables/models/errors/sdkerror.py): The fallback error class if no more specific error class is matched.
* [`ResponseValidationError`](./src/codat_sync_for_payables/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

Network failures, such as a refused connection or a timeout, are raised by the underlying HTTP library: `urllib3` by default, or `httpx` when you pass `client`.

## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.companies.list(request={
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
from codat_sync_for_payables import CodatSyncPayables
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatSyncPayables(client=http_client)
```

or you could subclass `httpx.Client` to wrap each request in your own custom logic:
```python
from codat_sync_for_payables import CodatSyncPayables
import httpx


class CustomClient(httpx.Client):
    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"
        return super().send(request, **kwargs)


s = CodatSyncPayables(client=CustomClient())
```

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type   | Scheme  |
| ------------- | ------ | ------- |
| `auth_header` | apiKey | API key |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Resource Management

The `CodatSyncPayables` class implements the context manager protocol, so existing code that uses it in a `with` or `async with` block keeps working. Leaving the context does not close any HTTP connections: if you pass your own `client`, close it yourself when you are done. In longer-lived programs, create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
def main():

    with CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_payables:
        # Rest of application here...
        pass


# Or when using async:
async def amain():

    async with CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_payables:
        # Rest of application here...
        pass
```

## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
