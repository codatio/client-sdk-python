# tracking_categories

## Overview

Tracking categories

### Available Operations

* [get](#get) - Get tracking categories
* [list](#list) - List tracking categories

## get

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    tracking_category_id='quas',
)

res = s.tracking_categories.get(req)

if res.tracking_category_tree is not None:
    # handle response
```

## list

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='expedita',
)

res = s.tracking_categories.list(req)

if res.tracking_categories is not None:
    # handle response
```
