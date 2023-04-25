# credit_notes

## Overview

Credit notes

### Available Operations

* [create_credit_note](#create_credit_note) - Create credit note
* [get_create_update_credit_notes_model](#get_create_update_credit_notes_model) - Get create/update credit note model
* [get_credit_note](#get_credit_note) - Get credit note
* [list_credit_notes](#list_credit_notes) - List credit notes
* [update_credit_note](#update_credit_note) - Update creditNote

## create_credit_note

Push credit note


Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating a credit note.

### Example Usage

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
        additional_tax_amount=8282.67,
        additional_tax_percentage=4716.93,
        allocated_on_date="sed",
        credit_note_number="optio",
        currency="nulla",
        currency_rate=1664.81,
        customer_ref=shared.CustomerRef(
            company_name="modi",
            id="84da2172-9f2a-4c41-af57-25f1169ac1e4",
        ),
        discount_percentage=1100.31,
        id="d8a23c23-e34f-42df-a4a1-97f6de922151",
        issue_date="delectus",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="17120998-53e9-4f54-bd85-4439ee224460",
                    name="Alicia Ebert",
                ),
                description="architecto",
                discount_amount=3290.16,
                discount_percentage=2991.66,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="188c2f56-e85d-4a78-b2ea-bd617c3b0d51",
                    name="Jim Grady",
                ),
                quantity=220.18,
                sub_total=1013.18,
                tax_amount=7340.76,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6450.47,
                    id="d8706d46-082b-4fbd-841f-f5d4e2ae4fb5",
                    name="Andres Fay",
                ),
                total_amount=1049.9,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="638f1edb-7835-49ec-85cb-860f8cd580ba",
                            name="Mr. Emily Macejkovic",
                        ),
                        shared.TrackingCategoryRef(
                            id="4fe44472-97cd-43b1-9d3b-bce247b7684e",
                            name="Mr. Emmett Heidenreich",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="laboriosam",
                        id="d71cffbd-0eb7-44b8-8219-53b44bd3c431",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="d33e5953-c001-4139-863a-a41e6c31cc2f",
                        name="May Sauer",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="c9a41ffb-e9cb-4d79-9ee6-5e076cc7abf6",
                        name="Jeanette Veum",
                    ),
                ],
                unit_amount=7817.77,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="71641934-b90f-42e0-9d19-d2fc2f9e2e10",
                    name="Daisy Fritsch",
                ),
                description="molestias",
                discount_amount=2261.98,
                discount_percentage=3180.3,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="d237a72f-9084-49d6-aed4-aecb7537cd92",
                    name="Lori Schneider",
                ),
                quantity=9816.77,
                sub_total=3461.64,
                tax_amount=4998.74,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2935.12,
                    id="91aabfa2-e761-4f0c-a4d4-56ef1031e689",
                    name="Terrell Bashirian Jr.",
                ),
                total_amount=557.9,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="e22cd55c-c058-44a1-84d7-6d971fc820c6",
                            name="Maryann Ankunding",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="rerum",
                        id="b8e0cc88-5187-4e4d-a04a-f28c5dddb46a",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="cfd6d828-da01-4319-9129-646645c1d81f",
                        name="Margarita Auer",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="569b7aff-0ea2-4216-8be0-71bc163e279a",
                        name="Kelli Beier",
                    ),
                    shared.TrackingCategoryRef(
                        id="da99257d-04f4-4084-ba74-2d84496cbdee",
                        name="Dominick Jakubowski",
                    ),
                    shared.TrackingCategoryRef(
                        id="9bc63562-ebfd-4f55-8294-c060b06a1287",
                        name="Stacey Fritsch",
                    ),
                    shared.TrackingCategoryRef(
                        id="f6d0c6d6-ed9c-473d-9634-571509a8e870",
                        name="Jeff Schimmel",
                    ),
                ],
                unit_amount=1021.82,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="f9c242c7-b66a-41f3-8c73-df5b6719890f",
                    name="Andrea Orn",
                ),
                description="expedita",
                discount_amount=2678.39,
                discount_percentage=2398.58,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="8d85b260-591d-4745-a3c2-059c9c3f567e",
                    name="Kellie Cormier",
                ),
                quantity=4884.47,
                sub_total=3792.36,
                tax_amount=3395.03,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7473.58,
                    id="1d62fcda-ce1f-4012-96ce-2239e8f25cd0",
                    name="Dennis Moen",
                ),
                total_amount=3460.81,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="f439e392-66cb-4d95-b7aa-2b24113695d1",
                            name="Charlie Jacobs",
                        ),
                        shared.TrackingCategoryRef(
                            id="fcc45962-17c2-4977-a763-34254038bfb5",
                            name="Clinton Bosco",
                        ),
                        shared.TrackingCategoryRef(
                            id="81905573-89ce-4dba-87fd-a39594d66bc2",
                            name="Erick Haag III",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="dolorem",
                        id="2b9954b6-fa22-4063-a982-8553cb10006b",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="4921ec20-53b7-4493-a6ac-8ee0f2bf1958",
                        name="Dr. Irving Gislason I",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="3deba297-be3e-490b-840d-f868fd52405c",
                        name="Dr. Rodney Dooley",
                    ),
                    shared.TrackingCategoryRef(
                        id="92f4f127-fb0e-40bf-9f82-17978d0acca7",
                        name="Iris VonRueden",
                    ),
                    shared.TrackingCategoryRef(
                        id="b7021a52-046b-464e-99fb-0e67e094fdfe",
                        name="Dustin Heidenreich DVM",
                    ),
                    shared.TrackingCategoryRef(
                        id="f53a34a1-b8fe-4997-b1ad-c05d85ae2dfb",
                        name="Lisa Wuckert",
                    ),
                ],
                unit_amount=5618.25,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="74290d33-6561-4eca-96ef-89451bd76eee",
                    name="Maurice Boehm",
                ),
                description="modi",
                discount_amount=8226.31,
                discount_percentage=6266.37,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="1fad3551-2f06-4d4e-9b72-f0f548568a04",
                    name="Mr. Lucille Weber",
                ),
                quantity=1009.76,
                sub_total=8459.84,
                tax_amount=4206.47,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9162.43,
                    id="b9434645-d030-484f-bba5-cceff5cb01fe",
                    name="Joyce Torp",
                ),
                total_amount=5425.06,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="45ac82b8-5f8b-4c2c-aba8-da4127dd597f",
                            name="Mr. Ray Koch",
                        ),
                        shared.TrackingCategoryRef(
                            id="a1bc74b8-6cec-4c74-b77b-4848bd6a6f04",
                            name="Diane Stokes",
                        ),
                        shared.TrackingCategoryRef(
                            id="3b808094-373e-4060-859b-ebbad02f2586",
                            name="Mrs. Forrest Wilkinson",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="exercitationem",
                        id="58daa95b-e6cd-4027-96c3-54aa432b47e1",
                    ),
                    is_billed_to="NotApplicable",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="3c5208c2-3e98-402d-82f0-d45eb4a8b674",
                        name="Clay Hintz",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="18edc7f7-87e3-42e0-8b3d-3ed0c5670ef4",
                        name="Maryann Stark",
                    ),
                    shared.TrackingCategoryRef(
                        id="9f1cc503-f6c3-49bc-90a6-290f957f3851",
                        name="Luther Nader",
                    ),
                    shared.TrackingCategoryRef(
                        id="ef807aae-03f3-43ca-b9fb-9de4032ba26f",
                        name="Jimmy Keebler",
                    ),
                    shared.TrackingCategoryRef(
                        id="a9216bcb-4158-435c-b364-1723133edc04",
                        name="Luz Schmidt III",
                    ),
                ],
                unit_amount=2277.13,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="facilis",
        note="libero",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="deserunt",
                    currency="eius",
                    currency_rate=5630.24,
                    total_amount=1737.52,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="27c42c22-c553-4504-95c5-dbb3c57c1e49",
                        name="Jack Ward",
                    ),
                    currency="similique",
                    currency_rate=1847.97,
                    id="57ddc191-2ebd-4e64-bfcc-5469d4015dfa",
                    note="esse",
                    paid_on_date="iste",
                    reference="ex",
                    total_amount=1421.73,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="voluptatem",
                    currency="voluptas",
                    currency_rate=7288.49,
                    total_amount=8766.36,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="f2b0a3e4-2c1a-4a01-8e9a-ac2e9135586d",
                        name="Billie Windler",
                    ),
                    currency="sint",
                    currency_rate=4450.02,
                    id="a4bfad2b-f7d6-47ca-84ad-99b41d612435",
                    note="nesciunt",
                    paid_on_date="sunt",
                    reference="blanditiis",
                    total_amount=4643.01,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="perferendis",
                    currency="cumque",
                    currency_rate=9639.68,
                    total_amount=4071.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="8b03ad42-1bd4-43d1-b0cb-0a0003eb22d9",
                        name="Leonard Padberg PhD",
                    ),
                    currency="excepturi",
                    currency_rate=3025.96,
                    id="faa741c5-7d1f-4edc-a050-d38dc3ce1854",
                    note="iusto",
                    paid_on_date="sunt",
                    reference="tenetur",
                    total_amount=5799.52,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="necessitatibus",
                    currency="necessitatibus",
                    currency_rate=4230.32,
                    total_amount=6203.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="166a8be3-444e-4ac8-b3a2-875c6c1fe606",
                        name="James Klocko",
                    ),
                    currency="deserunt",
                    currency_rate=6229.89,
                    id="c87ae50c-1666-41a1-9913-6a7e8d53213f",
                    note="velit",
                    paid_on_date="asperiores",
                    reference="commodi",
                    total_amount=3744.95,
                ),
            ),
        ],
        remaining_credit=5538.05,
        source_modified_date="esse",
        status="Draft",
        sub_total=1453.33,
        supplemental_data=shared.SupplementalData(
            content={
                "expedita": {
                    "autem": "aliquam",
                    "maxime": "nostrum",
                },
                "occaecati": {
                    "doloremque": "id",
                    "veniam": "ea",
                    "placeat": "necessitatibus",
                    "harum": "cumque",
                },
                "culpa": {
                    "laborum": "consequuntur",
                    "omnis": "maxime",
                    "officia": "iusto",
                    "natus": "ab",
                },
                "deleniti": {
                    "eligendi": "sint",
                },
            },
        ),
        total_amount=3694.92,
        total_discount=3887.15,
        total_tax_amount=4752.38,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4014.49,
                name="Dawn Schiller",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=55015,
)

res = s.credit_notes.create_credit_note(req)

if res.create_credit_note_response is not None:
    # handle response
```

## get_create_update_credit_notes_model

Get create/update credit note model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating and updating a credit note.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateCreditNotesModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.credit_notes.get_create_update_credit_notes_model(req)

if res.push_option is not None:
    # handle response
```

## get_credit_note

Gets a single creditNote corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreditNoteRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    credit_note_id="nam",
)

res = s.credit_notes.get_credit_note(req)

if res.credit_note is not None:
    # handle response
```

## list_credit_notes

Gets a list of all credit notes for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListCreditNotesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="minima",
)

res = s.credit_notes.list_credit_notes(req)

if res.credit_notes is not None:
    # handle response
```

## update_credit_note

Posts an updated credit note to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support updating a credit note.

### Example Usage

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
        additional_tax_amount=4263.08,
        additional_tax_percentage=3905.83,
        allocated_on_date="minima",
        credit_note_number="et",
        currency="autem",
        currency_rate=2204.55,
        customer_ref=shared.CustomerRef(
            company_name="culpa",
            id="3638512a-b252-41b9-b2e0-72467b8a40bc",
        ),
        discount_percentage=240.78,
        id="5fab0d65-0edf-422a-94d2-0ec90ea41d1f",
        issue_date="labore",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="5e85156f-ff73-4fdf-94fd-d5ea9543398d",
                    name="Timmy Robel",
                ),
                description="dolorum",
                discount_amount=5358.88,
                discount_percentage=8253.69,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="63388e4d-8039-4ea5-b9b1-8a244fd61903",
                    name="Drew Padberg",
                ),
                quantity=2456.35,
                sub_total=5302.25,
                tax_amount=9110.49,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8423.7,
                    id="0dc671dc-7f1e-43af-9592-0c90d1b4901f",
                    name="Opal Sporer",
                ),
                total_amount=8051.67,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="a32639da-5b7b-4690-ab88-1a94f643664a",
                            name="Irvin Baumbach",
                        ),
                        shared.TrackingCategoryRef(
                            id="8c691d73-2d9f-4baf-9476-a2ae8dcc50c8",
                            name="Mr. Jeffery Hegmann",
                        ),
                        shared.TrackingCategoryRef(
                            id="73784893-0750-4a00-a966-ec736d431943",
                            name="Sidney Ruecker",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="dolor",
                        id="c92398ed-3d3a-4b7c-a3c5-ca8649a70cfd",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="6989b720-6451-4077-919e-a83d492ed14b",
                        name="Blake Connelly V",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="4545e955-dcc1-485e-a490-1c7c43ad2daa",
                        name="Christy Gorczany",
                    ),
                    shared.TrackingCategoryRef(
                        id="a3d230ed-f738-411a-9153-82bd7ed56507",
                        name="Judy Bogan",
                    ),
                ],
                unit_amount=5330.96,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="f4d73965-64c2-40a0-b11a-961d24a7dbb8",
                    name="Bill Frami",
                ),
                description="atque",
                discount_amount=5968.02,
                discount_percentage=1421.56,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="cf7812cb-512c-4878-a40b-f548f88f8f1b",
                    name="James Reynolds",
                ),
                quantity=8881.27,
                sub_total=1202.57,
                tax_amount=9822.77,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1756.76,
                    id="06d5d831-d008-4109-8f67-06673f3a681c",
                    name="Nellie Kerluke",
                ),
                total_amount=7742.94,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="742409a2-15e0-4860-9489-a5f63e3af3dd",
                            name="Marty Spencer",
                        ),
                        shared.TrackingCategoryRef(
                            id="3dcd6348-3e4a-47a9-8e4d-f37e45b8955d",
                            name="Gloria Emard I",
                        ),
                        shared.TrackingCategoryRef(
                            id="a4823109-07bd-4354-8092-bd734f02449d",
                            name="Cecil Wintheiser",
                        ),
                        shared.TrackingCategoryRef(
                            id="b20fe5d9-11cb-4fe7-89ca-f45a27f69e2c",
                            name="Merle Keebler Jr.",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="debitis",
                        id="9db3ad4c-6b03-4108-99c3-37473082b94f",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="b1fd5671-e9c3-4263-90a4-67143789ce0e",
                        name="Evan Buckridge",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="d93a74c0-252f-4e3b-8b4d-b8b778ebb6e1",
                        name="Brandon Rutherford",
                    ),
                    shared.TrackingCategoryRef(
                        id="02bafb2c-bc46-435d-9e65-da028c3e951a",
                        name="Dr. Leigh Dickens",
                    ),
                ],
                unit_amount=6458.29,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="sint",
        note="eum",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="magnam",
                    currency="rem",
                    currency_rate=5808.35,
                    total_amount=8240.62,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="7b78673e-13a1-42a6-b992-494594487f5c",
                        name="Mario Fay",
                    ),
                    currency="ex",
                    currency_rate=7339.99,
                    id="86b3cdf6-415b-4044-9f9d-f13f4eedbe78",
                    note="tempore",
                    paid_on_date="reiciendis",
                    reference="commodi",
                    total_amount=261.97,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="ea",
                    currency="molestias",
                    currency_rate=1564.16,
                    total_amount=3730.95,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="894ea763-d5c7-4279-9b78-5148d6d549e5",
                        name="Kim Hegmann",
                    ),
                    currency="dolorem",
                    currency_rate=7110.04,
                    id="c0f970c4-2fc9-4f48-8422-5e75b796065c",
                    note="eaque",
                    paid_on_date="earum",
                    reference="earum",
                    total_amount=6367.75,
                ),
            ),
        ],
        remaining_credit=4254.84,
        source_modified_date="sapiente",
        status="Paid",
        sub_total=1904.44,
        supplemental_data=shared.SupplementalData(
            content={
                "molestias": {
                    "fuga": "beatae",
                },
                "distinctio": {
                    "eligendi": "unde",
                    "veniam": "nam",
                    "accusamus": "vitae",
                },
                "explicabo": {
                    "incidunt": "soluta",
                    "nihil": "adipisci",
                },
            },
        ),
        total_amount=5919.98,
        total_discount=9674.76,
        total_tax_amount=2952.84,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9078.26,
                name="Mr. Maureen Christiansen",
            ),
            shared.WithholdingTaxitems(
                amount=1182.21,
                name="Hector Hegmann",
            ),
            shared.WithholdingTaxitems(
                amount=7728.04,
                name="Marshall Schmitt",
            ),
            shared.WithholdingTaxitems(
                amount=1411.42,
                name="Billy Reichert DVM",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    credit_note_id="excepturi",
    force_update=False,
    timeout_in_minutes=256890,
)

res = s.credit_notes.update_credit_note(req)

if res.update_credit_note_response is not None:
    # handle response
```
