# Reimbursements

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
| Zoho Books            | Yes       |
| Sage Intacct          | Yes       |

### Example Usage: Create reimbursable expense

<!-- UsageSnippet language="python" operationID="create-reimbursable-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions" example="Create reimbursable expense" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.create(request={
        "request_body": [
            {
                "contact_ref": {
                    "id": "752",
                },
                "currency": "GBP",
                "currency_rate": Decimal("1"),
                "due_date": "2024-05-21",
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2024-05-21",
                "lines": [
                    shared.ReimbursableExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="35",
                        ),
                        description="Hotel",
                        invoice_to=shared.InvoiceTo(
                            id="504",
                            type=shared.InvoiceToType.CUSTOMER,
                        ),
                        net_amount=Decimal("100"),
                        tax_amount=Decimal("20"),
                        tax_rate_ref=shared.RecordRef(
                            id="23_Bills",
                        ),
                        tracking_refs=[
                            shared.TrackingRef(
                                id="DEPARTMENT_5",
                            ),
                        ],
                    ),
                ],
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
                "reference": "expenses w/c 01/07",
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Example 1

<!-- UsageSnippet language="python" operationID="create-reimbursable-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions" example="Example 1" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.create(request={
        "request_body": [
            {
                "ap_account_ref": None,
                "contact_ref": {
                    "id": "40e3e57c-2322-4898-966c-ca41adfd23fd",
                },
                "currency": "GBP",
                "due_date": "2022-10-23T00:00:00Z",
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2022-10-23T00:00:00Z",
                "lines": [
                    shared.ReimbursableExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                        ),
                        description="2-night hotel stay",
                        invoice_to=shared.InvoiceTo(
                            id="80000002-1674552702",
                            type=shared.InvoiceToType.CUSTOMER,
                        ),
                        item_ref=shared.ItemRef(
                            id="80000002-1675158984",
                        ),
                        net_amount=Decimal("100"),
                        tax_amount=Decimal("20"),
                        tax_rate_ref=shared.RecordRef(
                            id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                        ),
                        tracking_refs=[
                            shared.TrackingRef(
                                id="e9a1b63d-9ff0-40e7-8038-016354b987e6",
                            ),
                        ],
                    ),
                ],
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-reimbursable-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.create(request={
        "request_body": [
            {
                "ap_account_ref": None,
                "contact_ref": {
                    "id": "40e3e57c-2322-4898-966c-ca41adfd23fd",
                },
                "currency": "GBP",
                "due_date": "2022-10-23T00:00:00Z",
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2022-10-23T00:00:00Z",
                "lines": [
                    shared.ReimbursableExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                        ),
                        description="2-night hotel stay",
                        invoice_to=shared.InvoiceTo(
                            id="80000002-1674552702",
                            type=shared.InvoiceToType.CUSTOMER,
                        ),
                        item_ref=shared.ItemRef(
                            id="80000002-1675158984",
                        ),
                        net_amount=Decimal("100"),
                        tax_amount=Decimal("20"),
                        tax_rate_ref=shared.RecordRef(
                            id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                        ),
                        tracking_refs=[
                            shared.TrackingRef(
                                id="e9a1b63d-9ff0-40e7-8038-016354b987e6",
                            ),
                        ],
                    ),
                ],
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.CreateReimbursableExpenseTransactionRequest](../../models/operations/createreimbursableexpensetransactionrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[shared.CreateReimbursableExpenseResponse](../../models/shared/createreimbursableexpenseresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update

The *Update reimbursable expense* endpoint updates an existing employee expense claim in the accounting platform for a given company's connection. 

Updating an existing [reimbursable expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateReimbursableExpenseTransactionRequest) will update the existing **bill** against an employee (who exists as a supplier in the accounting software).

### Supported Integrations
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Online     | Yes       |
| Oracle NetSuite       | Yes       |
| Zoho Books            | Yes       |



### Example Usage: Example 1

<!-- UsageSnippet language="python" operationID="update-reimbursable-expense-transaction" method="put" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions/{transactionId}" example="Example 1" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.update(request={
        "update_reimbursable_expense_transaction_request": {
            "ap_account_ref": {
                "id": "8000004C-1724173136",
            },
            "contact_ref": {
                "id": "40e3e57c-2322-4898-966c-ca41adfd23fd",
            },
            "currency": "GBP",
            "due_date": "2022-10-23T00:00:00Z",
            "issue_date": "2022-10-23T00:00:00Z",
            "lines": [
                shared.ReimbursableExpenseTransactionLine(
                    account_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    description="2-night hotel stay",
                    invoice_to=shared.InvoiceTo(
                        id="80000002-1674552702",
                        type=shared.InvoiceToType.CUSTOMER,
                    ),
                    item_ref=shared.ItemRef(
                        id="80000002-1675158984",
                    ),
                    net_amount=Decimal("100"),
                    tax_amount=Decimal("20"),
                    tax_rate_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    tracking_refs=[
                        shared.TrackingRef(
                            id="e9a1b63d-9ff0-40e7-8038-016354b987e6",
                        ),
                    ],
                ),
            ],
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="update-reimbursable-expense-transaction" method="put" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions/{transactionId}" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.update(request={
        "update_reimbursable_expense_transaction_request": {
            "ap_account_ref": {
                "id": "8000004C-1724173136",
            },
            "contact_ref": {
                "id": "40e3e57c-2322-4898-966c-ca41adfd23fd",
            },
            "currency": "GBP",
            "due_date": "2022-10-23T00:00:00Z",
            "issue_date": "2022-10-23T00:00:00Z",
            "lines": [
                shared.ReimbursableExpenseTransactionLine(
                    account_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    description="2-night hotel stay",
                    invoice_to=shared.InvoiceTo(
                        id="80000002-1674552702",
                        type=shared.InvoiceToType.CUSTOMER,
                    ),
                    item_ref=shared.ItemRef(
                        id="80000002-1675158984",
                    ),
                    net_amount=Decimal("100"),
                    tax_amount=Decimal("20"),
                    tax_rate_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    tracking_refs=[
                        shared.TrackingRef(
                            id="e9a1b63d-9ff0-40e7-8038-016354b987e6",
                        ),
                    ],
                ),
            ],
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
    })

    # Handle response
    print(res)

```
### Example Usage: Update reimbursable expense

<!-- UsageSnippet language="python" operationID="update-reimbursable-expense-transaction" method="put" path="/companies/{companyId}/sync/expenses/reimbursable-expense-transactions/{transactionId}" example="Update reimbursable expense" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared
from decimal import Decimal


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.reimbursements.update(request={
        "update_reimbursable_expense_transaction_request": {
            "contact_ref": {
                "id": "752",
            },
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "due_date": "2024-05-21",
            "issue_date": "2024-05-21",
            "lines": [
                shared.ReimbursableExpenseTransactionLine(
                    account_ref=shared.RecordRef(
                        id="35",
                    ),
                    description="Hotel",
                    invoice_to=shared.InvoiceTo(
                        id="504",
                        type=shared.InvoiceToType.CUSTOMER,
                    ),
                    net_amount=Decimal("100"),
                    tax_amount=Decimal("20"),
                    tax_rate_ref=shared.RecordRef(
                        id="23_Bills",
                    ),
                    tracking_refs=[
                        shared.TrackingRef(
                            id="DEPARTMENT_5",
                        ),
                    ],
                ),
            ],
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            "reference": "expenses w/c 01/07",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.UpdateReimbursableExpenseTransactionRequest](../../models/operations/updatereimbursableexpensetransactionrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[shared.CreateReimbursableExpenseResponse](../../models/shared/createreimbursableexpenseresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |