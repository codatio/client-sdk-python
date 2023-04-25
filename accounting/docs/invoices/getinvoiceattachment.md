# get_invoice_attachment
Available in: `invoices`

Get invoice attachment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice_attachment(req)

if res.attachment is not None:
    # handle response
```