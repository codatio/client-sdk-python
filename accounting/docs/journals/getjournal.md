# get_journal
Available in: `journals`

Gets a single journal corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetJournalRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    journal_id="mollitia",
)

res = s.journals.get_journal(req)

if res.journal is not None:
    # handle response
```