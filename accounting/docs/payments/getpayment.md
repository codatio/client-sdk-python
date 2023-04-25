# get_payment
Available in: `payments`

Get payment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPaymentRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    payment_id="qui",
)

res = s.payments.get_payment(req)

if res.payment is not None:
    # handle response
```