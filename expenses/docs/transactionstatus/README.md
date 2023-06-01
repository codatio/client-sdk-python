# transaction_status

## Overview

Retrieve the status of transactions within a sync.

### Available Operations

* [get_sync_transaction](#get_sync_transaction) - Get Sync Transaction
* [list_sync_transactions](#list_sync_transactions) - Get Sync transactions

## get_sync_transaction

Gets the status of a transaction for a sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSyncTransactionRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
    transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee',
)

res = s.transaction_status.get_sync_transaction(req)

if res.transaction_metadata is not None:
    # handle response
```

## list_sync_transactions

Get's the transactions and status for a sync

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSyncTransactionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    page=1,
    page_size=100,
    sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002',
)

res = s.transaction_status.list_sync_transactions(req)

if res.transaction_metadata_list is not None:
    # handle response
```
