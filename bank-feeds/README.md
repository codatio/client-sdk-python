# Bank Feeds

Bank Feeds solution enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.

## Summary

Bank Feeds: Bank Feeds solution enables your SMB users to set up bank feeds from accounts in your application to supported accounting software.

A bank feed is a connection between a source bank account in your application and a target bank account in a supported accounting software.

[Explore solution](https://docs.codat.io/bank-feeds-api/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Source accounts | Provide and manage lists of source bank accounts. |
| Account mapping | Extra functionality for building an account management UI. |
| Company information | Get detailed information about a company from the underlying platform. |
| Transactions | Create new bank account transactions for a company's connections, and see previous operations. |

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
# requires-python = ">=3.10"
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

## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)

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
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
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
            "description": "Requested early access to the new financing scheme.",
            "name": "Bank of Dave",
        })

        # Handle response
        print(res)

asyncio.run(main())
```

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
* [generate_otp](docs/sdks/sourceaccounts/README.md#generate_otp) - Generate one-time password
* [list](docs/sdks/sourceaccounts/README.md#list) - List source accounts
* [update](docs/sdks/sourceaccounts/README.md#update) - Update source account

### [Transactions](docs/sdks/transactions/README.md)

* [create](docs/sdks/transactions/README.md#create) - Create bank transactions
* [get_create_model](docs/sdks/transactions/README.md#get_create_model) - Get create bank transactions model
* [get_create_operation](docs/sdks/transactions/README.md#get_create_operation) - Get create operation
* [list_create_operations](docs/sdks/transactions/README.md#list_create_operations) - List create operations

</details>

## Retries

Every operation in this SDK retries failed requests with a default backoff strategy. By default it retries connection errors and responses with status 408, 429 or 5XX, starting at 500 ms and backing off by a factor of 1.5 up to 60 s between attempts, for at most an hour. You can override the retry strategy for a single call, or across the entire SDK.

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
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations, you can use the `retry_config` optional parameter when initializing the SDK:
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
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    })

    # Handle response
    print(res)
```

## Error Handling

[`CodatBankFeedsError`](./src/codat_bankfeeds/models/errors/codatbankfeedserror.py) is the base class for all HTTP error responses. It has the following properties:

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
            "description": "Requested early access to the new financing scheme.",
            "name": "Bank of Dave",
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
  * [`ErrorMessage`](./src/codat_bankfeeds/models/errors/errormessage.py): A Codat API error response. Its structured fields are on `err.data`.

<details><summary>Less common errors (2)</summary>

<br />

**Inherit from [`CodatBankFeedsError`](./src/codat_bankfeeds/models/errors/codatbankfeedserror.py)**:
* [`SDKError`](./src/codat_bankfeeds/models/errors/sdkerror.py): The fallback error class if no more specific error class is matched.
* [`ResponseValidationError`](./src/codat_bankfeeds/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

Network failures, such as a refused connection or a timeout, are raised by the underlying HTTP library: `urllib3` by default, or `httpx` when you pass `client`.

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
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    })

    # Handle response
    print(res)
```

## Custom HTTP Client

The Python SDK can make its API calls through an [httpx](https://www.python-httpx.org/) client you provide. This is a convenient way to configure cookies, proxies, custom headers, and other low-level settings. Pass an `httpx.Client` instance as the `client` parameter when initializing the SDK. It carries every request, including those made by the `_async` methods. The `async_client` parameter is accepted for compatibility with earlier SDK versions but is not used.

The SDK sets the timeout of every request itself, so a timeout configured on the `httpx.Client` is overridden. Use the `timeout_ms` parameter instead, when initializing the SDK or on a single call. The default is 5000 ms.

For example, you could specify a header for every request that this SDK makes as follows:
```python
from codat_bankfeeds import CodatBankFeeds
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatBankFeeds(client=http_client)
```

or you could subclass `httpx.Client` to wrap each request in your own custom logic:
```python
from codat_bankfeeds import CodatBankFeeds
import httpx


class CustomClient(httpx.Client):
    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"
        return super().send(request, **kwargs)


s = CodatBankFeeds(client=CustomClient())
```

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
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    })

    # Handle response
    print(res)
```

## Resource Management

The `CodatBankFeeds` class implements the context manager protocol, so existing code that uses it in a `with` or `async with` block keeps working. Leaving the context does not close any HTTP connections: if you pass your own `client`, close it yourself when you are done. In longer-lived programs, create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

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
        pass


# Or when using async:
async def amain():

    async with CodatBankFeeds(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_bank_feeds:
        # Rest of application here...
        pass
```

## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
