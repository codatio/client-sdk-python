# bank_account_transactions

## Overview

Bank transactions for bank accounts

### Available Operations

* [create_bank_transactions](#create_bank_transactions) - Create bank transactions
* [get_create_bank_account_model](#get_create_bank_account_model) - List push options for bank account bank transactions
* [list_bank_account_transactions](#list_bank_account_transactions) - List bank transactions for bank account
* [list_bank_transactions](#list_bank_transactions) - List all bank transactions

## create_bank_transactions

Posts bank transactions to the accounting package for a given company.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id="excepturi",
        transactions=[
            shared.BankTransactionLine(
                amount=187.89,
                balance=3241.41,
                cleared_on_date="natus",
                counterparty="sed",
                description="iste",
                id="396fea75-96eb-410f-aaa2-352c5955907a",
                modified_date="doloribus",
                reconciled=False,
                reference="sapiente",
                source_modified_date="architecto",
                transaction_type="Check",
            ),
        ],
    ),
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    allow_sync_on_push_complete=False,
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=208876,
)

res = s.bank_account_transactions.create_bank_transactions(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

## get_create_bank_account_model

Gets the options of pushing bank account transactions.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateBankAccountModelRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bank_account_transactions.get_create_bank_account_model(req)

if res.push_option is not None:
    # handle response
```

## list_bank_account_transactions

Gets bank transactions for a given bank account ID

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankAccountTransactionsRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="culpa",
)

res = s.bank_account_transactions.list_bank_account_transactions(req)

if res.bank_transactions_response is not None:
    # handle response
```

## list_bank_transactions

Gets the latest bank transactions for given account ID and company. Doesn't require connection ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankTransactionsRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="consequuntur",
)

res = s.bank_account_transactions.list_bank_transactions(req)

if res.bank_account_transactions is not None:
    # handle response
```
