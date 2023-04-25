# delete_company
Available in: `companies`

Delete the given company from Codat.
This operation is not reversible.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteCompanyRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.delete_company(req)

if res.status_code == 200:
    # handle response
```