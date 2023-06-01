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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateJournalRequest(
    journal=shared.Journal(
        created_on='nostrum',
        has_children=False,
        id='040d6c8b-2a5f-4002-a07e-4048f90009ed',
        journal_code='consequuntur',
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='occaecati',
        name='Phyllis Koch',
        parent_id='quidem',
        source_modified_date='aliquam',
        status=shared.JournalStatus.ARCHIVED,
        type='itaque',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=612118,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetJournalRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    journal_id='pariatur',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListJournalsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='suscipit',
)

res = s.journals.list(req)

if res.journals is not None:
    # handle response
```
