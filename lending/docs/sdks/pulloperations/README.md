# ManageData.PullOperations

## Overview

### Available Operations

* [get](#get) - Get pull operation
* [list](#list) - List pull operations

## get

Retrieve information about a single dataset or pull operation.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-pull-operation" method="get" path="/companies/{companyId}/data/history/{datasetId}" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.manage_data.pull_operations.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "dataset_id": "fa5f3e86-bd80-49b8-853c-5fbba4b201f5",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPullOperationRequest](../../models/operations/getpulloperationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.PullOperation](../../models/shared/pulloperation.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list

Gets the pull operation history (datasets) for a given company.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-pull-operations" method="get" path="/companies/{companyId}/data/history" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.manage_data.pull_operations.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPullOperationsRequest](../../models/operations/listpulloperationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.PullOperations](../../models/shared/pulloperations.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |