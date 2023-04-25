# get_accounting_marketing_metrics
Available in: `excel_reports`

Request an Excel report for download.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountingMarketingMetricsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    include_display_names=False,
    number_of_periods=739264,
    period_length=19987,
    period_unit="Day",
    report_date="29-09-2020",
    show_input_values=False,
)

res = s.excel_reports.get_accounting_marketing_metrics(req)

if res.report is not None:
    # handle response
```