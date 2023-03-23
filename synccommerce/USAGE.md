<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="Basic YOUR_ENCODED_API_KEY",
    ),
)


req = operations.AddDataConnectionRequest(
    request_body="unde",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)
    
res = s.company_management.add_data_connection(req)

if res.add_data_connection_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->