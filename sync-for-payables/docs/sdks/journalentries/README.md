# journal_entries

## Overview

Journal entries

### Available Operations

* [create](#create) - Create journal entry
* [get_create_model](#get_create_model) - Get create journal entry model

## create

The *Create journal entry* endpoint creates a new [journal entry](https://docs.codat.io/sync-for-payables-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/sync-for-payables-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-journalEntries-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating a journal entry.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateJournalEntryRequest(
    journal_entry=shared.JournalEntry(
        created_on='2022-10-23T00:00:00.000Z',
        description='nam',
        id='dc41ff5d-4e2a-4e4f-b5cb-35d17638f1ed',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='78359ecc-5cb8-460f-8cd5-80ba73810e4f',
                    name='Don Hagenes',
                ),
                currency='magni',
                description='excepturi',
                net_amount=4576.85,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='transfer',
                            id='3b1dd3bb-ce24-47b7-a84e-ff50126d71cf',
                        ),
                        shared.RecordRef(
                            data_type='transfer',
                            id='bd0eb74b-8421-4953-b44b-d3c43159d33e',
                        ),
                        shared.RecordRef(
                            data_type='invoice',
                            id='953c0011-3986-43aa-81e6-c31cc2f1fcb5',
                        ),
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='c9a41ffb-e9cb-4d79-9ee6-5e076cc7abf6',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='16ea5c71-6419-434b-90f2-e09d19d2fc2f',
                    name='Merle Cormier Jr.',
                ),
                currency='nemo',
                description='provident',
                net_amount=2529.57,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='935d237a-72f9-4084-9d6a-ed4aecb7537c',
                        ),
                        shared.RecordRef(
                            data_type='transfer',
                            id='9222c9ff-5749-41aa-bfa2-e761f0ca4d45',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='6ef1031e-6899-4f0c-a001-e22cd55cc058',
                    name='Hattie Botsford',
                ),
                currency='possimus',
                description='nihil',
                net_amount=3758.77,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='71fc820c-65b0-437b-b8e0-cc885187e4de',
                        ),
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='4af28c5d-ddb4-46aa-9cfd-6d828da01319',
                        ),
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='12964664-5c1d-481f-a904-2f569b7aff0e',
                        ),
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='2216cbe0-71bc-4163-a279-a3b084da9925',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='7d04f408-47a7-442d-8449-6cbdeecf6b99',
            name='Wilbert Jerde',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.JournalEntryRecordReference(
            data_type='transfer',
            id='bfdf55c2-94c0-460b-86a1-287764eef6d0',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "temporibus": {
                    "itaque": 'nulla',
                    "excepturi": 'quod',
                },
                "in": {
                    "temporibus": 'temporibus',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=247927,
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


## get_create_model

﻿The *Get create journal entry model* endpoint returns the expected data for the request payload when creating a [journal entry](https://docs.codat.io/sync-for-payables-api#/schemas/JournalEntry) for a given company and integration.

[Journal entries](https://docs.codat.io/sync-for-payables-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating a journal entry.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
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

