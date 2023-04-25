# get_customer_attachments
Available in: `customers`

Get customer attachments

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCustomerAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    customer_id="pariatur",
)

res = s.customers.get_customer_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```