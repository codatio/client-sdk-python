# journal_entries

## Overview

Journal entries

### Available Operations

* [create_journal_entry](#create_journal_entry) - Create journal entry
* [delete_journal_entry](#delete_journal_entry) - Delete journal entry
* [get_create_journal_entries_model](#get_create_journal_entries_model) - Get create journal entry model
* [get_journal_entry](#get_journal_entry) - Get journal entry
* [list_journal_entries](#list_journal_entries) - List journal entries

## create_journal_entry

Posts a new journalEntry to the accounting package for a given company.

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
        created_on="tempora",
        description="nesciunt",
        id="fb0a4e66-ea47-4578-9171-e2941818fc67",
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="b6b2f253-59b8-455d-815b-62c8b83a38a8",
                    name="Dwayne MacGyver I",
                ),
                currency="labore",
                description="consequuntur",
                net_amount=317.03,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="optio",
                            id="2caeb1ae-1ecf-48c3-8946-bba7a05a8b4a",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="9ec5b368-8cca-4363-a727-60e966e97e05",
                    name="Teresa Anderson",
                ),
                currency="aliquam",
                description="esse",
                net_amount=8634.7,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="corrupti",
                            id="ff249114-5fab-49e5-9a4a-f336664eaa6b",
                        ),
                        shared.InvoiceTo(
                            data_type="sapiente",
                            id="2ff14e8c-1b35-42ac-8eda-cc5227814eca",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="016bc41e-a134-42d4-904a-25ef71de57a1",
                    name="Mrs. Janis Keeling",
                ),
                currency="tempora",
                description="velit",
                net_amount=1191.73,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="laboriosam",
                            id="92ea4867-3d52-42b8-a8a9-030660f024c7",
                        ),
                        shared.InvoiceTo(
                            data_type="sint",
                            id="b4cc64c2-b3a3-42c4-88ad-e62f6aa558a6",
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id="5e208301-6ca3-44bb-87d4-f62127a607d1",
            name="Betty Jacobi",
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="quaerat",
        posted_on="nostrum",
        record_ref=shared.InvoiceTo(
            data_type="beatae",
            id="4c3db9ca-9f38-4bd2-be87-8703493f49aa",
        ),
        source_modified_date="laudantium",
        supplemental_data=shared.SupplementalData(
            content={
                "ex": {
                    "mollitia": "sequi",
                    "eos": "laudantium",
                },
                "adipisci": {
                    "iusto": "natus",
                },
            },
        ),
        updated_on="facilis",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=465310,
)

res = s.journal_entries.create_journal_entry(req)

if res.create_journal_entry_response is not None:
    # handle response
```

## delete_journal_entry

Deletes a journal entry from the accounting package for a given company.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    journal_entry_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.journal_entries.delete_journal_entry(req)

if res.push_operation_summary is not None:
    # handle response
```

## get_create_journal_entries_model

Get create journal entry model. Returns the expected data for the request payload.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.journal_entries.get_create_journal_entries_model(req)

if res.push_option is not None:
    # handle response
```

## get_journal_entry

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    journal_entry_id="beatae",
)

res = s.journal_entries.get_journal_entry(req)

if res.journal_entry is not None:
    # handle response
```

## list_journal_entries

Gets the latest journal entries for a company, with pagination

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="error",
)

res = s.journal_entries.list_journal_entries(req)

if res.journal_entries is not None:
    # handle response
```
