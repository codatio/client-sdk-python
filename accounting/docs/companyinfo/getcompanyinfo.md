# get_company_info
Available in: `company_info`

Gets the latest basic info for a company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyInfoRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.company_info.get_company_info(req)

if res.company_dataset is not None:
    # handle response
```