# PurchaseOrders
(*purchase_orders*)

## Overview

Access standardized Purchase orders from linked accounting software.

### Available Operations

* [create](#create) - Create purchase order
* [download_attachment](#download_attachment) - Download purchase order attachment
* [download_purchase_order_pdf](#download_purchase_order_pdf) - Download purchase order as PDF
* [get](#get) - Get purchase order
* [get_attachment](#get_attachment) - Get purchase order attachment
* [get_create_update_model](#get_create_update_model) - Get create/update purchase order model
* [list](#list) - List purchase orders
* [list_attachments](#list_attachments) - List purchase order attachments
* [update](#update) - Update purchase order

## create

The *Create purchase order* endpoint creates a new [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating an account.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
from decimal import Decimal

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.create(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "purchase_order": {
        "created_by": {
            "email": "john.smith@codat.io",
            "first_name": "John",
            "last_name": "Smith",
        },
        "currency": "GBP",
        "currency_rate": Decimal("1"),
        "delivery_date": "2021-02-02T00:00:00Z",
        "expected_delivery_date": "2021-01-29T00:00:00Z",
        "id": "7e2380af-b51f-4393-92d7-6ff0382da26c",
        "issue_date": "2020-10-24T00:00:00Z",
        "line_items": [
            {
                "account_ref": {
                    "id": "13931cbf-ea06-4d6e-9538-a8457fa66011",
                    "name": "Cost of Goods Sold",
                },
                "description": "Electric Eye purchase",
                "discount_amount": Decimal("0"),
                "discount_percentage": Decimal("0"),
                "item_ref": {
                    "id": "9409d23d-1011-432e-98a4-591fcd8d5404",
                    "name": "ACME Electric Eye",
                },
                "quantity": Decimal("9"),
                "sub_total": Decimal("1035"),
                "tax_amount": Decimal("103.5"),
                "tax_rate_ref": {
                    "id": "6c88aff3-7cb9-4980-a3d3-443e72e02498",
                    "name": "ACME Sales Tax (10%)",
                },
                "total_amount": Decimal("1138.5"),
                "tracking_category_refs": [
                    {
                        "id": "<id>",
                    },
                ],
                "unit_amount": Decimal("115"),
            },
        ],
        "modified_date": "2020-11-17T21:11:20Z",
        "note": "purchaseorder with 1 line items, totalling 1138.5",
        "payment_due_date": "2021-09-13T00:00:00Z",
        "purchase_order_number": "89443280",
        "ship_to": {
            "address": {
                "type": shared.AccountingAddressType.BILLING,
                "city": "Dallas",
                "country": "USA",
                "line1": "1 Carolyns Circle",
                "line2": "",
                "postal_code": "511210",
                "region": "Texas",
            },
            "contact": {
                "email": "sales@carltoninnov.com",
                "name": "Carlton Innovations",
                "phone": "",
            },
        },
        "source_modified_date": "2020-10-25T06:37:33Z",
        "status": shared.PurchaseOrderStatus.CLOSED,
        "sub_total": Decimal("1035"),
        "supplier_ref": {
            "id": "7ff6add1-b0e7-496f-b655-48e20c8fdb2e",
            "supplier_name": "Carlton Innovations",
        },
        "total_amount": Decimal("1138.5"),
        "total_discount": Decimal("0"),
        "total_tax_amount": Decimal("103.5"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePurchaseOrderRequest](../../models/operations/createpurchaseorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[shared.CreatePurchaseOrderResponse](../../models/shared/createpurchaseorderresponse.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## download_attachment

The *Download purchase order attachment* endpoint downloads a specific attachment for a given `purchaseOrderId` and `attachmentId`.

[Purchase Orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support downloading a purchase order attachment.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.download_attachment(request={
    "attachment_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "purchase_order_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DownloadPurchaseOrderAttachmentRequest](../../models/operations/downloadpurchaseorderattachmentrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## download_purchase_order_pdf

The *Download purchase order as PDF* endpoint downloads the purchase order as a PDF for a given `purchaseOrderId`.

[Purchase Orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support getting a purchase order as PDF.

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.download_purchase_order_pdf(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "purchase_order_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DownloadPurchaseOrderPdfRequest](../../models/operations/downloadpurchaseorderpdfrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## get

The *Get purchase order* endpoint returns a single purchase order for a given purchaseOrderId.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support getting a specific purchase order.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "purchase_order_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPurchaseOrderRequest](../../models/operations/getpurchaseorderrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[shared.PurchaseOrder](../../models/shared/purchaseorder.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_attachment

The *Get purchase order attachment* endpoint returns a specific attachment for a given `purchaseOrderId` and `attachmentId`.

[Purchase Orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support getting a purchase order attachment.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.get_attachment(request={
    "attachment_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "purchase_order_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetPurchaseOrderAttachmentRequest](../../models/operations/getpurchaseorderattachmentrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[shared.Attachment](../../models/shared/attachment.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## get_create_update_model

The *Get create/update purchase order model* endpoint returns the expected data for the request payload when creating and updating a [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company and integration.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating and updating a purchase order.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.get_create_update_model(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetCreateUpdatePurchaseOrdersModelRequest](../../models/operations/getcreateupdatepurchaseordersmodelrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## list

The *List purchase orders* endpoint returns a list of [purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.list(request={
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

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPurchaseOrdersRequest](../../models/operations/listpurchaseordersrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.PurchaseOrders](../../models/shared/purchaseorders.md)**

### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |


## list_attachments

The *List purchase order attachments* endpoint returns a list of attachments available to download for a given `purchaseOrderId`.

[Purchase Orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support listing purchase order attachments.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.list_attachments(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "purchase_order_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListPurchaseOrderAttachmentsRequest](../../models/operations/listpurchaseorderattachmentsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[shared.AttachmentsDataset](../../models/shared/attachmentsdataset.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## update

The *Update purchase order* endpoint updates an existing [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating an account.


### Example Usage

```python
from codat_accounting import CodatAccounting
from codat_accounting.models import shared
from decimal import Decimal

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.purchase_orders.update(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "purchase_order_id": "<value>",
    "purchase_order": {
        "created_by": {
            "email": "john.smith@codat.io",
            "first_name": "John",
            "last_name": "Smith",
        },
        "currency": "GBP",
        "currency_rate": Decimal("1"),
        "delivery_date": "2021-02-02T00:00:00Z",
        "expected_delivery_date": "2021-01-29T00:00:00Z",
        "id": "7e2380af-b51f-4393-92d7-6ff0382da26c",
        "issue_date": "2020-10-24T00:00:00Z",
        "line_items": [
            {
                "account_ref": {
                    "id": "13931cbf-ea06-4d6e-9538-a8457fa66011",
                    "name": "Cost of Goods Sold",
                },
                "description": "Electric Eye purchase",
                "discount_amount": Decimal("0"),
                "discount_percentage": Decimal("0"),
                "item_ref": {
                    "id": "9409d23d-1011-432e-98a4-591fcd8d5404",
                    "name": "ACME Electric Eye",
                },
                "quantity": Decimal("9"),
                "sub_total": Decimal("1035"),
                "tax_amount": Decimal("103.5"),
                "tax_rate_ref": {
                    "id": "6c88aff3-7cb9-4980-a3d3-443e72e02498",
                    "name": "ACME Sales Tax (10%)",
                },
                "total_amount": Decimal("1138.5"),
                "tracking_category_refs": [
                    {
                        "id": "<id>",
                    },
                ],
                "unit_amount": Decimal("115"),
            },
        ],
        "modified_date": "2020-11-17T21:11:20Z",
        "note": "purchaseorder with 1 line items, totalling 1138.5",
        "payment_due_date": "2021-09-13T00:00:00Z",
        "purchase_order_number": "89443280",
        "ship_to": {
            "address": {
                "type": shared.AccountingAddressType.BILLING,
                "city": "Dallas",
                "country": "USA",
                "line1": "1 Carolyns Circle",
                "line2": "",
                "postal_code": "511210",
                "region": "Texas",
            },
            "contact": {
                "email": "sales@carltoninnov.com",
                "name": "Carlton Innovations",
                "phone": "",
            },
        },
        "source_modified_date": "2020-10-25T06:37:33Z",
        "status": shared.PurchaseOrderStatus.CLOSED,
        "sub_total": Decimal("1035"),
        "supplier_ref": {
            "id": "7ff6add1-b0e7-496f-b655-48e20c8fdb2e",
            "supplier_name": "Carlton Innovations",
        },
        "total_amount": Decimal("1138.5"),
        "total_discount": Decimal("0"),
        "total_tax_amount": Decimal("103.5"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdatePurchaseOrderRequest](../../models/operations/updatepurchaseorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[shared.UpdatePurchaseOrderResponse](../../models/shared/updatepurchaseorderresponse.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
