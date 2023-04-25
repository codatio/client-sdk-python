# get_company_data_status
Available in: `data_status`

Get the state of each data type for a company

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCompanyDataStatusRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.data_status.get_company_data_status(req)

if res.data_status_response is not None:
    # handle response
```