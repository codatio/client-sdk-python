# sales_orders

## Overview

Sales orders

### Available Operations

* [get](#get) - Get sales order
* [list](#list) - List sales orders

## get

Get sales order

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetSalesOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sales_order_id='distinctio',
)

res = s.sales_orders.get(req)

if res.sales_order is not None:
    # handle response
```

## list

Get sales orders

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListSalesOrdersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='fugit',
)

res = s.sales_orders.list(req)

if res.sales_orders is not None:
    # handle response
```
