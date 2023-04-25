# refresh_company_data
Available in: `refresh_data`

Refreshes all data types marked Fetch on first link.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.RefreshCompanyDataRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.refresh_data.refresh_company_data(req)

if res.status_code == 200:
    # handle response
```