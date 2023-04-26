# credit_notes

## Overview

Credit notes

### Available Operations

* [create](#create) - Create credit note
* [get](#get) - Get credit note
* [get_create_update_model](#get_create_update_model) - Get create/update credit note model
* [list](#list) - List credit notes
* [update](#update) - Update creditNote

## create

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
        additional_tax_amount=4618.53,
        additional_tax_percentage=5345.09,
        allocated_on_date="rem",
        credit_note_number="vel",
        currency="eos",
        currency_rate=2864.64,
        customer_ref=shared.CustomerRef(
            company_name="sunt",
            id="89eb4487-3f50-433f-99db-f125ce4152ea",
        ),
        discount_percentage=7125.23,
        id="9cd7e522-4a6a-40e1-a3b7-847ec59e1f67",
        issue_date="repellat",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="c4cce4b6-d769-46ff-bc57-47501357e44f",
                    name="Jean Welch",
                ),
                description="consequatur",
                discount_amount=5167.39,
                discount_percentage=2725.18,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="c3197e19-3a24-4546-bf94-874c2d5cc497",
                    name="Norma Feest",
                ),
                quantity=4358.41,
                sub_total=3961.88,
                tax_amount=7385.92,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8537.01,
                    id="8fe5d00b-979e-4f20-b873-20590ccc1096",
                    name="Sarah Bartell I",
                ),
                total_amount=6992.15,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="e5044f65-fe72-4dc4-877d-0cc3f408efc1",
                            name="Pat Upton",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="illum",
                        id="6e1eae0f-75ae-4df2-acab-58b991c926dd",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="89461e74-21cb-4e6d-9502-f0ea930b69f7",
                        name="Spencer Crooks",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="f8850090-4911-4608-a078-88ec66183bfe",
                        name="Ricardo Hermiston",
                    ),
                ],
                unit_amount=6946.11,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="magnam",
        note="doloremque",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="quod",
                    currency="sunt",
                    currency_rate=3774.3,
                    total_amount=9382.3,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="af75b0b5-32a4-4da3-bcba-af4452c4842c",
                        name="Garry Conn",
                    ),
                    currency="ipsum",
                    currency_rate=1292.7,
                    id="dafe81a8-8f44-4445-b3fe-cd47353f63c8",
                    note="sed",
                    paid_on_date="eaque",
                    reference="natus",
                    total_amount=1912.02,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="nihil",
                    currency="unde",
                    currency_rate=6463.21,
                    total_amount=6621.84,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="69cd5fbc-f79d-4a18-a782-2bf95894e686",
                        name="Lynda Schuppe",
                    ),
                    currency="quaerat",
                    currency_rate=9830.67,
                    id="9e5d751c-9fe8-4f75-82bf-dc3450841f17",
                    note="autem",
                    paid_on_date="dolore",
                    reference="eius",
                    total_amount=3423.93,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="ex",
                    currency="amet",
                    currency_rate=4543.86,
                    total_amount=5653.04,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="f3fb27e2-1f86-4265-bb36-fc6b9f587ce5",
                        name="Audrey Schimmel",
                    ),
                    currency="ea",
                    currency_rate=2569.41,
                    id="1a8312e5-047b-44c2-9ccb-423abcdc91fa",
                    note="est",
                    paid_on_date="distinctio",
                    reference="fugiat",
                    total_amount=8621.67,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="totam",
                    currency="praesentium",
                    currency_rate=8857.21,
                    total_amount=4610.94,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="1f6c4825-2d77-471e-bfd0-74009ef8d29d",
                        name="Raymond Schulist",
                    ),
                    currency="aut",
                    currency_rate=5912.2,
                    id="7b5da08c-57fa-46c7-8a21-6e19bafeca61",
                    note="cupiditate",
                    paid_on_date="veritatis",
                    reference="aliquam",
                    total_amount=5682.31,
                ),
            ),
        ],
        remaining_credit=5410.46,
        source_modified_date="dicta",
        status="Draft",
        sub_total=428.84,
        supplemental_data=shared.SupplementalData(
            content={
                "suscipit": {
                    "maiores": "delectus",
                    "quos": "id",
                },
                "officiis": {
                    "voluptate": "consequatur",
                },
                "itaque": {
                    "voluptatem": "dolor",
                    "distinctio": "quaerat",
                    "a": "neque",
                    "nihil": "recusandae",
                },
            },
        ),
        total_amount=2538.55,
        total_discount=6520.13,
        total_tax_amount=6515.04,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=3819.74,
                name="Tim Hamill",
            ),
            shared.WithholdingTaxitems(
                amount=4116.69,
                name="Maureen Dooley",
            ),
            shared.WithholdingTaxitems(
                amount=6762.74,
                name="Mona Schaden",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=419585,
)

res = s.credit_notes.create(req)

if res.create_credit_note_response is not None:
    # handle response
```

## get

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
    credit_note_id="praesentium",
)

res = s.credit_notes.get(req)

if res.credit_note is not None:
    # handle response
```

## get_create_update_model

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

res = s.credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

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
    query="magni",
)

res = s.credit_notes.list(req)

if res.credit_notes is not None:
    # handle response
```

## update

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
        additional_tax_amount=7874.67,
        additional_tax_percentage=7118.19,
        allocated_on_date="in",
        credit_note_number="eaque",
        currency="delectus",
        currency_rate=5019.46,
        customer_ref=shared.CustomerRef(
            company_name="minus",
            id="fd5fb6e9-1b9a-49f7-8846-e2c3309db053",
        ),
        discount_percentage=4343.82,
        id="d9e75ca0-06f5-4392-811a-25a8bf92f974",
        issue_date="aspernatur",
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="ad9a9f8b-f822-4112-9359-d98387f7a79c",
                    name="Christian Corwin",
                ),
                description="magni",
                discount_amount=2657.08,
                discount_percentage=5319.67,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="4da21729-f2ac-441e-b572-5f1169ac1e41",
                    name="Wallace Oberbrunner",
                ),
                quantity=7720.48,
                sub_total=1609.09,
                tax_amount=2042.92,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9044.85,
                    id="34f2dfa4-a197-4f6d-a922-151fe1712099",
                    name="Ronnie Donnelly",
                ),
                total_amount=9711.55,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="43d85443-9ee2-4244-a044-3bc154188c2f",
                            name="Kristin Tillman",
                        ),
                        shared.TrackingCategoryRef(
                            id="da7832ea-bd61-47c3-b0d5-1a44bf01bad8",
                            name="Patricia Kerluke",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="ea",
                        id="082bfbdc-41ff-45d4-a2ae-4fb5cb35d176",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="NotApplicable",
                    project_ref=shared.ProjectRef(
                        id="f1edb783-59ec-4c5c-b860-f8cd580ba738",
                        name="Kimberly Waters",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="4447297c-d3b1-4dd3-bbce-247b7684eff5",
                        name="Teresa Denesik",
                    ),
                    shared.TrackingCategoryRef(
                        id="71cffbd0-eb74-4b84-a195-3b44bd3c4315",
                        name="Sammy Fisher",
                    ),
                    shared.TrackingCategoryRef(
                        id="5953c001-1398-463a-a41e-6c31cc2f1fcb",
                        name="Joan Schaefer",
                    ),
                    shared.TrackingCategoryRef(
                        id="41ffbe9c-bd79-45ee-a5e0-76cc7abf616e",
                        name="Vernon Sauer III",
                    ),
                ],
                unit_amount=2640.9,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="1934b90f-2e09-4d19-92fc-2f9e2e105944",
                    name="Virgil Fahey",
                ),
                description="sed",
                discount_amount=2405.55,
                discount_percentage=4444.94,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="a72f9084-9d6a-4ed4-aecb-7537cd9222c9",
                    name="Elijah Hegmann",
                ),
                quantity=6152.06,
                sub_total=817.75,
                tax_amount=6258.15,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6644.91,
                    id="bfa2e761-f0ca-44d4-96ef-1031e6899f0c",
                    name="Dr. Sharon Bednar",
                ),
                total_amount=1347.95,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="d55cc058-4a18-44d7-ad97-1fc820c65b03",
                            name="Luz Rau",
                        ),
                        shared.TrackingCategoryRef(
                            id="0cc88518-7e4d-4e04-af28-c5dddb46aa1c",
                            name="Clint Jast",
                        ),
                        shared.TrackingCategoryRef(
                            id="28da0131-9112-4964-a645-c1d81f29042f",
                            name="Vanessa Monahan",
                        ),
                        shared.TrackingCategoryRef(
                            id="aff0ea22-16cb-4e07-9bc1-63e279a3b084",
                            name="Lorenzo Monahan",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="veniam",
                        id="7d04f408-47a7-442d-8449-6cbdeecf6b99",
                    ),
                    is_billed_to="Project",
                    is_rebilled_to="Project",
                    project_ref=shared.ProjectRef(
                        id="63562ebf-df55-4c29-8c06-0b06a1287764",
                        name="Darrel Wehner",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="c6d6ed9c-73dd-4634-9715-09a8e870d3c5",
                        name="Juan Wolff",
                    ),
                ],
                unit_amount=1690.72,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id="42c7b66a-1f30-4c73-9f5b-6719890f42a4",
                    name="Malcolm Gleichner",
                ),
                description="at",
                discount_amount=5236.07,
                discount_percentage=3465.34,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id="b260591d-745e-43c2-859c-9c3f567e0e25",
                    name="Courtney Hoeger",
                ),
                quantity=1074.24,
                sub_total=8313.04,
                tax_amount=4021.21,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1628.49,
                    id="fcdace1f-0121-46ce-a239-e8f25cd0d19d",
                    name="Greg Mayer",
                ),
                total_amount=2363.72,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id="e39266cb-d95f-47aa-ab24-113695d1e669",
                            name="Jerald Schowalter",
                        ),
                        shared.TrackingCategoryRef(
                            id="596217c2-9776-4763-b425-4038bfb5971e",
                            name="Casey Block II",
                        ),
                        shared.TrackingCategoryRef(
                            id="57389ced-bac7-4fda-b959-4d66bc2ae480",
                            name="Dawn Cole",
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name="occaecati",
                        id="54b6fa22-0636-4982-8553-cb10006bef49",
                    ),
                    is_billed_to="Unknown",
                    is_rebilled_to="Unknown",
                    project_ref=shared.ProjectRef(
                        id="ec2053b7-4936-46ac-8ee0-f2bf19588d40",
                        name="Richard Dietrich",
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id="eba297be-3e90-4bc4-8df8-68fd52405cb3",
                        name="Evelyn Stracke",
                    ),
                    shared.TrackingCategoryRef(
                        id="2f4f127f-b0e0-4bf1-b821-7978d0acca77",
                        name="Phil Rice",
                    ),
                    shared.TrackingCategoryRef(
                        id="7021a520-46b6-44e9-9fb0-e67e094fdfed",
                        name="Dr. Yvonne Grimes",
                    ),
                    shared.TrackingCategoryRef(
                        id="53a34a1b-8fe9-4973-9adc-05d85ae2dfb7",
                        name="Shawna Pouros",
                    ),
                ],
                unit_amount=4837.74,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="non",
        note="magni",
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="consequatur",
                    currency="illum",
                    currency_rate=2378.75,
                    total_amount=2106.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="6561eca1-6ef8-4945-9bd7-6eeeb518c4da",
                        name="Ollie Osinski",
                    ),
                    currency="nemo",
                    currency_rate=3353.52,
                    id="12f06d4e-5b72-4f0f-9485-68a0424e00a1",
                    note="quibusdam",
                    paid_on_date="autem",
                    reference="voluptates",
                    total_amount=7314.5,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="cupiditate",
                    currency="modi",
                    currency_rate=1916.53,
                    total_amount=3059.65,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="645d0308-4fbb-4a5c-8eff-5cb01fe51e52",
                        name="Lyle Gislason",
                    ),
                    currency="minus",
                    currency_rate=5544.29,
                    id="2b85f8bc-2cab-4a8d-a412-7dd597ff4711",
                    note="similique",
                    paid_on_date="id",
                    reference="et",
                    total_amount=7167.79,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date="porro",
                    currency="nihil",
                    currency_rate=2567.42,
                    total_amount=7030.15,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id="86cecc74-f77b-4484-8bd6-a6f0441d2c3b",
                        name="Ms. Daniel Langworth",
                    ),
                    currency="nesciunt",
                    currency_rate=4744.53,
                    id="3e060459-bebb-4ad0-af25-86bcf152558d",
                    note="fuga",
                    paid_on_date="fuga",
                    reference="excepturi",
                    total_amount=3583.94,
                ),
            ),
        ],
        remaining_credit=7230.31,
        source_modified_date="itaque",
        status="Submitted",
        sub_total=7837.02,
        supplemental_data=shared.SupplementalData(
            content={
                "consequatur": {
                    "in": "enim",
                },
                "vel": {
                    "consectetur": "quis",
                    "ut": "est",
                    "fuga": "labore",
                    "adipisci": "ratione",
                },
                "cum": {
                    "nihil": "officiis",
                    "inventore": "esse",
                },
                "ex": {
                    "minus": "ad",
                },
            },
        ),
        total_amount=1292.57,
        total_discount=27.7,
        total_tax_amount=5026.86,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=1863.18,
                name="Kate Metz Sr.",
            ),
            shared.WithholdingTaxitems(
                amount=8344.99,
                name="Dr. Sean Williamson",
            ),
            shared.WithholdingTaxitems(
                amount=3401.07,
                name="Gerardo Gislason",
            ),
            shared.WithholdingTaxitems(
                amount=7482.66,
                name="Glenda Grimes",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    credit_note_id="ipsam",
    force_update=False,
    timeout_in_minutes=788995,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```
