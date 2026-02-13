# Bills

## Overview

Get, create, and update Bills.

### Available Operations

* [get_bill_options](#get_bill_options) - Get bill mapping options
* [list](#list) - List bills
* [create](#create) - Create bill
* [update](#update) - Update bill
* [upload_attachment](#upload_attachment) - Upload bill attachment
* [list_attachments](#list_attachments) - List bill attachments
* [download_attachment](#download_attachment) - Download bill attachment

## get_bill_options

﻿Use the *Get mapping options - Bills* endpoint to return a list of available mapping options for a given company's connection ID.

By default, this endpoint returns a list of active accounts and tax rates. You can use [querying](https://docs.codat.io/using-the-api/querying) to change that.

Mapping options are a set of accounts and tax rates used to configure the SMB's payables integration.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-mapping-options-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/mappingOptions/bills" example="Mapping options" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.get_bill_options(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "status_query": "status=Archived",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetMappingOptionsBillsRequest](../../models/operations/getmappingoptionsbillsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.BillMappingOptions](../../models/shared/billmappingoptions.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List bills* endpoint returns a list of [bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

By default, the endpoint will return all bills with a status of 'Open' & 'PartiallyPaid' to show all oustanding bills.

### Example Usage: Bills

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Bills" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
    })

    # Handle response
    print(res)

```
### Example Usage: Source modified date

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (open)

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Status (open)" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "status=Open",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (open) & source modified date

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Status (open) & source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=Open",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (partially paid)

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Status (partially paid)" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "status=PartiallyPaid",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (partially paid) & source modified date

<!-- UsageSnippet language="python" operationID="list-bills" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Status (partially paid) & source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=PartiallyPaid",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListBillsRequest](../../models/operations/listbillsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[shared.Bills](../../models/shared/bills.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## create

The *Create bill* endpoint creates a new [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

### Example Usage: Create bill

<!-- UsageSnippet language="python" operationID="create-bill" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Create bill" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from decimal import Decimal


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_prototype": {
            "reference": "bill_b8qmmj4ksf1suax",
            "supplier_ref": {
                "id": "1262c350-fe0f-40ec-aeff-41c95b4a45af",
                "supplier_name": "DIISR - Small Business Services",
            },
            "issue_date": "2023-04-23T00:00:00",
            "due_date": "2023-04-23T00:00:00",
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "line_items": [
                {
                    "description": "Half day training - Microsoft Office",
                    "unit_amount": Decimal("1800"),
                    "quantity": Decimal("1"),
                    "tax_amount": Decimal("360"),
                    "account_ref": {
                        "id": "46f9461e-788b-4906-8b74-d1ea17f6dc10",
                    },
                    "total_amount": Decimal("2160"),
                    "tax_rate_ref": {
                        "id": "INPUT2",
                    },
                },
                {
                    "description": "Desktop/network support via email & phone.Per month fixed fee for minimum 20 hours/month.",
                    "unit_amount": Decimal("4000"),
                    "quantity": Decimal("1"),
                    "tax_amount": Decimal("800"),
                    "account_ref": {
                        "id": "f96c9458-d724-47bf-8f74-a9d5726465ce",
                    },
                    "total_amount": Decimal("4800"),
                    "tax_rate_ref": {
                        "id": "INPUT2",
                    },
                },
                {
                    "description": "Stationery charges",
                    "unit_amount": Decimal("32"),
                    "quantity": Decimal("8"),
                    "tax_amount": Decimal("51.2"),
                    "account_ref": {
                        "id": "cba6527d-f102-4538-b421-e483233e9d5a",
                    },
                    "total_amount": Decimal("307.2"),
                    "tax_rate_ref": {
                        "id": "INPUT2",
                    },
                    "tracking_refs": [
                        {
                            "id": "dba3d4da-f9ed-4eee-8e0b-452d11fdb1fa",
                            "data_type": shared.DataType.TRACKING_CATEGORIES,
                        },
                    ],
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Created bill

<!-- UsageSnippet language="python" operationID="create-bill" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Created bill" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_prototype": {
            "supplier_ref": {
                "id": "<id>",
            },
            "issue_date": "2022-10-23T00:00:00Z",
            "due_date": "2022-10-23T00:00:00Z",
            "currency": "GBP",
            "line_items": [
                {
                    "tracking_refs": None,
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-bill" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_prototype": {
            "supplier_ref": {
                "id": "<id>",
            },
            "issue_date": "2022-10-23T00:00:00Z",
            "due_date": "2022-10-23T00:00:00Z",
            "currency": "GBP",
            "line_items": [
                {
                    "tracking_refs": None,
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateBillRequest](../../models/operations/createbillrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[shared.Bill](../../models/shared/bill.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## update

The *Update bill* endpoint updates an existing [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| FreeAgent                     | Yes       |
| QuickBooks Online             | Yes       |
| Xero                          | Yes       |
| Oracle NetSuite               | No        |
| Sage Intacct                  | No        |
| Zoho Books                    | No        |


### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="update-bill" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_prototype": {
            "supplier_ref": {
                "id": "<id>",
            },
            "issue_date": "2022-10-23T00:00:00Z",
            "due_date": "2022-10-23T00:00:00Z",
            "currency": "GBP",
            "line_items": [
                {
                    "tracking_refs": [
                        {
                            "id": "e9a1b63d-9ff0-40e7-8038-016354b987e6",
                            "data_type": shared.DataType.TRACKING_CATEGORIES,
                        },
                    ],
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Update bill

<!-- UsageSnippet language="python" operationID="update-bill" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}" example="Update bill" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared
from decimal import Decimal


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_prototype": {
            "reference": "bill_updated_ref",
            "supplier_ref": {
                "id": "1262c350-fe0f-40ec-aeff-41c95b4a45af",
            },
            "issue_date": "2023-04-23T00:00:00",
            "due_date": "2023-05-23T00:00:00",
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "line_items": [
                {
                    "description": "Updated line item - Microsoft Office training",
                    "unit_amount": Decimal("2000"),
                    "quantity": Decimal("1"),
                    "tax_amount": Decimal("400"),
                    "account_ref": {
                        "id": "46f9461e-788b-4906-8b74-d1ea17f6dc10",
                    },
                    "total_amount": Decimal("2400"),
                    "tax_rate_ref": {
                        "id": "INPUT2",
                    },
                },
                {
                    "description": "Desktop/network support via email & phone - updated rate",
                    "unit_amount": Decimal("4500"),
                    "quantity": Decimal("1"),
                    "tax_amount": Decimal("900"),
                    "account_ref": {
                        "id": "f96c9458-d724-47bf-8f74-a9d5726465ce",
                    },
                    "total_amount": Decimal("5400"),
                    "tax_rate_ref": {
                        "id": "INPUT2",
                    },
                    "tracking_refs": [
                        {
                            "id": "dba3d4da-f9ed-4eee-8e0b-452d11fdb1fa",
                            "data_type": shared.DataType.TRACKING_CATEGORIES,
                        },
                    ],
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```
### Example Usage: Updated bill

<!-- UsageSnippet language="python" operationID="update-bill" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}" example="Updated bill" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "bill_prototype": {
            "supplier_ref": {
                "id": "<id>",
            },
            "issue_date": "2022-10-23T00:00:00Z",
            "due_date": "2022-10-23T00:00:00Z",
            "currency": "GBP",
            "line_items": [
                {
                    "tracking_refs": [
                        {
                            "id": "e9a1b63d-9ff0-40e7-8038-016354b987e6",
                            "data_type": shared.DataType.TRACKING_CATEGORIES,
                        },
                    ],
                },
            ],
            "status": shared.BillStatus.OPEN,
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateBillRequest](../../models/operations/updatebillrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[shared.Bill](../../models/shared/bill.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## upload_attachment

The *Upload bill attachment* endpoint uploads an attachment and assigns it against a specific `billId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload-bill-attachment" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/attachments" example="Attachment metadata" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.upload_attachment(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UploadBillAttachmentRequest](../../models/operations/uploadbillattachmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.Attachment](../../models/shared/attachment.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list_attachments

The *List bill attachments* endpoint returns a list of attachments available to download for a given `billId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-bill-attachments" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/attachments" example="Success" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.list_attachments(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListBillAttachmentsRequest](../../models/operations/listbillattachmentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[List[shared.Attachment]](../../models/.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## download_attachment

The *Download bill attachment* endpoint downloads a specific attachment for a given `billId` and `attachmentId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support downloading a bill attachment.


### Example Usage

<!-- UsageSnippet language="python" operationID="download-bill-attachment" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/bills/{billId}/attachments/{attachmentId}/download" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.bills.download_attachment(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "bill_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "attachment_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DownloadBillAttachmentRequest](../../models/operations/downloadbillattachmentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[httpx.Response](../../models/data.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |