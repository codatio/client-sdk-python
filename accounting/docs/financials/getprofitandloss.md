# get_profit_and_loss
Available in: `financials`

Gets the latest profit and loss for a company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProfitAndLossRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=251070,
    periods_to_compare=785469,
    start_month="2022-10-23T00:00:00Z",
)

res = s.financials.get_profit_and_loss(req)

if res.profit_and_loss_report is not None:
    # handle response
```