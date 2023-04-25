# list_bill_credit_notes
Available in: `bill_credit_notes`

Gets a list of all bill credit notes for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillCreditNotesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="voluptatibus",
)

res = s.bill_credit_notes.list_bill_credit_notes(req)

if res.bill_credit_notes is not None:
    # handle response
```