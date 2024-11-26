# PushOperations
(*push_operations*)

## Overview

View historic push operations.

### Available Operations

* [get](#get) - Get push operation
* [list](#list) - List push operations

## get

Retrieve push operation.

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.push_operations.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "push_operation_key": "b888f774-3e7c-4135-a18c-6b985523c4bc",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPushOperationRequest](../../models/operations/getpushoperationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.PushOperation](../../models/shared/pushoperation.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## list

List push operation records.

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.push_operations.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "page": 1,
        "page_size": 100,
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPushOperationsRequest](../../models/operations/listpushoperationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.PushOperations](../../models/shared/pushoperations.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |