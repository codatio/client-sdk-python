# list_companies
Available in: `companies`

List all companies that you have created in Codat.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCompaniesRequest(
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="iure",
)

res = s.companies.list_companies(req)

if res.companies is not None:
    # handle response
```