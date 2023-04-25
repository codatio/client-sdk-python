# list_sync_transactions
Available in: `transaction_status`

Get's the transactions and status for a sync

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSyncTransactionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    page=1,
    page_size=100,
    sync_id="6fb40d5e-b13e-11ed-afa1-0242ac120002",
)

res = s.transaction_status.list_sync_transactions(req)

if res.transaction_metadata_list is not None:
    # handle response
```