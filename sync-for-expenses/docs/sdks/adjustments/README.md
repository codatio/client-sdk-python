# Adjustments
(*adjustments*)

## Overview

Create transactions that represent your adjustments to your customers' spend.

### Available Operations

* [create](#create) - Create adjustment transaction

## create

Use the *Create adjustment expense* endpoint to create an [adjustment](https://docs.codat.io/sync-for-expenses-api#/schemas/AdjustmentTransactionRequest) in the accounting software for a given company's connection. 

Adjustments represent write-offs and transaction alterations, such as foreign exchange adjustments, in the form of a journal entry. 

### Supported Integrations

| Integration           | Supported |
|-----------------------|-----------|
| QuickBooks Desktop    | Yes       |

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:
    res = codat_sync_expenses.adjustments.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "request_body": [
            {
                "currency": "USD",
                "date_": "2024-05-21T00:00:00+00:00",
                "id": "3357b3df-5f2e-465d-b9ba-226519dbb8f1",
                "lines": [
                    {
                        "account_ref": {
                            "id": "80000018-1671793811",
                        },
                        "amount": Decimal("50"),
                        "description": "debit line",
                        "invoice_to": {
                            "id": "80000002-1674552702",
                            "type": shared.InvoiceToType.CUSTOMER,
                        },
                        "tracking_refs": [
                            {
                                "data_type": shared.TrackingRefAdjustmentTransactionDataType.TRACKING_CATEGORIES,
                                "id": "80000003-1674553958",
                            },
                        ],
                    },
                    {
                        "account_ref": {
                            "id": "80000028-1671794219",
                        },
                        "amount": Decimal("-50"),
                        "description": "credit line",
                        "tracking_refs": [
                            {
                                "data_type": shared.TrackingRefAdjustmentTransactionDataType.TRACKING_CATEGORIES,
                                "id": "80000003-1674553958",
                            },
                        ],
                    },
                ],
                "currency_rate": Decimal("1"),
                "reference": "test reference",
            },
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateAdjustmentTransactionRequest](../../models/operations/createadjustmenttransactionrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[shared.AdjustmentTransactionResponse](../../models/shared/adjustmenttransactionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |