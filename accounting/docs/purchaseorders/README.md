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
        currency='accusamus',
        currency_rate=2806.9,
        delivery_date='quae',
        expected_delivery_date='dolore',
        id='8f90009e-d290-4278-ab4a-e9d64161e915',
        issue_date='quae',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='323b2c09-b924-4771-b566-9e5b7ec76266',
                    name='Sherri Schuster',
                ),
                description='necessitatibus',
                discount_amount=7309.44,
                discount_percentage=5923.78,
                item_ref=shared.ItemRef(
                    id='e4cfd227-6e0b-488f-b87d-6fa5b6e8dbf8',
                    name='Phyllis Zboncak',
                ),
                quantity=7212.12,
                sub_total=809.04,
                tax_amount=7530.97,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6568.11,
                    id='6a9ffc56-1929-4cca-9560-a1395918da1d',
                    name='Penny Walsh',
                ),
                total_amount=8885.45,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='cf8e1143-da93-408b-a7a0-8af22184439b',
                        name='Desiree Walsh',
                    ),
                ],
                unit_amount=3395.66,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='eum',
        note='eligendi',
        payment_due_date='quisquam',
        purchase_order_number='optio',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='El Paso',
                country='Lesotho',
                line1='accusantium',
                line2='impedit',
                postal_code='10246-4931',
                region='ipsam',
                type=shared.AddressType.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Wendell84@hotmail.com',
                name='Cristina Lemke',
                phone='1-476-736-9523 x8985',
            ),
        ),
        source_modified_date='iure',
        status=shared.PurchaseOrderStatus.DRAFT,
        sub_total=9973.37,
        supplier_ref=shared.SupplierRef(
            id='a4b1e9c0-97ed-4a62-b442-e1a9237e9984',
            supplier_name='porro',
        ),
        total_amount=5572.49,
        total_discount=62.92,
        total_tax_amount=7081.21,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=281064,
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
    purchase_order_id='nihil',
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
    query='sint',
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
        currency='saepe',
        currency_rate=5389,
        delivery_date='excepturi',
        expected_delivery_date='architecto',
        id='923c18ca-8d69-4c56-8921-4fa20207e4fa',
        issue_date='saepe',
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id='38cd7f1b-c2ca-4baf-bfc2-ccba4bef0df6',
                    name='Darin O'Hara',
                ),
                description='facilis',
                discount_amount=1625.48,
                discount_percentage=9369.6,
                item_ref=shared.ItemRef(
                    id='e70be069-fb36-4add-b040-80e0a3fc73a5',
                    name='Jason Fisher',
                ),
                quantity=798.12,
                sub_total=679.91,
                tax_amount=2846.73,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5751.24,
                    id='9243afa6-987a-4472-b709-a153e2230106',
                    name='Tommy Emard',
                ),
                total_amount=9037.93,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='932d10ac-d15d-48cc-b06b-786b3d37bd20',
                        name='Harriet Berge',
                    ),
                ],
                unit_amount=2936.48,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='accusantium',
        note='nam',
        payment_due_date='rerum',
        purchase_order_number='dolor',
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city='Wavabury',
                country='Jersey',
                line1='odio',
                line2='dolorum',
                postal_code='53057',
                region='dolor',
                type=shared.AddressType.UNKNOWN,
            ),
            contact=shared.ShipToContact(
                email='Duncan13@yahoo.com',
                name='Tom Lind',
                phone='1-770-374-9811 x382',
            ),
        ),
        source_modified_date='in',
        status=shared.PurchaseOrderStatus.OPEN,
        sub_total=4798.4,
        supplier_ref=shared.SupplierRef(
            id='1a88ed72-a2d4-4af4-958a-c2d0f0f58c3b',
            supplier_name='totam',
        ),
        total_amount=4462.83,
        total_discount=7360.32,
        total_tax_amount=2850.04,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    purchase_order_id='molestiae',
    timeout_in_minutes=50921,
)

res = s.purchase_orders.update(req)

if res.update_purchase_order_response is not None:
    # handle response
```
