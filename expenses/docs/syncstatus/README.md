# sync_status

## Overview

Check the status of ongoing or previous expense syncs.

### Available Operations

* [get_last_successful_sync](#get_last_successful_sync) - Last successful sync
* [get_latest_sync](#get_latest_sync) - Latest sync status
* [get_sync_by_id](#get_sync_by_id) - Get Sync status
* [list_syncs](#list_syncs) - List sync statuses

## get_last_successful_sync

Gets the status of the last successfull sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetLastSuccessfulSyncRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync_status.get_last_successful_sync(req)

if res.company_sync_status is not None:
    # handle response
```

## get_latest_sync

Gets the latest sync status

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetLatestSyncRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync_status.get_latest_sync(req)

if res.company_sync_status is not None:
    # handle response
```

## get_sync_by_id

Get the sync status for a specified sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSyncByIDRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
)

res = s.sync_status.get_sync_by_id(req)

if res.company_sync_status is not None:
    # handle response
```

## list_syncs

Gets a list of sync statuses

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSyncsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.sync_status.list_syncs(req)

if res.company_sync_statuses is not None:
    # handle response
```
