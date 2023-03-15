<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyConfigurationRequest(
    company_id="unde",
)
    
res = s.configuration.get_company_configuration(req)

if res.get_company_configuration_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->