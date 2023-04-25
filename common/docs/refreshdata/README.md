# refresh_data

## Overview

Queue pull operations to refresh data in Codat.

### Available Operations

* [create_pull_operation](#create_pull_operation) - Queue pull operation
* [refresh_company_data](#refresh_company_data) - Queue pull operations

## create_pull_operation

Queue a single pull operation for the given company and data type.

This will bring updated data into Codat from the linked integration for you to view.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreatePullOperationRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="b7392059-2939-46fe-a759-6eb10faaa235",
    data_type="invoices",
)

res = s.refresh_data.create_pull_operation(req)

if res.pull_operation is not None:
    # handle response
```

## refresh_company_data

Refreshes all data types marked Fetch on first link.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.RefreshCompanyDataRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.refresh_data.refresh_company_data(req)

if res.status_code == 200:
    # handle response
```
