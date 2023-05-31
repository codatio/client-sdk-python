# accounts

## Overview

Where payments are made or received, and bank transactions are recorded.

### Available Operations

* [get](#get) - Get account
* [list](#list) - List accounts

## get

Gets a specified bank account for a given company

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountRequest(
    account_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.accounts.get(req)

if res.account is not None:
    # handle response
```

## list

Gets a list of all bank accounts of the SMB, with rich data like balances, account numbers and institutions holdingthe accounts.

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListAccountsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='distinctio',
)

res = s.accounts.list(req)

if res.accounts is not None:
    # handle response
```
