# get_commerce_lifetime_value_metrics
Available in: `reports`

Gets the lifetime value metric for a specific company connection, over one or more periods of time.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCommerceLifetimeValueMetricsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    include_display_names=False,
    number_of_periods=118727,
    period_length=688661,
    period_unit="Week",
    report_date="29-09-2020",
)

res = s.reports.get_commerce_lifetime_value_metrics(req)

if res.report is not None:
    # handle response
```