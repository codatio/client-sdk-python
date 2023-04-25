# get_data_integrity_details
Available in: `data_integrity`

Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegrityDetailsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type="banking-accounts",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="voluptatibus",
)

res = s.data_integrity.get_data_integrity_details(req)

if res.details is not None:
    # handle response
```