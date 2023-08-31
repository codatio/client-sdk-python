<!-- Start SDK Example Usage -->


```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateCompany(
    name='Bob's Burgers',
)

res = s.advanced_controls.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->