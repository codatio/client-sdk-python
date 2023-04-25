# get_supplier_attachment
Available in: `suppliers`

Get supplier attachment

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get_supplier_attachment(req)

if res.attachment is not None:
    # handle response
```