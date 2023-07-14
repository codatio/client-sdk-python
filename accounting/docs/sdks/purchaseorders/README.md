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

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='EUR',
        currency_rate=5759.77,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='5075bc25-3825-4334-bfb0-a4e66ea47578',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='71e29418-18fc-4679-b6b2-f25359b855d0',
                    name='Cathy Powlowski',
                ),
                description='eligendi',
                discount_amount=5505.76,
                discount_percentage=7374.84,
                item_ref=shared.ItemRef(
                    id='83a38a8a-88c1-4442-80c2-caeb1ae1ecf8',
                    name='Chad Gislason',
                ),
                quantity=4159.24,
                sub_total=6882.17,
                tax_amount=6973.55,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6797.33,
                    id='7a05a8b4-a9ec-45b3-a88c-ca363272760e',
                    name='Chester Johnson',
                ),
                total_amount=4684.82,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='05410334-7d78-4ff2-8911-45fab9e59a4a',
                        name='Nathan Fay',
                    ),
                    shared.TrackingCategoryRef(
                        id='64eaa6bf-2ff1-44e8-81b3-52accedacc52',
                        name='Mrs. Charlene Little',
                    ),
                    shared.TrackingCategoryRef(
                        id='ca016bc4-1ea1-4342-9410-4a25ef71de57',
                        name='Keith Bradtke',
                    ),
                    shared.TrackingCategoryRef(
                        id='14a43176-92ea-4486-b3d5-22b828a90306',
                        name='Mr. Michelle Zemlak',
                    ),
                ],
                unit_amount=7532.31,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='sint',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='ut',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Runteview',
                country='French Guiana',
                line1='eligendi',
                line2='magni',
                postal_code='16117-2556',
                region='facere',
                type=shared.AddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Cathrine_Wisoky@yahoo.com',
                name='Jon Heller',
                phone='1-491-252-0038 x612',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.CLOSED,
        sub_total=5615.97,
        supplier_ref=shared.SupplierRef(
            id='7d4f6212-7a60-47d1-a062-94514c3db9ca',
            supplier_name='omnis',
        ),
        total_amount=9600.37,
        total_discount=2360.34,
        total_tax_amount=5514.18,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=694759,
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
    purchase_order_id='at',
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
    query='quia',
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

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='EUR',
        currency_rate=8782.83,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='8703493f-49aa-4846-9a32-83279b719d1c',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='673d86e3-b35e-449a-b135-778ce54cacb0',
                    name='Chris Terry',
                ),
                description='ducimus',
                discount_amount=3264.82,
                discount_percentage=276.36,
                item_ref=shared.ItemRef(
                    id='45bacf63-b215-4186-ab5e-3a022614315d',
                    name='Bernice Jakubowski',
                ),
                quantity=5766.94,
                sub_total=5813.68,
                tax_amount=9207.5,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3778.77,
                    id='1afc7186-ff20-4b7a-b3df-40ca0d7657c1',
                    name='Esther Bernier',
                ),
                total_amount=9823,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='55271b25-11dd-4606-9d1b-28272bc9c322',
                        name='Tara Marquardt',
                    ),
                ],
                unit_amount=822.04,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='880fcbb2-b93c-415f-a70b-d1784831653e',
                    name='Kerry Farrell',
                ),
                description='vero',
                discount_amount=1407.83,
                discount_percentage=3102.85,
                item_ref=shared.ItemRef(
                    id='1c310998-3663-4c66-9cbb-7df6cb09c8b4',
                    name='Ms. Irma Walter I',
                ),
                quantity=4775.18,
                sub_total=4482.26,
                tax_amount=2986.6,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8337.81,
                    id='e4fee101-d978-40a1-8c47-b95040d6c8b2',
                    name='Mr. Roberto Wilkinson',
                ),
                total_amount=1526.43,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='7e4048f9-0009-4ed2-9027-8eb4ae9d6416',
                        name='Mrs. Delia Moore Jr.',
                    ),
                ],
                unit_amount=1887.19,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='23b2c09b-9247-471f-9669-e5b7ec762664',
                    name='Woodrow Littel',
                ),
                description='tempore',
                discount_amount=5923.78,
                discount_percentage=9275.83,
                item_ref=shared.ItemRef(
                    id='4cfd2276-e0b8-48fb-87d6-fa5b6e8dbf81',
                    name='Nettie Kuvalis',
                ),
                quantity=809.04,
                sub_total=7530.97,
                tax_amount=6568.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4189.32,
                    id='a9ffc561-929c-4ca9-960a-1395918da1d4',
                    name='Rolando Kovacek',
                ),
                total_amount=2178.8,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f8e1143d-a930-48b2-ba08-af22184439b3',
                        name='Rolando Lesch',
                    ),
                    shared.TrackingCategoryRef(
                        id='6ccce470-cd21-447b-ae61-52cf01d0d8c3',
                        name='Clifford Quigley',
                    ),
                    shared.TrackingCategoryRef(
                        id='5bf935df-e974-4fa4-b1e9-c097eda62344',
                        name='Alexis Braun',
                    ),
                    shared.TrackingCategoryRef(
                        id='237e9984-c80b-4479-a891-923c18ca8d69',
                        name='Jon Jacobs',
                    ),
                ],
                unit_amount=1303.91,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='tempora',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='animi',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='North Caylatown',
                country='Japan',
                line1='officiis',
                line2='eius',
                postal_code='69025-7849',
                region='ab',
                type=shared.AddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Cicero_Schowalter67@hotmail.com',
                name='Cody Zemlak',
                phone='876-479-9089 x35968',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.CLOSED,
        sub_total=1625.48,
        supplier_ref=shared.SupplierRef(
            id='ee70be06-9fb3-46ad-9704-080e0a3fc73a',
            supplier_name='ullam',
        ),
        total_amount=6283.94,
        total_discount=465.74,
        total_tax_amount=2391.23,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='aliquam',
    timeout_in_minutes=744576,
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

