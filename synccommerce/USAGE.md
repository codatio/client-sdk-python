<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.AddDataConnectionRequest(
    request_body="unde",
    company_id="deserunt",
)
    
res = s.company_management.add_data_connection(req)

if res.add_data_connection_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->