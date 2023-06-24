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

Posts a new purchase order to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) to see which integrations support this endpoint.

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
        currency_rate=8513.15,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='0c69a3d9-06f6-4ebd-9ad7-ec7394f25f63',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='3730714e-6be8-4c3e-89c6-4d342ac299a6',
                    name='Glen Toy',
                ),
                description='earum',
                discount_amount=9610.27,
                discount_percentage=791.87,
                item_ref=shared.ItemRef(
                    id='3402e945-f537-443e-bde1-198221f9b1f7',
                    name='Nick Nolan',
                ),
                quantity=9212.73,
                sub_total=4322.15,
                tax_amount=6074.58,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3980.98,
                    id='82aceefb-04f8-4c51-acaa-bea708ed5798',
                    name='Lee Luettgen',
                ),
                total_amount=2876.48,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='0599d5c3-3495-476d-9520-9e9a2253b6d7',
                        name='Lynn Lang',
                    ),
                    shared.TrackingCategoryRef(
                        id='eeae5fd4-b39f-48a1-8906-78f13c686d83',
                        name='Amos Roob',
                    ),
                ],
                unit_amount=756.85,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='75ffa906-ae55-49b7-aeb6-746030fe1837',
                    name='Sheri Cole',
                ),
                description='at',
                discount_amount=9103.82,
                discount_percentage=8766.6,
                item_ref=shared.ItemRef(
                    id='76790ed0-c16a-47ba-8784-04489f6770ef',
                    name='Ms. Suzanne Lang MD',
                ),
                quantity=1711.34,
                sub_total=7457.67,
                tax_amount=6341.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1475.97,
                    id='5ee6c75a-f8a6-40a7-ae34-6e0979e5afe6',
                    name='Cecilia Ryan',
                ),
                total_amount=6433.94,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='45de9867-551a-49cc-a61e-c2c79a39ae5a',
                        name='Krystal Hilll',
                    ),
                    shared.TrackingCategoryRef(
                        id='5b4d5562-d9b7-4d9e-ad6f-cf557629db87',
                        name='Adrienne Donnelly',
                    ),
                ],
                unit_amount=5958.7,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='0282a51f-41cf-4679-aed3-d724c18f581e',
                    name='Dwight Sauer',
                ),
                description='consectetur',
                discount_amount=9716.2,
                discount_percentage=4600.54,
                item_ref=shared.ItemRef(
                    id='16600da0-e3aa-461c-afe0-9d852b53b32c',
                    name='Spencer Kuhn',
                ),
                quantity=7573.4,
                sub_total=4608.74,
                tax_amount=958.62,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6.22,
                    id='e1673d90-5cb4-4bed-af3c-127c39099552',
                    name='Dr. Phillip Hilpert',
                ),
                total_amount=7498.85,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='cd3b121b-88c1-4ee5-a7a0-61391cc8fa0b',
                        name='Kari Breitenberg',
                    ),
                    shared.TrackingCategoryRef(
                        id='4926b0cf-5e6c-4b6e-babe-5e0b99f3b135',
                        name='Orville Hudson',
                    ),
                    shared.TrackingCategoryRef(
                        id='7bb7aecb-e569-4d70-8b06-9907f9894414',
                        name='Judith Nader',
                    ),
                ],
                unit_amount=592.69,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='sapiente',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='quaerat',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='East Nya',
                country='Isle of Man',
                line1='inventore',
                line2='quidem',
                postal_code='02176-7883',
                region='neque',
                type=shared.AddressType.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Halie38@hotmail.com',
                name='Max Homenick',
                phone='(399) 353-5882 x111',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.UNKNOWN,
        sub_total=9856.77,
        supplier_ref=shared.SupplierRef(
            id='e6664c41-d2fb-4a5c-ba06-9b8d291beb81',
            supplier_name='eaque',
        ),
        total_amount=6653.38,
        total_discount=1485.57,
        total_tax_amount=6798.42,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=672553,
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

Get purchase order

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetPurchaseOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    purchase_order_id='atque',
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

Get create/update purchase order model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating and updating purchase orders.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

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
from codataccounting.models import operations

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
    query='molestiae',
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

Posts an updated purchase order to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support updating purchase orders.

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
        currency_rate=5976.63,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='9edd4fcf-7b50-4cf8-bf08-f39271076a24',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='0c8f08bf-f108-41e8-8f86-996c8e22be0a',
                    name='Kendra White',
                ),
                description='blanditiis',
                discount_amount=5720.7,
                discount_percentage=2089.59,
                item_ref=shared.ItemRef(
                    id='bd23f866-00c6-41c7-8342-73caa9118b38',
                    name='Harold Ritchie MD',
                ),
                quantity=2482.29,
                sub_total=1910.69,
                tax_amount=781.25,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6791.41,
                    id='54dc1029-4f92-4fed-939b-a8f71e2992c2',
                    name='Mr. Casey Towne',
                ),
                total_amount=5593.62,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c3adc647-d240-4bc1-9ea4-82824ccc6a2f',
                        name='Johanna Heathcote',
                    ),
                    shared.TrackingCategoryRef(
                        id='d3cb11a7-687d-4310-8e8e-2b9b0d746d2a',
                        name='Adrienne Kreiger PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='a0e79fa9-bbe5-4f17-9f65-0b1e707e7e43',
                        name='Mrs. Angel Kuhn',
                    ),
                ],
                unit_amount=6307.18,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='cce072ab-d619-418d-a79c-10c18516fd78',
                    name='Grady Considine',
                ),
                description='ab',
                discount_amount=1562.87,
                discount_percentage=4579.62,
                item_ref=shared.ItemRef(
                    id='2628fa50-3962-4867-a72b-3a65024b157f',
                    name='Pete Rohan',
                ),
                quantity=9998.39,
                sub_total=4376.21,
                tax_amount=1341.14,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6278.1,
                    id='50871d99-b661-4a7d-af16-8b6ccb2822b4',
                    name='Enrique Larson DVM',
                ),
                total_amount=8556.65,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f4a1e9c4-ae55-4140-a757-26e003c2f029',
                        name='Diane Marks',
                    ),
                ],
                unit_amount=991.13,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='cumque',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='accusamus',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='North Orin',
                country='Nauru',
                line1='excepturi',
                line2='natus',
                postal_code='23594-9179',
                region='quasi',
                type=shared.AddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Velma19@gmail.com',
                name='Ricardo Johnston',
                phone='1-741-500-1876 x034',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.OPEN,
        sub_total=5264.74,
        supplier_ref=shared.SupplierRef(
            id='c6720c31-03f1-4a40-80f3-ec8688fd8ec6',
            supplier_name='tenetur',
        ),
        total_amount=7601.6,
        total_discount=64.47,
        total_tax_amount=2341.76,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='illo',
    timeout_in_minutes=175186,
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

