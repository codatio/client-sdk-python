# get_balance_sheet
Available in: `financials`

Gets the latest balance sheet for a company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBalanceSheetRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=992382,
    periods_to_compare=843875,
    start_month="2022-10-23T00:00:00Z",
)

res = s.financials.get_balance_sheet(req)

if res.balance_sheet is not None:
    # handle response
```