# download_bill_attachment
Available in: `bills`

Download bill attachment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadBillAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bills.download_bill_attachment(req)

if res.data is not None:
    # handle response
```