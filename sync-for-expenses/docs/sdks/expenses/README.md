# Expenses

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
| Sage Intacct                  | Yes       |
| Xero                          | Yes       |
| Zoho Books                    | Yes       |


### Example Usage: Example 1

<!-- UsageSnippet language="python" operationID="create-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/expense-transactions" example="Example 1" -->
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
        "request_body": [
            {
                "bank_account_ref": {
                    "id": "97",
                },
                "contact_ref": {
                    "id": "430",
                },
                "currency": "GBP",
                "currency_rate": Decimal("1"),
                "id": "a44135b0-6882-489a-83fe-a0c57a4afb19",
                "issue_date": "2024-05-21T00:00:00+00:00",
                "lines": [
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="35",
                        ),
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
                                id="DEPARTMENT_3",
                            ),
                            shared.TrackingRef(),
                        ],
                    ),
                ],
                "merchant_name": "Amazon UK",
                "notes": "amazon purchase",
                "type": shared.ExpenseTransactionType.PAYMENT,
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/expense-transactions" example="Malformed query" -->
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
        "request_body": [
            {
                "bank_account_ref": {
                    "id": "97",
                },
                "contact_ref": {
                    "id": "430",
                },
                "currency": "GBP",
                "currency_rate": Decimal("1"),
                "id": "a44135b0-6882-489a-83fe-a0c57a4afb19",
                "issue_date": "2024-05-21T00:00:00+00:00",
                "lines": [
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="35",
                        ),
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
                                id="DEPARTMENT_3",
                            ),
                            shared.TrackingRef(),
                        ],
                    ),
                ],
                "merchant_name": "Amazon UK",
                "notes": "amazon purchase",
                "type": shared.ExpenseTransactionType.PAYMENT,
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Payment

<!-- UsageSnippet language="python" operationID="create-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/expense-transactions" example="Payment" -->
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
        "request_body": [
            {
                "bank_account_ref": {
                    "id": "97",
                },
                "contact_ref": {
                    "id": "430",
                },
                "currency": "GBP",
                "currency_rate": Decimal("1"),
                "id": "4d7c6929-7770-412b-91bb-44d3bc71d111",
                "issue_date": "2024-05-21T00:00:00+00:00",
                "lines": [
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="35",
                        ),
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
                "merchant_name": "Amazon UK",
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
                "type": shared.ExpenseTransactionType.PAYMENT,
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Refund

<!-- UsageSnippet language="python" operationID="create-expense-transaction" method="post" path="/companies/{companyId}/sync/expenses/expense-transactions" example="Refund" -->
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
        "request_body": [
            {
                "bank_account_ref": {
                    "id": "97",
                },
                "contact_ref": {
                    "id": "430",
                },
                "currency": "GBP",
                "id": "7008d3f2-aeb4-11ed-afa1-0242ac120002",
                "issue_date": "2024-02-17T00:00:00+00:00",
                "lines": [
                    shared.ExpenseTransactionLine(
                        account_ref=shared.RecordRef(
                            id="42",
                        ),
                        net_amount=Decimal("100"),
                        tax_amount=Decimal("20"),
                        tax_rate_ref=shared.RecordRef(
                            id="23_Bills",
                        ),
                        tracking_refs=[
                            shared.TrackingRef(
                                id="DEPARTMENT_6",
                            ),
                        ],
                    ),
                ],
                "merchant_name": "Amazon UK",
                "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
                "type": shared.ExpenseTransactionType.REFUND,
            },
        ],
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateExpenseTransactionRequest](../../models/operations/createexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[shared.CreateExpenseResponse](../../models/shared/createexpenseresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update

The *Update expense* endpoint updates an existing [expense transaction](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateExpenseRequest) in the accounting software for a given company's connection. 

[Expense transactions](https://docs.codat.io/sync-for-expenses-api#/schemas/UpdateExpenseRequest) represent transactions made with a company debit or credit card. 

### Supported integrations
The following integrations are supported for the [Payment](https://docs.codat.io/expenses/sync-process/expense-transactions#transaction-types) transaction `type` only: 
| Integration           | Supported |
|-----------------------|-----------|
| FreeAgent             | Yes       |
| QuickBooks Desktop    | Yes       |
| QuickBooks Online     | Yes       |
| Oracle NetSuite       | Yes       |
| Sage Intacct          | Yes       |
| Xero                  | Yes       |
| Zoho Books            | Yes       |

#### Integration-specific behavior

| Integration           | Specifics |
|-----------------------|-----------|
| Sage Intacct          | To sync **debit card expenses**, map the debit card to a Credit Card with the account type set to `Debit`.|

### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="update-expense-transaction" method="put" path="/companies/{companyId}/sync/expenses/expense-transactions/{transactionId}" example="Malformed query" -->
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
        "update_expense_request": {
            "bank_account_ref": {
                "id": "787dfb37-5707-4dc0-8a86-8d74e4cc78ea",
            },
            "contact_ref": {
                "id": "40e3e57c-2322-4898-966c-ca41adfd23fd",
            },
            "currency": "GBP",
            "issue_date": "2022-06-28T00:00:00.000Z",
            "lines": [
                shared.ExpenseTransactionLine(
                    account_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    invoice_to=None,
                    item_ref=None,
                    net_amount=Decimal("100"),
                    tax_amount=Decimal("20"),
                    tax_rate_ref=shared.RecordRef(
                        id="40e3e57c-2322-4898-966c-ca41adfd23fd",
                    ),
                    tracking_refs=None,
                ),
            ],
            "merchant_name": "Amazon UK",
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            "type": shared.UpdateExpenseRequestType.PAYMENT,
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
    })

    # Handle response
    print(res)

```
### Example Usage: Payment

<!-- UsageSnippet language="python" operationID="update-expense-transaction" method="put" path="/companies/{companyId}/sync/expenses/expense-transactions/{transactionId}" example="Payment" -->
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
        "update_expense_request": {
            "bank_account_ref": {
                "id": "97",
            },
            "contact_ref": {
                "id": "430",
            },
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "issue_date": "2024-05-21T00:00:00+00:00",
            "lines": [
                shared.ExpenseTransactionLine(
                    account_ref=shared.RecordRef(
                        id="35",
                    ),
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
            "merchant_name": "Amazon UK",
            "notes": "APPLE.COM/BILL - 09001077498 - Card Ending: 4590",
            "type": shared.UpdateExpenseRequestType.PAYMENT,
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "transaction_id": "336694d8-2dca-4cb5-a28d-3ccb83e55eee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateExpenseTransactionRequest](../../models/operations/updateexpensetransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[shared.UpdateExpenseResponse](../../models/shared/updateexpenseresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 422, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |