<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        authorization=shared.SchemeAuthorization(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.GetCompanyConfigurationRequest(
    path_params=operations.GetCompanyConfigurationPathParams(
        company_id="unde",
    ),
)
    
res = s.configuration.get_company_configuration(req)

if res.get_company_configuration_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->