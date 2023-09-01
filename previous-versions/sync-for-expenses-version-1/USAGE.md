<!-- Start SDK Example Usage -->


```python
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    name='Bank of Dave',
)

res = s.companies.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->