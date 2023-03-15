<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceInfoRequest(
    company_id="unde",
    connection_id="deserunt",
)
    
res = s.company_info.get_commerce_info(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->