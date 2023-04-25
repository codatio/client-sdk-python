# get_invoice
Available in: `invoices`

Get invoice

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice(req)

if res.invoice is not None:
    # handle response
```