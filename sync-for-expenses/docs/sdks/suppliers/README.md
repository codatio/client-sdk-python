# Suppliers

## Overview

Get, create, and update suppliers.

### Available Operations

* [create](#create) - Create supplier
* [get](#get) - Get supplier
* [list](#list) - List suppliers
* [update](#update) - Update supplier

## create

The *Create supplier* endpoint creates a new [supplier](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-suppliers-model).

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| Dynamics 365 Business Central | Yes       |
| FreeAgent                     | Yes       |
| Oracle NetSuite               | Yes       |
| QuickBooks Desktop            | Yes       |
| QuickBooks Online             | Yes       |
| Sage Intacct                  | Yes       |
| Xero                          | Yes       |
| Zoho Books                    | Yes       |


### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-supplier" method="post" path="/companies/{companyId}/connections/{connectionId}/push/suppliers" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.create(request={
        "supplier": {
            "addresses": [
                {
                    "city": "Bakersfield",
                    "country": "USA",
                    "line1": "Unit 51",
                    "line2": "Bakersfield Industrial Estate",
                    "region": "California",
                    "type": shared.AccountingAddressType.BILLING,
                },
            ],
            "contact_name": "Kelly's Industrial Supplies",
            "default_currency": "string",
            "email_address": "sales@kellysupplies.com",
            "id": "C520FFD4-F6F6-4FC2-A6D2-5D7088B2B14F",
            "metadata": {
                "is_deleted": True,
            },
            "modified_date": "2022-10-23T00:00:00Z",
            "phone": "07999 999999",
            "registration_number": "string",
            "source_modified_date": "2022-10-23T00:00:00Z",
            "status": shared.SupplierStatus.UNKNOWN,
            "supplemental_data": {
                "content": {
                    "property1": {
                        "property1": "<value>",
                        "property2": "<value>",
                    },
                    "property2": {
                        "property1": "<value>",
                        "property2": "<value>",
                    },
                },
            },
            "supplier_name": "Kelly's Industrial Supplies",
            "tax_number": "string",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="create-supplier" method="post" path="/companies/{companyId}/connections/{connectionId}/push/suppliers" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.create(request={
        "supplier": {
            "contact_name": "Joe Bloggs",
            "id": "73593",
            "status": shared.SupplierStatus.ACTIVE,
            "supplier_name": "test 20230420 1004",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSupplierRequest](../../models/operations/createsupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.CreateSupplierResponse](../../models/shared/createsupplierresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get

The *Get supplier* endpoint returns a single supplier for a given supplierId.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-all-data-types).

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| Dynamics 365 Business Central | Yes       |
| FreeAgent                     | Yes       |
| Oracle NetSuite               | Yes       |
| QuickBooks Desktop            | Yes       |
| QuickBooks Online             | Yes       |
| Sage Intacct                  | Yes       |
| Xero                          | Yes       |
| Zoho Books                    | Yes       |


### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Clear Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Dynamics 365 Business Central" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Exact (Netherlands)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Exact (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="FreeAgent" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="FreshBooks" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="KashFlow" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Oracle NetSuite" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="QuickBooks Desktop" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="QuickBooks Online" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="QuickBooks Online Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Sage 200cloud" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Sage 50 (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Sage Business Cloud Accounting" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Wave

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Wave" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Xero" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-supplier" method="get" path="/companies/{companyId}/data/suppliers/{supplierId}" example="Zoho Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSupplierRequest](../../models/operations/getsupplierrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[shared.Supplier](../../models/shared/supplier.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List suppliers* endpoint returns a list of [suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-all-data-types).

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| Dynamics 365 Business Central | Yes       |
| FreeAgent                     | Yes       |
| Oracle NetSuite               | Yes       |
| QuickBooks Desktop            | Yes       |
| QuickBooks Online             | Yes       |
| Sage Intacct                  | Yes       |
| Xero                          | Yes       |
| Zoho Books                    | Yes       |


### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Clear Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Dynamics 365 Business Central" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Exact (Netherlands)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Exact (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="FreeAgent" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="FreshBooks" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="KashFlow" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Oracle NetSuite" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="QuickBooks Desktop" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="QuickBooks Online" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="QuickBooks Online Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Sage 200cloud" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Sage 50 (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Sage Business Cloud Accounting" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Wave

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Wave" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Xero" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/data/suppliers" example="Zoho Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSuppliersRequest](../../models/operations/listsuppliersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.Suppliers](../../models/shared/suppliers.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## update

The *Update supplier* endpoint updates an existing [supplier](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-suppliers-model).

### Supported Integrations

| Integration       | Supported |
|-------------------|-----------|
| FreeAgent         | Yes       |
| QuickBooks Online | Yes       |
| Xero              | Yes       |


### Example Usage

<!-- UsageSnippet language="python" operationID="update-supplier" method="put" path="/companies/{companyId}/connections/{connectionId}/push/suppliers/{supplierId}" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.suppliers.update(request={
        "supplier": {
            "addresses": [
                {
                    "city": "Bakersfield",
                    "country": "USA",
                    "line1": "Unit 51",
                    "line2": "Bakersfield Industrial Estate",
                    "region": "California",
                    "type": shared.AccountingAddressType.BILLING,
                },
            ],
            "contact_name": "Kelly's Industrial Supplies",
            "default_currency": "string",
            "email_address": "sales@kellysupplies.com",
            "id": "C520FFD4-F6F6-4FC2-A6D2-5D7088B2B14F",
            "metadata": {
                "is_deleted": True,
            },
            "modified_date": "2022-10-23T00:00:00Z",
            "phone": "07999 999999",
            "registration_number": "string",
            "source_modified_date": "2022-10-23T00:00:00Z",
            "status": shared.SupplierStatus.UNKNOWN,
            "supplemental_data": {
                "content": {
                    "property1": {
                        "property1": "<value>",
                        "property2": "<value>",
                    },
                    "property2": {
                        "property1": "<value>",
                        "property2": "<value>",
                    },
                },
            },
            "supplier_name": "Kelly's Industrial Supplies",
            "tax_number": "string",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSupplierRequest](../../models/operations/updatesupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.UpdateSupplierResponse](../../models/shared/updatesupplierresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |