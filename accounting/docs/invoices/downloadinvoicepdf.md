# download_invoice_pdf
Available in: `invoices`

Get invoice as PDF

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadInvoicePdfRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.download_invoice_pdf(req)

if res.data is not None:
    # handle response
```