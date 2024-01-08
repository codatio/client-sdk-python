<!-- Start SDK Example Usage [usage] -->
```python
import codatbankfeeds
from codatbankfeeds.models import shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    description='Requested early access to the new financing scheme.',
    groups=[
        shared.Items(
            id='60d2fa12-8a04-11ee-b9d1-0242ac120002',
        ),
    ],
    name='Bank of Dave',
)

res = s.companies.create(req)

if res.company is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->