# create_bill
Available in: `bills`

Posts a new bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=8487.22,
        currency="facilis",
        currency_rate=2476.18,
        due_date="2022-10-23T00:00:00Z",
        id="adebd5da-ea4c-4506-a8aa-94c02644cf5e",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="d9a4578a-dc1a-4c60-8dec-001ac802e2ec",
                    name="Sonia Wiegand",
                ),
                description="maiores",
                discount_amount=6.91,
                discount_percentage=9926.67,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="816ff347-7c13-4e90-ac14-125b0960a668",
                    name="Dana Berge",
                ),
                quantity=4625.83,
                sub_total=1693.12,
                tax_amount=6463.29,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9650.95,
                    id="923c5949-f83f-4350-8f87-6ffb901c6ecb",
                    name="Joel Von",
                ),
                total_amount=1940.58,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="f789ffaf-eda5-43e5-ae6e-0ac184c2b9c2",
                            name="Bessie Schmidt",
                        ),
                        shared.TrackingCategoryRef(
                            id="373a40e1-942f-432e-9505-5756f5d56d0b",
                            name="Joseph Olson",
                        ),
                        shared.TrackingCategoryRef(
                            id="dfe13db4-f62c-4ba3-b894-1aebc0b80a69",
                            name="Rhonda Schuster",
                        ),
                        shared.TrackingCategoryRef(
                            id="2ecfcc8f-8950-410f-9dd3-d6fa1804e54c",
                            name="Ms. Russell Wunsch",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="est",
                        id="363c8873-e484-4380-b1f6-b8ca275a60a0",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="495cc699-171b-451c-9bdb-1cf4b888ebdf",
                        name="Randall Schmeler",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="99bc7fc0-b2dc-4e10-873e-42b006d67887",
                        name="Rickey Oberbrunner",
                    ),
                    shared.TrackingCategoryRef(
                        id="81a58208-c54f-4efa-9c95-f2eac5565d30",
                        name="Bethany Zboncak",
                    ),
                    shared.TrackingCategoryRef(
                        id="81206e28-13fa-44a4-9c48-0d3f2132af03",
                        name="Sarah Collier",
                    ),
                ],
                unit_amount=735.74,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="4f4cc6f1-8bf9-4621-a6a4-f77a87ee3e4b",
                    name="Lance Hintz",
                ),
                description="aliquid",
                discount_amount=3398.43,
                discount_percentage=7044.02,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="34418e3b-b91c-48d9-b5e0-e8419d8f84f1",
                    name="Clara Wyman",
                ),
                quantity=89.04,
                sub_total=4587.23,
                tax_amount=8913.02,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8174.54,
                    id="cc4aa5f3-cabd-4905-a972-e056728227b2",
                    name="Antonio Beer",
                ),
                total_amount=4570.63,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="bf7a4fa8-7cf5-435a-afae-54ebf60c321f",
                            name="Tammy Farrell",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="nostrum",
                        id="d2367fe1-a0cc-48df-b9f0-a396d90c364b",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="15dfbace-188b-41c4-ae2c-8c6ce611feeb",
                        name="Angelica Kulas",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="b6eec743-78ba-4253-9774-7dc915ad2caf",
                        name="Angel Sporer",
                    ),
                    shared.TrackingCategoryRef(
                        id="23dc0f5a-e2f3-4a6b-b008-78756143f5a6",
                        name="Eduardo Larkin",
                    ),
                    shared.TrackingCategoryRef(
                        id="5554080d-40bc-4acc-acbd-6b5f3ec90930",
                        name="Kristie Mohr",
                    ),
                    shared.TrackingCategoryRef(
                        id="bad25538-19b4-474b-8ed2-0e56248fff63",
                        name="Mr. Matt McLaughlin",
                    ),
                ],
                unit_amount=7211.38,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="dcab6267-6696-4e1e-8002-21b335d89acb",
                    name="Raquel Rolfson",
                ),
                description="id",
                discount_amount=5420.17,
                discount_percentage=8453.65,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="0c549ef0-3004-4978-a61f-a1cf20688f77",
                    name="Justin Willms",
                ),
                quantity=4515.89,
                sub_total=779.92,
                tax_amount=8156.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8049.36,
                    id="a163f2a3-c80a-497f-b334-cddf857a9e61",
                    name="Darren Johnson",
                ),
                total_amount=6484.97,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="21d29dfc-94d6-4fec-9799-390066a6d2d0",
                            name="Linda Frami",
                        ),
                        shared.TrackingCategoryRef(
                            id="338cec08-6fa2-41e9-952c-b3119167b8e3",
                            name="Julian Stanton I",
                        ),
                        shared.TrackingCategoryRef(
                            id="408d6d36-4ffd-4455-906d-1263d48e935c",
                            name="Nichole Marks",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="dicta",
                        id="f30be3e4-3202-4d72-9657-6506641870d9",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="1f9ad030-c4ec-4c11-a083-6429068b8502",
                        name="Jon Hessel",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="73bc845e-320a-4319-b4ba-df947c9a867b",
                        name="Barry Daugherty",
                    ),
                    shared.TrackingCategoryRef(
                        id="6665816d-dca8-4ef5-9fcb-4c593ec12cda",
                        name="Marty Beer",
                    ),
                    shared.TrackingCategoryRef(
                        id="7afedbd8-0df4-448a-87f9-390c58880983",
                        name="Blake Purdy",
                    ),
                    shared.TrackingCategoryRef(
                        id="ef3ffdd9-f7f0-479a-b4d3-5724cdb0f4d2",
                        name="Roger Bradtke",
                    ),
                ],
                unit_amount=8548,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="enim",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="laudantium",
                    currency_rate=2653.03,
                    total_amount=3017.01,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="eded85a9-065e-4628-bdfc-2032b6c87992",
                        name="Melody Kreiger I",
                    ),
                    currency="ad",
                    currency_rate=5398.86,
                    id="4f7ae12c-6891-4f82-8e11-57172305377d",
                    note="minus",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="a",
                    total_amount=6863.01,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="totam",
                    currency_rate=5875.39,
                    total_amount=8701,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="f975e356-6860-492e-9c3d-dc5f111dea10",
                        name="Jeanne Stracke",
                    ),
                    currency="architecto",
                    currency_rate=6659.52,
                    id="4d190feb-2178-40bc-8c0d-bbddb484708f",
                    note="facilis",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="aliquam",
                    total_amount=9229.15,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="91e6bc15-8c4c-44e5-8599-ea342260e9b2",
                purchase_order_number="accusantium",
            ),
        ],
        reference="consequatur",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Void",
        sub_total=9277.54,
        supplemental_data=shared.BillSupplementalData(
            content={
                "deleniti": {
                    "et": "expedita",
                    "quibusdam": "quos",
                    "maiores": "quidem",
                },
                "in": {
                    "doloremque": "fuga",
                    "dicta": "architecto",
                    "suscipit": "eligendi",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="e723d409-7fa3-40e9-af72-5b29122030d8",
            supplier_name="velit",
        ),
        tax_amount=9427.8,
        total_amount=3564.85,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=9319.53,
                name="Mathew Kunde",
            ),
            shared.BillWithholdingTax(
                amount=8287.35,
                name="Theresa Terry",
            ),
            shared.BillWithholdingTax(
                amount=988.05,
                name="Ivan Gulgowski",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=546089,
)

res = s.bills.create_bill(req)

if res.create_bill_response is not None:
    # handle response
```