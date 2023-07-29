# sync

## Overview

Initiate a sync of Sync for Commerce company data into their respective accounting software.

### Available Operations

* [request_sync](#request_sync) - Initiate new sync
* [request_sync_for_date_range](#request_sync_for_date_range) - Initiate sync for specific range

## request_sync

Run a Commerce sync from the last successful sync up to the date provided (optional), otherwise UtcNow is used.\r\nIf there was no previously successful sync, the start date in the config is used.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.RequestSyncRequest(
    sync_to_latest_args=shared.SyncToLatestArgs(
        sync_to='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.request_sync(req)

if res.sync_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.RequestSyncRequest](../../models/operations/requestsyncrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.RequestSyncResponse](../../models/operations/requestsyncresponse.md)**


## request_sync_for_date_range

Initiate a sync for the specified start date to the specified finish date in the request payload.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.RequestSyncForDateRangeRequest(
    sync_range=shared.SyncRange(
        date_range=shared.SyncRangeDateRange(
            finish='2022-10-23T00:00:00.000Z',
            start='2022-10-23T00:00:00.000Z',
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.request_sync_for_date_range(req)

if res.sync_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RequestSyncForDateRangeRequest](../../models/operations/requestsyncfordaterangerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.RequestSyncForDateRangeResponse](../../models/operations/requestsyncfordaterangeresponse.md)**

