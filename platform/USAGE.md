<!-- Start SDK Example Usage -->


```python
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    name='Bank of Dave',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->