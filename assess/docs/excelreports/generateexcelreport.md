# generate_excel_report
Available in: `excel_reports`

Generate an Excel report which can subsequently be downloaded.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GenerateExcelReportRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_type="assess",
)

res = s.excel_reports.generate_excel_report(req)

if res.excel_status is not None:
    # handle response
```