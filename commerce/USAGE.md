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
   
req = operations.GetCommerceInfoRequest(
    path_params=operations.GetCommerceInfoPathParams(
        company_id="unde",
        connection_id="deserunt",
    ),
)
    
res = s.company_info.get_commerce_info(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->