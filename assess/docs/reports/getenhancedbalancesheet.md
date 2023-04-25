# get_enhanced_balance_sheet
Available in: `reports`

Gets a fully categorized balance sheet statement for a given company, over one or more period(s).

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedBalanceSheetRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    include_display_names=False,
    number_of_periods=265389,
    period_length=508969,
    report_date="29-09-2020",
)

res = s.reports.get_enhanced_balance_sheet(req)

if res.report is not None:
    # handle response
```