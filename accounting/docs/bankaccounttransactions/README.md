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
    create_bank_transactions=shared.CreateBankTransactions(
        account_id='excepturi',
        transactions=[
            shared.CreateBankAccountTransaction(
                amount=9255.97,
                date_='2022-10-23T00:00:00.000Z',
                description='ab',
                id='51a05dfc-2ddf-47cc-b8ca-1ba928fc8167',
            ),
            shared.CreateBankAccountTransaction(
                amount=2645.55,
                date_='2022-10-23T00:00:00.000Z',
                description='impedit',
                id='b7392059-2939-46fe-a759-6eb10faaa235',
            ),
        ],
    ),
    account_id='explicabo',
    allow_sync_on_push_complete=False,
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=750686,
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
    account_id='enim',
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
    account_id='omnis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='nemo',
)

res = s.bank_account_transactions.list(req)

if res.bank_transactions_response is not None:
    # handle response
```
