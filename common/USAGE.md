<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.CreateCompanyRequest(
    request=operations.CreateCompanyRequestBody(
        description="unde",
        name="deserunt",
    ),
)
    
res = s.companies.create_company(req)

if res.create_company_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->