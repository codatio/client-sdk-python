<!-- Start SDK Example Usage -->
```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CompanyRequestBody(
    description="corrupti",
    name="provident",
)
    
res = s.companies.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->