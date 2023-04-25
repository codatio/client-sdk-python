# update_company
Available in: `companies`

Updates the given company with a new name and description

## Example Usage
```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateCompanyRequest(
    company_request_body=shared.CompanyRequestBody(
        description="magnam",
        name="Larry Windler",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.companies.update_company(req)

if res.company is not None:
    # handle response
```