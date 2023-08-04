<!-- Start SDK Example Usage -->


```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDataTypeDataIntegrityDetailsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='corrupti',
)

res = s.data_integrity.details(req)

if res.details is not None:
    # handle response
```
<!-- End SDK Example Usage -->