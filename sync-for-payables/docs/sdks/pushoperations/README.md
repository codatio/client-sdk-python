# push_operations

## Overview

Access create, update and delete operations made to an SMB's data connection.

### Available Operations

* [get](#get) - Get push operation
* [list](#list) - List push operations

## get

Retrieve push operation.

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPushOperationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    push_operation_key='c9c3f567-e0e2-4527-a5b1-d62fcdace1f0',
)

res = s.push_operations.get(req)

if res.push_operation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPushOperationRequest](../../models/operations/getpushoperationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetPushOperationResponse](../../models/operations/getpushoperationresponse.md)**


## list

List push operation records.

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListPushOperationsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='sunt',
)

res = s.push_operations.list(req)

if res.push_operations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPushOperationsRequest](../../models/operations/listpushoperationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListPushOperationsResponse](../../models/operations/listpushoperationsresponse.md)**

