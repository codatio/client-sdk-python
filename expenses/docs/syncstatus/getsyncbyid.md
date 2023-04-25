# get_sync_by_id
Available in: `sync_status`

Get the sync status for a specified sync

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSyncByIDRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    sync_id="6fb40d5e-b13e-11ed-afa1-0242ac120002",
)

res = s.sync_status.get_sync_by_id(req)

if res.company_sync_status is not None:
    # handle response
```