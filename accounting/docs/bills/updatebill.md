# update_bill
Available in: `bills`

Posts an updated bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support updating a bill.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=3642.84,
        currency="delectus",
        currency_rate=8484.39,
        due_date="2022-10-23T00:00:00Z",
        id="c42c876c-2c2d-4fb4-8fc1-c76230f841fb",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id="bd23fdb1-4db6-4be5-a685-998e22ae20da",
                    name="Lucy Wilkinson",
                ),
                description="nam",
                discount_amount=1554.73,
                discount_percentage=4801.08,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id="1a289c57-e854-4e90-839d-222465694624",
                    name="Viola Bailey",
                ),
                quantity=9624.11,
                sub_total=4618.53,
                tax_amount=6759.55,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7262.44,
                    id="37cef022-2519-44db-9541-0adc669af90a",
                    name="Stacey Satterfield",
                ),
                total_amount=8149.5,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="981f0689-81d6-4bb3-bcfa-a348c31bf407",
                            name="Santiago Fritsch",
                        ),
                        shared.TrackingCategoryRef(
                            id="f0c42b78-f156-4263-98a0-dc766324ccb0",
                            name="Leticia Leannon",
                        ),
                        shared.TrackingCategoryRef(
                            id="12d02529-270b-48d5-b22d-d895b8bcf24d",
                            name="Kent Hickle",
                        ),
                        shared.TrackingCategoryRef(
                            id="93352f74-5339-494d-b8de-3b6e9389f5ab",
                            name="Harvey Wisoky",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="fugit",
                        id="550a2838-2ac4-483a-bd23-15bba650164e",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="f5bf6ae5-91bc-48bd-af36-12b63c205fda",
                        name="Alex Bayer",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="a68a9a35-d086-4b6f-a6fe-f020e9f443b4",
                        name="Erin Kozey",
                    ),
                    shared.TrackingCategoryRef(
                        id="92c8dbda-6a61-4efa-a198-258fd0a9eba4",
                        name="Shari Konopelski",
                    ),
                ],
                unit_amount=9156.53,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="a",
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="quaerat",
                    currency_rate=5698.72,
                    total_amount=3999.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="40d6a183-1c87-4adf-996f-df1ad837ae80",
                        name="Ms. Terry Runolfsson",
                    ),
                    currency="occaecati",
                    currency_rate=3396.51,
                    id="ba998678-fa3f-4696-991a-f388ce036144",
                    note="modi",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="quos",
                    total_amount=7914.54,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id="977a0ef2-f536-4028-afee-f934152ed7e2",
                purchase_order_number="ullam",
            ),
            shared.PurchaseOrderRef(
                id="3f4c157d-eaa7-4170-b445-accf667aaf9b",
                purchase_order_number="tempore",
            ),
        ],
        reference="culpa",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Draft",
        sub_total=780.74,
        supplemental_data=shared.BillSupplementalData(
            content={
                "ad": {
                    "voluptates": "ut",
                    "nesciunt": "ab",
                    "quibusdam": "suscipit",
                    "quidem": "delectus",
                },
                "nemo": {
                    "voluptatum": "sequi",
                    "atque": "maiores",
                    "expedita": "rerum",
                    "totam": "quod",
                },
                "aspernatur": {
                    "impedit": "nam",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="67fc4b42-5e99-4e62-b4c9-f7b79dfeb77a",
            supplier_name="ad",
        ),
        tax_amount=8010.59,
        total_amount=1887.05,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=8736.81,
                name="Candice Nienow",
            ),
            shared.BillWithholdingTax(
                amount=752.03,
                name="Ronnie Bechtelar",
            ),
            shared.BillWithholdingTax(
                amount=9625.43,
                name="Eduardo Armstrong",
            ),
        ],
    ),
    bill_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=270862,
)

res = s.bills.update_bill(req)

if res.update_bill_response is not None:
    # handle response
```