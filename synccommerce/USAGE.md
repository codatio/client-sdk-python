<!-- Start SDK Example Usage -->
```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CreateCompany(
    name="Bob's Burgers",
)

res = s.company_management.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->