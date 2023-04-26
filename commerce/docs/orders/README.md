# orders

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [list](#list) - List orders

## list

Get a list of orders placed or held on the linked commerce platform

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListOrdersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="distinctio",
)

res = s.orders.list(req)

if res.orders is not None:
    # handle response
```
