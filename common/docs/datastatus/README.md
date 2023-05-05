# data_status

## Overview

Understand the state of data within Codat.

### Available Operations

* [get](#get) - Get data status
* [get_pull_operation](#get_pull_operation) - Get pull operation
* [list_pull_operations](#list_pull_operations) - Get pull operations

## get

Get the state of each data type for a company

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCompanyDataStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.data_status.get(req)

if res.data_status_response is not None:
    # handle response
```

## get_pull_operation

Retrieve information about a single dataset or pull operation.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetPullOperationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    dataset_id='eaed9f0f-e77b-4bc9-a58f-ab8b4b99ab18',
)

res = s.data_status.get_pull_operation(req)

if res.pull_operation is not None:
    # handle response
```

## list_pull_operations

Gets the pull operation history (datasets) for a given company.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListPullOperationsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='quis',
)

res = s.data_status.list_pull_operations(req)

if res.data_connection_history is not None:
    # handle response
```
