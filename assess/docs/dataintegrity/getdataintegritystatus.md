# get_data_integrity_status
Available in: `data_integrity`

Gets match status for a given company and datatype.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegrityStatusRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type="banking-accounts",
)

res = s.data_integrity.get_data_integrity_status(req)

if res.status is not None:
    # handle response
```