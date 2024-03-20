# Sync
(*sync*)

## Overview

Trigger and monitor expense syncs to accounting software.

### Available Operations

* [get](#get) - Get sync status
* [get_last_successful_sync](#get_last_successful_sync) - Last successful sync
* [get_latest_sync](#get_latest_sync) - Latest sync status
* [initiate_sync](#initiate_sync) - Initiate sync
* [list](#list) - List sync statuses

## get

Get the sync status for a specified sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSyncByIDRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
)

res = s.sync.get(req)

if res.company_sync_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSyncByIDRequest](../../models/operations/getsyncbyidrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.GetSyncByIDResponse](../../models/operations/getsyncbyidresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## get_last_successful_sync

Gets the status of the last successful sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetLastSuccessfulSyncRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.get_last_successful_sync(req)

if res.company_sync_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetLastSuccessfulSyncRequest](../../models/operations/getlastsuccessfulsyncrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.GetLastSuccessfulSyncResponse](../../models/operations/getlastsuccessfulsyncresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## get_latest_sync

Gets the latest sync status

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetLatestSyncRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.get_latest_sync(req)

if res.company_sync_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLatestSyncRequest](../../models/operations/getlatestsyncrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetLatestSyncResponse](../../models/operations/getlatestsyncresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## initiate_sync

Initiate sync of pending transactions.

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.InitiateSyncRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.initiate_sync(req)

if res.sync_initiated is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.InitiateSyncRequest](../../models/operations/initiatesyncrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.InitiateSyncResponse](../../models/operations/initiatesyncresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,422,429,500,503 | application/json                    |
| errors.SDKError                     | 4x-5xx                              | */*                                 |

## list

Gets a list of sync statuses

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSyncsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.list(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListSyncsRequest](../../models/operations/listsyncsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListSyncsResponse](../../models/operations/listsyncsresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |
