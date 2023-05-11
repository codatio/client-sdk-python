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

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating purchase orders.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='quo',
        currency_rate=9804.63,
        delivery_date='maxime',
        expected_delivery_date='suscipit',
        id='c0e503f5-6831-4f1d-8ed8-7b28e8afabc9',
        issue_date='laudantium',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='e241e43b-2342-4417-913e-3f62aa9ae4ae',
                    name='Lyle Rath',
                ),
                description='provident',
                discount_amount=7674.79,
                discount_percentage=2960.36,
                item_ref=shared.ItemRef(
                    id='92c5e8ba-5d4a-4a4a-908b-d380c29aa8dd',
                    name='Teresa Predovic',
                ),
                quantity=6509.18,
                sub_total=6484.89,
                tax_amount=2149.29,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=623.49,
                    id='b7b91449-ae69-4c08-8d41-8bb71804f423',
                    name='Clyde Goldner',
                ),
                total_amount=1897.28,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f377ac5c-9b7e-493b-aa3c-523105e7c34c',
                        name='Preston Abernathy',
                    ),
                    shared.TrackingCategoryRef(
                        id='b812a661-4894-44a8-a908-5075bc253825',
                        name='Robin Goodwin',
                    ),
                ],
                unit_amount=7488.6,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='0a4e66ea-4757-48d1-b1e2-941818fc679b',
                    name='Shelley Cronin II',
                ),
                description='dolorem',
                discount_amount=3596.63,
                discount_percentage=6053.38,
                item_ref=shared.ItemRef(
                    id='b855d015-b62c-48b8-ba38-a8a88c144200',
                    name='Benjamin Schoen',
                ),
                quantity=7210.53,
                sub_total=879.15,
                tax_amount=6295.87,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9062.13,
                    id='1ecf8c34-946b-4ba7-a05a-8b4a9ec5b368',
                    name='Simon Rutherford',
                ),
                total_amount=4247.55,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='272760e9-66e9-47e0-9410-3347d78ff249',
                        name='Evelyn Gutkowski',
                    ),
                ],
                unit_amount=6574.81,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='soluta',
        note='excepturi',
        payment_due_date='voluptates',
        purchase_order_number='veniam',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Marcusboro',
                country='Palestinian Territory',
                line1='a',
                line2='ipsum',
                postal_code='33428',
                region='deserunt',
                type=shared.AddressTypeEnum.BILLING,
            ),
            contact=shared.ShipToContact(
                email='Maxine96@yahoo.com',
                name='Ryan Hagenes',
                phone='272-416-7898 x68731',
            ),
        ),
        source_modified_date='qui',
        status=shared.PurchaseOrderStatusEnum.OPEN,
        sub_total=5437.75,
        supplier_ref=shared.SupplierRef(
            id='14eca016-bc41-4ea1-b42d-4104a25ef71d',
            supplier_name='debitis',
        ),
        total_amount=3264.43,
        total_discount=4979.58,
        total_tax_amount=6690.5,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=117700,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetPurchaseOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    purchase_order_id='architecto',
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
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating and updating purchase orders.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListPurchaseOrdersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='fugiat',
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
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support updating purchase orders.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='eum',
        currency_rate=1110.45,
        delivery_date='numquam',
        expected_delivery_date='deserunt',
        id='4317692e-a486-473d-922b-828a9030660f',
        issue_date='doloremque',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='4c79b4cc-64c2-4b3a-b2c4-88ade62f6aa5',
                    name='Leona Olson',
                ),
                description='eveniet',
                discount_amount=1787.12,
                discount_percentage=483.47,
                item_ref=shared.ItemRef(
                    id='83016ca3-4bb8-47d4-b621-27a607d16062',
                    name='Mrs. Alex Heaney',
                ),
                quantity=2049.69,
                sub_total=8634.15,
                tax_amount=7188.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5826.59,
                    id='ca9f38bd-2be8-4787-8349-3f49aa8465a3',
                    name='Myrtle Feil',
                ),
                total_amount=6184.81,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='719d1cea-673d-486e-bb35-e49a3135778c',
                        name='Derek Funk',
                    ),
                    shared.TrackingCategoryRef(
                        id='cb0e3ea9-7504-45ba-8f63-b215186ab5e3',
                        name='Robert Daugherty',
                    ),
                    shared.TrackingCategoryRef(
                        id='14315d15-6829-49e6-9afc-7186ff20b7a7',
                        name='Elena Wisoky DDS',
                    ),
                ],
                unit_amount=6606.02,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='alias',
        note='at',
        payment_due_date='dignissimos',
        purchase_order_number='aliquid',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='South Raheem',
                country='Bahrain',
                line1='ex',
                line2='eius',
                postal_code='77903',
                region='veniam',
                type=shared.AddressTypeEnum.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Augusta31@yahoo.com',
                name='Heather Simonis',
                phone='588-271-5141',
            ),
        ),
        source_modified_date='quidem',
        status=shared.PurchaseOrderStatusEnum.CLOSED,
        sub_total=5873.6,
        supplier_ref=shared.SupplierRef(
            id='c3221697-b188-40fc-bb2b-93c15f670bd1',
            supplier_name='nihil',
        ),
        total_amount=5049.32,
        total_discount=2535.46,
        total_tax_amount=5040.97,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='sequi',
    timeout_in_minutes=122858,
)

res = s.purchase_orders.update(req)

if res.update_purchase_order_response is not None:
    # handle response
```
