# intiate_sync
Available in: `sync`

Initiate sync of pending transactions.

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.IntiateSyncRequest(
    post_sync=shared.PostSync(
        dataset_ids=[
            "7cc8796e-d151-4a05-9fc2-ddf7cc78ca1b",
            "a928fc81-6742-4cb7-b920-5929396fea75",
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.sync.intiate_sync(req)

if res.sync_initiated is not None:
    # handle response
```