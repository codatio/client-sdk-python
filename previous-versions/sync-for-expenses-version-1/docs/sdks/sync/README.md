# Sync
(*sync*)

## Overview

Triggering a new sync of expenses to accounting software.

### Available Operations

* [initiate_sync](#initiate_sync) - Initiate sync

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

if res is not None:
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
