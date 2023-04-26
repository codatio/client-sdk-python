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
        created_on="delectus",
        description="id",
        id="1011a091-b3ec-48b5-b862-de1a9d14fe72",
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="521f9030-3dfc-4338-b97f-ffa6d1d32090",
                    name="Salvatore Boyer",
                ),
                currency="mollitia",
                description="cumque",
                net_amount=5632.6,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="accusamus",
                            id="1961ce9b-e41c-4869-9d7d-9719d07b200a",
                        ),
                        shared.InvoiceTo(
                            data_type="corporis",
                            id="8ffd2967-df8f-4d88-aa8e-60be620cd9c5",
                        ),
                        shared.InvoiceTo(
                            data_type="officia",
                            id="fdd04c37-5251-42be-ae1d-87ecc5fdcea8",
                        ),
                        shared.InvoiceTo(
                            data_type="eveniet",
                            id="7a883116-62cd-4a6d-b7c1-d86066237d42",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="27866db8-a749-4e39-8451-1cc75e4f0c00",
                    name="Patty Harber",
                ),
                currency="molestiae",
                description="ipsam",
                net_amount=5541.62,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="nobis",
                            id="94562f00-6968-45fc-91a1-73d84bbe24f2",
                        ),
                        shared.InvoiceTo(
                            data_type="error",
                            id="834afb07-35cb-4628-9d4a-29aaa1e16915",
                        ),
                        shared.InvoiceTo(
                            data_type="nisi",
                            id="f7d2ee20-9505-4bf0-ba93-e94480ca37fb",
                        ),
                        shared.InvoiceTo(
                            data_type="ab",
                            id="0789032a-c333-4172-a2dd-79ec74ba7e88",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="ddb36fd1-ccc3-441c-8657-3474f0a740fb",
                    name="Sandy Reichel",
                ),
                currency="illo",
                description="impedit",
                net_amount=2164.48,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="doloremque",
                            id="9e763995-d808-4bbe-b944-55ebc550a1c4",
                        ),
                        shared.InvoiceTo(
                            data_type="qui",
                            id="6b59c836-6fdc-4c13-9582-c1b855e889d9",
                        ),
                        shared.InvoiceTo(
                            data_type="officiis",
                            id="f932e900-0a13-4ad8-9242-08efd2341189",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="8e73879e-fbe8-4bae-babb-794536e90351",
                    name="Rickey Miller",
                ),
                currency="adipisci",
                description="architecto",
                net_amount=4393.34,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="voluptatem",
                            id="b77a5a53-65a7-49f1-9271-f01c0d361fed",
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id="8dc5effb-453e-4908-9e87-1fdb4d697bdd",
            name="Sylvester Maggio",
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="repudiandae",
        posted_on="incidunt",
        record_ref=shared.InvoiceTo(
            data_type="neque",
            id="734a5d72-d9ed-4d78-9be5-e7afe55297ba",
        ),
        source_modified_date="laboriosam",
        supplemental_data=shared.SupplementalData(
            content={
                "laudantium": {
                    "repellat": "aliquam",
                },
            },
        ),
        updated_on="modi",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=907650,
)

res = s.journal_entries.create(req)

if res.create_journal_entry_response is not None:
    # handle response
```

## delete

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    journal_entry_id="dolorem",
)

res = s.journal_entries.get(req)

if res.journal_entry is not None:
    # handle response
```

## get_create_model

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

res = s.journal_entries.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

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
    query="laborum",
)

res = s.journal_entries.list(req)

if res.journal_entries is not None:
    # handle response
```
