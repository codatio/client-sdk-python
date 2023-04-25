# get_bill_credit_note
Available in: `bill_credit_notes`

Gets a single billCreditNote corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id="velit",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_credit_notes.get_bill_credit_note(req)

if res.bill_credit_note is not None:
    # handle response
```