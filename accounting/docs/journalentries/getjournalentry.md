# get_journal_entry
Available in: `journal_entries`

Gets a single JournalEntry corresponding to the given ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetJournalEntryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    journal_entry_id="voluptatum",
)

res = s.journal_entries.get_journal_entry(req)

if res.journal_entry is not None:
    # handle response
```