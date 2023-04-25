# request_recurring_revenue_metrics
Available in: `reports`

Request production of key subscription revenue metrics.

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.RequestRecurringRevenueMetricsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.reports.request_recurring_revenue_metrics(req)

if res.report is not None:
    # handle response
```