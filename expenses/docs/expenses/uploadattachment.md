# upload_attachment
Available in: `expenses`

Creates an attachment in the accounting software against the given transactionId

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadAttachmentRequest(
    request_body=operations.UploadAttachmentRequestBody(
        content="delectus".encode(),
        request_body="tempora",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    sync_id="6fb40d5e-b13e-11ed-afa1-0242ac120002",
    transaction_id="336694d8-2dca-4cb5-a28d-3ccb83e55eee",
)

res = s.expenses.upload_attachment(req)

if res.attachment is not None:
    # handle response
```