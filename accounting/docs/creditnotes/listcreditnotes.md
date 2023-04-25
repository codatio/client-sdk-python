# list_credit_notes
Available in: `credit_notes`

Gets a list of all credit notes for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCreditNotesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="consequuntur",
)

res = s.credit_notes.list_credit_notes(req)

if res.credit_notes is not None:
    # handle response
```