# sync_status

## Overview

Status of the sync between commerce company data into their respective accounting software.

### Available Operations

* [get_sync_status](#get_sync_status) - Get sync status

## get_sync_status

Gets a list of sync statuses.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSyncStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync_status.get_sync_status(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetSyncStatusRequest](../../models/operations/getsyncstatusrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetSyncStatusResponse](../../models/operations/getsyncstatusresponse.md)**

