# create_credit_note
Available in: `credit_notes`

Push credit note


Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating a credit note.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=4884.33,
        additional_tax_percentage=3427.72,
        allocated_on_date="2022-10-23T00:00:00Z",
        credit_note_number="maiores",
        currency="veritatis",
        currency_rate=4226.1,
        customer_ref=shared.CustomerRef(
            company_name="earum",
            id="56d385a3-c4ac-4631-b99e-26ced8f9fdb9",
        ),
        discount_percentage=2913.44,
        id="10f63bbf-8178-437b-81af-dd788624189e",
        issue_date="2022-10-23T00:00:00Z",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="44873f50-33f1-49db-b125-ce4152eab9cd",
                    name="Sonja Hansen",
                ),
                description="eius",
                discount_amount=6253.78,
                discount_percentage=4274.61,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="a0e123b7-847e-4c59-a1f6-7f3c4cce4b6d",
                    name="Vicki Mayer",
                ),
                quantity=9570.32,
                sub_total=2322.09,
                tax_amount=7574.94,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3534.24,
                    id="74750135-7e44-4f51-b8b0-84c3197e193a",
                    name="Eva Hettinger",
                ),
                total_amount=4990.05,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="94874c2d-5cc4-4972-a33e-66bd8fe5d00b",
                            name="Darren Monahan",
                        ),
                        shared.TrackingCategoryRef(
                            id="20387320-590c-4cc1-8964-00313b3e5044",
                            name="Gene Herman",
                        ),
                        shared.TrackingCategoryRef(
                            id="72dc4077-d0cc-43f4-88ef-c15ceb4d6e1e",
                            name="Alonzo Bartell",
                        ),
                        shared.TrackingCategoryRef(
                            id="5aedf2ac-ab58-4b99-9c92-6ddb589461e7",
                            name="Beverly Block",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="recusandae",
                        id="6d9502f0-ea93-40b6-9f7a-c2f72f885009",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="91160820-7888-4ec6-a183-bfe9659eb40e",
                        name="Willie Hodkiewicz",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="75b0b532-a4da-437c-baaf-4452c4842c9b",
                        name="Jodi Stroman",
                    ),
                    shared.TrackingCategoryRef(
                        id="dafe81a8-8f44-4445-b3fe-cd47353f63c8",
                        name="Cynthia Morissette",
                    ),
                    shared.TrackingCategoryRef(
                        id="9aa69cd5-fbcf-479d-a18a-7822bf95894e",
                        name="Miss Maxine Kemmer",
                    ),
                    shared.TrackingCategoryRef(
                        id="b55f9e5d-751c-49fe-8f75-02bfdc345084",
                        name="Josefina Borer",
                    ),
                ],
                unit_amount=2943.14,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="456379f3-fb27-4e21-b862-657b36fc6b9f",
                    name="Nina Kshlerin",
                ),
                description="ad",
                discount_amount=1676.13,
                discount_percentage=3457.46,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="c67641a8-312e-4504-bb4c-21ccb423abcd",
                    name="Arturo Bosco",
                ),
                quantity=6654.27,
                sub_total=7160.24,
                tax_amount=8546.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8621.67,
                    id="88e71f6c-4825-42d7-b71e-7fd074009ef8",
                    name="Carlos Morissette",
                ),
                total_amount=717.41,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="d7097b5d-a08c-457f-a6c7-8a216e19bafe",
                            name="Ms. Gerard Hudson II",
                        ),
                        shared.TrackingCategoryRef(
                            id="98140b64-ff8a-4e17-8ef0-3b5f37e4aa86",
                            name="Tim Hamill",
                        ),
                        shared.TrackingCategoryRef(
                            id="66732aa5-dcb6-4682-8b70-f8cfd5fb6e91",
                            name="Alejandro Pacocha",
                        ),
                        shared.TrackingCategoryRef(
                            id="74846e2c-3309-4db0-936d-9e75ca006f53",
                            name="Mr. Jeremy Sanford",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="quia",
                        id="5a8bf92f-9742-48ad-9a9f-8bf822112535",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="98387f7a-79cd-472c-9248-4da21729f2ac",
                        name="Amanda Tromp",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="25f1169a-c1e4-41d8-a23c-23e34f2dfa4a",
                        name="Claire Koepp",
                    ),
                    shared.TrackingCategoryRef(
                        id="de922151-fe17-4120-9985-3e9f543d8544",
                        name="Katrina Thompson",
                    ),
                ],
                unit_amount=1351.1,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="4460443b-c154-4188-82f5-6e85da7832ea",
                    name="Ms. Ismael Hodkiewicz",
                ),
                description="nesciunt",
                discount_amount=6902.11,
                discount_percentage=454.45,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="d51a44bf-01ba-4d87-86d4-6082bfbdc41f",
                    name="Maurice Strosin",
                ),
                quantity=1528.07,
                sub_total=6511.36,
                tax_amount=9016.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2893.73,
                    id="fb5cb35d-1763-48f1-adb7-8359ecc5cb86",
                    name="Marta Macejkovic",
                ),
                total_amount=3563.51,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="0ba73810-e4fe-4444-b297-cd3b1dd3bbce",
                            name="Debbie Kozey",
                        ),
                        shared.TrackingCategoryRef(
                            id="684eff50-126d-471c-bfbd-0eb74b842195",
                            name="Melody Grady",
                        ),
                        shared.TrackingCategoryRef(
                            id="d3c43159-d33e-4595-bc00-1139863aa41e",
                            name="Dr. Kara Feil",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="explicabo",
                        id="f1fcb51c-9a41-4ffb-a9cb-d795ee65e076",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="7abf616e-a5c7-4164-9934-b90f2e09d19d",
                        name="Dr. Lorene Runte",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="2e105944-b935-4d23-ba72-f90849d6aed4",
                        name="Ramiro Rowe",
                    ),
                    shared.TrackingCategoryRef(
                        id="537cd922-2c9f-4f57-891a-abfa2e761f0c",
                        name="Troy Stroman",
                    ),
                    shared.TrackingCategoryRef(
                        id="6ef1031e-6899-4f0c-a001-e22cd55cc058",
                        name="Hattie Botsford",
                    ),
                    shared.TrackingCategoryRef(
                        id="d76d971f-c820-4c65-b037-bb8e0cc88518",
                        name="Rochelle Grant",
                    ),
                ],
                unit_amount=96.87,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        note="ut",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="hic",
                    currency_rate=1531.31,
                    total_amount=5461.33,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="c5dddb46-aa1c-4fd6-9828-da0131911296",
                        name="Beth Keeling",
                    ),
                    currency="cumque",
                    currency_rate=701.73,
                    id="d81f2904-2f56-49b7-aff0-ea2216cbe071",
                    note="harum",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="cumque",
                    total_amount=697.88,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="ex",
                    currency_rate=2198.04,
                    total_amount=8847.04,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="279a3b08-4da9-4925-bd04-f40847a742d8",
                        name="Charlotte McGlynn",
                    ),
                    currency="tempore",
                    currency_rate=8142.92,
                    id="eecf6b99-bc63-4562-abfd-f55c294c060b",
                    note="accusantium",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="ea",
                    total_amount=6715.04,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="2022-10-23T00:00:00Z",
                    currency="et",
                    currency_rate=1448.56,
                    total_amount=5505.79,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7764eef6-d0c6-4d6e-99c7-3dd634571509",
                        name="Nelson Walker",
                    ),
                    currency="doloremque",
                    currency_rate=8440.94,
                    id="3c5a1f9c-242c-47b6-aa1f-30c73df5b671",
                    note="excepturi",
                    paid_on_date="2022-10-23T00:00:00Z",
                    reference="voluptatum",
                    total_amount=6108.73,
                ),
            ),
        ],
        remaining_credit=509.03,
        source_modified_date="2022-10-23T00:00:00Z",
        status="PartiallyPaid",
        sub_total=3021.47,
        supplemental_data=shared.SupplementalData(
            content={
                "est": {
                    "nobis": "expedita",
                    "modi": "adipisci",
                },
            },
        ),
        total_amount=5401.92,
        total_discount=8712.98,
        total_tax_amount=5236.07,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=7311.86,
                name="Vanessa Beahan",
            ),
            shared.WithholdingTaxitems(
                amount=1195.43,
                name="Ron Goodwin",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=195946,
)

res = s.credit_notes.create_credit_note(req)

if res.create_credit_note_response is not None:
    # handle response
```