# bill_credit_notes

## Overview

Bill credit notes

### Available Operations

* [create_bill_credit_note](#create_bill_credit_note) - Create bill credit note
* [get_bill_credit_note](#get_bill_credit_note) - Get bill credit note
* [get_create_update_bill_credit_notes_model](#get_create_update_bill_credit_notes_model) - Get create/update bill credit note model
* [list_bill_credit_notes](#list_bill_credit_notes) - List bill credit notes
* [update_bill_credit_note](#update_bill_credit_note) - Update bill credit note

## create_bill_credit_note

Posts a new billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating bill credit notes.

### Example Usage

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
        allocated_on_date="facilis",
        bill_credit_note_number="tempore",
        currency="labore",
        currency_rate=9621.89,
        discount_percentage=4332.88,
        id="3c969e9a-3efa-477d-bb14-cd66ae395efb",
        issue_date="provident",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="a88f3a66-9970-474b-a446-9b6e21419598",
                    name="Kenneth O'Hara",
                ),
                description="ad",
                discount_amount=4314.18,
                discount_percentage=2212.62,
                item_ref=shared.ItemRef(
                    id="e2516fe4-c8b7-411e-9b7f-d2ed028921cd",
                    name="Simon Jenkins",
                ),
                quantity=4071.83,
                sub_total=332.22,
                tax_amount=691.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9825.75,
                    id="b576b0d5-f0d3-40c5-bbb2-587053202c73",
                    name="Dean Welch",
                ),
                total_amount=7044.15,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="0c28909b-3fe4-49a8-99cb-f48633323f9b",
                            name="Marian Wisozk",
                        ),
                        shared.TrackingCategoryRef(
                            id="4100674e-bf69-4280-91ba-77a89ebf737a",
                            name="Mrs. Ray Collins",
                        ),
                        shared.TrackingCategoryRef(
                            id="e5e6a95d-8a0d-4446-8e2a-f7a73cf3be45",
                            name="Jeannie Leannon MD",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="neque",
                        id="26b5a734-29cd-4b1a-8422-bb679d232271",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="f0cbb1e3-1b8b-490f-b443-a1108e0adcf4",
                        name="Ms. Terrance Davis",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="fce953f7-3ef7-4fbc-babd-74dd39c0f5d2",
                        name="Elijah Wyman",
                    ),
                    shared.TrackingCategoryRef(
                        id="70a45626-d436-4813-b16d-9f5fce6c5561",
                        name="Rosemary Ryan",
                    ),
                    shared.TrackingCategoryRef(
                        id="250fb008-c42e-4141-aac3-66c8dd6b1442",
                        name="Jose Kreiger",
                    ),
                ],
                unit_amount=2621.18,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="778a7bd4-66d2-48c1-8ab3-cdca4251904e",
                    name="Kelly Donnelly",
                ),
                description="recusandae",
                discount_amount=446.12,
                discount_percentage=7151.79,
                item_ref=shared.ItemRef(
                    id="c7178e47-96f2-4a70-8688-282aa482562f",
                    name="Norma Christiansen",
                ),
                quantity=5438.06,
                sub_total=922.6,
                tax_amount=4569.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9105.45,
                    id="e17cbe61-e6b7-4b95-bc0a-b3c20c4f3789",
                    name="Ismael Lynch DVM",
                ),
                total_amount=6216.79,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="dd2efd12-1aa6-4f1e-a74b-db04f1575608",
                            name="Rosemarie Jacobs",
                        ),
                        shared.TrackingCategoryRef(
                            id="a19f1d17-0513-439d-8808-6a1840394c26",
                            name="Marian Buckridge",
                        ),
                        shared.TrackingCategoryRef(
                            id="3f5f0642-dac7-4af5-95cc-413aa63aae8d",
                            name="Dora Luettgen",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="possimus",
                        id="bb675fd5-e60b-4375-ad4f-6fbee41f3331",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="e35b60eb-1ea4-4265-95ba-3c28744ed53b",
                        name="Morris Weissnat",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="d8f5c0b2-f2fb-47b1-94a2-76b26916fe1f",
                        name="Naomi Wuckert",
                    ),
                    shared.TrackingCategoryRef(
                        id="94e3698f-447f-4603-a8b4-45e80ca55efd",
                        name="Deborah Turcotte",
                    ),
                    shared.TrackingCategoryRef(
                        id="7e1858b6-a89f-4be3-a5aa-8e4824d0ab40",
                        name="Brittany Bailey",
                    ),
                ],
                unit_amount=9221.12,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="51862065-e904-4f3b-9194-b8abf603a79f",
                    name="Marcos Windler MD",
                ),
                description="quidem",
                discount_amount=4406.66,
                discount_percentage=8136.79,
                item_ref=shared.ItemRef(
                    id="a8a50ce1-87f8-46bc-973d-689eee9526f8",
                    name="Jeremiah Kuvalis",
                ),
                quantity=5421.29,
                sub_total=5413.81,
                tax_amount=1209.19,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9233.06,
                    id="ad4f0e10-1256-43f9-8e29-e973e922a57a",
                    name="Ana Predovic",
                ),
                total_amount=8784.93,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="60807e2b-6e3a-4b88-85f0-597a60ff2a54",
                            name="Danny Berge",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="quaerat",
                        id="764a3e86-5e79-456f-9251-a5a9da660ff5",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="faad4f9e-fc1b-4451-ac10-32648dc2f615",
                        name="Misty McKenzie",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="d0e9fe6c-632c-4a3a-ad01-17996312fde0",
                        name="Ms. Marcia Kozey",
                    ),
                    shared.TrackingCategoryRef(
                        id="8ff61d01-7476-4360-a15d-b6a660659a1a",
                        name="Pat O'Keefe",
                    ),
                    shared.TrackingCategoryRef(
                        id="5851d6c6-45b0-48b6-9891-baa0fe1ade00",
                        name="Darin Jakubowski",
                    ),
                    shared.TrackingCategoryRef(
                        id="c5f350d8-cdb5-4a34-9814-3010421813d5",
                        name="Cynthia Macejkovic",
                    ),
                ],
                unit_amount=8849.52,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="esse",
        note="necessitatibus",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="veniam",
                    currency="nesciunt",
                    currency_rate=7129.27,
                    total_amount=4329.84,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="68451c6c-6e20-45e1-adea-b3fec9578a64",
                        name="Brandy Gibson",
                    ),
                    currency="nesciunt",
                    currency_rate=6817.4,
                    id="8418d162-309f-4b09-a992-1aefb9f58c4d",
                    note="quos",
                    paid_on_date="commodi",
                    reference="itaque",
                    total_amount=4156.08,
                ),
            ),
        ],
        remaining_credit=5207.61,
        source_modified_date="earum",
        status="Draft",
        sub_total=7221.84,
        supplemental_data=shared.SupplementalData(
            content={
                "voluptatem": {
                    "vel": "alias",
                    "quasi": "non",
                },
                "maiores": {
                    "sint": "nulla",
                    "deserunt": "esse",
                },
                "nemo": {
                    "est": "quis",
                    "sint": "accusamus",
                },
                "impedit": {
                    "necessitatibus": "asperiores",
                    "ex": "voluptas",
                    "debitis": "delectus",
                    "quae": "minus",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="aa3383c2-beb4-4773-b3c8-d72f64d1db1f",
            supplier_name="quia",
        ),
        total_amount=7820.9,
        total_discount=3041.98,
        total_tax_amount=2470.45,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=365.61,
                name="Rosemary Breitenberg",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=431994,
)

res = s.bill_credit_notes.create_bill_credit_note(req)

if res.create_bill_credit_note_response is not None:
    # handle response
```

## get_bill_credit_note

Gets a single billCreditNote corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id="velit",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_credit_notes.get_bill_credit_note(req)

if res.bill_credit_note is not None:
    # handle response
```

## get_create_update_bill_credit_notes_model

Get create/update bill credit note model.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating bill credit notes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateBillCreditNotesModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.bill_credit_notes.get_create_update_bill_credit_notes_model(req)

if res.push_option is not None:
    # handle response
```

## list_bill_credit_notes

Gets a list of all bill credit notes for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBillCreditNotesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="ut",
)

res = s.bill_credit_notes.list_bill_credit_notes(req)

if res.bill_credit_notes is not None:
    # handle response
```

## update_bill_credit_note

Posts an updated billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support updating bill credit notes.

### Example Usage

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
        allocated_on_date="perspiciatis",
        bill_credit_note_number="earum",
        currency="dicta",
        currency_rate=7722.66,
        discount_percentage=9758.84,
        id="9e06e3a4-3700-40ae-ab6b-c9b8f759eac5",
        issue_date="corporis",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="9741d311-3529-465b-b8a7-202611435e13",
                    name="Orville Ratke",
                ),
                description="quia",
                discount_amount=3421.37,
                discount_percentage=6057.12,
                item_ref=shared.ItemRef(
                    id="b1abda8c-070e-4108-8cb0-672d1ad879ee",
                    name="Kirk Jast",
                ),
                quantity=7029.52,
                sub_total=5156.38,
                tax_amount=3572.07,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8890.6,
                    id="fbd02bae-0be2-4d78-a259-e3ea4b5197f9",
                    name="Elaine Gerhold",
                ),
                total_amount=6378.56,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="ce52b895-c537-4c64-94ef-b0b34896c3ca",
                            name="Jodi Russel",
                        ),
                        shared.TrackingCategoryRef(
                            id="e2fd5707-5779-4291-b7de-ac646ecb5734",
                            name="Bobbie Terry",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="cum",
                        id="1e5a2b12-eb07-4f11-adb9-9545fc95fa88",
                    ),
                    is_billed_to="Customer",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="0e189dbb-30fc-4b33-aa05-5b197cd44e2f",
                        name="Louise Schulist",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="3513bb6f-48b6-456b-8db3-5ff2e4b27537",
                        name="Jordan Romaguera",
                    ),
                    shared.TrackingCategoryRef(
                        id="e7319c17-7d52-45f7-bb11-4eeb52ff785f",
                        name="Jimmy Konopelski II",
                    ),
                    shared.TrackingCategoryRef(
                        id="d4c98e0c-2bb8-49eb-b5da-d636c600503d",
                        name="Willis Rippin Sr.",
                    ),
                    shared.TrackingCategoryRef(
                        id="80f739ae-9e05-47eb-809e-2810331f3981",
                        name="Leroy Schinner Jr.",
                    ),
                ],
                unit_amount=6985.58,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="607f3c93-c73b-49da-bf2c-eda7e23f2257",
                    name="Virginia Bins",
                ),
                description="delectus",
                discount_amount=2512.12,
                discount_percentage=7193.89,
                item_ref=shared.ItemRef(
                    id="7544e472-e802-4857-a5b4-0463a7d575f1",
                    name="Maria Ankunding",
                ),
                quantity=4137.58,
                sub_total=2561.14,
                tax_amount=6770.45,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8237.18,
                    id="7334ec1b-781b-436a-8808-8d100efada20",
                    name="Mrs. Olive Weissnat",
                ),
                total_amount=1858.97,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="b2164cf9-ab83-466c-b23f-fda9e06bee48",
                            name="Dr. Marion Schaefer",
                        ),
                        shared.TrackingCategoryRef(
                            id="0e115c80-bff9-4185-84ec-42defcce8f19",
                            name="Joy Kessler",
                        ),
                        shared.TrackingCategoryRef(
                            id="e63562a7-b408-4f05-a3d4-8fdaf313a1f5",
                            name="Woodrow Mitchell III",
                        ),
                        shared.TrackingCategoryRef(
                            id="9c0b36f2-5ea9-444f-bb75-6c11f6c37a51",
                            name="Beth Cummerata",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="praesentium",
                        id="35bbc05a-23a4-45ce-bc5f-de10a0ce2169",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="10019c6d-c5e3-4476-a799-bfbbe6949fb2",
                        name="Alton Goyette",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="e6c3d5db-3ade-4bd5-9aea-4c506a8aa94c",
                        name="Theresa Jacobi",
                    ),
                    shared.TrackingCategoryRef(
                        id="cf5e9d9a-4578-4adc-9ac6-00dec001ac80",
                        name="Rochelle Cormier",
                    ),
                    shared.TrackingCategoryRef(
                        id="09ff8f0f-816f-4f34-b7c1-3e902c14125b",
                        name="Miss Isabel Kassulke",
                    ),
                ],
                unit_amount=4016.88,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="8151a472-af92-43c5-949f-83f350cf876f",
                    name="Mr. Robin Miller",
                ),
                description="commodi",
                discount_amount=9087.34,
                discount_percentage=7815.82,
                item_ref=shared.ItemRef(
                    id="bb4e243c-f789-4ffa-beda-53e5ae6e0ac1",
                    name="Frederick Schaden",
                ),
                quantity=6200.54,
                sub_total=7935.68,
                tax_amount=1543.89,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3006.51,
                    id="7c88373a-40e1-4942-b32e-55055756f5d5",
                    name="Meredith Bailey",
                ),
                total_amount=177.68,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="f2dfe13d-b4f6-42cb-a3f8-941aebc0b80a",
                            name="Velma Cummings",
                        ),
                        shared.TrackingCategoryRef(
                            id="3b2ecfcc-8f89-4501-8f5d-d3d6fa1804e5",
                            name="Rosalie Lynch",
                        ),
                        shared.TrackingCategoryRef(
                            id="168a363c-8873-4e48-8380-b1f6b8ca275a",
                            name="Mrs. Mary Pfannerstill",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="aliquam",
                        id="95cc6991-71b5-41c1-bdb1-cf4b888ebdfc",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="cca99bc7-fc0b-42dc-a108-73e42b006d67",
                        name="Guy Kovacek",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="8581a582-08c5-44fe-ba9c-95f2eac5565d",
                        name="Nancy Kuhlman",
                    ),
                    shared.TrackingCategoryRef(
                        id="ee81206e-2813-4fa4-a41c-480d3f2132af",
                        name="Mr. Connie Brakus",
                    ),
                    shared.TrackingCategoryRef(
                        id="514f4cc6-f18b-4f96-a1a6-a4f77a87ee3e",
                        name="Susie Ward",
                    ),
                ],
                unit_amount=1316.87,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="impedit",
        note="aliquid",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="facilis",
                    currency="ipsum",
                    currency_rate=2848.85,
                    total_amount=3088.19,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="18e3bb91-c8d9-475e-8e84-19d8f84f144f",
                        name="Kerry Altenwerth",
                    ),
                    currency="facere",
                    currency_rate=7890.16,
                    id="c4aa5f3c-abd9-405a-972e-056728227b2d",
                    note="nesciunt",
                    paid_on_date="ipsa",
                    reference="sint",
                    total_amount=2913.89,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="esse",
                    currency="accusantium",
                    currency_rate=7181.19,
                    total_amount=9565.45,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7a4fa87c-f535-4a6f-ae54-ebf60c321f02",
                        name="Luz King",
                    ),
                    currency="ratione",
                    currency_rate=2218.24,
                    id="67fe1a0c-c8df-479f-8a39-6d90c364b7c1",
                    note="enim",
                    paid_on_date="nulla",
                    reference="maiores",
                    total_amount=7156.22,
                ),
            ),
        ],
        remaining_credit=6496.57,
        source_modified_date="impedit",
        status="PartiallyPaid",
        sub_total=911.2,
        supplemental_data=shared.SupplementalData(
            content={
                "blanditiis": {
                    "dicta": "impedit",
                    "tempora": "eveniet",
                    "repudiandae": "sed",
                },
                "impedit": {
                    "impedit": "vel",
                    "eligendi": "recusandae",
                    "ex": "beatae",
                },
                "veritatis": {
                    "itaque": "vero",
                    "quidem": "illo",
                    "quo": "dignissimos",
                    "minus": "distinctio",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="db6eec74-378b-4a25-b177-47dc915ad2ca",
            supplier_name="repellat",
        ),
        total_amount=3419.83,
        total_discount=8473.08,
        total_tax_amount=8450.86,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4563.71,
                name="Edith Spencer DVM",
            ),
            shared.WithholdingTaxitems(
                amount=3502.71,
                name="Phil Collier",
            ),
        ],
    ),
    bill_credit_note_id="officia",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=379661,
)

res = s.bill_credit_notes.update_bill_credit_note(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
