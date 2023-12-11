<!-- Start SDK Example Usage [usage] -->
```python
import codatcommerce
from codatcommerce.models import operations

s = codatcommerce.CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GetCustomerRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    customer_id='string',
)

res = s.customers.get(req)

if res.customer is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->