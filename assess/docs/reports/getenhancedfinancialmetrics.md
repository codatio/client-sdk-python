# get_enhanced_financial_metrics
Available in: `reports`

Gets all the available financial metrics for a given company, over one or more periods.

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedFinancialMetricsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    number_of_periods=916723,
    period_length=93940,
    report_date="29-09-2020",
    show_metric_inputs=False,
)

res = s.reports.get_enhanced_financial_metrics(req)

if res.financial_metrics is not None:
    # handle response
```