# Accounting

<!-- Start Codat Library Description -->
﻿Codat's Accounting API is a flexible API for pulling and pushing up-to-date accounting data to your customer's accounting software.
It gives you a simple way to view, create, update adn delete data without having to worry about each platform's specific complexities.

<!-- End Codat Library Description -->


<!-- Start Summary [summary] -->
## Summary

Accounting API: > ### New to Codat?
>
> Our Accounting API reference is relevant only to our existing clients.
> Please reach out to your Codat contact so that we can find the right product for you.

A flexible API for pulling accounting data, normalized and aggregated from 20 accounting integrations.

Standardize how you connect to your customers’ accounting software. View, create, update, and delete data in the same way for all the leading accounting software.

<!-- Start Codat Tags Table -->
## Endpoints

| Endpoints | Description |
| :- |:- |
| Accounts | Access standardized Accounts from linked accounting software. |
| Account transactions | Access standardized Account transactions from linked accounting software. |
| Bank accounts | Access standardized Bank accounts from linked accounting software. |
| Bank account transactions | Access standardized Bank transactions for bank accounts from linked accounting software. |
| Bills | Access standardized Bills from linked accounting software. |
| Bill credit notes | Access standardized Bill credit notes from linked accounting software. |
| Bill payments | Access standardized Bill payments from linked accounting software. |
| Credit notes | Access standardized Credit notes from linked accounting software. |
| Customers | Access standardized Customers from linked accounting software. |
| Direct costs | Access standardized Direct costs from linked accounting software. |
| Direct incomes | Access standardized Direct incomes from linked accounting software. |
| Company info | Access standardized Company info from linked accounting software. |
| Invoices | Access standardized Invoices from linked accounting software. |
| Item receipts | Access standardized Item receipts from linked accounting software. |
| Items | Access standardized Items from linked accounting software. |
| Journals | Access standardized Journals from linked accounting software. |
| Journal entries | Access standardized Journal entries from linked accounting software. |
| Payments | Access standardized Payments from linked accounting software. |
| Payment methods | Access standardized Payment methods from linked accounting software. |
| Purchase orders | Access standardized Purchase orders from linked accounting software. |
| Sales orders | Access standardized Sales orders from linked accounting software. |
| Suppliers | Access standardized Suppliers from linked accounting software. |
| Tax rates | Access standardized Tax rates from linked accounting software. |
| Tracking categories | Access standardized Tracking categories from linked accounting software. |
| Transfers | Access standardized Transfers from linked accounting software. |
| Reports | Access standardized Reports from linked accounting software. |
<!-- End Codat Tags Table -->

[Read more...](https://docs.codat.io/accounting-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas)
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
pip install codat-accounting
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add codat-accounting
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

async def main():
    s = CodatAccounting(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    )
    res = await s.account_transactions.get_async(request={
        "account_transaction_id": "<value>",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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

### [account_transactions](docs/sdks/accounttransactions/README.md)

* [get](docs/sdks/accounttransactions/README.md#get) - Get account transaction
* [list](docs/sdks/accounttransactions/README.md#list) - List account transactions

### [accounts](docs/sdks/accounts/README.md)

* [create](docs/sdks/accounts/README.md#create) - Create account
* [get](docs/sdks/accounts/README.md#get) - Get account
* [get_create_model](docs/sdks/accounts/README.md#get_create_model) - Get create account model
* [list](docs/sdks/accounts/README.md#list) - List accounts

### [bank_account_transactions](docs/sdks/bankaccounttransactions/README.md)

* [create](docs/sdks/bankaccounttransactions/README.md#create) - Create bank account transactions
* [get_create_model](docs/sdks/bankaccounttransactions/README.md#get_create_model) - Get create bank account transactions model
* [list](docs/sdks/bankaccounttransactions/README.md#list) - List bank account transactions

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [create](docs/sdks/bankaccounts/README.md#create) - Create bank account
* [get](docs/sdks/bankaccounts/README.md#get) - Get bank account
* [get_create_update_model](docs/sdks/bankaccounts/README.md#get_create_update_model) - Get create/update bank account model
* [list](docs/sdks/bankaccounts/README.md#list) - List bank accounts
* [update](docs/sdks/bankaccounts/README.md#update) - Update bank account

### [bill_credit_notes](docs/sdks/billcreditnotes/README.md)

* [create](docs/sdks/billcreditnotes/README.md#create) - Create bill credit note
* [get](docs/sdks/billcreditnotes/README.md#get) - Get bill credit note
* [get_create_update_model](docs/sdks/billcreditnotes/README.md#get_create_update_model) - Get create/update bill credit note model
* [list](docs/sdks/billcreditnotes/README.md#list) - List bill credit notes
* [update](docs/sdks/billcreditnotes/README.md#update) - Update bill credit note
* [upload_attachment](docs/sdks/billcreditnotes/README.md#upload_attachment) - Upload bill credit note attachment

### [bill_payments](docs/sdks/billpayments/README.md)

* [create](docs/sdks/billpayments/README.md#create) - Create bill payments
* [delete](docs/sdks/billpayments/README.md#delete) - Delete bill payment
* [get](docs/sdks/billpayments/README.md#get) - Get bill payment
* [get_create_model](docs/sdks/billpayments/README.md#get_create_model) - Get create bill payment model
* [list](docs/sdks/billpayments/README.md#list) - List bill payments

### [bills](docs/sdks/bills/README.md)

* [create](docs/sdks/bills/README.md#create) - Create bill
* [delete](docs/sdks/bills/README.md#delete) - Delete bill
* [download_attachment](docs/sdks/bills/README.md#download_attachment) - Download bill attachment
* [get](docs/sdks/bills/README.md#get) - Get bill
* [get_attachment](docs/sdks/bills/README.md#get_attachment) - Get bill attachment
* [get_create_update_model](docs/sdks/bills/README.md#get_create_update_model) - Get create/update bill model
* [list](docs/sdks/bills/README.md#list) - List bills
* [list_attachments](docs/sdks/bills/README.md#list_attachments) - List bill attachments
* [update](docs/sdks/bills/README.md#update) - Update bill
* [upload_attachment](docs/sdks/bills/README.md#upload_attachment) - Upload bill attachment


### [company_info](docs/sdks/companyinfo/README.md)

* [get](docs/sdks/companyinfo/README.md#get) - Get company info
* [refresh](docs/sdks/companyinfo/README.md#refresh) - Refresh company info

### [credit_notes](docs/sdks/creditnotes/README.md)

* [create](docs/sdks/creditnotes/README.md#create) - Create credit note
* [get](docs/sdks/creditnotes/README.md#get) - Get credit note
* [get_create_update_model](docs/sdks/creditnotes/README.md#get_create_update_model) - Get create/update credit note model
* [list](docs/sdks/creditnotes/README.md#list) - List credit notes
* [update](docs/sdks/creditnotes/README.md#update) - Update credit note

### [customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [download_attachment](docs/sdks/customers/README.md#download_attachment) - Download customer attachment
* [get](docs/sdks/customers/README.md#get) - Get customer
* [get_attachment](docs/sdks/customers/README.md#get_attachment) - Get customer attachment
* [get_create_update_model](docs/sdks/customers/README.md#get_create_update_model) - Get create/update customer model
* [list](docs/sdks/customers/README.md#list) - List customers
* [list_attachments](docs/sdks/customers/README.md#list_attachments) - List customer attachments
* [update](docs/sdks/customers/README.md#update) - Update customer

### [direct_costs](docs/sdks/directcosts/README.md)

* [create](docs/sdks/directcosts/README.md#create) - Create direct cost
* [delete](docs/sdks/directcosts/README.md#delete) - Delete direct cost
* [download_attachment](docs/sdks/directcosts/README.md#download_attachment) - Download direct cost attachment
* [get](docs/sdks/directcosts/README.md#get) - Get direct cost
* [get_attachment](docs/sdks/directcosts/README.md#get_attachment) - Get direct cost attachment
* [get_create_model](docs/sdks/directcosts/README.md#get_create_model) - Get create direct cost model
* [list](docs/sdks/directcosts/README.md#list) - List direct costs
* [list_attachments](docs/sdks/directcosts/README.md#list_attachments) - List direct cost attachments
* [upload_attachment](docs/sdks/directcosts/README.md#upload_attachment) - Upload direct cost attachment

### [direct_incomes](docs/sdks/directincomes/README.md)

* [create](docs/sdks/directincomes/README.md#create) - Create direct income
* [download_attachment](docs/sdks/directincomes/README.md#download_attachment) - Download direct income attachment
* [get](docs/sdks/directincomes/README.md#get) - Get direct income
* [get_attachment](docs/sdks/directincomes/README.md#get_attachment) - Get direct income attachment
* [get_create_model](docs/sdks/directincomes/README.md#get_create_model) - Get create direct income model
* [list](docs/sdks/directincomes/README.md#list) - List direct incomes
* [list_attachments](docs/sdks/directincomes/README.md#list_attachments) - List direct income attachments
* [upload_attachment](docs/sdks/directincomes/README.md#upload_attachment) - Create direct income attachment

### [invoices](docs/sdks/invoices/README.md)

* [create](docs/sdks/invoices/README.md#create) - Create invoice
* [delete](docs/sdks/invoices/README.md#delete) - Delete invoice
* [download_attachment](docs/sdks/invoices/README.md#download_attachment) - Download invoice attachment
* [download_pdf](docs/sdks/invoices/README.md#download_pdf) - Get invoice as PDF
* [get](docs/sdks/invoices/README.md#get) - Get invoice
* [get_attachment](docs/sdks/invoices/README.md#get_attachment) - Get invoice attachment
* [get_create_update_model](docs/sdks/invoices/README.md#get_create_update_model) - Get create/update invoice model
* [list](docs/sdks/invoices/README.md#list) - List invoices
* [list_attachments](docs/sdks/invoices/README.md#list_attachments) - List invoice attachments
* [update](docs/sdks/invoices/README.md#update) - Update invoice
* [upload_attachment](docs/sdks/invoices/README.md#upload_attachment) - Upload invoice attachment

### [item_receipts](docs/sdks/itemreceipts/README.md)

* [get](docs/sdks/itemreceipts/README.md#get) - Get item receipt
* [list](docs/sdks/itemreceipts/README.md#list) - List item receipts

### [items](docs/sdks/items/README.md)

* [create](docs/sdks/items/README.md#create) - Create item
* [get](docs/sdks/items/README.md#get) - Get item
* [get_create_model](docs/sdks/items/README.md#get_create_model) - Get create item model
* [list](docs/sdks/items/README.md#list) - List items

### [journal_entries](docs/sdks/journalentries/README.md)

* [create](docs/sdks/journalentries/README.md#create) - Create journal entry
* [delete](docs/sdks/journalentries/README.md#delete) - Delete journal entry
* [get](docs/sdks/journalentries/README.md#get) - Get journal entry
* [get_create_model](docs/sdks/journalentries/README.md#get_create_model) - Get create journal entry model
* [list](docs/sdks/journalentries/README.md#list) - List journal entries

### [journals](docs/sdks/journals/README.md)

* [create](docs/sdks/journals/README.md#create) - Create journal
* [get](docs/sdks/journals/README.md#get) - Get journal
* [get_create_model](docs/sdks/journals/README.md#get_create_model) - Get create journal model
* [list](docs/sdks/journals/README.md#list) - List journals

### [payment_methods](docs/sdks/paymentmethods/README.md)

* [get](docs/sdks/paymentmethods/README.md#get) - Get payment method
* [list](docs/sdks/paymentmethods/README.md#list) - List payment methods

### [payments](docs/sdks/payments/README.md)

* [create](docs/sdks/payments/README.md#create) - Create payment
* [get](docs/sdks/payments/README.md#get) - Get payment
* [get_create_model](docs/sdks/payments/README.md#get_create_model) - Get create payment model
* [list](docs/sdks/payments/README.md#list) - List payments
* [payments](docs/sdks/payments/README.md#payments) - List payments

### [purchase_orders](docs/sdks/purchaseorders/README.md)

* [create](docs/sdks/purchaseorders/README.md#create) - Create purchase order
* [download_attachment](docs/sdks/purchaseorders/README.md#download_attachment) - Download purchase order attachment
* [download_purchase_order_pdf](docs/sdks/purchaseorders/README.md#download_purchase_order_pdf) - Download purchase order as PDF
* [get](docs/sdks/purchaseorders/README.md#get) - Get purchase order
* [get_attachment](docs/sdks/purchaseorders/README.md#get_attachment) - Get purchase order attachment
* [get_create_update_model](docs/sdks/purchaseorders/README.md#get_create_update_model) - Get create/update purchase order model
* [list](docs/sdks/purchaseorders/README.md#list) - List purchase orders
* [list_attachments](docs/sdks/purchaseorders/README.md#list_attachments) - List purchase order attachments
* [update](docs/sdks/purchaseorders/README.md#update) - Update purchase order

### [reports](docs/sdks/reports/README.md)

* [get_aged_creditors_report](docs/sdks/reports/README.md#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](docs/sdks/reports/README.md#get_aged_debtors_report) - Aged debtors report
* [get_balance_sheet](docs/sdks/reports/README.md#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](docs/sdks/reports/README.md#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](docs/sdks/reports/README.md#get_profit_and_loss) - Get profit and loss
* [is_aged_creditors_report_available](docs/sdks/reports/README.md#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](docs/sdks/reports/README.md#is_aged_debtor_report_available) - Aged debtors report available

### [sales_orders](docs/sdks/salesorders/README.md)

* [get](docs/sdks/salesorders/README.md#get) - Get sales order
* [list](docs/sdks/salesorders/README.md#list) - List sales orders

### [suppliers](docs/sdks/suppliers/README.md)

* [create](docs/sdks/suppliers/README.md#create) - Create supplier
* [download_attachment](docs/sdks/suppliers/README.md#download_attachment) - Download supplier attachment
* [get](docs/sdks/suppliers/README.md#get) - Get supplier
* [get_attachment](docs/sdks/suppliers/README.md#get_attachment) - Get supplier attachment
* [get_create_update_model](docs/sdks/suppliers/README.md#get_create_update_model) - Get create/update supplier model
* [list](docs/sdks/suppliers/README.md#list) - List suppliers
* [list_attachments](docs/sdks/suppliers/README.md#list_attachments) - List supplier attachments
* [update](docs/sdks/suppliers/README.md#update) - Update supplier

### [tax_rates](docs/sdks/taxrates/README.md)

* [get](docs/sdks/taxrates/README.md#get) - Get tax rate
* [list](docs/sdks/taxrates/README.md#list) - List all tax rates

### [tracking_categories](docs/sdks/trackingcategories/README.md)

* [get](docs/sdks/trackingcategories/README.md#get) - Get tracking categories
* [list](docs/sdks/trackingcategories/README.md#list) - List tracking categories

### [transfers](docs/sdks/transfers/README.md)

* [create](docs/sdks/transfers/README.md#create) - Create transfer
* [get](docs/sdks/transfers/README.md#get) - Get transfer
* [get_create_model](docs/sdks/transfers/README.md#get_create_model) - Get create transfer model
* [list](docs/sdks/transfers/README.md#list) - List transfers
* [upload_attachment](docs/sdks/transfers/README.md#upload_attachment) - Upload transfer attachment

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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
from codataccounting.utils import BackoffStrategy, RetryConfig

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
},
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
from codataccounting.utils import BackoffStrategy, RetryConfig

s = CodatAccounting(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

### Example

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import errors, shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = None
try:
    res = s.account_transactions.get(request={
        "account_transaction_id": "<value>",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    server_idx=0,
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    server_url="https://api.codat.io",
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
from codat_accounting import CodatAccounting
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CodatAccounting(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from codat_accounting import CodatAccounting
from codat_accounting.httpclient import AsyncHttpClient
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

s = CodatAccounting(async_client=CustomClient(httpx.AsyncClient()))
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
from codat_accounting import CodatAccounting
import logging

logging.basicConfig(level=logging.DEBUG)
s = CodatAccounting(debug_logger=logging.getLogger("codat_accounting"))
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