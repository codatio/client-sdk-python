<!-- Start SDK Example Usage -->


```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    auth_header="",
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