<!-- Start SDK Example Usage -->


```python
import codatcommerce
from codatcommerce.models import operations, shared

s = codatcommerce.CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GetCompanyInfoRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.company_info.get(req)

if res.company_info is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->