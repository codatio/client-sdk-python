# get_bill_payments
Available in: `bill_payments`

Get a bill payment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillPaymentsRequest(
    bill_payment_id="illum",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_payments.get_bill_payments(req)

if res.bill_payment is not None:
    # handle response
```