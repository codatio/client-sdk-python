# get_accounts_for_enhanced_profit_and_loss
Available in: `reports`

The Enhanced Profit and Loss Accounts endpoint returns a list of categorized accounts that appear on a company’s Profit and Loss. It also includes a balance per the financial statement date.

Codat suggests a category for each account automatically, but you can [change it](/docs/assess-categorizing-accounts-ecommerce-lending) to a more suitable one.

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountsForEnhancedProfitAndLossRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    number_of_periods=120196,
    report_date="29-09-2020",
)

res = s.reports.get_accounts_for_enhanced_profit_and_loss(req)

if res.enhanced_report is not None:
    # handle response
```