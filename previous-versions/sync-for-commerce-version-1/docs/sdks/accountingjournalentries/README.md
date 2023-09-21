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
        description='pariatur',
        id='e008e6f8-c5f3-450d-8cdb-5a3418143010',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='421813d5-208e-4ce7-a253-b668451c6c6e',
                    name='Helen Heller III',
                ),
                currency='at',
                description='vero',
                net_amount=Decimal('6675.93'),
                tracking=shared.JournalLineTracking(
                    record_refs=[
                        shared.RecordRef(
                            data_type='accountTransaction',
                            id='3fec9578-a645-4842-b3a8-418d162309fb',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.AccountingJournalEntryJournalReference(
            id='0929921a-efb9-4f58-84d8-6e68e4be0560',
            name='Sheila Wolff',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        posted_on='2022-10-23T00:00:00.000Z',
        record_ref=shared.AccountingJournalEntryRecordReference(
            data_type='invoice',
            id='57a59ecf-ef66-4ef1-8aa3-383c2beb4773',
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        supplemental_data=shared.SupplementalData(
            content={
                "neque": {
                    "quo": 'deleniti',
                },
            },
        ),
        updated_on='2022-10-23T00:00:00.000Z',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=437814,
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

