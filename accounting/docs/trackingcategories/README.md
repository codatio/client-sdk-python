# tracking_categories

## Overview

Tracking categories

### Available Operations

* [get_tracking_category](#get_tracking_category) - Get tracking categories
* [list_tracking_categories](#list_tracking_categories) - List tracking categories

## get_tracking_category

Gets the specified tracking categories for a given company.

### Example Usage

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
    tracking_category_id="perferendis",
)

res = s.tracking_categories.get_tracking_category(req)

if res.tracking_category_tree is not None:
    # handle response
```

## list_tracking_categories

Gets the latest tracking categories for a given company.

### Example Usage

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
    query="nostrum",
)

res = s.tracking_categories.list_tracking_categories(req)

if res.tracking_categories is not None:
    # handle response
```
