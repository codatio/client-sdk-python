# Suppliers
(*suppliers*)

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

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-suppliers-model).


### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:
    res = codat_sync_expenses.suppliers.create(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "supplier": {
            "status": shared.SupplierStatus.ACTIVE,
            "contact_name": "Joe Bloggs",
            "id": "73593",
            "supplier_name": "test 20230420 1004",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSupplierRequest](../../models/operations/createsupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.CreateSupplierResponse](../../models/shared/createsupplierresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get

The *Get supplier* endpoint returns a single supplier for a given supplierId.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).


### Example Usage

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
        "supplier_id": "7110701885",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSupplierRequest](../../models/operations/getsupplierrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[shared.Supplier](../../models/shared/supplier.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## list

The *List suppliers* endpoint returns a list of [suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).
    

### Example Usage

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
        "page": 1,
        "page_size": 100,
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSuppliersRequest](../../models/operations/listsuppliersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.Suppliers](../../models/shared/suppliers.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 409, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |

## update

The *Update supplier* endpoint updates an existing [supplier](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/sync-for-expenses-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-suppliers-model).

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:
    res = codat_sync_expenses.suppliers.update(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "supplier_id": "EILBDVJVNUAGVKRQ",
        "supplier": {
            "status": shared.SupplierStatus.UNKNOWN,
            "addresses": [
                {
                    "type": shared.AccountingAddressType.BILLING,
                    "city": "Bakersfield",
                    "country": "USA",
                    "line1": "Unit 51",
                    "line2": "Bakersfield Industrial Estate",
                    "region": "California",
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
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSupplierRequest](../../models/operations/updatesupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.UpdateSupplierResponse](../../models/shared/updatesupplierresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |