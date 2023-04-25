# update_bill_credit_note
Available in: `bill_credit_notes`

Posts an updated billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support updating bill credit notes.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date="2022-10-23T00:00:00Z",
        bill_credit_note_number="voluptas",
        currency="asperiores",
        currency_rate=456.59,
        discount_percentage=4090.54,
        id="42dac7af-515c-4c41-baa6-3aae8d67864d",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="b675fd5e-60b3-475e-94f6-fbee41f33317",
                    name="Doyle Feest",
                ),
                description="laboriosam",
                discount_amount=583.56,
                discount_percentage=9167.27,
                item_ref=shared.ItemRef(
                    id="b1ea4265-55ba-43c2-8744-ed53b88f3a8d",
                    name="Terrell Heidenreich MD",
                ),
                quantity=1488.29,
                sub_total=9679.66,
                tax_amount=1318.52,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9944.01,
                    id="b7b194a2-76b2-4691-afe1-f08f4294e369",
                    name="Courtney Goldner",
                ),
                total_amount=9700.76,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="03e8b445-e80c-4a55-afd2-0e457e1858b6",
                            name="Bob Mueller",
                        ),
                        shared.TrackingCategoryRef(
                            id="e3a5aa8e-4824-4d0a-b407-5088e5186206",
                            name="Mrs. Tricia Mueller",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="dolorem",
                        id="b1194b8a-bf60-43a7-9f9d-fe0ab7da8a50",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="187f86bc-173d-4689-aee9-526f8d986e88",
                        name="Delia Parisian",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="0e101256-3f94-4e29-a973-e922a57a15be",
                        name="Meghan Batz IV",
                    ),
                    shared.TrackingCategoryRef(
                        id="07e2b6e3-ab88-445f-8597-a60ff2a54a31",
                        name="Arturo Hagenes",
                    ),
                    shared.TrackingCategoryRef(
                        id="4a3e865e-7956-4f92-91a5-a9da660ff57b",
                        name="Oliver Osinski",
                    ),
                    shared.TrackingCategoryRef(
                        id="f9efc1b4-512c-4103-a648-dc2f615199eb",
                        name="Gilberto Bechtelar",
                    ),
                ],
                unit_amount=9834.27,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="e6c632ca-3aed-4011-b996-312fde047717",
                    name="Irma Wuckert",
                ),
                description="architecto",
                discount_amount=8571.25,
                discount_percentage=396.5,
                item_ref=shared.ItemRef(
                    id="17476360-a15d-4b6a-a606-59a1adeaab58",
                    name="Gloria Skiles",
                ),
                quantity=4053.73,
                sub_total=2811.53,
                tax_amount=3210.43,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7139.27,
                    id="08b61891-baa0-4fe1-ade0-08e6f8c5f350",
                    name="Jimmie Russel",
                ),
                total_amount=3732.16,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="34181430-1042-4181-bd52-08ece7e253b6",
                            name="Jennie Gutkowski DDS",
                        ),
                        shared.TrackingCategoryRef(
                            id="6c6e205e-16de-4ab3-bec9-578a64584273",
                            name="Ms. Armando Gottlieb",
                        ),
                        shared.TrackingCategoryRef(
                            id="162309fb-0929-4921-aefb-9f58c4d86e68",
                            name="Edwin Reichert III",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="vel",
                        id="013f59da-757a-459e-8fef-66ef1caa3383",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="beb47737-3c8d-472f-a4d1-db1f2c431066",
                        name="Leigh Mante",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="9e1cf9e0-6e3a-4437-800a-e6b6bc9b8f75",
                        name="Terence O'Keefe",
                    ),
                    shared.TrackingCategoryRef(
                        id="5a9741d3-1135-4296-9bb8-a7202611435e",
                        name="Tracy Mills",
                    ),
                ],
                unit_amount=8028.94,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="2259b1ab-da8c-4070-a108-4cb0672d1ad8",
                    name="Daisy Tillman",
                ),
                description="sint",
                discount_amount=4097.26,
                discount_percentage=4218.19,
                item_ref=shared.ItemRef(
                    id="5b85efbd-02ba-4e0b-a2d7-82259e3ea4b5",
                    name="Lindsey Kreiger",
                ),
                quantity=1478.01,
                sub_total=2536.25,
                tax_amount=2569.16,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2010.1,
                    id="da7ce52b-895c-4537-8645-4efb0b34896c",
                    name="Bethany Paucek",
                ),
                total_amount=7708.73,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="be2fd570-7577-4929-977d-eac646ecb573",
                            name="Melissa Mayer",
                        ),
                        shared.TrackingCategoryRef(
                            id="eb1e5a2b-12eb-407f-916d-b99545fc95fa",
                            name="Felix Mann PhD",
                        ),
                        shared.TrackingCategoryRef(
                            id="189dbb30-fcb3-43ea-855b-197cd44e2f52",
                            name="Dwight Connelly",
                        ),
                        shared.TrackingCategoryRef(
                            id="513bb6f4-8b65-46bc-9b35-ff2e4b27537a",
                            name="Delbert Stehr",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="ducimus",
                        id="319c177d-525f-477b-914e-eb52ff785fc3",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="14d4c98e-0c2b-4b89-ab75-dad636c60050",
                        name="Desiree Lakin",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="1180f739-ae9e-4057-ab80-9e2810331f39",
                        name="Albert Stroman",
                    ),
                ],
                unit_amount=4567.04,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="voluptatem",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="rerum",
                    currency_rate=4116.15,
                    total_amount=467.91,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7f3c93c7-3b9d-4a3f-aced-a7e23f225741",
                        name="May Nolan",
                    ),
                    currency="distinctio",
                    currency_rate=4502.24,
                    id="544e472e-8028-457a-9b40-463a7d575f14",
                    note="aut",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="aut",
                    total_amount=9116.57,
                ),
            ),
        ],
        remaining_credit=4837.53,
        source_modified_date="2022-10-23T00:00:00Z",
        status="Submitted",
        sub_total=2561.14,
        supplemental_data=shared.SupplementalData(
            content={
                "possimus": {
                    "consectetur": "nesciunt",
                    "quaerat": "itaque",
                },
                "minus": {
                    "distinctio": "iusto",
                },
                "quas": {
                    "facilis": "amet",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="6a08088d-100e-4fad-a200-ef0422eb2164",
            supplier_name="optio",
        ),
        total_amount=9750.95,
        total_discount=5629.48,
        total_tax_amount=6394.63,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5206.78,
                name="Beth Jenkins",
            ),
            shared.WithholdingTaxitems(
                amount=1409.57,
                name="Faith Zulauf",
            ),
            shared.WithholdingTaxitems(
                amount=6176.57,
                name="Anthony Huel",
            ),
        ],
    ),
    bill_credit_note_id="voluptates",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=251627,
)

res = s.bill_credit_notes.update_bill_credit_note(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```