# bill_credit_notes

## Overview

Bill credit notes

### Available Operations

* [create](#create) - Create bill credit note
* [get](#get) - Get bill credit note
* [get_create_update_model](#get_create_update_model) - Get create/update bill credit note model
* [list](#list) - List bill credit notes
* [update](#update) - Update bill credit note

## create

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
        allocated_on_date="ipsum",
        bill_credit_note_number="91fe2a83-e161-4c21-929d-c5c10c4b07e5",
        currency="quidem",
        currency_rate=5651.89,
        discount_percentage=5666.02,
        id="1509398f-98e2-436d-8a5d-c042e0c74ffc",
        issue_date="pariatur",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="88e1e91e-450a-4d2a-bd44-269802d502a9",
                    name="Olivia Rice",
                ),
                description="eum",
                discount_amount=2487.53,
                discount_percentage=7561.07,
                item_ref=shared.ItemRef(
                    id="969e9a3e-fa77-4dfb-94cd-66ae395efb9b",
                    name="Nelson Lesch",
                ),
                quantity=6439.9,
                sub_total=3948.69,
                tax_amount=4238.55,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6188.09,
                    id="97074ba4-469b-46e2-9419-59890afa563e",
                    name="Vivian Boyle",
                ),
                total_amount=8919.24,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="c8b711e5-b7fd-42ed-8289-21cddc692601",
                            name="Rickey Hintz",
                        ),
                        shared.TrackingCategoryRef(
                            id="b0d5f0d3-0c5f-4bb2-9870-53202c73d5fe",
                            name="Miss Cesar Metz",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="blanditiis",
                        id="909b3fe4-9a8d-49cb-b486-33323f9b77f3",
                    ),
                    is_billed_to="Customer",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="100674eb-f692-480d-9ba7-7a89ebf737ae",
                        name="Judy Aufderhar",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="5e6a95d8-a0d4-446c-a2af-7a73cf3be453",
                        name="Miss Jimmie Kozey",
                    ),
                    shared.TrackingCategoryRef(
                        id="26b5a734-29cd-4b1a-8422-bb679d232271",
                        name="Miss Candice Weimann",
                    ),
                    shared.TrackingCategoryRef(
                        id="b1e31b8b-90f3-4443-a110-8e0adcf4b921",
                        name="Darren McClure",
                    ),
                    shared.TrackingCategoryRef(
                        id="e953f73e-f7fb-4c7a-bd74-dd39c0f5d2cf",
                        name="Ted Romaguera MD",
                    ),
                ],
                unit_amount=2694.79,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="5626d436-813f-416d-9f5f-ce6c556146c3",
                    name="Dr. Bruce Hane",
                ),
                description="aut",
                discount_amount=114.27,
                discount_percentage=5334.66,
                item_ref=shared.ItemRef(
                    id="c42e141a-ac36-46c8-9d6b-144290747477",
                    name="Blake Kihn",
                ),
                quantity=2835.19,
                sub_total=4334.39,
                tax_amount=3799.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8268.71,
                    id="28c10ab3-cdca-4425-9904-e523c7e0bc71",
                    name="Christy Tillman",
                ),
                total_amount=5775.43,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="f2a70c68-8282-4aa4-8256-2f222e9817ee",
                            name="Joy Schmidt",
                        ),
                        shared.TrackingCategoryRef(
                            id="61e6b7b9-5bc0-4ab3-820c-4f3789fd871f",
                            name="Kirk Stracke",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="eveniet",
                        id="fd121aa6-f1e6-474b-9b04-f15756082d68",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Customer",
                    project_ref=shared.ProjectRef(
                        id="19f1d170-5133-49d0-8086-a1840394c260",
                        name="Jean Wunsch",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="5f0642da-c7af-4515-8c41-3aa63aae8d67",
                        name="Cecil Grant",
                    ),
                    shared.TrackingCategoryRef(
                        id="b675fd5e-60b3-475e-94f6-fbee41f33317",
                        name="Doyle Feest",
                    ),
                    shared.TrackingCategoryRef(
                        id="60eb1ea4-2655-45ba-bc28-744ed53b88f3",
                        name="Byron Stroman",
                    ),
                    shared.TrackingCategoryRef(
                        id="5c0b2f2f-b7b1-494a-a76b-26916fe1f08f",
                        name="Tammy Medhurst",
                    ),
                ],
                unit_amount=2155.29,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="ea",
        note="Bill Credit Note with 1 line items, totaling 805.78",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="quos",
                    currency="voluptatibus",
                    currency_rate=2716.53,
                    total_amount=2730.09,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7f603e8b-445e-480c-a55e-fd20e457e185",
                        name="Bennie Howe",
                    ),
                    currency="error",
                    currency_rate=9447.08,
                    id="be3a5aa8-e482-44d0-ab40-75088e518620",
                    note="vel",
                    paid_on_date="nostrum",
                    reference="saepe",
                    total_amount=6222.31,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="consequatur",
                    currency="incidunt",
                    currency_rate=9688.65,
                    total_amount=2097.5,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="b1194b8a-bf60-43a7-9f9d-fe0ab7da8a50",
                        name="Phil Boyer",
                    ),
                    currency="asperiores",
                    currency_rate=5199.52,
                    id="6bc173d6-89ee-4e95-a6f8-d986e881ead4",
                    note="reiciendis",
                    paid_on_date="doloremque",
                    reference="repudiandae",
                    total_amount=1160.98,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="accusantium",
                    currency="beatae",
                    currency_rate=1747.72,
                    total_amount=3164.88,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="63f94e29-e973-4e92-aa57-a15be3e06080",
                        name="Tricia Denesik",
                    ),
                    currency="necessitatibus",
                    currency_rate=1875.52,
                    id="ab8845f0-597a-460f-b2a5-4a31e94764a3",
                    note="debitis",
                    paid_on_date="laudantium",
                    reference="eum",
                    total_amount=3679.27,
                ),
            ),
        ],
        remaining_credit=9282.19,
        source_modified_date="esse",
        status="Paid",
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "quis": {
                    "reiciendis": "provident",
                    "aspernatur": "ullam",
                },
                "quasi": {
                    "nostrum": "mollitia",
                    "provident": "possimus",
                    "animi": "ex",
                },
                "aliquid": {
                    "repellat": "doloribus",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="57bfaad4-f9ef-4c1b-8512-c1032648dc2f",
            supplier_name="eum",
        ),
        total_amount=805.78,
        total_discount=1173.2,
        total_tax_amount=3251.18,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5834.04,
                name="Darin Rodriguez",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=52508,
)

res = s.bill_credit_notes.create(req)

if res.create_bill_credit_note_response is not None:
    # handle response
```

## get

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
    bill_credit_note_id="earum",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.bill_credit_notes.get(req)

if res.bill_credit_note is not None:
    # handle response
```

## get_create_update_model

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

res = s.bill_credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

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
    query="perspiciatis",
)

res = s.bill_credit_notes.list(req)

if res.bill_credit_notes is not None:
    # handle response
```

## update

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
        allocated_on_date="maiores",
        bill_credit_note_number="91fe2a83-e161-4c21-929d-c5c10c4b07e5",
        currency="debitis",
        currency_rate=3998.02,
        discount_percentage=7809.31,
        id="1509398f-98e2-436d-8a5d-c042e0c74ffc",
        issue_date="suscipit",
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="2ca3aed0-1179-4963-92fd-e04771778ff6",
                    name="Ms. Janis Batz",
                ),
                description="esse",
                discount_amount=4037.93,
                discount_percentage=2352.63,
                item_ref=shared.ItemRef(
                    id="60a15db6-a660-4659-a1ad-eaab5851d6c6",
                    name="Ms. Geraldine Ratke",
                ),
                quantity=3996.6,
                sub_total=1097.84,
                tax_amount=5308.6,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6063.08,
                    id="1baa0fe1-ade0-408e-af8c-5f350d8cdb5a",
                    name="Michele Bode II",
                ),
                total_amount=2213.96,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="10421813-d520-48ec-a7e2-53b668451c6c",
                            name="Mrs. Kate Cronin",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="quasi",
                        id="6deab3fe-c957-48a6-8584-273a8418d162",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="9fb09299-21ae-4fb9-b58c-4d86e68e4be0",
                        name="Mrs. Gina Abbott",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="9da757a5-9ecf-4ef6-aef1-caa3383c2beb",
                        name="Glenda Kling",
                    ),
                    shared.TrackingCategoryRef(
                        id="3c8d72f6-4d1d-4b1f-ac43-10661e96349e",
                        name="Pat Wolf",
                    ),
                ],
                unit_amount=26.77,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="nisi",
        note="Bill Credit Note with 1 line items, totaling 805.78",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="velit",
                    currency="laborum",
                    currency_rate=2503.98,
                    total_amount=2244.67,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7000ae6b-6bc9-4b8f-b59e-ac55a9741d31",
                        name="Florence Hand",
                    ),
                    currency="ex",
                    currency_rate=3676.26,
                    id="bb8a7202-6114-435e-939d-bc2259b1abda",
                    note="quos",
                    paid_on_date="placeat",
                    reference="sit",
                    total_amount=4793.85,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="ipsa",
                    currency="voluptates",
                    currency_rate=800.61,
                    total_amount=493.48,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="84cb0672-d1ad-4879-aeb9-665b85efbd02",
                        name="Miss Grant VonRueden",
                    ),
                    currency="eos",
                    currency_rate=8448.54,
                    id="782259e3-ea4b-4519-bf92-443da7ce52b8",
                    note="cupiditate",
                    paid_on_date="minima",
                    reference="placeat",
                    total_amount=3165.42,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="neque",
                    currency="in",
                    currency_rate=7963.97,
                    total_amount=4330.77,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="454efb0b-3489-46c3-8a5a-cfbe2fd57075",
                        name="Dora Mante",
                    ),
                    currency="veritatis",
                    currency_rate=4981.8,
                    id="7deac646-ecb5-4734-89e3-eb1e5a2b12eb",
                    note="ipsa",
                    paid_on_date="ducimus",
                    reference="maiores",
                    total_amount=873.82,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="quasi",
                    currency="laboriosam",
                    currency_rate=8634.71,
                    total_amount=7294.48,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="99545fc9-5fa8-4897-8e18-9dbb30fcb33e",
                        name="Anthony Hayes",
                    ),
                    currency="architecto",
                    currency_rate=5845.93,
                    id="7cd44e2f-52d8-42d3-913b-b6f48b656bcd",
                    note="facilis",
                    paid_on_date="ipsum",
                    reference="ad",
                    total_amount=9738.19,
                ),
            ),
        ],
        remaining_credit=9745.89,
        source_modified_date="consequuntur",
        status="Paid",
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "labore": {
                    "eos": "reprehenderit",
                    "nostrum": "neque",
                    "iusto": "est",
                },
                "rem": {
                    "fugiat": "unde",
                    "officiis": "ducimus",
                    "dolor": "dicta",
                    "error": "porro",
                },
                "vitae": {
                    "esse": "fugiat",
                    "ad": "aspernatur",
                },
                "enim": {
                    "iusto": "dignissimos",
                    "libero": "illo",
                    "ab": "incidunt",
                    "accusamus": "saepe",
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id="b52ff785-fc37-4814-94c9-8e0c2bb89eb7",
            supplier_name="corporis",
        ),
        total_amount=805.78,
        total_discount=8738.33,
        total_tax_amount=6293.77,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4348.27,
                name="Gertrude Russel Jr.",
            ),
            shared.WithholdingTaxitems(
                amount=3228.29,
                name="Wendy Stanton",
            ),
            shared.WithholdingTaxitems(
                amount=7368.53,
                name="Joyce Carroll DVM",
            ),
            shared.WithholdingTaxitems(
                amount=4797.07,
                name="Shelly Pagac",
            ),
        ],
    ),
    bill_credit_note_id="repudiandae",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    timeout_in_minutes=10063,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
