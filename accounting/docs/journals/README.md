# journals

## Overview

Journals

### Available Operations

* [create](#create) - Create journal
* [get](#get) - Get journal
* [get_create_model](#get_create_model) - Get create journal model
* [list](#list) - List journals

## create

Posts a new journal to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal model](https://docs.codat.io/accounting-api#/operations/get-create-journals-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journals) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateJournalRequest(
    journal=shared.Journal(
        created_on='cum',
        has_children=False,
        id='56065a50-74be-4fb8-af68-49d2b9940436',
        journal_code='adipisci',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='mollitia',
        name='Faye Huels',
        parent_id='voluptatem',
        source_modified_date='ipsam',
        status=shared.JournalStatus.UNKNOWN,
        type='praesentium',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=452831,
)

res = s.journals.create(req)

if res.create_journal_response is not None:
    # handle response
```

## get

Gets a single journal corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetJournalRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    journal_id='ea',
)

res = s.journals.get(req)

if res.journal is not None:
    # handle response
```

## get_create_model

Get create journal model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journals) for integrations that support creating journals.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateJournalsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.journals.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the latest journals for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListJournalsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='eveniet',
)

res = s.journals.list(req)

if res.journals is not None:
    # handle response
```
