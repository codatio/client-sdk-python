# journal_entries

## Overview

Journal entries

### Available Operations

* [create](#create) - Create journal entry
* [get](#get) - Get journal entry
* [get_create_model](#get_create_model) - Get create journal entry model
* [list](#list) - List journal entries

## create

The *Create journal entry* endpoint creates a new [journal entry](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/sync-for-payroll-api#/operations/get-create-journalEntries-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating a journal entry.


### Example Usage

```python
import codatsyncpayroll
from codatsyncpayroll.models import operations, shared

s = codatsyncpayroll.CodatSyncPayroll(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateJournalEntryRequest(
    journal_entry=shared.JournalEntry(
        created_on='2022-10-23T00:00:00.000Z',
        description='molestiae',
        id='cc78ca1b-a928-4fc8-9674-2cb739205929',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='96fea759-6eb1-40fa-aa23-52c5955907af',
                    name='Juan O'Hara',
                ),
                currency='consequuntur',
                description='repellat',
                net_amount=6531.08,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='invoice',
                            id='67739251-aa52-4c3f-9ad0-19da1ffe78f0',
                        ),
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='7b0074f1-5471-4b5e-ae13-b99d488e1e91',
                        ),
                        shared.RecordRef(
                            data_type='transfer',
                            id='450ad2ab-d442-4698-82d5-02a94bb4f63c',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='969e9a3e-fa77-4dfb-94cd-66ae395efb9b',
            name='Nelson Lesch',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.JournalEntryRecordReference(
            data_type='invoice',
            id='997074ba-4469-4b6e-a141-959890afa563',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.JournalEntrySupplementalData(
            content={
                "nemo": {
                    "iure": 'doloribus',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=260341,
)

res = s.journal_entries.create(req)

if res.create_journal_entry_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateJournalEntryRequest](../../models/operations/createjournalentryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.CreateJournalEntryResponse](../../models/operations/createjournalentryresponse.md)**


## get

The *Get journal entry* endpoint returns a single journal entry for a given `journalEntryId`.

[Journal entries](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support getting a specific journal entry.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payroll-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsyncpayroll
from codatsyncpayroll.models import operations, shared

s = codatsyncpayroll.CodatSyncPayroll(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetJournalEntryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    journal_entry_id='maxime',
)

res = s.journal_entries.get(req)

if res.journal_entry is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetJournalEntryRequest](../../models/operations/getjournalentryrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.GetJournalEntryResponse](../../models/operations/getjournalentryresponse.md)**


## get_create_model

﻿The *Get create journal entry model* endpoint returns the expected data for the request payload when creating a [journal entry](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) for a given company and integration.

[Journal entries](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating a journal entry.


### Example Usage

```python
import codatsyncpayroll
from codatsyncpayroll.models import operations, shared

s = codatsyncpayroll.CodatSyncPayroll(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateJournalEntryModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.journal_entries.get_create_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCreateJournalEntryModelRequest](../../models/operations/getcreatejournalentrymodelrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.GetCreateJournalEntryModelResponse](../../models/operations/getcreatejournalentrymodelresponse.md)**


## list

The *List journal entries* endpoint returns a list of [journal entries](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/sync-for-payroll-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payroll-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsyncpayroll
from codatsyncpayroll.models import operations, shared

s = codatsyncpayroll.CodatSyncPayroll(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListJournalEntriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='deleniti',
)

res = s.journal_entries.list(req)

if res.journal_entries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListJournalEntriesRequest](../../models/operations/listjournalentriesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListJournalEntriesResponse](../../models/operations/listjournalentriesresponse.md)**

