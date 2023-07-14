<!-- Start SDK Example Usage -->


```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDataIntegrityStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
)

res = s.data_integrity.get_data_integrity_status(req)

if res.status is not None:
    # handle response
```
<!-- End SDK Example Usage -->