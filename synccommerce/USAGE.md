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
   
req = operations.AddDataConnectionRequest(
    path_params=operations.AddDataConnectionPathParams(
        company_id="unde",
    ),
    request="deserunt",
)
    
res = s.company_management.add_data_connection(req)

if res.add_data_connection_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->