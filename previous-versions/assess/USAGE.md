<!-- Start SDK Example Usage [usage] -->
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

req = operations.GenerateLoanSummaryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    source_type=operations.SourceType.ACCOUNTING,
)

res = s.reports.generate_loan_summary(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->