# list_tracking_categories
Available in: `tracking_categories`

Gets the latest tracking categories for a given company.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListTrackingCategoriesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="vitae",
)

res = s.tracking_categories.list_tracking_categories(req)

if res.tracking_categories is not None:
    # handle response
```