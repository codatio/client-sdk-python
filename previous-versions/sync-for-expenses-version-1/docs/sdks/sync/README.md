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
            'c2ddf7cc-78ca-41ba-928f-c816742cb739',
            '20592939-6fea-4759-aeb1-0faaa2352c59',
            '55907aff-1a3a-42fa-9467-739251aa52c3',
            'f5ad019d-a1ff-4e78-b097-b0074f15471b',
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

