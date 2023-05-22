# bank_account_transactions

## Overview

Bank transactions for bank accounts

### Available Operations

* [create](#create) - Create bank transactions
* [get_create_model](#get_create_model) - List push options for bank account bank transactions
* [list](#list) - List bank transactions for bank account

## create

Posts bank transactions to the accounting package for a given company.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) for integrations that support POST methods.

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
        account_id='quis',
        transactions=[
            shared.BankTransactionLine(
                amount=6481.72,
                balance=202.18,
                cleared_on_date='ipsam',
                counterparty='repellendus',
                description='sapiente',
                id='c2ddf7cc-78ca-41ba-928f-c816742cb739',
                modified_date='aspernatur',
                reconciled=False,
                reference='perferendis',
                source_modified_date='ad',
                transaction_type=shared.BankTransactionType.CHECK,
            ),
        ],
    ),
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=149675,
)

res = s.bank_account_transactions.create(req)

if res.create_bank_transactions_response is not None:
    # handle response
```

## get_create_model

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
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bank_account_transactions.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

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
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='iste',
)

res = s.bank_account_transactions.list(req)

if res.bank_transactions_response is not None:
    # handle response
```
