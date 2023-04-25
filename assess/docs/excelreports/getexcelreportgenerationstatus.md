# get_excel_report_generation_status
Available in: `excel_reports`

Returns the status of the latest report requested.

## Example Usage
```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetExcelReportGenerationStatusRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    report_type="assess",
)

res = s.excel_reports.get_excel_report_generation_status(req)

if res.excel_status is not None:
    # handle response
```