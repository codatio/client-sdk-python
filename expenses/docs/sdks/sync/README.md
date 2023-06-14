# sync

## Overview

Triggering a new sync of expenses to accounting software.

### Available Operations

* [intiate_sync](#intiate_sync) - Initiate sync

## intiate_sync

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

req = operations.IntiateSyncRequest(
    post_sync=shared.PostSync(
        dataset_ids=[
            '96ed151a-05df-4c2d-9f7c-c78ca1ba928f',
            'c816742c-b739-4205-9293-96fea7596eb1',
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.intiate_sync(req)

if res.sync_initiated is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.IntiateSyncRequest](../../models/operations/intiatesyncrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.IntiateSyncResponse](../../models/operations/intiatesyncresponse.md)**
