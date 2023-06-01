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
        created_on='corporis',
        description='omnis',
        id='b855d015-b62c-48b8-ba38-a8a88c144200',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='2caeb1ae-1ecf-48c3-8946-bba7a05a8b4a',
                    name='Noah Rutherford',
                ),
                currency='amet',
                description='eum',
                net_amount=5102.81,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='maxime',
                            id='ca363272-760e-4966-a97e-054103347d78',
                        ),
                        shared.InvoiceTo(
                            data_type='asperiores',
                            id='f2491145-fab9-4e59-a4af-336664eaa6bf',
                        ),
                        shared.InvoiceTo(
                            data_type='dolores',
                            id='ff14e8c1-b352-4acc-adac-c5227814eca0',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='16bc41ea-1342-4d41-84a2-5ef71de57a11',
                    name='Franklin Brown',
                ),
                currency='tempora',
                description='velit',
                net_amount=1191.73,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='laboriosam',
                            id='92ea4867-3d52-42b8-a8a9-030660f024c7',
                        ),
                        shared.InvoiceTo(
                            data_type='sint',
                            id='b4cc64c2-b3a3-42c4-88ad-e62f6aa558a6',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='5e208301-6ca3-44bb-87d4-f62127a607d1',
                    name='Betty Jacobi',
                ),
                currency='quaerat',
                description='nostrum',
                net_amount=1080.29,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='cumque',
                            id='3db9ca9f-38bd-42be-8787-03493f49aa84',
                        ),
                        shared.InvoiceTo(
                            data_type='ex',
                            id='5a328327-9b71-49d1-8ea6-73d86e3b35e4',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='9a313577-8ce5-44ca-8b0e-3ea975045bac',
                    name='Nathaniel DuBuque',
                ),
                currency='quasi',
                description='nemo',
                net_amount=1217.04,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='commodi',
                            id='ab5e3a02-2614-4315-9156-8299e61afc71',
                        ),
                        shared.InvoiceTo(
                            data_type='totam',
                            id='6ff20b7a-73df-440c-a0d7-657c1641bbf0',
                        ),
                        shared.InvoiceTo(
                            data_type='nostrum',
                            id='5271b251-1dd6-406d-91b2-8272bc9c3221',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='697b1880-fcbb-42b9-bc15-f670bd178483',
            name='Kristin Herman',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='necessitatibus',
        posted_on='harum',
        record_ref=shared.InvoiceTo(
            data_type='amet',
            id='b6e241c3-1099-4836-a3c6-6dcbb7df6cb0',
        ),
        source_modified_date='molestias',
        supplemental_data=shared.SupplementalData(
            content={
                "totam": {
                    "modi": 'aperiam',
                    "praesentium": 'recusandae',
                    "eaque": 'nihil',
                },
                "dicta": {
                    "molestiae": 'in',
                },
                "magnam": {
                    "saepe": 'non',
                    "a": 'voluptates',
                    "vero": 'quae',
                    "doloremque": 'et',
                },
                "possimus": {
                    "esse": 'praesentium',
                    "aperiam": 'laborum',
                    "dicta": 'doloremque',
                },
            },
        ),
        updated_on='minus',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=260242,
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
    journal_entry_id='odio',
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
    journal_entry_id='rerum',
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
    query='provident',
)

res = s.journal_entries.list(req)

if res.journal_entries is not None:
    # handle response
```
