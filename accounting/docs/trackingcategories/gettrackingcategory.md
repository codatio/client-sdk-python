# get_tracking_category
Available in: `tracking_categories`

Gets the specified tracking categories for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetTrackingCategoryRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    tracking_category_id="provident",
)

res = s.tracking_categories.get_tracking_category(req)

if res.tracking_category_tree is not None:
    # handle response
```