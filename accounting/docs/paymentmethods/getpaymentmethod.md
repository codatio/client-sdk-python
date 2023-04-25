# get_payment_method
Available in: `payment_methods`

Gets the specified payment method for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPaymentMethodRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    payment_method_id="facere",
)

res = s.payment_methods.get_payment_method(req)

if res.payment_method is not None:
    # handle response
```