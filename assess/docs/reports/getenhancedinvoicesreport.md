# get_enhanced_invoices_report
Available in: `reports`

Gets a list of invoices linked to the corresponding banking transaction

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedInvoicesReportRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    page=1,
    page_size=100,
    query="repudiandae",
)

res = s.reports.get_enhanced_invoices_report(req)

if res.enhanced_invoices_report is not None:
    # handle response
```