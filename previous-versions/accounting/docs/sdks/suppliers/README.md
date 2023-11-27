# Suppliers
(*suppliers*)

## Overview

Suppliers

### Available Operations

* [create](#create) - Create supplier
* [download_attachment](#download_attachment) - Download supplier attachment
* [get](#get) - Get supplier
* [get_attachment](#get_attachment) - Get supplier attachment
* [get_create_update_model](#get_create_update_model) - Get create/update supplier model
* [list](#list) - List suppliers
* [list_attachments](#list_attachments) - List supplier attachments
* [update](#update) - Update supplier

## create

The *Create supplier* endpoint creates a new [supplier](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Items(
                type=shared.AccountingAddressType.BILLING,
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(877) 492-8687',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.suppliers.create(req)

if res.create_supplier_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSupplierRequest](../../models/operations/createsupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.CreateSupplierResponse](../../models/operations/createsupplierresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

## download_attachment

The *Download supplier attachment* endpoint downloads a specific attachment for a given `supplierId` and `attachmentId`.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support downloading a supplier attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='string',
)

res = s.suppliers.download_attachment(req)

if res.data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DownloadSupplierAttachmentRequest](../../models/operations/downloadsupplierattachmentrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[operations.DownloadSupplierAttachmentResponse](../../models/operations/downloadsupplierattachmentresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## get

The *Get supplier* endpoint returns a single supplier for a given supplierId.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support getting a specific supplier.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSupplierRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    supplier_id='string',
)

res = s.suppliers.get(req)

if res.supplier is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSupplierRequest](../../models/operations/getsupplierrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.GetSupplierResponse](../../models/operations/getsupplierresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

## get_attachment

The *Get supplier attachment* endpoint returns a specific attachment for a given `supplierId` and `attachmentId`.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support getting a supplier attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSupplierAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='string',
)

res = s.suppliers.get_attachment(req)

if res.attachment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetSupplierAttachmentRequest](../../models/operations/getsupplierattachmentrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.GetSupplierAttachmentResponse](../../models/operations/getsupplierattachmentresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## get_create_update_model

The *Get create/update supplier model* endpoint returns the expected data for the request payload when creating and updating a [supplier](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company and integration.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating a supplier.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateSuppliersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.suppliers.get_create_update_model(req)

if res.push_option is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetCreateUpdateSuppliersModelRequest](../../models/operations/getcreateupdatesuppliersmodelrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.GetCreateUpdateSuppliersModelResponse](../../models/operations/getcreateupdatesuppliersmodelresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 400-600                     | */*                         |

## list

The *List suppliers* endpoint returns a list of [suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSuppliersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
)

res = s.suppliers.list(req)

if res.suppliers is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSuppliersRequest](../../models/operations/listsuppliersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListSuppliersResponse](../../models/operations/listsuppliersresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 400-600                             | */*                                 |

## list_attachments

The *List supplier attachments* endpoint returns a list of attachments available to download for given `supplierId`.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support listing supplier attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListSupplierAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='string',
)

res = s.suppliers.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListSupplierAttachmentsRequest](../../models/operations/listsupplierattachmentsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.ListSupplierAttachmentsResponse](../../models/operations/listsupplierattachmentsresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

## update

The *Update supplier* endpoint updates an existing [supplier](https://docs.codat.io/accounting-api#/schemas/Supplier) for a given company's connection.

[Suppliers](https://docs.codat.io/accounting-api#/schemas/Supplier) are people or organizations that provide something, such as a product or service.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Items(
                type=shared.AccountingAddressType.DELIVERY,
            ),
        ],
        metadata=shared.Metadata(),
        modified_date='2022-10-23T00:00:00.000Z',
        phone='(877) 492-8687',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.SupplierStatus.ACTIVE,
        supplemental_data=shared.SupplementalData(
            content={
                "key": {
                    "key": 'string',
                },
            },
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    supplier_id='string',
)

res = s.suppliers.update(req)

if res.update_supplier_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateSupplierRequest](../../models/operations/updatesupplierrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.UpdateSupplierResponse](../../models/operations/updatesupplierresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
