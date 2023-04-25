# get_credit_note
Available in: `credit_notes`

Gets a single creditNote corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreditNoteRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    credit_note_id="eligendi",
)

res = s.credit_notes.get_credit_note(req)

if res.credit_note is not None:
    # handle response
```