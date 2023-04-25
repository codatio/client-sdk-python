# list_invoices
Available in: `invoices`

Gets the latest invoices for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListInvoicesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="nesciunt",
)

res = s.invoices.list_invoices(req)

if res.invoices is not None:
    # handle response
```