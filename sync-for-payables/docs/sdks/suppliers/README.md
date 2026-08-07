# Suppliers

## Overview

Get, create, and update Suppliers.

### Available Operations

* [list](#list) - List suppliers
* [create](#create) - Create supplier
* [update](#update) - Update supplier

## list

The *List suppliers* endpoint returns a list of [suppliers](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

By default, this endpoint returns a list of active and archived suppliers. You can use [querying](https://docs.codat.io/using-the-api/querying) to change that. 

For example, to retrieve only active suppliers (i.e. `status=Active`) or suppliers created within the specified number of days (e.g. `sourceModifiedDate>2023-12-15T00:00:00.000Z`), query the endpoint as follows: `/payables/suppliers?query=sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=Active`.For example, to retrieve active suppliers modified after a particular date use `query=sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=Active`.

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| FreeAgent                     | Yes       |
| QuickBooks Online             | Yes       |
| Xero                          | Yes       |
| Oracle NetSuite               | Yes       |
| Sage Intacct                  | Yes       |
| Zoho Books                    | Yes       |

### Example Usage: Source modified date

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (active)

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Status (active)" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "status=Active",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (active) & source modified date

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Status (active) & source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=Active",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (archived)

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Status (archived)" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "status=Archived",
    })

    # Handle response
    print(res)

```
### Example Usage: Status (archived) & source modified date

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Status (archived) & source modified date" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
        "query": "sourceModifiedDate>2023-12-15T00:00:00.000Z&&status=Archived",
    })

    # Handle response
    print(res)

```
### Example Usage: Suppliers

<!-- UsageSnippet language="python" operationID="list-suppliers" method="get" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Suppliers" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "continuation_token": "continuationToken=eyJwYWdlIjoyLCJwYWdlU2l6ZSI6MTAwLCJwYWdlQ291bnQiOjExfQ==",
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

## create

The *Create supplier* endpoint creates a new [supplier](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| FreeAgent                     | Yes       |
| QuickBooks Online             | Yes       |
| Xero                          | Yes       |
| Oracle NetSuite               | Yes       |
| Sage Intacct                  | Yes       |
| Zoho Books                    | Yes       |


### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-supplier" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.create(request={
        "supplier_prototype": {
            "phone": "+44 25691 154789",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Suppliers

<!-- UsageSnippet language="python" operationID="create-supplier" method="post" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers" example="Suppliers" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.create(request={
        "supplier_prototype": {
            "addresses": [],
            "contact_name": "Sarah Johnson",
            "default_currency": "GBP",
            "email_address": "sarah.johnson@northridgesupplies.co.uk",
            "phone": "+44 (0)1223 322410",
            "status": shared.SupplierStatus.ACTIVE,
            "supplier_name": "Northridge Office Supplies",
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

**[shared.Supplier](../../models/shared/supplier.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update

The *Update supplier* endpoint updates an existing [supplier](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-payables-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

This is a full-replace PUT endpoint. Any fields not included in the request body will be cleared on the supplier record.

### Supported Integrations

| Integration                   | Supported |
|-------------------------------|-----------|
| FreeAgent                     | Yes       |
| QuickBooks Online             | Yes       |
| Xero                          | Yes       |
| Oracle NetSuite               | No        |
| Sage Intacct                  | No        |
| Zoho Books                    | No        |

### Platform-specific behavior

- **Xero**: Archived suppliers cannot be updated (returns `400`). Suppliers must be unarchived manually in the Xero UI before updating.
- **QuickBooks Online**: Currency can only be set when creating a supplier, and cannot be changed via update.


### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="update-supplier" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers/{supplierId}" example="Malformed query" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.update(request={
        "supplier_prototype": {
            "phone": "+44 25691 154789",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Update supplier

<!-- UsageSnippet language="python" operationID="update-supplier" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers/{supplierId}" example="Update supplier" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.update(request={
        "supplier_prototype": {
            "addresses": [],
            "contact_name": "Sarah Johnson",
            "default_currency": "GBP",
            "email_address": "sarah.johnson@northridgesupplies.co.uk",
            "phone": "+44 (0)1223 322410",
            "status": shared.SupplierStatus.ACTIVE,
            "supplier_name": "Northridge Office Supplies",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "supplier_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Updated supplier

<!-- UsageSnippet language="python" operationID="update-supplier" method="put" path="/companies/{companyId}/connections/{connectionId}/payables/suppliers/{supplierId}" example="Updated supplier" -->
```python
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared


with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:

    res = codat_sync_payables.suppliers.update(request={
        "supplier_prototype": {
            "phone": "+44 25691 154789",
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

**[shared.Supplier](../../models/shared/supplier.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |