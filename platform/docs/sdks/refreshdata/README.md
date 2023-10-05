# RefreshData
(*refresh_data*)

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
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.RefreshCompanyDataRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.refresh_data.all(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RefreshCompanyDataRequest](../../models/operations/refreshcompanydatarequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.RefreshCompanyDataResponse](../../models/operations/refreshcompanydataresponse.md)**


## by_data_type

Refreshes a given data type for a given company.

This is an asynchronous operation, and will bring updated data into Codat from the linked integration for you to view.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.RefreshDataTypeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='8803f6d1-c3aa-40d5-a409-b9d7f498be91',
    data_type=shared.DataType.INVOICES,
)

res = s.refresh_data.by_data_type(req)

if res.pull_operation is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RefreshDataTypeRequest](../../models/operations/refreshdatatyperequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.RefreshDataTypeResponse](../../models/operations/refreshdatatyperesponse.md)**


## get

Get the state of each data type for a company

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetCompanyDataStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.refresh_data.get(req)

if res.data_statuses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetCompanyDataStatusRequest](../../models/operations/getcompanydatastatusrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetCompanyDataStatusResponse](../../models/operations/getcompanydatastatusresponse.md)**


## get_pull_operation

Retrieve information about a single dataset or pull operation.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetPullOperationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    dataset_id='7911a54a-c808-4f4b-b87e-b195f52b4da5',
)

res = s.refresh_data.get_pull_operation(req)

if res.pull_operation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPullOperationRequest](../../models/operations/getpulloperationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetPullOperationResponse](../../models/operations/getpulloperationresponse.md)**


## list_pull_operations

Gets the pull operation history (datasets) for a given company.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.ListPullOperationsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='Dock Elegant Buckinghamshire',
)

res = s.refresh_data.list_pull_operations(req)

if res.pull_operations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPullOperationsRequest](../../models/operations/listpulloperationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListPullOperationsResponse](../../models/operations/listpulloperationsresponse.md)**

