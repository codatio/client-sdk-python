# BillCreditNotes
(*bill_credit_notes*)

## Overview

Get, create, and update Bill credit notes.

### Available Operations

* [create](#create) - Create bill credit note
* [get](#get) - Get bill credit note
* [get_create_update_model](#get_create_update_model) - Get create/update bill credit note model
* [list](#list) - List bill credit notes
* [update](#update) - Update bill credit note

## create

The *Create bill credit note* endpoint creates a new [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating a bill credit note.


### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared
from decimal import Decimal

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_credit_notes.create(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "bill_credit_note": {
        "discount_percentage": Decimal("0"),
        "status": shared.BillCreditNoteStatus.SUBMITTED,
        "sub_total": Decimal("100"),
        "total_amount": Decimal("100"),
        "total_discount": Decimal("0"),
        "total_tax_amount": Decimal("0"),
        "allocated_on_date": "2022-10-23T00:00:00Z",
        "bill_credit_note_number": "309",
        "created_from_refs": [
            {
                "data_type": "invoice",
            },
            {
                "data_type": "journalEntry",
            },
        ],
        "currency": "GBP",
        "currency_rate": Decimal("1.242097"),
        "id": "1509398f-98e2-436d-8a5d-c042e0c74ffc",
        "issue_date": "2023-04-20T00:00:00",
        "line_items": [
            {
                "quantity": Decimal("1"),
                "unit_amount": Decimal("100"),
                "account_ref": {
                    "id": "7",
                },
                "description": "",
                "sub_total": Decimal("100"),
                "tax_amount": Decimal("0"),
                "tax_rate_ref": {
                    "effective_tax_rate": Decimal("0"),
                    "id": "NON",
                    "name": "NON",
                },
                "total_amount": Decimal("100"),
                "tracking": {
                    "category_refs": [
                        {
                            "id": "<id>",
                        },
                    ],
                    "is_billed_to": shared.BilledToType.UNKNOWN,
                    "is_rebilled_to": shared.BilledToType.NOT_APPLICABLE,
                },
                "tracking_category_refs": [
                    {
                        "id": "<id>",
                    },
                ],
            },
        ],
        "modified_date": "2022-10-23T00:00:00Z",
        "note": "Bill Credit Note with 1 line items, totaling 805.78",
        "payment_allocations": [
            {
                "allocation": {
                    "allocated_on_date": "2022-10-23T00:00:00Z",
                    "currency": "GBP",
                },
                "payment": {
                    "currency": "GBP",
                    "paid_on_date": "2022-10-23T00:00:00Z",
                },
            },
            {
                "allocation": {
                    "allocated_on_date": "2022-10-23T00:00:00Z",
                    "currency": "EUR",
                },
                "payment": {
                    "currency": "USD",
                    "paid_on_date": "2022-10-23T00:00:00Z",
                },
            },
            {
                "allocation": {
                    "allocated_on_date": "2022-10-23T00:00:00Z",
                    "currency": "USD",
                },
                "payment": {
                    "currency": "GBP",
                    "paid_on_date": "2022-10-23T00:00:00Z",
                },
            },
        ],
        "remaining_credit": Decimal("100"),
        "source_modified_date": "2022-10-23T00:00:00Z",
        "supplier_ref": {
            "id": "87",
            "supplier_name": "Ankunding Inc",
        },
        "withholding_tax": [
            {
                "amount": Decimal("4865.89"),
                "name": "<value>",
            },
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateBillCreditNoteRequest](../../models/operations/createbillcreditnoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.CreateBillCreditNoteResponse](../../models/shared/createbillcreditnoteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get

The *Get bill credit note* endpoint returns a single bill credit note for a given `billCreditNoteId`.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support getting a specific bill credit note.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_credit_notes.get(request={
    "bill_credit_note_id": "<id>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetBillCreditNoteRequest](../../models/operations/getbillcreditnoterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.BillCreditNote](../../models/shared/billcreditnote.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_create_update_model

The *Get create/update bill credit note model* endpoint returns the expected data for the request payload when creating and updating a [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company and integration.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating a bill credit note.


### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_credit_notes.get_create_update_model(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetCreateUpdateBillCreditNoteModelRequest](../../models/operations/getcreateupdatebillcreditnotemodelrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## list

The *List bill credit notes* endpoint returns a list of [bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_credit_notes.list(request={
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

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListBillCreditNotesRequest](../../models/operations/listbillcreditnotesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[shared.BillCreditNotes](../../models/shared/billcreditnotes.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 409, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |

## update

The *Update bill credit note* endpoint updates an existing [bill credit note](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/sync-for-payables-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-billCreditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating a bill credit note.


### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared
from decimal import Decimal

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.bill_credit_notes.update(request={
    "bill_credit_note_id": "<id>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "bill_credit_note": {
        "discount_percentage": Decimal("0"),
        "status": shared.BillCreditNoteStatus.SUBMITTED,
        "sub_total": Decimal("805.78"),
        "total_amount": Decimal("693"),
        "total_discount": Decimal("0"),
        "total_tax_amount": Decimal("0"),
        "allocated_on_date": "2022-10-23T00:00:00Z",
        "bill_credit_note_number": "14763237",
        "created_from_refs": [
            {
                "data_type": "invoice",
            },
            {
                "data_type": "transfer",
            },
        ],
        "currency": "USD",
        "id": "6a0e9dfb-87b0-47d3-aaaf-9753ae9e757d",
        "issue_date": "2019-02-18T16:03:07.268Z",
        "line_items": [
            {
                "quantity": Decimal("4"),
                "unit_amount": Decimal("25"),
                "account_ref": {
                    "id": "3f267b10-757d-44c0-bef9-20f70cc8fbe3",
                },
                "description": "AcmeMagnet",
                "discount_amount": Decimal("0"),
                "item_ref": {
                    "id": "3",
                },
                "sub_total": Decimal("100"),
                "tax_amount": Decimal("10"),
                "tax_rate_ref": {
                    "id": "6c88aff3-7cb9-4980-a3d3-443e72e02498",
                },
                "total_amount": Decimal("110"),
                "tracking_category_refs": [
                    {
                        "id": "department_1",
                        "name": "ACMERockets",
                    },
                    {
                        "id": "costcode_2",
                        "name": "ACM2-ACMESigns",
                    },
                ],
            },
            {
                "quantity": Decimal("3"),
                "unit_amount": Decimal("25"),
                "account_ref": {
                    "id": "3f267b10-757d-44c0-bef9-20f70cc8fbe3",
                },
                "description": "ACMEDisintegratingPistol",
                "discount_amount": Decimal("0"),
                "item_ref": {
                    "id": "3abf0883-03f7-44c6-bc15-1372522d25e1",
                },
                "sub_total": Decimal("75"),
                "tax_amount": Decimal("7.5"),
                "tax_rate_ref": {
                    "id": "6c88aff3-7cb9-4980-a3d3-443e72e02498",
                },
                "total_amount": Decimal("82.5"),
            },
            {
                "quantity": Decimal("6"),
                "unit_amount": Decimal("52"),
                "account_ref": {
                    "id": "3f267b10-757d-44c0-bef9-20f70cc8fbe3",
                },
                "description": "ACMEWhippedCreamDispenser",
                "discount_amount": Decimal("0"),
                "item_ref": {
                    "id": "3691f3d9-0ff7-4358-8a93-bed31c1b4b03",
                },
                "sub_total": Decimal("312"),
                "tax_amount": Decimal("31.2"),
                "tax_rate_ref": {
                    "id": "6c88aff3-7cb9-4980-a3d3-443e72e02498",
                },
                "total_amount": Decimal("343.2"),
            },
            {
                "quantity": Decimal("1"),
                "unit_amount": Decimal("130"),
                "account_ref": {
                    "id": "3f267b10-757d-44c0-bef9-20f70cc8fbe3",
                },
                "description": "ACMEJetPropelledPogoStick",
                "discount_amount": Decimal("0"),
                "item_ref": {
                    "id": "075410d4-7edc-4936-ba52-9e1e43cbe300",
                },
                "sub_total": Decimal("130"),
                "tax_amount": Decimal("27.3"),
                "tax_rate_ref": {
                    "id": "d606732b-db18-44d7-823b-7f15f42c32ea",
                },
                "total_amount": Decimal("157.3"),
            },
        ],
        "modified_date": "2022-10-23T00:00:00Z",
        "note": "Track separately",
        "payment_allocations": [
            {
                "allocation": {
                    "allocated_on_date": "2022-10-23T00:00:00Z",
                    "currency": "GBP",
                },
                "payment": {
                    "currency": "EUR",
                    "paid_on_date": "2022-10-23T00:00:00Z",
                },
            },
        ],
        "remaining_credit": Decimal("693"),
        "source_modified_date": "2022-10-23T00:00:00Z",
        "supplier_ref": {
            "id": "67C6A7A1-5E84-4AC4-B950-24A114E379D0",
            "supplier_name": "Chin's Gas and Oil",
        },
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UpdateBillCreditNoteRequest](../../models/operations/updatebillcreditnoterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.UpdateBillCreditNoteResponse](../../models/shared/updatebillcreditnoteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |