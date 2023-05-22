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

﻿Posts a new journalEntry to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.
 

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateJournalEntryRequest(
    journal_entry=shared.JournalEntry(
        created_on='quibusdam',
        description='natus',
        id='8ccf89d3-8611-486e-976c-002facb13ac2',
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='c8143b86-6c57-45a1-a266-8730be37b0e8',
                    name='Alton Schmitt',
                ),
                currency='facere',
                description='temporibus',
                net_amount=7790.58,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='officiis',
                            id='69b53510-5050-414d-8a10-5882484c36e9',
                        ),
                        shared.InvoiceTo(
                            data_type='ut',
                            id='8892782d-34e0-4b8f-80d5-9f57b9f9820b',
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id='e07808c3-6c9e-42f7-8344-e00f478eb539',
                    name='Maxine Dietrich',
                ),
                currency='dolore',
                description='blanditiis',
                net_amount=9119.94,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='delectus',
                            id='ccb69d54-1b4b-4393-b356-6625bea32201',
                        ),
                        shared.InvoiceTo(
                            data_type='temporibus',
                            id='ec379c59-8ea1-4d48-85c2-f9e21d90fd53',
                        ),
                        shared.InvoiceTo(
                            data_type='esse',
                            id='76bfc767-7f0f-4504-a6e4-828fb6daee19',
                        ),
                        shared.InvoiceTo(
                            data_type='cumque',
                            id='26c0cb61-8c63-431c-abda-b767a444dd0d',
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id='a0abe58e-b3d5-44ba-9cb3-ad49b8e5c18b',
            name='Holly Trantow',
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='maiores',
        posted_on='ea',
        record_ref=shared.InvoiceTo(
            data_type='incidunt',
            id='823255be-95c0-4cbc-b2ca-87908d73809a',
        ),
        source_modified_date='aut',
        supplemental_data=shared.SupplementalData(
            content={
                "doloribus": {
                    "eum": 'itaque',
                },
            },
        ),
        updated_on='unde',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=148478,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteJournalEntryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    journal_entry_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetJournalEntryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    journal_entry_id='qui',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListJournalEntriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='totam',
)

res = s.journal_entries.list(req)

if res.journal_entries is not None:
    # handle response
```
