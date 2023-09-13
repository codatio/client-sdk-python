# purchase_orders

## Overview

Purchase orders

### Available Operations

* [create](#create) - Create purchase order
* [get](#get) - Get purchase order
* [get_create_update_model](#get_create_update_model) - Get create/update purchase order model
* [list](#list) - List purchase orders
* [update](#update) - Update purchase order

## create

The *Create purchase order* endpoint creates a new [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='EUR',
        currency_rate=Decimal('1356.92'),
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='309db053-6d9e-475c-a006-f5392c11a25a',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='bf92f974-28ad-49a9-b8bf-8221125359d9',
                    name='Glenn Lebsack',
                ),
                description='iusto',
                discount_amount=Decimal('6339.56'),
                discount_percentage=Decimal('4531.11'),
                item_ref=shared.ItemRef(
                    id='9cd72cd2-484d-4a21-b29f-2ac41ef5725f',
                    name='Jean Kemmer',
                ),
                quantity=Decimal('7500.75'),
                sub_total=Decimal('944.87'),
                tax_amount=Decimal('9313.93'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('3062.69'),
                    id='1d8a23c2-3e34-4f2d-ba4a-197f6de92215',
                    name='Ms. Dixie Turner Sr.',
                ),
                total_amount=Decimal('309.62'),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='99853e9f-543d-4854-839e-e224460443bc',
                        name='Ms. Lorraine Gusikowski',
                    ),
                ],
                unit_amount=Decimal('7911.29'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='asperiores',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='vel',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Madison',
                country='Guyana',
                line1='at',
                line2='culpa',
                postal_code='52186',
                region='libero',
                type=shared.AccountingAddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Augustine.Kuhlman69@yahoo.com',
                name='Miss Meredith Hand',
                phone='790-276-8540 x482',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.UNKNOWN,
        sub_total=Decimal('5142.34'),
        supplier_ref=shared.SupplierRef(
            id='2bfbdc41-ff5d-44e2-ae4f-b5cb35d17638',
            supplier_name='delectus',
        ),
        total_amount=Decimal('1230.16'),
        total_discount=Decimal('9225.93'),
        total_tax_amount=Decimal('8182.73'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=716538,
)

res = s.purchase_orders.create(req)

if res.create_purchase_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreatePurchaseOrderRequest](../../models/operations/createpurchaseorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.CreatePurchaseOrderResponse](../../models/operations/createpurchaseorderresponse.md)**


## get

The *Get purchase order* endpoint returns a single purchase order for a given purchaseOrderId.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support getting a specific purchase order.

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

req = operations.GetPurchaseOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    purchase_order_id='ducimus',
)

res = s.purchase_orders.get(req)

if res.purchase_order is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetPurchaseOrderRequest](../../models/operations/getpurchaseorderrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetPurchaseOrderResponse](../../models/operations/getpurchaseorderresponse.md)**


## get_create_update_model

The *Get create/update purchase order model* endpoint returns the expected data for the request payload when creating and updating a [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company and integration.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating and updating a purchase order.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdatePurchaseOrdersModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.purchase_orders.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetCreateUpdatePurchaseOrdersModelRequest](../../models/operations/getcreateupdatepurchaseordersmodelrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |


### Response

**[operations.GetCreateUpdatePurchaseOrdersModelResponse](../../models/operations/getcreateupdatepurchaseordersmodelresponse.md)**


## list

The *List purchase orders* endpoint returns a list of [purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

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

req = operations.ListPurchaseOrdersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='atque',
)

res = s.purchase_orders.list(req)

if res.purchase_orders is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListPurchaseOrdersRequest](../../models/operations/listpurchaseordersrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListPurchaseOrdersResponse](../../models/operations/listpurchaseordersresponse.md)**


## update

The *Update purchase order* endpoint updates an existing [purchase order](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) for a given company's connection.

[Purchase orders](https://docs.codat.io/accounting-api#/schemas/PurchaseOrder) represent a business's intent to purchase goods or services from a supplier.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='GBP',
        currency_rate=Decimal('3670.96'),
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='cc5cb860-f8cd-4580-ba73-810e4fe44472',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='7cd3b1dd-3bbc-4e24-bb76-84eff50126d7',
                    name='Vicky Wolf',
                ),
                description='facere',
                discount_amount=Decimal('113.92'),
                discount_percentage=Decimal('9309.42'),
                item_ref=shared.ItemRef(
                    id='b74b8421-953b-444b-93c4-3159d33e5953',
                    name='Mr. Michael Bashirian',
                ),
                quantity=Decimal('5784.52'),
                sub_total=Decimal('5525.12'),
                tax_amount=Decimal('3971.12'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('1930.48'),
                    id='aa41e6c3-1cc2-4f1f-8b51-c9a41ffbe9cb',
                    name='Brad Mraz',
                ),
                total_amount=Decimal('9358'),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='65e076cc-7abf-4616-aa5c-71641934b90f',
                        name='Rochelle Bailey',
                    ),
                ],
                unit_amount=Decimal('683'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='possimus',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='a',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Champlinworth',
                country='Nepal',
                line1='earum',
                line2='fugit',
                postal_code='10352-2752',
                region='enim',
                type=shared.AccountingAddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Dayana.Kilback@gmail.com',
                name='Ms. Nettie McCullough',
                phone='(836) 983-6977 x4324',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.VOID,
        sub_total=Decimal('5678.21'),
        supplier_ref=shared.SupplierRef(
            id='222c9ff5-7491-4aab-ba2e-761f0ca4d456',
            supplier_name='vero',
        ),
        total_amount=Decimal('9708.48'),
        total_discount=Decimal('1170.53'),
        total_tax_amount=Decimal('234.1'),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='adipisci',
    timeout_in_minutes=80294,
)

res = s.purchase_orders.update(req)

if res.update_purchase_order_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdatePurchaseOrderRequest](../../models/operations/updatepurchaseorderrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.UpdatePurchaseOrderResponse](../../models/operations/updatepurchaseorderresponse.md)**

