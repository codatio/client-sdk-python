# delete_bill_payment
Available in: `bill_payments`

Deletes a bill payment from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our Oracle NetSuite integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteBillPaymentRequest(
    bill_payment_id="autem",
    company_id="quo",
    connection_id="nesciunt",
)

res = s.bill_payments.delete_bill_payment(req)

if res.push_operation_summary is not None:
    # handle response
```