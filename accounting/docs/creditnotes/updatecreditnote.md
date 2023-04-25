# update_credit_note
Available in: `credit_notes`

Posts an updated credit note to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support updating a credit note.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpdateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=613,
        additional_tax_percentage=3298.36,
        allocated_on_date="2022-10-23T00:00:00Z",
        credit_note_number="sint",
        currency="minus",
        currency_rate=5674.41,
        customer_ref=shared.CustomerRef(
            company_name="porro",
            id="3f567e0e-2527-465b-9d62-fcdace1f0121",
        ),
        discount_percentage=3888.89,
        id="ce2239e8-f25c-4d0d-99d9-59f439e39266",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="bd95f7aa-2b24-4113-a95d-1e6698fcc459",
                    name="Bonnie Carroll",
                ),
                description="dolores",
                discount_amount=5658.09,
                discount_percentage=4624.26,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="76763342-5403-48bf-b597-1e9819055738",
                    name="Benny Ward",
                ),
                quantity=6636.42,
                sub_total=7673.61,
                tax_amount=4498.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9508.94,
                    id="da39594d-66bc-42ae-8806-32b9954b6fa2",
                    name="Ruth Kemmer",
                ),
                total_amount=5646.65,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="28553cb1-0006-4bef-8921-ec2053b74936",
                            name="Brandi Schaefer",
                        ),
                        shared.TrackingCategoryRef(
                            id="e0f2bf19-588d-440d-83f3-deba297be3e9",
                            name="Maryann Rolfson PhD",
                        ),
                        shared.TrackingCategoryRef(
                            id="f868fd52-405c-4b33-9d49-2f4f127fb0e0",
                            name="Moses Brekke",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="fugit",
                        id="17978d0a-cca7-47ae-b7b7-021a52046b64",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="9fb0e67e-094f-4dfe-9554-0ef53a34a1b8",
                        name="Lamar Mertz",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="1adc05d8-5ae2-4dfb-b0fb-3874290d3365",
                        name="Janet Torphy",
                    ),
                ],
                unit_amount=993.43,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="6ef89451-bd76-4eee-b518-c4da1fad3551",
                    name="Faith Baumbach",
                ),
                description="dolore",
                discount_amount=9328.83,
                discount_percentage=3163.35,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="b72f0f54-8568-4a04-a4e0-0a1d6eb94346",
                    name="Mrs. Dana Swaniawski V",
                ),
                quantity=3105.42,
                sub_total=9999.32,
                tax_amount=7093,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7284.66,
                    id="a5cceff5-cb01-4fe5-9e52-8a45ac82b85f",
                    name="Dr. Marco Schulist",
                ),
                total_amount=7142.4,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="8da4127d-d597-4ff4-b11a-a1bc74b86cec",
                            name="Kelly Goyette",
                        ),
                        shared.TrackingCategoryRef(
                            id="7b4848bd-6a6f-4044-9d2c-3b808094373e",
                            name="Katie Bailey",
                        ),
                        shared.TrackingCategoryRef(
                            id="9bebbad0-2f25-486b-8f15-2558daa95be6",
                            name="Jody Altenwerth",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="enim",
                        id="6c354aa4-32b4-47e1-b63c-5208c23e9802",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="2f0d45eb-4a8b-4674-ae5c-fc18edc7f787",
                        name="Travis Dach I",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="3d3ed0c5-670e-4f42-bd3c-9f1cc503f6c3",
                        name="Preston Runte MD",
                    ),
                    shared.TrackingCategoryRef(
                        id="6290f957-f385-4189-ad7e-f807aae03f33",
                        name="Dana Kuhlman",
                    ),
                    shared.TrackingCategoryRef(
                        id="b9de4032-ba26-4fd3-a8ba-9216bcb41583",
                        name="Marianne Koelpin",
                    ),
                ],
                unit_amount=2708.4,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="1723133e-dc04-46bc-9163-bbca49227c42",
                    name="Brandon Cummings",
                ),
                description="ipsam",
                discount_amount=1931.99,
                discount_percentage=3126.17,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="0495c5db-b3c5-47c1-a498-1e8aa257ddc1",
                    name="Dennis Considine",
                ),
                quantity=8734.29,
                sub_total=8953.49,
                tax_amount=4286.45,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2501.01,
                    id="bfcc5469-d401-45df-a796-206bef2b0a3e",
                    name="Miss Lori Sawayn",
                ),
                total_amount=173.42,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="0e9aac2e-9135-4586-918f-9f97a4bfad2b",
                            name="Erik Stehr",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="quo",
                        id="a84ad99b-41d6-4124-b531-870cf68b03ad",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="1bd43d1f-0cb0-4a00-83eb-22d9b3a70d94",
                        name="Grant Oberbrunner",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="c57d1fed-c205-40d3-8dc3-ce185472f9ee",
                        name="Natasha Boyer",
                    ),
                ],
                unit_amount=6250.09,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="8be3444e-ac8b-43a2-875c-6c1fe606d07d",
                    name="Joanna Mueller",
                ),
                description="nihil",
                discount_amount=6406.81,
                discount_percentage=9201.94,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="50c16661-a1d9-4136-a7e8-d53213f3f658",
                    name="Lynn Considine",
                ),
                quantity=4758.59,
                sub_total=4218.34,
                tax_amount=3058.33,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8030.15,
                    id="59f0a56c-ebca-4da2-9ca7-9181c9567166",
                    name="Brooke Hand MD",
                ),
                total_amount=3255.27,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="65163a36-3851-42ab-a521-b9f2e072467b",
                            name="Miss Homer Gislason",
                        ),
                        shared.TrackingCategoryRef(
                            id="05fab0d6-50ed-4f22-a94d-20ec90ea41d1",
                            name="Leroy Huels",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="praesentium",
                        id="5156fff7-3fdf-454f-9d5e-a9543398dafb",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="a8d63388-e4d8-4039-aa5f-9b18a244fd61",
                        name="Charles Emmerich",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="cd38ed0d-c671-4dc7-b1e3-af15920c90d1",
                        name="Mr. Clifford Morissette",
                    ),
                    shared.TrackingCategoryRef(
                        id="2bd89c8a-3263-49da-9b7b-6902b881a94f",
                        name="Emma Dickinson",
                    ),
                    shared.TrackingCategoryRef(
                        id="4a8f0af8-c691-4d73-ad9f-baf9476a2ae8",
                        name="Benny Ryan DDS",
                    ),
                ],
                unit_amount=5567.19,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="culpa",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="nostrum",
                    currency_rate=1196.85,
                    total_amount=1793.01,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="c7378489-3075-40a0-8e96-6ec736d43194",
                        name="Belinda Lockman",
                    ),
                    currency="atque",
                    currency_rate=2239.23,
                    id="c92398ed-3d3a-4b7c-a3c5-ca8649a70cfd",
                    note="veniam",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="pariatur",
                    total_amount=4175.19,
                ),
            ),
        ],
        remaining_credit=6115.25,
        source_modified_date="2022-10-23T00:00:00Z",
        status="Paid",
        sub_total=6125.84,
        supplemental_data=shared.SupplementalData(
            content={
                "in": {
                    "voluptatem": "voluptas",
                },
                "magnam": {
                    "quae": "ipsa",
                    "iure": "voluptate",
                },
                "illum": {
                    "perspiciatis": "accusamus",
                },
            },
        ),
        total_amount=6755.33,
        total_discount=5296.77,
        total_tax_amount=1880.08,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2619.53,
                name="Russell Weber II",
            ),
            shared.WithholdingTaxitems(
                amount=7320.16,
                name="Blake Connelly V",
            ),
            shared.WithholdingTaxitems(
                amount=3475.83,
                name="Lynn Hahn",
            ),
            shared.WithholdingTaxitems(
                amount=6009.33,
                name="Veronica Schultz",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    credit_note_id="et",
    force_update=False,
    timeout_in_minutes=510079,
)

res = s.credit_notes.update_credit_note(req)

if res.update_credit_note_response is not None:
    # handle response
```