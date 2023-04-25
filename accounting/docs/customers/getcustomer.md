# get_customer
Available in: `customers`

Gets a single customer corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    customer_id="tenetur",
)

res = s.customers.get_customer(req)

if res.customer is not None:
    # handle response
```