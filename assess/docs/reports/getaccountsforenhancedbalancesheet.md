# get_accounts_for_enhanced_balance_sheet
Available in: `reports`

The Enhanced Balance Sheet Accounts endpoint returns a list of categorized accounts that appear on a company’s Balance Sheet along with a balance per financial statement date.

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


req = operations.GetAccountsForEnhancedBalanceSheetRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    number_of_periods=979587,
    report_date="29-09-2020",
)

res = s.reports.get_accounts_for_enhanced_balance_sheet(req)

if res.enhanced_report is not None:
    # handle response
```