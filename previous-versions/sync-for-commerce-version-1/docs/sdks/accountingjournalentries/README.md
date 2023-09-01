# accounting_journal_entries

## Overview

Journal entries

### Available Operations

* [create_accounting_journal_entry](#create_accounting_journal_entry) - Create journal entry

## create_accounting_journal_entry

The *Create journal entry* endpoint creates a new [journal entry](https://docs.codat.io/accounting-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/accounting-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating an account.


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingJournalEntryRequest(
    accounting_journal_entry=shared.AccountingJournalEntry(
        created_on='2022-10-23T00:00:00.000Z',
        description='excepturi',
        id='e81f30be-3e43-4202-9721-657650664187',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='d9d21f9a-d030-4c4e-8c11-a0836429068b',
                    name='Pedro Armstrong',
                ),
                currency='quaerat',
                description='corporis',
                net_amount=8843.25,
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='transfer',
                            id='73bc845e-320a-4319-b4ba-df947c9a867b',
                        ),
                        shared.RecordRef(
                            data_type='transfer',
                            id='42426665-816d-4dca-8ef5-1fcb4c593ec1',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.AccountingJournalEntryJournalReference(
            id='2cdaad0e-c7af-4edb-980d-f448a47f9390',
            name='Derek Lubowitz',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.AccountingJournalEntryRecordReference(
            data_type='accountTransaction',
            id='3dabf9ef-3ffd-4d9f-bf07-9af4d35724cd',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "reiciendis": {
                    "vero": 'eos',
                    "quas": 'quasi',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=509799,
)

res = s.accounting_journal_entries.create_accounting_journal_entry(req)

if res.accounting_create_journal_entry_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateAccountingJournalEntryRequest](../../models/operations/createaccountingjournalentryrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.CreateAccountingJournalEntryResponse](../../models/operations/createaccountingjournalentryresponse.md)**

