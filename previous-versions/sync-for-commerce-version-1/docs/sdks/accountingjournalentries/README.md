# AccountingJournalEntries

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
from decimal import Decimal

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateAccountingJournalEntryRequest(
    accounting_journal_entry=shared.AccountingJournalEntry(
        created_on='2022-10-23T00:00:00.000Z',
        description='nam',
        id='5a341814-3010-4421-813d-5208ece7e253',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='b668451c-6c6e-4205-a16d-eab3fec9578a',
                    name='Marjorie Hickle',
                ),
                currency='aspernatur',
                description='ducimus',
                net_amount=Decimal('2005.16'),
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='8418d162-309f-4b09-a992-1aefb9f58c4d',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.AccountingJournalEntryJournalReference(
            id='86e68e4b-e056-4013-b59d-a757a59ecfef',
            name='Loretta Tremblay DDS',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.AccountingJournalEntryRecordReference(
            data_type='journalEntry',
            id='383c2beb-4773-473c-8d72-f64d1db1f2c4',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "illo": {
                    "accusantium": 'vel',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=107617,
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

