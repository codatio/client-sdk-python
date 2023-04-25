# get_invoice_attachments
Available in: `invoices`

Get invoice attachments

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetInvoiceAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.get_invoice_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```