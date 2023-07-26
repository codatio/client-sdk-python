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
        currency='USD',
        currency_rate=7740.9,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='a645de98-6755-41a9-8ce6-1ec2c79a39ae',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='4d5a65b4-d556-42d9-b7d9-e2d6fcf55762',
                    name='Drew Pollich',
                ),
                description='ad',
                discount_amount=7877.69,
                discount_percentage=1972.67,
                item_ref=shared.ItemRef(
                    id='a890282a-51f4-41cf-a796-ed3d724c18f5',
                    name='Jonathan Tromp',
                ),
                quantity=7803.32,
                sub_total=7948.94,
                tax_amount=8856.75,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2355.79,
                    id='f716600d-a0e3-4aa6-9c6f-e09d852b53b3',
                    name='Nichole Kutch',
                ),
                total_amount=8112.21,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c710e167-3d90-45cb-8bed-ef3c127c3909',
                        name='Alvin Hartmann',
                    ),
                ],
                unit_amount=1730.52,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='50dcbbcd-3b12-41b8-8c1e-e5e7a061391c',
                    name='Dwight Wisoky DDS',
                ),
                description='iusto',
                discount_amount=8302.89,
                discount_percentage=1060.35,
                item_ref=shared.ItemRef(
                    id='764926b0-cf5e-46cb-aeba-be5e0b99f3b1',
                    name='Veronica Luettgen',
                ),
                quantity=6429.43,
                sub_total=5465.01,
                tax_amount=4401.02,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7240.6,
                    id='b7aecbe5-69d7-40cb-8699-07f989441452',
                    name='Mr. Perry Wiza',
                ),
                total_amount=2102.37,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='42c61be1-33ba-4cde-932b-6526f862853f',
                        name='Alan Langworth',
                    ),
                    shared.TrackingCategoryRef(
                        id='ce322231-fe66-464c-81d2-fba5cba069b8',
                        name='Miss Billy McCullough',
                    ),
                ],
                unit_amount=7299.76,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='810a2aa8-7494-479e-9d4f-cf7b50cf87f0',
                    name='Emmett Ernser',
                ),
                description='esse',
                discount_amount=762.27,
                discount_percentage=197.89,
                item_ref=shared.ItemRef(
                    id='76a24b40-c8f0-48bf-b108-1e88f86996c8',
                    name='Fred Dare',
                ),
                quantity=164.13,
                sub_total=6264.24,
                tax_amount=2164.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8056.07,
                    id='f47893bd-23f8-4660-8c61-c7834273caa9',
                    name='Anna Lemke',
                ),
                total_amount=5420.06,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1b61a331-a54d-4c10-a94f-92fed939ba8f',
                        name='Janet Upton',
                    ),
                    shared.TrackingCategoryRef(
                        id='92c20ee1-228a-4c3a-9c64-7d240bc11ea4',
                        name='Mrs. Nicholas Leannon',
                    ),
                    shared.TrackingCategoryRef(
                        id='cc6a2f0f-5b9d-43cb-91a7-687d3100e8e2',
                        name='Dr. Salvador Roberts',
                    ),
                    shared.TrackingCategoryRef(
                        id='46d2a7c7-d1ea-40e7-9fa9-bbe5f179f650',
                        name='Arthur Wehner IV',
                    ),
                ],
                unit_amount=9205.44,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='officiis',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='neque',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Haliemouth',
                country='Brazil',
                line1='non',
                line2='soluta',
                postal_code='77804-1678',
                region='ex',
                type=shared.AddressType.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Blaise.Leffler44@yahoo.com',
                name='Dr. Wilbert Buckridge IV',
                phone='(239) 845-6914 x101',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.UNKNOWN,
        sub_total=4110.09,
        supplier_ref=shared.SupplierRef(
            id='28fa5039-6286-47e7-ab3a-65024b157f9b',
            supplier_name='nobis',
        ),
        total_amount=3859.93,
        total_discount=9232.4,
        total_tax_amount=9998.39,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=437621,
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
    purchase_order_id='aspernatur',
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
    query='similique',
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
        currency='GBP',
        currency_rate=600.68,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='1d99b661-a7de-4f16-8b6c-cb2822b4a985',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='d2f4a1e9-c4ae-4551-80e7-5726e003c2f0',
                    name='Ms. Ada Haag',
                ),
                description='enim',
                discount_amount=991.13,
                discount_percentage=5431.77,
                item_ref=shared.ItemRef(
                    id='cee41c99-9f46-49f6-b1cf-1a3f023c669e',
                    name='Fannie Jerde',
                ),
                quantity=324.74,
                sub_total=680.19,
                tax_amount=1256.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8751.44,
                    id='ba057988-c672-40c3-903f-1a40c0f3ec86',
                    name='Clayton Yost',
                ),
                total_amount=8912.43,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6fc03128-f0aa-4aee-a004-eba7bf8732be',
                        name='Linda McKenzie',
                    ),
                    shared.TrackingCategoryRef(
                        id='087131f0-6f0b-4ce5-9a86-87143c97905f',
                        name='Kurt Marvin',
                    ),
                    shared.TrackingCategoryRef(
                        id='5da664b7-e778-4a74-baaa-2832bb65862d',
                        name='Dr. Lee Frami',
                    ),
                    shared.TrackingCategoryRef(
                        id='b14aa6bd-ec7f-4444-a32e-9a5dee1acd72',
                        name='Jaime McKenzie',
                    ),
                ],
                unit_amount=711.51,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='b58fe682-e1c2-4dbe-a3d5-8e8247d122c9',
                    name='Gilbert Kshlerin',
                ),
                description='praesentium',
                discount_amount=9796.97,
                discount_percentage=6607.28,
                item_ref=shared.ItemRef(
                    id='27958367-363d-4a07-9096-faeb86480730',
                    name='Armando Wiza',
                ),
                quantity=5237.4,
                sub_total=6038.54,
                tax_amount=8675.31,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6062.34,
                    id='ca607565-6fc0-4ebe-a715-5e2d06a3070d',
                    name='Sonja Christiansen',
                ),
                total_amount=9410.3,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='81fabaaa-7d80-4108-8076-ff5f6ed29814',
                        name='Mrs. Brandy Lehner',
                    ),
                    shared.TrackingCategoryRef(
                        id='b6a70b0d-d82f-494f-bfbd-1e1e21ddc690',
                        name='Dr. Margie Powlowski IV',
                    ),
                ],
                unit_amount=4675.79,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='b51eb5fd-30bf-4e03-890c-f20254a95904',
                    name='Kendra Rau',
                ),
                description='aspernatur',
                discount_amount=8202.86,
                discount_percentage=3958.97,
                item_ref=shared.ItemRef(
                    id='bc9917f9-8e47-492b-979a-413d6a8c9168',
                    name='Alison Stroman',
                ),
                quantity=992.09,
                sub_total=8469.9,
                tax_amount=606.59,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8453.97,
                    id='98ccf89d-3861-4186-ad76-c002facb13ac',
                    name='Debbie Schowalter II',
                ),
                total_amount=1929.94,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='866c575a-1e26-4687-b0be-37b0e8fbc48d',
                        name='Cedric Koch',
                    ),
                    shared.TrackingCategoryRef(
                        id='9b535105-0501-44dc-a105-882484c36e94',
                        name='Byron Mayert',
                    ),
                    shared.TrackingCategoryRef(
                        id='82d34e0b-8fc0-4d59-b57b-9f9820be0780',
                        name='Leland Douglas',
                    ),
                ],
                unit_amount=5874.85,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='e2f70344-e00f-4478-ab53-9483f748eefc',
                    name='Kelvin Keebler',
                ),
                description='minima',
                discount_amount=2545.32,
                discount_percentage=700.77,
                item_ref=shared.ItemRef(
                    id='b4b393f3-5666-425b-aa32-201dec379c59',
                    name='Dr. Elias Nitzsche',
                ),
                quantity=5072.63,
                sub_total=7816.86,
                tax_amount=3272.41,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8119.2,
                    id='2f9e21d9-0fd5-4377-abfc-7677f0f504a6',
                    name='Oscar Lesch',
                ),
                total_amount=9417.31,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6daee19c-26c0-4cb6-98c6-331cabdab767',
                        name='Miguel Goldner',
                    ),
                    shared.TrackingCategoryRef(
                        id='d0da0abe-58eb-43d5-8ba1-cb3ad49b8e5c',
                        name='Lena Pouros',
                    ),
                    shared.TrackingCategoryRef(
                        id='e87f6482-3255-4be9-9c0c-bcb2ca87908d',
                        name='Miss Tiffany Lowe',
                    ),
                ],
                unit_amount=116.47,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='doloribus',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='eum',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='New Brunswick',
                country='Cameroon',
                line1='qui',
                line2='totam',
                postal_code='34033-6304',
                region='numquam',
                type=shared.AddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Zula_Ritchie@hotmail.com',
                name='Duane Legros',
                phone='(365) 620-2242 x60633',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.UNKNOWN,
        sub_total=3727.48,
        supplier_ref=shared.SupplierRef(
            id='3876e39d-ef9c-4765-9fd7-354e5cb94977',
            supplier_name='voluptatem',
        ),
        total_amount=963.17,
        total_discount=4507.31,
        total_tax_amount=6874.97,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='quia',
    timeout_in_minutes=375533,
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

