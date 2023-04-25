# post_sync_info
Available in: `company_info`

Initiates the process of synchronising basic info for a company

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.PostSyncInfoRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.company_info.post_sync_info(req)

if res.dataset is not None:
    # handle response
```