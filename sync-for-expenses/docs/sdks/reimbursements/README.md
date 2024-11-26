# Reimbursements
(*reimbursements*)

## Overview

Create and update transactions that represent your customers' repayable spend.

### Available Operations

* [create](#create) - Create reimbursable expense transaction
* [update](#update) - Update reimbursable expense transaction

## create

Use the *Create reimbursable expense* endpoint to submit an employee expense claim in the accounting platform for a given company's connection.

[Reimbursable expense requests](https://docs.codat.io/sync-for-expenses-api#/schemas/ReimbursableExpenseTransactionRequest) are reflected in the accounting software in the form of **Bills** against an employee (who exists as a supplier in the accounting platform).

### Supported Integrations
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Desktop    | Yes       |
| QuickBooks Online     | Yes       |
| Oracle NetSuite       | Yes       |

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
    res = s.reimbursements.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "request_body": [
            {
                "contact_ref": {
                    "id": "752",
                },
                "currency": "GBP",
                "due_date": "2024-05-21",
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2024-05-21",
                "currency_rate": Decimal("1"),
                "lines": [
                    {
                        "net_amount": Decimal("100"),
                        "account_ref": {
                            "id": "35",
                        },
                        "description": "Hotel",
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
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
                "reference": "expenses w/c 01/07",
            },
        ],
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.CreateReimbursableExpenseTransactionRequest](../../models/operations/createreimbursableexpensetransactionrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[shared.CreateReimbursableExpenseResponse](../../models/shared/createreimbursableexpenseresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## update

The *Update reimbursable expense* endpoint updates an existing employee expense claim in the accounting platform for a given company's connection. 

Updating an existing [reimbursable expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateReimbursableExpenseTransactionRequest) will update the existing **bill** against an employee (who exists as a supplier in the accounting software).

### Supported Integrations
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Online     | Yes       |
| Oracle NetSuite       | Yes       |

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
    res = s.reimbursements.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
        "update_reimbursable_expense_transaction_request": {
            "contact_ref": {
                "id": "752",
            },
            "currency": "GBP",
            "due_date": "2024-05-21",
            "issue_date": "2024-05-21",
            "currency_rate": Decimal("1"),
            "lines": [
                {
                    "net_amount": Decimal("100"),
                    "account_ref": {
                        "id": "35",
                    },
                    "description": "Hotel",
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
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            "reference": "expenses w/c 01/07",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.UpdateReimbursableExpenseTransactionRequest](../../models/operations/updatereimbursableexpensetransactionrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[shared.CreateReimbursableExpenseResponse](../../models/shared/createreimbursableexpenseresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |