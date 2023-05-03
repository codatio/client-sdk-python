# account_transactions

## Overview

Account transactions

### Available Operations

* [get](#get) - Get account transaction
* [list](#list) - List account transactions

## get

Returns a specific [account transaction](https://docs.codat.io/accounting-api#/schemas/AccountTransaction).

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountTransactionRequest(
    account_transaction_id='provident',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.account_transactions.get(req)

if res.account_transaction is not None:
    # handle response
```

## list

Returns a list of [account transactions](https://docs.codat.io/accounting-api#/schemas/AccountTransaction) for a given company's connection.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListAccountTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='distinctio',
)

res = s.account_transactions.list(req)

if res.account_transactions is not None:
    # handle response
```
