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
        description='culpa',
        id='bcdc91fa-abdd-488e-b1f6-c48252d7771e',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='fd074009-ef8d-429d-a1dd-7097b5da08c5',
                    name='Ora Olson',
                ),
                currency='odio',
                description='atque',
                net_amount=6288.11,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='6e19bafe-ca61-4914-9814-0b64ff8ae170',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='ef03b5f3-7e4a-4a86-8555-966732aa5dcb',
                    name='Ella Lang',
                ),
                currency='expedita',
                description='in',
                net_amount=526.59,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='cfd5fb6e-91b9-4a9f-b484-6e2c3309db05',
                        ),
                        shared.RecordRef(
                            data_type='journalEntry',
                            id='6d9e75ca-006f-4539-ac11-a25a8bf92f97',
                        ),
                        shared.RecordRef(
                            data_type='invoice',
                            id='28ad9a9f-8bf8-4221-9253-59d98387f7a7',
                        ),
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='cd72cd24-84da-4217-a9f2-ac41ef5725f1',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='169ac1e4-1d8a-423c-a3e3-4f2dfa4a197f',
            name='Betsy Walter',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.JournalEntryRecordReference(
            data_type='invoice',
            id='1fe17120-9985-43e9-b543-d854439ee224',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "accusantium": {
                    "aliquam": 'dolorem',
                    "expedita": 'impedit',
                },
                "architecto": {
                    "magnam": 'vitae',
                    "quos": 'atque',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=125488,
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

