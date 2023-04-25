# create_bill_credit_note
Available in: `bill_credit_notes`

Posts a new billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating bill credit notes.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date="2022-10-23T00:00:00Z",
        bill_credit_note_number="aliquid",
        currency="laborum",
        currency_rate=8811.04,
        discount_percentage=2497.96,
        id="95efb9ba-88f3-4a66-9970-74ba4469b6e2",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="41959890-afa5-463e-a516-fe4c8b711e5b",
                    name="Kristie Spencer",
                ),
                description="pariatur",
                discount_amount=375.59,
                discount_percentage=1624.93,
                item_ref=shared.ItemRef(
                    id="8921cddc-6926-401f-b576-b0d5f0d30c5f",
                    name="Robin D'Amore",
                ),
                quantity=4895.49,
                sub_total=543.38,
                tax_amount=3389.85,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1999.96,
                    id="202c73d5-fe9b-490c-a890-9b3fe49a8d9c",
                    name="Toby Hahn",
                ),
                total_amount=2123.9,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="323f9b77-f3a4-4100-a74e-bf69280d1ba7",
                            name="Sonya Leuschke",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="distinctio",
                        id="f737ae42-03ce-45e6-a95d-8a0d446ce2af",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="73cf3be4-53f8-470b-b26b-5a73429cdb1a",
                        name="Randall Cole",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="679d2322-715b-4f0c-bb1e-31b8b90f3443",
                        name="Ms. Joe Berge",
                    ),
                    shared.TrackingCategoryRef(
                        id="0adcf4b9-2187-49fc-a953-f73ef7fbc7ab",
                        name="Allan Greenholt",
                    ),
                    shared.TrackingCategoryRef(
                        id="39c0f5d2-cff7-4c70-a456-26d436813f16",
                        name="Marshall Wiza",
                    ),
                ],
                unit_amount=7888.73,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="saepe",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="impedit",
                    currency_rate=3592.71,
                    total_amount=3331.45,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="6146c3e2-50fb-4008-842e-141aac366c8d",
                        name="Mrs. Shane Reinger",
                    ),
                    currency="explicabo",
                    currency_rate=5919.35,
                    id="07474778-a7bd-4466-928c-10ab3cdca425",
                    note="ab",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="cupiditate",
                    total_amount=96.88,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="tempora",
                    currency_rate=8920.5,
                    total_amount=3708.53,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="23c7e0bc-7178-4e47-96f2-a70c688282aa",
                        name="Leah Champlin",
                    ),
                    currency="fugit",
                    currency_rate=9564.06,
                    id="222e9817-ee17-4cbe-a1e6-b7b95bc0ab3c",
                    note="consequuntur",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="consequatur",
                    total_amount=7963.92,
                ),
            ),
        ],
        remaining_credit=3082.86,
        source_modified_date="2022-10-23T00:00:00Z",
        status="PartiallyPaid",
        sub_total=2328.65,
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "a": "nulla",
                    "quas": "esse",
                    "quasi": "a",
                },
                "error": {
                    "pariatur": "possimus",
                    "quia": "eveniet",
                    "asperiores": "facere",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="121aa6f1-e674-4bdb-84f1-5756082d68ea",
            supplier_name="architecto",
        ),
        total_amount=6091.78,
        total_discount=9453.02,
        total_tax_amount=984.78,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=920.27,
                name="Mrs. Cynthia Hansen",
            ),
            shared.WithholdingTaxitems(
                amount=6144.65,
                name="Ms. Kenneth Ledner",
            ),
            shared.WithholdingTaxitems(
                amount=6498.32,
                name="Mrs. Priscilla Fritsch",
            ),
            shared.WithholdingTaxitems(
                amount=2531.91,
                name="Ms. Benjamin Hirthe DVM",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=618480,
)

res = s.bill_credit_notes.create_bill_credit_note(req)

if res.create_bill_credit_note_response is not None:
    # handle response
```