# ManagedBankFeeds

## Overview

Manage bank feed syncs for source accounts.

### Available Operations

* [get_latest_sync](#get_latest_sync) - Get latest sync
* [get_sync](#get_sync) - Get sync
* [run_ad_hoc_sync](#run_ad_hoc_sync) - Run ad-hoc sync

## get_latest_sync

The _Get latest sync_ endpoint returns the status for a given source account's [most recent sync](https://docs.codat.io/bank-feeds-api#/schemas/SyncStatusResult). 

A sync is a single execution that fetches bank transactions from a connected bank account and records them in the company's accounting software.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-latest-managed-bank-feed-sync" method="get" path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/{sourceAccountId}/managedBankFeeds/syncs/latest" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.managed_bank_feeds.get_latest_sync(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "source_account_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetLatestManagedBankFeedSyncRequest](../../models/operations/getlatestmanagedbankfeedsyncrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[shared.SyncStatusResult](../../models/shared/syncstatusresult.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_sync

The _Get sync_ endpoint returns the [sync status](https://docs.codat.io/bank-feeds-api#/schemas/SyncStatusResult) for a given 'syncId'. 

A sync is a single execution that fetches bank transactions from a connected bank account and records them in the company's accounting software.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-managed-bank-feed-sync" method="get" path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/{sourceAccountId}/managedBankFeeds/syncs/{syncId}" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.managed_bank_feeds.get_sync(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "source_account_id": "<id>",
        "sync_id": "823d304f-a204-4760-9b5d-b8a89bf29bed",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetManagedBankFeedSyncRequest](../../models/operations/getmanagedbankfeedsyncrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.SyncStatusResult](../../models/shared/syncstatusresult.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## run_ad_hoc_sync

The _Run ad-hoc sync_ endpoint immediately runs a sync with a fetch period from the last successful sync to the execution time of the new sync.

A sync is a single execution that fetches bank transactions from a connected bank account and records them in the company's accounting software.

Use either the [_Get latest sync_](https://docs.codat.io/bank-feeds-api#/operations/get-latest-managed-bank-feed-sync) endpoint or the [_Get sync_](https://docs.codat.io/bank-feeds-api#/operations/fetch-managed-bank-feed-sync-by-id) endpoint to get the result of this sync.

### Example Usage

<!-- UsageSnippet language="python" operationID="run-managed-bank-feed-ad-hoc-sync" method="post" path="/companies/{companyId}/connections/{connectionId}/bankFeedAccounts/{sourceAccountId}/managedBankFeeds/syncs" -->
```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.managed_bank_feeds.run_ad_hoc_sync(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "source_account_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RunManagedBankFeedAdHocSyncRequest](../../models/operations/runmanagedbankfeedadhocsyncrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[shared.StartScheduledSyncResult](../../models/shared/startscheduledsyncresult.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |