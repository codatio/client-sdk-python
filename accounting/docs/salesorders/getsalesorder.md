# get_sales_order
Available in: `sales_orders`

Get sales order

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSalesOrderRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    sales_order_id="voluptatibus",
)

res = s.sales_orders.get_sales_order(req)

if res.sales_order is not None:
    # handle response
```