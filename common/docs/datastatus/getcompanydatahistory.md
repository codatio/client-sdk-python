# get_company_data_history
Available in: `data_status`

Gets the pull operation history (datasets) for a given company.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyDataHistoryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="quis",
)

res = s.data_status.get_company_data_history(req)

if res.data_connection_history is not None:
    # handle response
```