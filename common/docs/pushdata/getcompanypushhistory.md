# get_company_push_history
Available in: `push_data`

List push operation records.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyPushHistoryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="deserunt",
)

res = s.push_data.get_company_push_history(req)

if res.push_history_response is not None:
    # handle response
```