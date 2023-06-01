# journal_entries

## Overview

Journal entries

### Available Operations

* [create](#create) - Create journal entry
* [delete](#delete) - Delete journal entry
* [get](#get) - Get journal entry
* [get_create_model](#get_create_model) - Get create journal entry model
* [list](#list) - List journal entries

## create

Posts a new journalEntry to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateJournalEntryRequest(
    journal_entry=shared.JournalEntry(
        created_on='quas',
        description='soluta',
        id='d380c29a-a8dd-471b-9daa-30b7b91449ae',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='9c088d41-8bb7-4180-8f42-3d543935f377',
                    name='Devin Hintz',
                ),
                currency='nam',
                description='ducimus',
                net_amount=8873.03,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='velit',
                            id='b6a3c523-105e-47c3-8cab-0ecb812a6614',
                        ),
                        shared.InvoiceTo(
                            data_type='atque',
                            id='944a8e90-8507-45bc-a538-253343fb0a4e',
                        ),
                        shared.InvoiceTo(
                            data_type='autem',
                            id='6ea47578-d171-4e29-8181-8fc679b6b2f2',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='5359b855-d015-4b62-88b8-3a38a8a88c14',
                    name='Miss Andrea Bartell',
                ),
                currency='maxime',
                description='deserunt',
                net_amount=9204.81,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='et',
                            id='ae1ecf8c-3494-46bb-a7a0-5a8b4a9ec5b3',
                        ),
                        shared.InvoiceTo(
                            data_type='eum',
                            id='88cca363-2727-460e-966e-97e054103347',
                        ),
                        shared.InvoiceTo(
                            data_type='pariatur',
                            id='78ff2491-145f-4ab9-a59a-4af336664eaa',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='6bf2ff14-e8c1-4b35-aacc-edacc5227814',
            name='Mr. Sherman Pfannerstill',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='cum',
        posted_on='quo',
        record_ref=shared.InvoiceTo(
            data_type='aliquam',
            id='1ea1342d-4104-4a25-af71-de57a11d614a',
        ),
        source_modified_date='tempora',
        supplemental_data=shared.SupplementalData(
            content={
                "dicta": {
                    "laboriosam": 'sint',
                    "dolores": 'repudiandae',
                },
            },
        ),
        updated_on='fuga',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=284514,
)

res = s.journal_entries.create(req)

if res.create_journal_entry_response is not None:
    # handle response
```

## delete

﻿> **Use with caution**
>
>Because Journal Entries underpin every transaction in an accounting platform, deleting a Journal Entry can affect every transaction for a given company.
> 
> **Before you proceed, make sure you understand the implications of deleting Journal Entries from an accounting perspective.**

The _Delete Journal entries_ endpoint allows you to delete a specified Journal entry from an accounting platform.

### Process
1. Pass the `{journalEntryId}` to the _Delete Journal Entries_ endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete by checking the status of push operation either via
   1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
   2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation). 
   
   A `Success` status indicates that the Journal Entry object was deleted from the accounting platform.
3. (Optional) Check that the Journal Entry was deleted from the accounting platform.

### Effect on related objects

Be aware that deleting a Journal Entry from an accounting platform might cause related objects to be modified. For example, if you delete the Journal Entry for a paid invoice in QuickBooks Online, the invoice is deleted but the payment against that invoice is not. The payment is converted to a payment on account.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Deleted | 
|-------------|--------------|
| QuickBooks Online | Yes    |       

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteJournalEntryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    journal_entry_id='totam',
)

res = s.journal_entries.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## get

Gets a single JournalEntry corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetJournalEntryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    journal_entry_id='laboriosam',
)

res = s.journal_entries.get(req)

if res.journal_entry is not None:
    # handle response
```

## get_create_model

﻿Get create journal entry model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateJournalEntriesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.journal_entries.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets the latest journal entries for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListJournalEntriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='esse',
)

res = s.journal_entries.list(req)

if res.journal_entries is not None:
    # handle response
```
