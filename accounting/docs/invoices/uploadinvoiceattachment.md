# upload_invoice_attachment
Available in: `invoices`

Push invoice attachment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadInvoiceAttachmentRequest(
    request_body=operations.UploadInvoiceAttachmentRequestBody(
        content="alias".encode(),
        request_body="illum",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    invoice_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.invoices.upload_invoice_attachment(req)

if res.status_code == 200:
    # handle response
```