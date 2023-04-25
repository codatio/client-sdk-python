# journals

## Overview

Journals

### Available Operations

* [get_create_journals_model](#get_create_journals_model) - Get create journal model
* [get_journal](#get_journal) - Get journal
* [list_journals](#list_journals) - List journals
* [push_journal](#push_journal) - Create journal

## get_create_journals_model

Get create journal model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journals) for integrations that support creating journals.

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.journals.get_create_journals_model(req)

if res.push_option is not None:
    # handle response
```

## get_journal

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    journal_id="quibusdam",
)

res = s.journals.get_journal(req)

if res.journal is not None:
    # handle response
```

## list_journals

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="ab",
)

res = s.journals.list_journals(req)

if res.journals is not None:
    # handle response
```

## push_journal

Posts a new journal to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal model](https://docs.codat.io/accounting-api#/operations/get-create-journals-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journals) for integrations that support creating journals.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.PushJournalRequest(
    journal=shared.Journal(
        created_on="eligendi",
        has_children=False,
        id="ea673d86-e3b3-45e4-9a31-35778ce54cac",
        journal_code="libero",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="perferendis",
        name="Chris Terry",
        parent_id="ducimus",
        source_modified_date="minima",
        status="Unknown",
        type="labore",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=359649,
)

res = s.journals.push_journal(req)

if res.push_journal_200_application_json_object is not None:
    # handle response
```
