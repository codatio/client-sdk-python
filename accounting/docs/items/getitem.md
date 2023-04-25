# get_item
Available in: `items`

Gets the specified item for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetItemRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    item_id="assumenda",
)

res = s.items.get_item(req)

if res.item is not None:
    # handle response
```