# get_direct_cost
Available in: `direct_costs`

Gets the specified direct cost for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectCostRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_cost_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.direct_costs.get_direct_cost(req)

if res.direct_cost is not None:
    # handle response
```