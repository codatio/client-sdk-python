# get_latest_sync
Available in: `sync_status`

Gets the latest sync status

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetLatestSyncRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.sync_status.get_latest_sync(req)

if res.company_sync_status is not None:
    # handle response
```