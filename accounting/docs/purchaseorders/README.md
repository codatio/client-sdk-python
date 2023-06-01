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
        currency='occaecati',
        currency_rate=5196.11,
        delivery_date='in',
        expected_delivery_date='est',
        id='472b709a-153e-4223-8106-8539ce0932d1',
        issue_date='aperiam',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='cd15d8cc-306b-4786-b3d3-7bd204a1f340',
                    name='Jean Fahey',
                ),
                description='voluptas',
                discount_amount=4441.02,
                discount_percentage=4856.38,
                item_ref=shared.ItemRef(
                    id='a48519c3-3749-4028-8882-6bb03c7fd225',
                    name='Micheal King',
                ),
                quantity=1000.75,
                sub_total=6359.09,
                tax_amount=5010.45,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5418.34,
                    id='ed72a2d4-af41-458a-82d0-f0f58c3b87b4',
                    name='Dr. Jessica Goldner PhD',
                ),
                total_amount=5697.11,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e9d82c5e-306f-4557-af5c-deb0286d0bc4',
                        name='Maryann Boehm',
                    ),
                    shared.TrackingCategoryRef(
                        id='b378f2fc-ff81-4ddf-be08-8f74ef54c921',
                        name='Meghan Lindgren',
                    ),
                    shared.TrackingCategoryRef(
                        id='6313bb6f-c2c8-4d27-8109-6b66ad6e3e1d',
                        name='Nicolas Emmerich',
                    ),
                ],
                unit_amount=3972.04,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='0334a11a-a1d5-4d22-87de-9b3d46170e76',
                    name='Cameron Metz',
                ),
                description='facilis',
                discount_amount=1958.51,
                discount_percentage=6132.25,
                item_ref=shared.ItemRef(
                    id='8788398e-ba1b-4bf7-9433-56f6349a1642',
                    name='Shelly Quitzon Sr.',
                ),
                quantity=7569.85,
                sub_total=9251.22,
                tax_amount=3035.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4049.25,
                    id='b951652b-158c-4a91-82f0-52632b31cad6',
                    name='Wayne Wilkinson',
                ),
                total_amount=5042.69,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='45005e9d-3d93-44e0-b6f5-c388664f6985',
                        name='Tracy Bahringer',
                    ),
                    shared.TrackingCategoryRef(
                        id='e2aed6aa-f863-4c28-9040-c69a3d906f6e',
                        name='Josh Heathcote',
                    ),
                ],
                unit_amount=4666.58,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='ec7394f2-5f63-44b3-b307-14e6be8c3e09',
                    name='Cecil Hahn',
                ),
                description='aliquam',
                discount_amount=1723.11,
                discount_percentage=6784.76,
                item_ref=shared.ItemRef(
                    id='c299a6e5-e7ae-4f13-802e-945f53743efd',
                    name='Ryan Berge',
                ),
                quantity=1577.51,
                sub_total=1756.68,
                tax_amount=716.71,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9955.38,
                    id='9b1f7d9a-ffe6-4968-aace-efb04f8c512c',
                    name='Orlando Reilly',
                ),
                total_amount=4577.97,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8ed5798d-385d-4460-999d-5c3349576d55',
                        name='Ruth Muller',
                    ),
                ],
                unit_amount=6702.81,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='eos',
        note='qui',
        payment_due_date='corporis',
        purchase_order_number='neque',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Jacobifield',
                country='Kyrgyz Republic',
                line1='nisi',
                line2='veniam',
                postal_code='53896-8398',
                region='dolore',
                type=shared.AddressType.DELIVERY,
            ),
            contact=shared.ShipToContact(
                email='Lauren_Wolf@gmail.com',
                name='Mrs. Esther Medhurst',
                phone='912-845-3852 x6975',
            ),
        ),
        source_modified_date='saepe',
        status=shared.PurchaseOrderStatus.UNKNOWN,
        sub_total=4594.79,
        supplier_ref=shared.SupplierRef(
            id='5ffa906a-e559-4b72-ab67-46030fe18376',
            supplier_name='eligendi',
        ),
        total_amount=1311.2,
        total_discount=7109.21,
        total_tax_amount=9353.25,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=870347,
)

res = s.purchase_orders.create(req)

if res.create_purchase_order_response is not None:
    # handle response
```

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
    purchase_order_id='eveniet',
)

res = s.purchase_orders.get(req)

if res.purchase_order is not None:
    # handle response
```

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

## list

Get purchase orders

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
    query='vero',
)

res = s.purchase_orders.list(req)

if res.purchase_orders is not None:
    # handle response
```

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
        currency='iure',
        currency_rate=4003.93,
        delivery_date='dignissimos',
        expected_delivery_date='perspiciatis',
        id='0ed0c16a-7ba4-4784-8448-9f6770ef0480',
        issue_date='occaecati',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='a2ba25ee-6c75-4af8-a60a-7ae346e0979e',
                    name='Blanche Will',
                ),
                description='consequatur',
                discount_amount=6343.86,
                discount_percentage=7740.9,
                item_ref=shared.ItemRef(
                    id='aca645de-9867-4551-a9cc-e61ec2c79a39',
                    name='Stewart Hintz',
                ),
                quantity=8250.33,
                sub_total=3666.61,
                tax_amount=6621.26,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3870.84,
                    id='5b4d5562-d9b7-4d9e-ad6f-cf557629db87',
                    name='Adrienne Donnelly',
                ),
                total_amount=5958.7,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='282a51f4-1cf6-4796-ad3d-724c18f581e9',
                        name='Lowell Schimmel',
                    ),
                ],
                unit_amount=9716.2,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='esse',
        note='sunt',
        payment_due_date='autem',
        purchase_order_number='aliquid',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='North Retafurt',
                country='Argentina',
                line1='officiis',
                line2='dolor',
                postal_code='63074-9905',
                region='assumenda',
                type=shared.AddressType.BILLING,
            ),
            contact=shared.ShipToContact(
                email='Brandt23@gmail.com',
                name='Danny Daugherty',
                phone='581-840-0803 x42850',
            ),
        ),
        source_modified_date='nostrum',
        status=shared.PurchaseOrderStatus.CLOSED,
        sub_total=7098.7,
        supplier_ref=shared.SupplierRef(
            id='4bedef3c-127c-4390-9955-28250dcbbcd3',
            supplier_name='facilis',
        ),
        total_amount=1020.04,
        total_discount=1677.86,
        total_tax_amount=1207.36,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='tempore',
    timeout_in_minutes=539092,
)

res = s.purchase_orders.update(req)

if res.update_purchase_order_response is not None:
    # handle response
```
