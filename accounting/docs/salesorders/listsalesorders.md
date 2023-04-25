# list_sales_orders
Available in: `sales_orders`

Get sales orders

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSalesOrdersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="ipsa",
)

res = s.sales_orders.list_sales_orders(req)

if res.sales_orders is not None:
    # handle response
```