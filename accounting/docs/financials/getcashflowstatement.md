# get_cash_flow_statement
Available in: `financials`

Gets the latest cash flow statement for a company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCashFlowStatementRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=656964,
    periods_to_compare=1990,
    start_month="2022-10-23T00:00:00Z",
)

res = s.financials.get_cash_flow_statement(req)

if res.cash_flow_statement is not None:
    # handle response
```