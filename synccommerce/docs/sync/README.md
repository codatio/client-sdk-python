# sync

## Overview

Initiate a sync of Sync for Commerce company data into their respective accounting software.

### Available Operations

* [request_sync](#request_sync) - Run a Commerce sync from the last successful sync
* [request_sync_for_date_range](#request_sync_for_date_range) - Run a Commerce sync from a given date range

## request_sync

Run a Commerce sync from the last successful sync up to the date provided (optional), otherwise UtcNow is used.
If there was no previously successful sync, the start date in the config is used.

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
        sync_to='nulla',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.request_sync(req)

if res.sync_summary is not None:
    # handle response
```

## request_sync_for_date_range

Run a Commerce sync from the specified start date to the specified finish date in the request payload.

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
    date_range=shared.DateRange(
        finish='corrupti',
        start='illum',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync.request_sync_for_date_range(req)

if res.sync_summary is not None:
    # handle response
```
