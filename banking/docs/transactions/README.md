# transactions

## Overview

An immutable source of up-to-date information on income and expenditure.

### Available Operations

* [get](#get) - Get bank transaction
* [list](#list) - List transactions
* [~~list_bank_transactions~~](#list_bank_transactions) - List banking transactions :warning: **Deprecated** - Use `list` instead.

## get

Gets a specified bank transaction for a given company

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTransactionRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    transaction_id='corrupti',
)

res = s.transactions.get(req)

if res.transaction is not None:
    # handle response
```

## list

Gets a list of transactions incurred by a bank account.

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='illum',
)

res = s.transactions.list(req)

if res.transactions is not None:
    # handle response
```

## ~~list_bank_transactions~~

Gets a list of transactions incurred by a company across all bank accounts.

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible. Use `list` instead.

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBankTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='vel',
)

res = s.transactions.list_bank_transactions(req)

if res.transactions is not None:
    # handle response
```
