# Invoices
(*accounts_receivable.invoices*)

## Overview

### Available Operations

* [download_attachment](#download_attachment) - Download invoice attachment
* [download_pdf](#download_pdf) - Get invoice as PDF
* [get](#get) - Get invoice
* [get_attachment](#get_attachment) - Get invoice attachment
* [list](#list) - List invoices
* [list_attachments](#list_attachments) - List invoice attachments
* [list_reconciled](#list_reconciled) - List reconciled invoices

## download_attachment

The *Download invoice attachment* endpoint downloads a specific attachment for a given `invoiceId` and `attachmentId`.

[Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.download_attachment(request={
    "attachment_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "invoice_id": "EILBDVJVNUAGVKRQ",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DownloadAccountingInvoiceAttachmentRequest](../../models/operations/downloadaccountinginvoiceattachmentrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## download_pdf

﻿Download invoice as a pdf.

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.download_pdf(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "invoice_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DownloadAccountingInvoicePdfRequest](../../models/operations/downloadaccountinginvoicepdfrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get

The *Get invoice* endpoint returns a single invoice for a given invoiceId.

[Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).

### Tips and traps

To access the `paymentAllocations` property, ensure that the `payments` data type is queued and cached in Codat before retrieving `invoices` from Codat's cache.


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "invoice_id": "7110701885",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingInvoiceRequest](../../models/operations/getaccountinginvoicerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.AccountingInvoice](../../models/shared/accountinginvoice.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_attachment

The *Get invoice attachment* endpoint returns a specific attachment for a given `invoiceId` and `attachmentId`.

[Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.get_attachment(request={
    "attachment_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "invoice_id": "EILBDVJVNUAGVKRQ",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAccountingInvoiceAttachmentRequest](../../models/operations/getaccountinginvoiceattachmentrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.AccountingAttachment](../../models/shared/accountingattachment.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## list

The *List invoices* endpoint returns a list of [invoices](https://docs.codat.io/lending-api#/schemas/Invoice) for a given company's connection.

[Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    
### Useful queries

- Outstanding invoices - `query = amountDue > 0`
- Invoices due after a certain date: `query = dueDate > 2021-01-28`

[Read more about querying](https://docs.codat.io/using-the-api/querying).

### Tips and traps

To access the `paymentAllocations` property, ensure that the `payments` data type is queued and cached in Codat before retrieving `invoices` from Codat's cache.


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "order_by": "-modifiedDate",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingInvoicesRequest](../../models/operations/listaccountinginvoicesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.AccountingInvoices](../../models/shared/accountinginvoices.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 409, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |

## list_attachments

The *List invoice attachments* endpoint returns a list of attachments available to download for given `invoiceId`.

[Invoices](https://docs.codat.io/lending-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.list_attachments(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "invoice_id": "EILBDVJVNUAGVKRQ",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListAccountingInvoiceAttachmentsRequest](../../models/operations/listaccountinginvoiceattachmentsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[shared.Attachments](../../models/shared/attachments.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## list_reconciled

Gets a list of invoices linked to the corresponding banking transaction

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.accounts_receivable.invoices.list_reconciled(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListReconciledInvoicesRequest](../../models/operations/listreconciledinvoicesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.EnhancedInvoicesReport](../../models/shared/enhancedinvoicesreport.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |