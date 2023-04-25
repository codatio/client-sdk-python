# update_purchase_order
Available in: `purchase_orders`

Posts an updated purchase order to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call []().

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=purchaseOrders) for integrations that support updating purchase orders.

## Example Usage
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
        currency="dolor",
        currency_rate=2424.79,
        delivery_date="2022-10-23T00:00:00Z",
        expected_delivery_date="2022-10-23T00:00:00Z",
        id="74902848-826b-4b03-87fd-225e47871a88",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="d72a2d4a-f415-48ac-ad0f-0f58c3b87b47",
                    name="Rhonda Ankunding PhD",
                ),
                description="excepturi",
                discount_amount=5506.48,
                discount_percentage=9007.56,
                item_ref=shared.ItemRef(
                    id="9d82c5e3-06f5-4576-b5cd-eb0286d0bc43",
                    name="Patrick Lynch",
                ),
                quantity=2190.95,
                sub_total=4751.31,
                tax_amount=5490.08,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9580.48,
                    id="2fcff81d-df7e-4088-b74e-f54c9216e892",
                    name="Emily Bergnaum",
                ),
                total_amount=7427.97,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="fc2c8d27-0109-46b6-aad6-e3e1d9d3b660",
                        name="Ethel Hagenes Sr.",
                    ),
                    shared.TrackingCategoryRef(
                        id="aa1d5d22-47de-49b3-9461-70e768a96bb3",
                        name="Everett Kiehn",
                    ),
                ],
                unit_amount=1975.93,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="98eba1bb-f714-4335-af63-49a164249b21",
                    name="Sheri Walsh",
                ),
                description="tempore",
                discount_amount=6131.78,
                discount_percentage=3665.61,
                item_ref=shared.ItemRef(
                    id="1652b158-ca91-442f-8526-32b31cad692f",
                    name="Sherman Labadie",
                ),
                quantity=3433.66,
                sub_total=555.05,
                tax_amount=27.62,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3143.21,
                    id="e9d3d934-e036-4f5c-b886-64f6985530a2",
                    name="Jeremy Murazik",
                ),
                total_amount=4284.76,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="af863c28-d040-4c69-a3d9-06f6ebd5ad7e",
                        name="Kelly DuBuque",
                    ),
                    shared.TrackingCategoryRef(
                        id="f25f634b-3730-4714-a6be-8c3e09c64d34",
                        name="Jan Schowalter",
                    ),
                    shared.TrackingCategoryRef(
                        id="9a6e5e7a-ef13-4402-a945-f53743efde11",
                        name="Hugh Crona DVM",
                    ),
                ],
                unit_amount=6123.82,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="b1f7d9af-fe69-4682-acee-fb04f8c512ca",
                    name="Marco Ullrich",
                ),
                description="voluptatem",
                discount_amount=5033.38,
                discount_percentage=9159.33,
                item_ref=shared.ItemRef(
                    id="d5798d38-5d46-4059-9d5c-3349576d5520",
                    name="Frankie Miller",
                ),
                quantity=1818.58,
                sub_total=3579.41,
                tax_amount=2057.04,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7058.26,
                    id="6d765886-eeae-45fd-8b39-f8a1490678f1",
                    name="Adrienne Johnson",
                ),
                total_amount=8309.31,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="39fc9e17-5ffa-4906-ae55-9b72eb674603",
                        name="Ms. Ora Thompson",
                    ),
                    shared.TrackingCategoryRef(
                        id="76c2bede-e767-490e-90c1-6a7ba4784044",
                        name="Austin Ziemann",
                    ),
                    shared.TrackingCategoryRef(
                        id="70ef0480-91a2-4ba2-9ee6-c75af8a60a7a",
                        name="Curtis Grimes",
                    ),
                ],
                unit_amount=193,
            ),
            shared.PurchaseOrderLineItem(
                account_ref=shared.AccountRef(
                    id="979e5afe-60ac-4aca-a45d-e9867551a9cc",
                    name="Ben Berge",
                ),
                description="sunt",
                discount_amount=7629.97,
                discount_percentage=4878.89,
                item_ref=shared.ItemRef(
                    id="9a39ae5a-4d5a-465b-8d55-62d9b7d9e2d6",
                    name="Jermaine Wiegand",
                ),
                quantity=4577.32,
                sub_total=3923.07,
                tax_amount=1751.03,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5752.06,
                    id="db875c3a-8902-482a-91f4-1cf6796ed3d7",
                    name="Ms. Elaine Schroeder",
                ),
                total_amount=3231.27,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="1e98cce3-f716-4600-9a0e-3aa61c6fe09d",
                        name="Warren Champlin",
                    ),
                    shared.TrackingCategoryRef(
                        id="3b32c8c7-c3c7-410e-9673-d905cb4bedef",
                        name="Bernadette Block",
                    ),
                    shared.TrackingCategoryRef(
                        id="c3909955-2825-40dc-bbcd-3b121b88c1ee",
                        name="Kerry Klocko III",
                    ),
                ],
                unit_amount=959.1,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="adipisci",
        payment_due_date="2022-10-23T00:00:00Z",
        purchase_order_number="excepturi",
        ship_to=shared.ShipTo(
            address=shared.Addressesitems(
                city="Port Rachelmouth",
                country="Venezuela",
                line1="deserunt",
                line2="aut",
                postal_code="48144-2514",
                region="facilis",
                type="Unknown",
            ),
            contact=shared.ShipToContact(
                email="Xzavier.Hane77@hotmail.com",
                name="Marc Treutel",
                phone="938.276.5927 x0235",
            ),
        ),
        source_modified_date="2022-10-23T00:00:00Z",
        status="Void",
        sub_total=3902.15,
        supplier_ref=shared.SupplierRef(
            id="a87bb7ae-cbe5-469d-b0cb-069907f98944",
            supplier_name="vitae",
        ),
        total_amount=2776.66,
        total_discount=3416.95,
        total_tax_amount=1275.33,
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    purchase_order_id="culpa",
    timeout_in_minutes=573150,
)

res = s.purchase_orders.update_purchase_order(req)

if res.update_purchase_order_response is not None:
    # handle response
```