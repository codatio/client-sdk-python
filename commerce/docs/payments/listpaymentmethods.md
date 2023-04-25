# list_payment_methods
Available in: `payments`

Retrieve a list of payment methods, such as card, cash or other online payment methods, as held in the linked commerce platform.

## Example Usage
```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPaymentMethodsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="quibusdam",
)

res = s.payments.list_payment_methods(req)

if res.payment_methods is not None:
    # handle response
```