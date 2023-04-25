# get_customers
Available in: `customers`

Gets the latest customers for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="vero",
)

res = s.customers.get_customers(req)

if res.customers is not None:
    # handle response
```