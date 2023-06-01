# company_info

## Overview

Company info

### Available Operations

* [get](#get) - Get company info
* [refresh](#refresh) - Refresh company info

## get

Gets the latest basic info for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyInfoRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.company_info.get(req)

if res.company_dataset is not None:
    # handle response
```

## refresh

Initiates the process of synchronising basic info for a company

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.RefreshCompanyInfoRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.company_info.refresh(req)

if res.dataset is not None:
    # handle response
```
