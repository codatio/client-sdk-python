# orders

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get](#get) - Get order
* [list](#list) - List orders

## get

Get a specific order placed or held on the linked commerce platform.

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_id='nulla',
)

res = s.orders.get(req)

if res.order is not None:
    # handle response
```

## list

Get a list of orders placed or held on the linked commerce platform

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListOrdersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='corrupti',
)

res = s.orders.list(req)

if res.orders is not None:
    # handle response
```
