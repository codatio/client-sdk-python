# Expenses
(*expenses*)

## Overview

Create and update transactions that represent your customers' spend.

### Available Operations

* [create](#create) - Create expense transaction
* [update](#update) - Update expense transactions

## create

The *Create expense* endpoint creates an [expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) in the accounting software for a given company's connection. 

[Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/ExpenseTransaction) represent transactions made with a company debit or credit card. 

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| Dynamics 365 Business Central | Yes       |
| FreeAgent                     | Yes       |
| QuickBooks Desktop            | Yes       |
| QuickBooks Online             | Yes       |
| Oracle NetSuite               | Yes       |
| Xero                          | Yes       |

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
    res = codat_sync_expenses.expenses.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "request_body": [
            {
                "currency": "GBP",
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2024-05-21T00:00:00+00:00",
                "type": shared.ExpenseTransactionType.PAYMENT,
                "bank_account_ref": {
                    "id": "97",
                },
                "contact_ref": {
                    "id": "430",
                    "type": shared.Type.SUPPLIER,
                },
                "currency_rate": Decimal("1"),
                "lines": [
                    {
                        "net_amount": Decimal("100"),
                        "account_ref": {
                            "id": "35",
                        },
                        "invoice_to": {
                            "id": "504",
                            "type": shared.InvoiceToType.CUSTOMER,
                        },
                        "tax_amount": Decimal("20"),
                        "tax_rate_ref": {
                            "id": "23_Bills",
                        },
                        "tracking_refs": [
                            {
                                "data_type": shared.TrackingRefDataType.TRACKING_CATEGORIES,
                                "id": "DEPARTMENT_5",
                            },
                        ],
                    },
                ],
                "merchant_name": "Amazon UK",
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            },
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateExpenseTransactionRequest](../../models/operations/createexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[shared.CreateExpenseResponse](../../models/shared/createexpenseresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update

The *Update expense* endpoint updates an existing [expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateExpenseRequest) in the accounting software for a given company's connection. 

[Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateExpenseRequest) represent transactions made with a company debit or credit card. 

### Supported Integrations
The following integrations are supported for the [Payment](https://docs.codat.io/expenses/sync-process/expense-transactions#transaction-types) transaction `type` only: 
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Online     | Yes       |
| Oracle NetSuite       | Yes       |
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
) as codat_sync_expenses:
    res = codat_sync_expenses.expenses.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
        "update_expense_request": {
            "currency": "GBP",
            "issue_date": "2024-05-21T00:00:00+00:00",
            "type": shared.UpdateExpenseRequestType.PAYMENT,
            "bank_account_ref": {
                "id": "97",
            },
            "contact_ref": {
                "id": "430",
                "type": shared.Type.SUPPLIER,
            },
            "currency_rate": Decimal("1"),
            "lines": [
                {
                    "net_amount": Decimal("100"),
                    "account_ref": {
                        "id": "35",
                    },
                    "invoice_to": {
                        "id": "504",
                        "type": shared.InvoiceToType.CUSTOMER,
                    },
                    "tax_amount": Decimal("20"),
                    "tax_rate_ref": {
                        "id": "23_Bills",
                    },
                    "tracking_refs": [
                        {
                            "data_type": shared.TrackingRefDataType.TRACKING_CATEGORIES,
                            "id": "DEPARTMENT_5",
                        },
                    ],
                },
            ],
            "merchant_name": "Amazon UK",
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateExpenseTransactionRequest](../../models/operations/updateexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[shared.UpdateExpenseResponse](../../models/shared/updateexpenseresponse.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 422, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |