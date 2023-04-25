# get_excel_report
Available in: `excel_reports`

Download the previously generated Excel report to a local drive.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetExcelReportRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_type="assess",
)

res = s.excel_reports.get_excel_report(req)

if res.body is not None:
    # handle response
```