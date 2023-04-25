# purchase_orders

## Overview

Purchase orders

### Available Operations

* [create_purchase_order](#create_purchase_order) - Create purchase order
* [get_create_update_purchase_orders_model](#get_create_update_purchase_orders_model) - Get create/update purchase order model
* [get_purchase_order](#get_purchase_order) - Get purchase order
* [list_purchase_orders](#list_purchase_orders) - List purchase orders
* [update_purchase_order](#update_purchase_order) - Update purchase order

## create_purchase_order

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
        currency="et",
        currency_rate=8193.41,
        delivery_date="unde",
        expected_delivery_date="esse",
        id="80a10c47-b950-440d-ac8b-2a5f002207e4",
        issue_date="quae",
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="8f90009e-d290-4278-ab4a-e9d64161e915",
                    name="Patricia Dickens",
                ),
                description="rerum",
                discount_amount=1793.89,
                discount_percentage=7581.19,
                item_ref=shared.ItemRef(
                    id="09b92477-1f56-469e-9b7e-c7626649d84e",
                    name="Terrence Walter",
                ),
                quantity=9525.87,
                sub_total=8696.62,
                tax_amount=1739.26,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1417.37,
                    id="76e0b88f-b87d-46fa-9b6e-8dbf812f83b1",
                    name="Matt Johnston",
                ),
                total_amount=9738.23,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="c561929c-ca95-460a-9395-918da1d48e78",
                        name="Dale Schamberger",
                    ),
                    shared.TrackingCategoryRef(
                        id="e1143da9-308b-427a-88af-22184439b3de",
                        name="Brad Hayes",
                    ),
                    shared.TrackingCategoryRef(
                        id="cce470cd-2147-4b6e-a152-cf01d0d8c3a4",
                        name="Luther Osinski",
                    ),
                    shared.TrackingCategoryRef(
                        id="f935dfe9-74fa-44b1-a9c0-97eda623442e",
                        name="Alberta Mills",
                    ),
                ],
                unit_amount=4631.93,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="e9984c80-b479-4e89-9923-c18ca8d69c56",
                    name="Mrs. Terrance Christiansen",
                ),
                description="animi",
                discount_amount=1643.63,
                discount_percentage=411.11,
                item_ref=shared.ItemRef(
                    id="207e4fae-038c-4d7f-9bc2-cabaf7fc2ccb",
                    name="Jesus Reinger",
                ),
                quantity=461.14,
                sub_total=8366.2,
                tax_amount=9710.36,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3915.17,
                    id="8eaedb2e-e70b-4e06-9fb3-6add704080e0",
                    name="Leonard Wiegand",
                ),
                total_amount=2204.14,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="5a034b11-4992-443a-ba69-87a472b709a1",
                        name="Tracy Thiel",
                    ),
                    shared.TrackingCategoryRef(
                        id="30106853-9ce0-4932-910a-cd15d8cc306b",
                        name="Irma Huels",
                    ),
                    shared.TrackingCategoryRef(
                        id="d37bd204-a1f3-440b-b36f-677a48519c33",
                        name="Mr. Eva Marvin",
                    ),
                ],
                unit_amount=3069.7,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="deleniti",
        note="quos",
        payment_due_date="qui",
        purchase_order_number="ex",
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city="Rauton",
                country="Denmark",
                line1="porro",
                line2="nihil",
                postal_code="81138-2454",
                region="architecto",
                type="Billing",
            ),
            contact=shared.ShipToContact(
                email="Karelle.Treutel18@yahoo.com",
                name="Roy Simonis",
                phone="403.667.1809 x09357",
            ),
        ),
        source_modified_date="adipisci",
        status="Closed",
        sub_total=5198.96,
        supplier_ref=shared.SupplierRef(
            id="7b47040d-0d98-4e9d-82c5-e306f5576f5c",
            supplier_name="quibusdam",
        ),
        total_amount=9167.97,
        total_discount=7367.93,
        total_tax_amount=57.18,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=178911,
)

res = s.purchase_orders.create_purchase_order(req)

if res.create_purchase_order_response is not None:
    # handle response
```

## get_create_update_purchase_orders_model

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.purchase_orders.get_create_update_purchase_orders_model(req)

if res.push_option is not None:
    # handle response
```

## get_purchase_order

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    purchase_order_id="totam",
)

res = s.purchase_orders.get_purchase_order(req)

if res.purchase_order is not None:
    # handle response
```

## list_purchase_orders

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
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="ea",
)

res = s.purchase_orders.list_purchase_orders(req)

if res.purchase_orders is not None:
    # handle response
```

## update_purchase_order

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
        currency="pariatur",
        currency_rate=27.26,
        delivery_date="distinctio",
        expected_delivery_date="maxime",
        id="43b18ab3-78f2-4fcf-b81d-df7e088f74ef",
        issue_date="quis",
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="c9216e89-2631-43bb-afc2-c8d2701096b6",
                    name="Genevieve Steuber",
                ),
                description="amet",
                discount_amount=9260.74,
                discount_percentage=963.03,
                item_ref=shared.ItemRef(
                    id="d9d3b660-334a-411a-a1d5-d2247de9b3d4",
                    name="Dr. Frances Kutch",
                ),
                quantity=4290.14,
                sub_total=5505.38,
                tax_amount=6701.68,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5968.46,
                    id="6bb39878-8398-4eba-9bbf-7143356f6349",
                    name="Keith Hoeger",
                ),
                total_amount=2761.09,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="b211ce46-b951-4652-b158-ca9142f05263",
                        name="Miss Opal Dickinson",
                    ),
                    shared.TrackingCategoryRef(
                        id="d692ffc8-7450-405e-9d3d-934e036f5c38",
                        name="Brett Hudson",
                    ),
                    shared.TrackingCategoryRef(
                        id="6985530a-2e2a-4ed6-aaf8-63c28d040c69",
                        name="Marvin Stracke III",
                    ),
                ],
                unit_amount=9418.45,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="6ebd5ad7-ec73-494f-a5f6-34b3730714e6",
                    name="Clay Lockman",
                ),
                description="debitis",
                discount_amount=63.56,
                discount_percentage=5959.44,
                item_ref=shared.ItemRef(
                    id="c64d342a-c299-4a6e-9e7a-ef13402e945f",
                    name="Cindy Koepp",
                ),
                quantity=9094.5,
                sub_total=9428.69,
                tax_amount=8126.55,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9230.35,
                    id="1198221f-9b1f-47d9-affe-69682aceefb0",
                    name="Lela Lemke",
                ),
                total_amount=750.04,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="caabea70-8ed5-4798-9385-d460599d5c33",
                        name="Shelly Hickle",
                    ),
                ],
                unit_amount=8165.54,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="minima",
        note="ullam",
        payment_due_date="dolores",
        purchase_order_number="accusantium",
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city="Torphystead",
                country="Oman",
                line1="eos",
                line2="qui",
                postal_code="27384",
                region="nisi",
                type="Unknown",
            ),
            contact=shared.ShipToContact(
                email="Jordyn_Hyatt62@yahoo.com",
                name="Vernon Will",
                phone="359.660.2503 x4591",
            ),
        ),
        source_modified_date="dolor",
        status="Closed",
        sub_total=4172.21,
        supplier_ref=shared.SupplierRef(
            id="86d839fc-9e17-45ff-a906-ae559b72eb67",
            supplier_name="magnam",
        ),
        total_amount=4246.29,
        total_discount=361.86,
        total_tax_amount=2316.09,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    purchase_order_id="sit",
    timeout_in_minutes=987456,
)

res = s.purchase_orders.update_purchase_order(req)

if res.update_purchase_order_response is not None:
    # handle response
```
