# Transactions.JournalEntries

## Overview

### Available Operations

* [get](#get) - Get journal entry
* [list](#list) - List journal entries

## get

The *Get journal entry* endpoint returns a single journal entry for a given journalEntryId.

[Journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-journal-entry" method="get" path="/companies/{companyId}/data/journalEntries/{journalEntryId}" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "journal_entry_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAccountingJournalEntryRequest](../../models/operations/getaccountingjournalentryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.AccountingJournalEntry](../../models/shared/accountingjournalentry.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List journal entries* endpoint returns a list of [journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) for a given company's connection.

[Journal entries](https://docs.codat.io/lending-api#/schemas/JournalEntry) are  made in a company's general ledger, or accounts, when transactions are approved.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="list-accounting-journal-entries" method="get" path="/companies/{companyId}/data/journalEntries" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.transactions.journal_entries.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListAccountingJournalEntriesRequest](../../models/operations/listaccountingjournalentriesrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[shared.AccountingJournalEntries](../../models/shared/accountingjournalentries.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |