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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='amet',
        currency_rate=256.85,
        delivery_date='quos',
        expected_delivery_date='voluptas',
        id='c10a856a-19d4-4665-ba97-259875dc0cec',
        issue_date='facilis',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='78bd248e-c6e8-4b24-8b1c-06c9c0649d2b',
                    name='Laurence Mraz',
                ),
                description='deleniti',
                discount_amount=8562.89,
                discount_percentage=8359.95,
                item_ref=shared.ItemRef(
                    id='b1665c31-2c7f-4550-9472-1c176292dd78',
                    name='Mattie Treutel DDS',
                ),
                quantity=9633.21,
                sub_total=5503.18,
                tax_amount=7788.66,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1193.26,
                    id='41841fe1-f87e-4a10-ba98-06ea1606399e',
                    name='Jack Kris',
                ),
                total_amount=1221.4,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='58d4ab5b-c80d-4ea7-bfd9-931ec9d106cf',
                        name='Bobby Schiller',
                    ),
                    shared.TrackingCategoryRef(
                        id='ab840a28-ea06-472d-ab73-a34ca434cdb3',
                        name='Rhonda Medhurst V',
                    ),
                ],
                unit_amount=9691.25,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='252078a1-8a4b-40da-ad4b-5cf0616ee922',
                    name='Samantha Kuhic',
                ),
                description='nulla',
                discount_amount=4354.13,
                discount_percentage=416.21,
                item_ref=shared.ItemRef(
                    id='daa0e149-cd1c-4cdd-b62b-bf92390015f2',
                    name='Cassandra Mann',
                ),
                quantity=9894.06,
                sub_total=2550.98,
                tax_amount=9668.03,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9639.86,
                    id='eb9bec50-318a-481e-b01d-297f7b456a85',
                    name='Ms. Casey Heathcote',
                ),
                total_amount=8073.54,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a326341a-cccc-4a66-bd4a-8595c1b32bb2',
                        name='Edith VonRueden',
                    ),
                    shared.TrackingCategoryRef(
                        id='31cd6a5b-e749-406b-96c6-36e74d28a481',
                        name='Miss Velma Murphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='41198640-5876-4b30-8711-3de4061082d0',
                        name='Zachary Effertz',
                    ),
                ],
                unit_amount=5757.79,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='cd927a5b-a551-41bb-8370-d9784fb14647',
                    name='Emily Brakus',
                ),
                description='minima',
                discount_amount=7006.85,
                discount_percentage=9129.06,
                item_ref=shared.ItemRef(
                    id='61b3f371-7287-44c3-b7c8-d439ec6bd2ca',
                    name='John Beatty',
                ),
                quantity=4610.28,
                sub_total=4580.46,
                tax_amount=7955.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4356.49,
                    id='ebbbc9e9-744c-45b6-85a4-af2fcabccbca',
                    name='Denise Marks',
                ),
                total_amount=8858.4,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='06a6cabe-22a1-41f7-ba75-d8ff4452bed7',
                        name='Dora Ankunding',
                    ),
                    shared.TrackingCategoryRef(
                        id='48c282b8-716c-427f-ab17-5780304c40ac',
                        name='Lula Gulgowski',
                    ),
                    shared.TrackingCategoryRef(
                        id='8254fde3-7724-4350-ad85-a7f8cc2911a6',
                        name='Cory Toy',
                    ),
                ],
                unit_amount=7840.43,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='6009f01d-d385-423c-9a4e-bb9fd83f83df',
                    name='Abraham Anderson',
                ),
                description='vel',
                discount_amount=6843.48,
                discount_percentage=534.75,
                item_ref=shared.ItemRef(
                    id='94e2e9c2-205d-4fe7-a5bf-fbcb86015f21',
                    name='Mrs. Genevieve Pfannerstill IV',
                ),
                quantity=99.38,
                sub_total=4855.86,
                tax_amount=9424.35,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6764.72,
                    id='7398247a-8721-47fe-9962-df3eee7c385c',
                    name='Dr. Ada King MD',
                ),
                total_amount=1095.45,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8dbcf6e1-9b90-412c-844e-231ba147727d',
                        name='Nick Hermann',
                    ),
                    shared.TrackingCategoryRef(
                        id='2adabf68-00b0-41bc-bc03-2f2c19dbf711',
                        name='Kristi Mann',
                    ),
                    shared.TrackingCategoryRef(
                        id='f21523e3-7136-4521-ba6e-596aa41b9e20',
                        name='Edna O'Reilly',
                    ),
                ],
                unit_amount=8049.73,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='nesciunt',
        note='ab',
        payment_due_date='ullam',
        purchase_order_number='consectetur',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='West Melvinaborough',
                country='Turkey',
                line1='eaque',
                line2='dolores',
                postal_code='62413',
                region='assumenda',
                type=shared.AddressType.BILLING,
            ),
            contact=shared.ShipToContact(
                email='Bo_Ernser@yahoo.com',
                name='Lucas Ward',
                phone='(360) 661-7480 x44002',
            ),
        ),
        source_modified_date='sequi',
        status=shared.PurchaseOrderStatus.CLOSED,
        sub_total=4563.81,
        supplier_ref=shared.SupplierRef(
            id='99a2a18d-b129-4dc5-a4ab-b7b10caf244d',
            supplier_name='itaque',
        ),
        total_amount=1039.82,
        total_discount=522.31,
        total_tax_amount=2042.81,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=861729,
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
    purchase_order_id='consequatur',
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
    query='quos',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdatePurchaseOrderRequest(
    purchase_order=shared.PurchaseOrder(
        currency='ratione',
        currency_rate=313.23,
        delivery_date='id',
        expected_delivery_date='eligendi',
        id='4d070c4e-396e-4562-85cc-b16373314dad',
        issue_date='minima',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='b890542e-5a55-4a10-bd8a-c0f482f9e9a5',
                    name='Mrs. Marianne Dibbert',
                ),
                description='dolorum',
                discount_amount=8885.29,
                discount_percentage=1224.04,
                item_ref=shared.ItemRef(
                    id='22f0bfec-c419-432d-b04b-3ae70934d9eb',
                    name='Rick O'Reilly',
                ),
                quantity=9449.55,
                sub_total=4261.48,
                tax_amount=9895.04,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4380.7,
                    id='1b0652fe-6536-4fb3-8a41-4aa294d64c08',
                    name='Alan Torp MD',
                ),
                total_amount=5153.47,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='7151a354-ba1a-46d7-9dc3-9917b844c850',
                        name='Brandi Moen',
                    ),
                ],
                unit_amount=3811.97,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='2f4946ca-2d72-466c-9763-812723aa03f8',
                    name='Kristi Bins PhD',
                ),
                description='quam',
                discount_amount=6684.99,
                discount_percentage=6945.05,
                item_ref=shared.ItemRef(
                    id='3e07c05e-13db-488f-991f-98329f91922f',
                    name='Angelica Nienow IV',
                ),
                quantity=7196.87,
                sub_total=3786.8,
                tax_amount=3422.36,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2715.17,
                    id='5000a5b3-6a22-42e3-bf77-0a2b42e5edf6',
                    name='Isabel Dare',
                ),
                total_amount=4624.39,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c6a710e5-4b47-4ec6-aaf9-bd8327e8f7d3',
                        name='Alma Brown',
                    ),
                    shared.TrackingCategoryRef(
                        id='ebdd822a-f2c1-4679-98a0-a46646ec658e',
                        name='Gwendolyn Bernhard',
                    ),
                ],
                unit_amount=8534.49,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='e0aee8c7-2213-4f42-9a03-38b71b3d2fd3',
                    name='Brad Farrell',
                ),
                description='accusantium',
                discount_amount=4920.29,
                discount_percentage=2368.27,
                item_ref=shared.ItemRef(
                    id='088e75ab-7ff2-4a12-bb07-4cd44c23c0b1',
                    name='Dr. Norma Kuvalis',
                ),
                quantity=4240.66,
                sub_total=5411.69,
                tax_amount=2221.75,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3622.4,
                    id='b93ced68-7bb4-453f-84af-461c7cb91c79',
                    name='Stuart Howe',
                ),
                total_amount=8904.64,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='23875a4a-2e87-4d87-b51e-22e77c0e6e11',
                        name='Dave Lockman',
                    ),
                ],
                unit_amount=1771.68,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='laboriosam',
        note='pariatur',
        payment_due_date='minus',
        purchase_order_number='ipsam',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Breitenbergton',
                country='Cuba',
                line1='voluptatem',
                line2='suscipit',
                postal_code='65659',
                region='aspernatur',
                type=shared.AddressType.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Grady78@hotmail.com',
                name='Ellen Willms V',
                phone='454.712.0503 x206',
            ),
        ),
        source_modified_date='dicta',
        status=shared.PurchaseOrderStatus.DRAFT,
        sub_total=4036.82,
        supplier_ref=shared.SupplierRef(
            id='0070c0bc-de7e-450e-a441-101c138b4629',
            supplier_name='fugit',
        ),
        total_amount=2485.73,
        total_discount=8394.11,
        total_tax_amount=3242.71,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='sit',
    timeout_in_minutes=985872,
)

res = s.purchase_orders.update(req)

if res.update_purchase_order_response is not None:
    # handle response
```
