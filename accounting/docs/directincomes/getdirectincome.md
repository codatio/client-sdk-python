# get_direct_income
Available in: `direct_incomes`

Gets the specified direct income for a given company and connection.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetDirectIncomeRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    direct_income_id="excepturi",
)

res = s.direct_incomes.get_direct_income(req)

if res.direct_income is not None:
    # handle response
```