# get_purchase_order
Available in: `purchase_orders`

Get purchase order

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPurchaseOrderRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    purchase_order_id="provident",
)

res = s.purchase_orders.get_purchase_order(req)

if res.purchase_order is not None:
    # handle response
```