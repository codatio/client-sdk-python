# create_company
Available in: `companies`

Create a new company

## Example Usage
```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.CompanyRequestBody(
    description="corrupti",
    name="Ben Mueller",
)

res = s.companies.create_company(req)

if res.company is not None:
    # handle response
```