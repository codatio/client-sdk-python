# delete_journal_entry
Available in: `journal_entries`

Deletes a journal entry from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteJournalEntryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    journal_entry_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.journal_entries.delete_journal_entry(req)

if res.push_operation_summary is not None:
    # handle response
```