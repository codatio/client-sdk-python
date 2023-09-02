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
        currency_rate=9054.35,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='5ffa906a-e559-4b72-ab67-46030fe18376',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='bedee767-90ed-40c1-aa7b-a478404489f6',
                    name='Courtney Bednar',
                ),
                description='ipsa',
                discount_amount=3059.71,
                discount_percentage=5075.68,
                item_ref=shared.ItemRef(
                    id='091a2ba2-5ee6-4c75-af8a-60a7ae346e09',
                    name='Misty Toy',
                ),
                quantity=9569.24,
                sub_total=8931.29,
                tax_amount=4306.16,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=72.7,
                    id='acaca645-de98-4675-91a9-cce61ec2c79a',
                    name='Miriam Pfannerstill',
                ),
                total_amount=6840.34,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d5a65b4d-5562-4d9b-bd9e-2d6fcf557629',
                        name='Kerry Lockman',
                    ),
                    shared.TrackingCategoryRef(
                        id='c3a89028-2a51-4f41-8f67-96ed3d724c18',
                        name='Dr. Leon Ledner',
                    ),
                ],
                unit_amount=5132.8,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='minus',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='consectetur',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='La Habra',
                country='British Indian Ocean Territory (Chagos Archipelago)',
                line1='autem',
                line2='aliquid',
                postal_code='08608',
                region='dolor',
                type=shared.AccountingAddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Giles.Bogan99@yahoo.com',
                name='James Marvin',
                phone='(373) 362-1857 x481',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.OPEN,
        sub_total=958.62,
        supplier_ref=shared.SupplierRef(
            id='0e1673d9-05cb-44be-9ef3-c127c3909955',
            supplier_name='consequuntur',
        ),
        total_amount=5021.78,
        total_discount=1730.52,
        total_tax_amount=3712.26,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=57599,
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
    purchase_order_id='pariatur',
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
    query='maxime',
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
        currency_rate=7439.49,
        delivery_date='2022-10-23T00:00:00.000Z',
        expected_delivery_date='2022-10-23T00:00:00.000Z',
        id='3b121b88-c1ee-45e7-a061-391cc8fa0b7d',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='64926b0c-f5e6-4cb6-abab-e5e0b99f3b13',
                    name='Billie Stokes',
                ),
                description='corrupti',
                discount_amount=4401.02,
                discount_percentage=7240.6,
                item_ref=shared.ItemRef(
                    id='b7aecbe5-69d7-40cb-8699-07f989441452',
                    name='Mr. Perry Wiza',
                ),
                quantity=2102.37,
                sub_total=3116.04,
                tax_amount=2769.43,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1795.24,
                    id='c61be133-bacd-4e53-ab65-26f862853fe2',
                    name='Ronnie McKenzie',
                ),
                total_amount=2499.78,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='2231fe66-64c4-41d2-bba5-cba069b8d291',
                        name='Percy Renner Jr.',
                    ),
                ],
                unit_amount=6653.38,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='2aa87494-79ed-4d4f-8f7b-50cf87f08f39',
                    name='Ms. Joy Blick',
                ),
                description='culpa',
                discount_amount=1832.7,
                discount_percentage=2964.52,
                item_ref=shared.ItemRef(
                    id='b40c8f08-bff1-4081-a88f-86996c8e22be',
                    name='Marguerite Emmerich',
                ),
                quantity=2955.55,
                sub_total=4539.1,
                tax_amount=5001.01,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5720.7,
                    id='3bd23f86-600c-461c-b834-273caa9118b3',
                    name='Emilio Bogisich',
                ),
                total_amount=810,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='331a54dc-1029-44f9-afed-939ba8f71e29',
                        name='Adam Schroeder DVM',
                    ),
                    shared.TrackingCategoryRef(
                        id='e1228ac3-adc6-447d-a40b-c11ea482824c',
                        name='Gregg Jacobs',
                    ),
                    shared.TrackingCategoryRef(
                        id='f0f5b9d3-cb11-4a76-87d3-100e8e2b9b0d',
                        name='Bertha Hudson',
                    ),
                ],
                unit_amount=6766.65,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quisquam',
        payment_due_date='2022-10-23T00:00:00.000Z',
        purchase_order_number='fugiat',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Fort Mariannatown',
                country='Turkey',
                line1='quam',
                line2='iste',
                postal_code='65779-3904',
                region='sint',
                type=shared.AccountingAddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Flossie.Bailey93@yahoo.com',
                name='Margaret Kutch',
                phone='1-425-541-2767 x78041',
            ),
        ),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.PurchaseOrderStatus.CLOSED,
        sub_total=8436.48,
        supplier_ref=shared.SupplierRef(
            id='61918d27-9c10-4c18-916f-d78be2621272',
            supplier_name='ea',
        ),
        total_amount=1382.52,
        total_discount=5494.57,
        total_tax_amount=9854.77,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='officia',
    timeout_in_minutes=352126,
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

