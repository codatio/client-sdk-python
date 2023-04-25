# get_aged_debtors_report
Available in: `reports`

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

## Example Usage
```python
import codataccounting
import dateutil.parser
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAgedDebtorsReportRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.reports.get_aged_debtors_report(req)

if res.aged_debtor_report is not None:
    # handle response
```