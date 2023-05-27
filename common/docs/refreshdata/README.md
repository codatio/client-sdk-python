# refresh_data

## Overview

Asynchronously retrieve data from an integration to refresh data in Codat.

### Available Operations

* [all](#all) - Refresh all data
* [by_data_type](#by_data_type) - Refresh data type
* [get](#get) - Get data status
* [get_pull_operation](#get_pull_operation) - Get pull operation
* [list_pull_operations](#list_pull_operations) - List pull operations

## all

Refreshes all data types with `fetch on first link` set to `true` for a given company.

This is an asynchronous operation, and will bring updated data into Codat from the linked integration for you to view.

[Read more](https://docs.codat.io/core-concepts/data-type-settings) about data type settings and `fetch on first link`.

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

Refreshes a given data type for a given company.

This is an asynchronous operation, and will bring updated data into Codat from the linked integration for you to view.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations, shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.RefreshDataTypeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='78ca1ba9-28fc-4816-b42c-b73920592939',
    data_type=shared.DataType.INVOICES,
)

res = s.refresh_data.by_data_type(req)

if res.pull_operation is not None:
    # handle response
```

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

res = s.refresh_data.get(req)

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

res = s.refresh_data.get_pull_operation(req)

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
    query='laboriosam',
)

res = s.refresh_data.list_pull_operations(req)

if res.data_connection_history is not None:
    # handle response
```
