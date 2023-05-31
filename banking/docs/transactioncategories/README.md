# transaction_categories

## Overview

Hierarchical categories associated with a transaction for greater contextual meaning to transaction activity.

### Available Operations

* [get](#get) - Get transaction category
* [list](#list) - List all transaction categories

## get

Gets a specified bank transaction category for a given company

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTransactionCategoryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    transaction_category_id='quibusdam',
)

res = s.transaction_categories.get(req)

if res.transaction_category is not None:
    # handle response
```

## list

Gets a list of hierarchical categories associated with a transaction for greater contextual meaning to transactionactivity.

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListTransactionCategoriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='unde',
)

res = s.transaction_categories.list(req)

if res.transaction_categories is not None:
    # handle response
```
