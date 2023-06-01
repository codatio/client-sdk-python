<!-- Start SDK Example Usage -->
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get_company_configuration(req)

if res.company_configuration is not None:
    # handle response
```
<!-- End SDK Example Usage -->