# Sync for Expenses

Embedded accounting integrations for corporate card providers.

## Summary

Expenses: The API for Codat's Expenses solution.

Expenses is an API and a set of supporting tools. It has been built to enable corporate card and expense management platforms to provide high-quality integrations with multiple accounting software through a standardized API.

[Explore solution](https://docs.codat.io/sync-for-expenses/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

Not seeing the endpoints you're expecting? We've [reorganized our solutions](https://docs.codat.io/updates/230901-new-products), and you may be using a [different version of Expenses](https://docs.codat.io/sync-for-expenses-v1-api#/).

## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Configuration | View and manage mapping configuration and defaults for expense transactions. |
| Sync | Monitor the status of data syncs. |
| Expenses | Create and update transactions that represent your customers' spend. |
| Transfers | Create and update transactions that represent the movement of your customers' money. |
| Reimbursements | Create and update transactions that represent your customers' repayable spend. |
| Attachments | Attach receipts to a transaction for a complete audit trail. |
| Transaction status | Monitor the status of individual transactions in data syncs. |
| Manage data | Control and monitor the retrieval of data from an integration. |
| Push operations | View historic push operations. |
| Accounts | Create accounts and view account schemas. |
| Customers | Get, create, and update customers. |
| Suppliers | Get, create, and update suppliers. |

## Table of Contents

* [Summary](#summary)
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
uv add codat-sync-for-expenses
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-sync-for-expenses
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-sync-for-expenses
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from codat-sync-for-expenses python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "codat-sync-for-expenses",
# ]
# ///

from codat_sync_for_expenses import CodatSyncExpenses

sdk = CodatSyncExpenses(
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
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.companies.list(request={
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
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

async def main():

    async with CodatSyncExpenses(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_expenses:

        res = await codat_sync_expenses.companies.list_async(request={
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

### [Accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model

### [Adjustments](docs/sdks/adjustments/README.md)

* [create](docs/sdks/adjustments/README.md#create) - Create adjustment transaction

### [Attachments](docs/sdks/attachments/README.md)

* [upload](docs/sdks/attachments/README.md#upload) - Upload attachment

### [BankAccounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_model](docs/sdks/bankaccounts/README.md#get_create_model) - Get create bank account model

### [Companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [replace](docs/sdks/companies/README.md#replace) - Replace company
* [update](docs/sdks/companies/README.md#update) - Update company

### [CompanyInfo](docs/sdks/companyinfo/README.md)

* [get](docs/sdks/companyinfo/README.md#get) - Get company info

### [Configuration](docs/sdks/configuration/README.md)

* [get](docs/sdks/configuration/README.md#get) - Get company configuration
* [set](docs/sdks/configuration/README.md#set) - Set company configuration

### [Connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [create_partner_expense_connection](docs/sdks/connections/README.md#create_partner_expense_connection) - Create partner expense connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [Customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [get](docs/sdks/customers/README.md#get) - Get customer
* [list](docs/sdks/customers/README.md#list) - List customers
* [update](docs/sdks/customers/README.md#update) - Update customer

### [Expenses](docs/sdks/expenses/README.md)

* [create](docs/sdks/expenses/README.md#create) - Create expense transaction
* [update](docs/sdks/expenses/README.md#update) - Update expense transactions

### [ManageData](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [MappingOptions](docs/sdks/mappingoptions/README.md)

* [get_mapping_options](docs/sdks/mappingoptions/README.md#get_mapping_options) - Mapping options

### [PushOperations](docs/sdks/pushoperations/README.md)

* [get](docs/sdks/pushoperations/README.md#get) - Get push operation
* [list](docs/sdks/pushoperations/README.md#list) - List push operations

### [Reimbursements](docs/sdks/reimbursements/README.md)

* [create](docs/sdks/reimbursements/README.md#create) - Create reimbursable expense transaction
* [update](docs/sdks/reimbursements/README.md#update) - Update reimbursable expense transaction

### [Suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [Sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [list](docs/sdks/sync/README.md#list) - List sync statuses

### [TransactionStatus](docs/sdks/transactionstatus/README.md)

* [get](docs/sdks/transactionstatus/README.md#get) - Get sync transaction
* [list](docs/sdks/transactionstatus/README.md#list) - List sync transactions

### [Transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer transaction

</details>

## File uploads

Certain SDK methods accept files as part of a multi-part request. Pass each file as its name and its contents in bytes. The following example demonstrates how to attach a file to a request.

```python
from pathlib import Path
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.attachments.upload(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "sync_id": "6fb40d5e-b13e-11ed-afa1-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
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
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from codat_sync_for_expenses.utils import BackoffStrategy, RetryConfig


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)
```

If you'd like to override the default retry strategy for all operations, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from codat_sync_for_expenses.utils import BackoffStrategy, RetryConfig


with CodatSyncExpenses(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Error Handling

[`CodatSyncExpensesError`](./src/codat_sync_for_expenses/models/errors/codatsyncexpenseserror.py) is the base class for all HTTP error responses. It has the following properties:

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
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import errors, shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:
    res = None
    try:

        res = codat_sync_expenses.companies.list(request={
            "order_by": "-modifiedDate",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "tags": "region=uk && team=invoice-finance",
        })

        # Handle response
        print(res)

    except errors.CodatSyncExpensesError as e:
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
* [`CodatSyncExpensesError`](./src/codat_sync_for_expenses/models/errors/codatsyncexpenseserror.py): The base class for HTTP error responses.
  * [`ErrorMessage`](./src/codat_sync_for_expenses/models/errors/errormessage.py): A Codat API error response. Its structured fields are on `err.data`.

<details><summary>Less common errors (2)</summary>

<br />

**Inherit from [`CodatSyncExpensesError`](./src/codat_sync_for_expenses/models/errors/codatsyncexpenseserror.py)**:
* [`SDKError`](./src/codat_sync_for_expenses/models/errors/sdkerror.py): The fallback error class if no more specific error class is matched.
* [`ResponseValidationError`](./src/codat_sync_for_expenses/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

Network failures, such as a refused connection or a timeout, are raised by the underlying HTTP library: `urllib3` by default, or `httpx` when you pass `client`.

## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.companies.list(request={
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
from codat_sync_for_expenses import CodatSyncExpenses
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatSyncExpenses(client=http_client)
```

or you could subclass `httpx.Client` to wrap each request in your own custom logic:
```python
from codat_sync_for_expenses import CodatSyncExpenses
import httpx


class CustomClient(httpx.Client):
    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"
        return super().send(request, **kwargs)


s = CodatSyncExpenses(client=CustomClient())
```

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type   | Scheme  |
| ------------- | ------ | ------- |
| `auth_header` | apiKey | API key |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)
```

## Resource Management

The `CodatSyncExpenses` class implements the context manager protocol, so existing code that uses it in a `with` or `async with` block keeps working. Leaving the context does not close any HTTP connections: if you pass your own `client`, close it yourself when you are done. In longer-lived programs, create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
def main():

    with CodatSyncExpenses(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_expenses:
        # Rest of application here...
        pass


# Or when using async:
async def amain():

    async with CodatSyncExpenses(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_expenses:
        # Rest of application here...
        pass
```

## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by contacting your dedicated Codat representative or reaching out to our [support team](mailto:support@codat.io).
We're here to help ensure a smooth experience for you.
