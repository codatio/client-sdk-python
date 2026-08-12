# AccountsPayable.BillCreditNotes

## Overview

### Available Operations

* [get](#get) - Get bill credit note
* [list](#list) - List bill credit notes

## get

The *Get bill credit note* endpoint returns a single bill credit note for a given billCreditNoteId.

[Bill credit notes](https://docs.codat.io/lending-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-bill-credit-note" method="get" path="/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.get(request={
        "bill_credit_note_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAccountingBillCreditNoteRequest](../../models/operations/getaccountingbillcreditnoterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[shared.AccountingBillCreditNote](../../models/shared/accountingbillcreditnote.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List bill credit notes* endpoint returns a list of [bill credit notes](https://docs.codat.io/lending-api#/schemas/BillCreditNote) for a given company's connection.

[Bill credit notes](https://docs.codat.io/lending-api#/schemas/BillCreditNote) are issued by a supplier for the purpose of recording credit.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="list-accounting-bill-credit-notes" method="get" path="/companies/{companyId}/data/billCreditNotes" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_payable.bill_credit_notes.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.ListAccountingBillCreditNotesRequest](../../models/operations/listaccountingbillcreditnotesrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[shared.AccountingBillCreditNotes](../../models/shared/accountingbillcreditnotes.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |