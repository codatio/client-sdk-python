# Sync for Payables

<!-- Start Codat Library Description -->
Streamline your customers' accounts payable workflow.
<!-- End Codat Library Description -->

<!-- Start Summary [summary] -->
## Summary

Sync for Payables: The API for Sync for Payables. 

Sync for Payables is an API and a set of supporting tools built to help integrate with your customers' accounting software, and keep their supplier information, invoices, and payments in sync.

[Explore product](https://docs.codat.io/payables/overview) | [See OpenAPI spec](https://github.com/codatio/oas)

---
<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Companies | Create and manage your SMB users' companies. |
| Connections | Create new and manage existing data connections for a company. |
| Accounts | Get, create, and update Accounts. |
| Bank accounts | Get, create, and update Bank accounts. |
| Bills | Get, create, and update Bills. |
| Bill credit notes | Get, create, and update Bill credit notes. |
| Bill payments | Get, create, and update Bill payments. |
| Journals | Get, create, and update Journals. |
| Journal entries | Get, create, and update Journal entries. |
| Payment methods | Get, create, and update Payment methods. |
| Suppliers | Get, create, and update Suppliers. |
| Tax rates | Get, create, and update Tax rates. |
| Tracking categories | Get, create, and update Tracking categories. |
| Company info | View company profile from the source platform. |
| Push operations | View historic push operations. |
| Manage data | Control how data is retrieved from an integration. |
<!-- End Codat Tags Table -->
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

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
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install codat-sync-for-payables-version-1
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-sync-for-payables-version-1
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
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

async def main():
    s = CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    )
    res = await s.companies.create_async(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get](docs/sdks/accounts/README.md#get) - Get account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model
* [list](docs/sdks/accounts/README.md#list) - List accounts

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get_create_model](docs/sdks/bankaccounts/README.md#get_create_model) - Get create/update bank account model

### [bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [create](docs/sdks/billcreditnotes/README.md#create) - Create bill credit note
* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [get_create_update_model](docs/sdks/billcreditnotes/README.md#get_create_update_model) - Get create/update bill credit note model
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes
* [update](docs/sdks/billcreditnotes/README.md#update) - Update bill credit note

### [bill_payments](docs/sdks/billpayments/README.md)

* [create](docs/sdks/billpayments/README.md#create) - Create bill payments
* [delete](docs/sdks/billpayments/README.md#delete) - Delete bill payment
* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [get_create_model](docs/sdks/billpayments/README.md#get_create_model) - Get create bill payment model
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

### [bills](docs/sdks/bills/README.md)

* [create](docs/sdks/bills/README.md#create) - Create bill
* [delete](docs/sdks/bills/README.md#delete) - Delete bill
* [delete_attachment](docs/sdks/bills/README.md#delete_attachment) - Delete bill attachment
* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [get_create_update_model](docs/sdks/bills/README.md#get_create_update_model) - Get create/update bill model
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments
* [update](docs/sdks/bills/README.md#update) - Update bill
* [upload_attachment](docs/sdks/bills/README.md#upload_attachment) - Upload bill attachment


### [companies](docs/sdks/companies/README.md)

* [create](docs/sdks/companies/README.md#create) - Create company
* [delete](docs/sdks/companies/README.md#delete) - Delete a company
* [get](docs/sdks/companies/README.md#get) - Get company
* [list](docs/sdks/companies/README.md#list) - List companies
* [update](docs/sdks/companies/README.md#update) - Update company

### [company_info](docs/sdks/companyinfo/README.md)

* [get_accounting_profile](docs/sdks/companyinfo/README.md#get_accounting_profile) - Get company accounting profile

### [connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [delete](docs/sdks/connections/README.md#delete) - Delete connection
* [get](docs/sdks/connections/README.md#get) - Get connection
* [list](docs/sdks/connections/README.md#list) - List connections
* [unlink](docs/sdks/connections/README.md#unlink) - Unlink connection

### [journal_entries](docs/sdks/journalentries/README.md)

* [create](docs/sdks/journalentries/README.md#create) - Create journal entry
* [get_create_model](docs/sdks/journalentries/README.md#get_create_model) - Get create journal entry model

### [journals](docs/sdks/journals/README.md)

* [create](docs/sdks/journals/README.md#create) - Create journal
* [get](docs/sdks/journals/README.md#get) - Get journal
* [get_create_model](docs/sdks/journals/README.md#get_create_model) - Get create journal model
* [list](docs/sdks/journals/README.md#list) - List journals

### [manage_data](docs/sdks/managedata/README.md)

* [get](docs/sdks/managedata/README.md#get) - Get data status
* [get_pull_operation](docs/sdks/managedata/README.md#get_pull_operation) - Get pull operation
* [list_pull_operations](docs/sdks/managedata/README.md#list_pull_operations) - List pull operations
* [refresh_all_data_types](docs/sdks/managedata/README.md#refresh_all_data_types) - Refresh all data
* [refresh_data_type](docs/sdks/managedata/README.md#refresh_data_type) - Refresh data type

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [push_operations](docs/sdks/pushoperations/README.md)

* [get](docs/sdks/pushoperations/README.md#get) - Get push operation
* [list](docs/sdks/pushoperations/README.md#list) - List push operations

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_create_update_model](docs/sdks/suppliers/README.md#get_create_update_model) - Get create/update supplier model
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [tax_rates](docs/sdks/taxrates/README.md)

* [get](docs/sdks/taxrates/README.md#get) - Get tax rate
* [list](docs/sdks/taxrates/README.md#list) - List all tax rates

### [tracking_categories](docs/sdks/trackingcategories/README.md)

* [get](docs/sdks/trackingcategories/README.md#get) - Get tracking categories
* [list](docs/sdks/trackingcategories/README.md#list) - List tracking categories

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
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

s.bills.upload_attachment(request={
    "bill_id": "EILBDVJVNUAGVKRQ",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

# Use the SDK ...

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared
from codatsyncpayables.utils import BackoffStrategy, RetryConfig

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared
from codatsyncpayables.utils import BackoffStrategy, RetryConfig

s = CodatSyncPayables(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

### Example

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import errors, shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = None
try:
    res = s.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
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

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.codat.io` | None |

#### Example

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
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
from codat_sync_for_payables_version_1 import CodatSyncPayables
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatSyncPayables(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.httpclient import AsyncHttpClient
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

s = CodatSyncPayables(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
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
from codat_sync_for_payables_version_1 import CodatSyncPayables
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatSyncPayables(debug_logger=logging.getLogger("codat_sync_for_payables_version_1"))
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