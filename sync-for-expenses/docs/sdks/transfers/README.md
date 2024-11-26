# Transfers
(*transfers*)

## Overview

Create and update transactions that represent the movement of your customers' money.

### Available Operations

* [create](#create) - Create transfer transaction

## create

Use the *Create transfer* endpoint to create or update a [transfer transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/TransferTransactionRequest) in the accounting software for a given company's connection. 

Transfers record the movement of money between two bank accounts, or between a bank account and a nominal account. Use them to represent actions such as topping up a debit card account or a balance transfer to another credit card.

The `from.amount` and `to.amount` fields are in the native currency of the account.

### Supported Integrations
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Desktop    | Yes       |
| QuickBooks Online     | Yes       |
| Xero                  | Yes       |

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.transfers.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
        "transfer_transaction_request": {
            "date_": "2021-05-21T00:00:00+00:00",
            "from_": {
                "account_ref": {
                    "id": "787dfb37-5707-4dc0-8a86-8d74e4cc78ea",
                },
                "amount": Decimal("100"),
            },
            "to": {
                "account_ref": {
                    "id": "777dfb37-5506-3dc0-6g86-8d34z4cc78ea",
                },
                "amount": Decimal("100"),
            },
            "description": "Sample transfer description",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateTransferTransactionRequest](../../models/operations/createtransfertransactionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.TransferTransactionResponse](../../models/shared/transfertransactionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |