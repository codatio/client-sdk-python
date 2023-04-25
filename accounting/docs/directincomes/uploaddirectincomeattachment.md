# upload_direct_income_attachment
Available in: `direct_incomes`

Posts a new direct income attachment for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content="doloribus".encode(),
        request_body="corporis",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="alias",
)

res = s.direct_incomes.upload_direct_income_attachment(req)

if res.status_code == 200:
    # handle response
```