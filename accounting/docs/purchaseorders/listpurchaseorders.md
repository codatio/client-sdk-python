# list_purchase_orders
Available in: `purchase_orders`

Get purchase orders

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPurchaseOrdersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="quod",
)

res = s.purchase_orders.list_purchase_orders(req)

if res.purchase_orders is not None:
    # handle response
```