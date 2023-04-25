# get_data_integrity_summaries
Available in: `data_integrity`

Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDataIntegritySummariesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    data_type="banking-accounts",
    query="ipsa",
)

res = s.data_integrity.get_data_integrity_summaries(req)

if res.summaries is not None:
    # handle response
```