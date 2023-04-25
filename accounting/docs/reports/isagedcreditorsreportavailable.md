# is_aged_creditors_report_available
Available in: `reports`

Indicates whether the aged creditor report is available for the company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.IsAgedCreditorsReportAvailableRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.reports.is_aged_creditors_report_available(req)

if res.is_aged_creditors_report_available_200_application_json_boolean is not None:
    # handle response
```