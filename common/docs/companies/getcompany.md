# get_company
Available in: `companies`

Get metadata for a single company

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.get_company(req)

if res.company is not None:
    # handle response
```