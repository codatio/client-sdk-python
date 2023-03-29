<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CompanyRequestBody(
    description="unde",
    name="deserunt",
)
    
res = s.companies.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->