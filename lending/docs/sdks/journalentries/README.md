# JournalEntries
(*transactions.journal_entries*)

## Overview

### Available Operations

* [get](#get) - Get journal entry
* [list](#list) - List journal entries

## get

The *Get journal entry* endpoint returns a single journal entry for a given journalEntryId.

[Journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "7110701885",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingJournalEntryRequest](../../models/operations/getaccountingjournalentryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.AccountingJournalEntry](../../models/shared/accountingjournalentry.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## list

The *List journal entries* endpoint returns a list of [journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "page": 1,
        "page_size": 100,
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingJournalEntriesRequest](../../models/operations/listaccountingjournalentriesrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[shared.AccountingJournalEntries](../../models/shared/accountingjournalentries.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 409, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |