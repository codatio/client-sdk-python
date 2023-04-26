# transactions

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [list](#list) - List transactions

## list

Details of all financial transactions recorded in the commerce or point of sale system are added to the Transactions data type. For example, payments, service charges, and fees.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListTransactionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="illum",
)

res = s.transactions.list(req)

if res.transactions is not None:
    # handle response
```
