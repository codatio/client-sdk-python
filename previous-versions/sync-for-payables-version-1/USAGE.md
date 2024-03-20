<!-- Start SDK Example Usage [usage] -->
```python
import codatsyncpayables
from codatsyncpayables.models import shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->