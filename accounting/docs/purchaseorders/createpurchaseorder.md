# create_purchase_order
Available in: `purchase_orders`

Posts a new purchase order to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update purchase order model](https://docs.codat.io/accounting-api#/operations/get-create-update-purchaseOrders-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support creating purchase orders.

## Example Usage
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
        currency_rate=5307.21,
        delivery_date="2022-10-23T00:00:00Z",
        expected_delivery_date="2022-10-23T00:00:00Z",
        id="4439b3de-8756-4ccc-a470-cd2147b6e615",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="cf01d0d8-c3a4-4b9a-9bf9-35dfe974fa4b",
                    name="Tasha Mante V",
                ),
                description="molestiae",
                discount_amount=8810.35,
                discount_percentage=8368.04,
                item_ref=shared.ItemRef(
                    id="a623442e-1a92-437e-9984-c80b479e8919",
                    name="Ms. Connie Romaguera",
                ),
                quantity=6399.68,
                sub_total=5263.14,
                tax_amount=8167.53,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4265.02,
                    id="9c568921-4fa2-4020-be4f-ae038cd7f1bc",
                    name="Nichole Ortiz",
                ),
                total_amount=9965.51,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="fc2ccba4-bef0-4df6-8eae-db2ee70be069",
                        name="Archie Feeney",
                    ),
                    shared.TrackingCategoryRef(
                        id="dd704080-e0a3-4fc7-ba5a-034b11499243",
                        name="Emilio O'Keefe",
                    ),
                ],
                unit_amount=5196.11,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="in",
        payment_due_date="2022-10-23T00:00:00Z",
        purchase_order_number="est",
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city="South Caesar",
                country="Reunion",
                line1="esse",
                line2="sit",
                postal_code="61328-1120",
                region="dicta",
                type="Unknown",
            ),
            contact=shared.ShipToContact(
                email="Joyce60@yahoo.com",
                name="Elias Bednar",
                phone="1-810-778-1385",
            ),
        ),
        source_modified_date="2022-10-23T00:00:00Z",
        status="Closed",
        sub_total=7865.82,
        supplier_ref=shared.SupplierRef(
            id="306b786b-3d37-4bd2-84a1-f340bb36f677",
            supplier_name="dolorum",
        ),
        total_amount=2612.94,
        total_discount=5072.49,
        total_tax_amount=3603.33,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=80773,
)

res = s.purchase_orders.create_purchase_order(req)

if res.create_purchase_order_response is not None:
    # handle response
```