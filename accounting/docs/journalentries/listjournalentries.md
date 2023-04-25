# list_journal_entries
Available in: `journal_entries`

Gets the latest journal entries for a company, with pagination

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListJournalEntriesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="deleniti",
)

res = s.journal_entries.list_journal_entries(req)

if res.journal_entries is not None:
    # handle response
```