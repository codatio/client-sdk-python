# get_sync_transaction
Available in: `transaction_status`

Gets the status of a transaction for a sync

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSyncTransactionRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    sync_id="6fb40d5e-b13e-11ed-afa1-0242ac120002",
    transaction_id="336694d8-2dca-4cb5-a28d-3ccb83e55eee",
)

res = s.transaction_status.get_sync_transaction(req)

if res.transaction_metadata is not None:
    # handle response
```