<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountCategoryRequest(
    account_id="unde",
    company_id="deserunt",
    connection_id="porro",
)
    
res = s.categories.get_account_category(req)

if res.categorised_account is not None:
    # handle response
```
<!-- End SDK Example Usage -->