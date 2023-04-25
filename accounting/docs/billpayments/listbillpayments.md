# list_bill_payments
Available in: `bill_payments`

Gets the latest billPayments for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillPaymentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nemo",
)

res = s.bill_payments.list_bill_payments(req)

if res.bill_payments is not None:
    # handle response
```