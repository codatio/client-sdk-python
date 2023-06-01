# bank_account_transactions

## Overview

Bank transactions for bank accounts

### Available Operations

* [create](#create) - Create bank transactions
* [get_create_model](#get_create_model) - List push options for bank account bank transactions
* [list](#list) - List bank transactions for bank account

## create

Posts bank transactions to the accounting package for a given company.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankTransactions) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBankTransactionsRequest(
    bank_transactions=shared.BankTransactions(
        account_id='veritatis',
        transactions=[
            shared.BankTransactionLine(
                amount=202.18,
                balance=3682.41,
                cleared_on_date='repellendus',
                counterparty='sapiente',
                description='quo',
                id='2ddf7cc7-8ca1-4ba9-a8fc-816742cb7392',
                modified_date='perferendis',
                reconciled=False,
                reference='ad',
                source_modified_date='natus',
                transaction_type=shared.BankTransactionType.DEBIT,
            ),
            shared.BankTransactionLine(
                amount=6120.96,
                balance=2223.21,
                cleared_on_date='natus',
                counterparty='laboriosam',
                description='hic',
                id='ea7596eb-10fa-4aa2-b52c-5955907aff1a',
                modified_date='dolorem',
                reconciled=False,
                reference='culpa',
                source_modified_date='consequuntur',
                transaction_type=shared.BankTransactionType.OTHER,
            ),
            shared.BankTransactionLine(
                amount=6531.08,
                balance=5818.5,
                cleared_on_date='numquam',
                counterparty='commodi',
                description='quam',
                id='739251aa-52c3-4f5a-9019-da1ffe78f097',
                modified_date='cum',
                reconciled=False,
                reference='perferendis',
                source_modified_date='doloremque',
                transaction_type=shared.BankTransactionType.DEP,
            ),
        ],
    ),
    account_id='ut',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=979587,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateBankAccountModelRequest(
    account_id='dicta',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBankAccountTransactionsRequest(
    account_id='corporis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='dolore',
)

res = s.bank_account_transactions.list(req)

if res.bank_transactions_response is not None:
    # handle response
```
