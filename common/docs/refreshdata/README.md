# refresh_data

## Overview

Queue pull operations to refresh data in Codat.

### Available Operations

* [all](#all) - Queue pull operations
* [by_data_type](#by_data_type) - Queue pull operation

## all

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.refresh_data.all(req)

if res.status_code == 200:
    # handle response
```

## by_data_type

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='b7392059-2939-46fe-a759-6eb10faaa235',
    data_type=shared.DataTypeEnum.INVOICES,
)

res = s.refresh_data.by_data_type(req)

if res.pull_operation is not None:
    # handle response
```
