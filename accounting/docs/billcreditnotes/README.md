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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='molestias',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='excepturi',
        currency_rate=8651.03,
        discount_percentage=2653.89,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='praesentium',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='e1e91e45-0ad2-4abd-8426-9802d502a94b',
                    name='Francisco Windler',
                ),
                description='eligendi',
                discount_amount=5761.57,
                discount_percentage=3960.98,
                item_ref=shared.ItemRef(
                    id='9e9a3efa-77df-4b14-8d66-ae395efb9ba8',
                    name='Timmy Feeney',
                ),
                quantity=4238.55,
                sub_total=6188.09,
                tax_amount=6063.93,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4748.67,
                    id='074ba446-9b6e-4214-9959-890afa563e25',
                    name='Vera Wyman',
                ),
                total_amount=8061.94,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b711e5b7-fd2e-4d02-8921-cddc692601fb',
                            name='Colleen Johnston PhD',
                        ),
                        shared.TrackingCategoryRef(
                            id='5f0d30c5-fbb2-4587-8532-02c73d5fe9b9',
                            name='Robyn Cruickshank',
                        ),
                        shared.TrackingCategoryRef(
                            id='09b3fe49-a8d9-4cbf-8863-3323f9b77f3a',
                            name='Ms. Christine Beer',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quaerat',
                        id='ebf69280-d1ba-477a-89eb-f737ae4203ce',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='6a95d8a0-d446-4ce2-af7a-73cf3be453f8',
                        name='Karen Rath',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='b5a73429-cdb1-4a84-a2bb-679d2322715b',
                        name='George Runolfsdottir',
                    ),
                    shared.TrackingCategoryRef(
                        id='1e31b8b9-0f34-443a-9108-e0adcf4b9218',
                        name='Toni Wolff',
                    ),
                ],
                unit_amount=6064.76,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='53f73ef7-fbc7-4abd-b4dd-39c0f5d2cff7',
                    name='Kurt Abernathy',
                ),
                description='ipsam',
                discount_amount=4104.92,
                discount_percentage=1369,
                item_ref=shared.ItemRef(
                    id='6d436813-f16d-49f5-bce6-c556146c3e25',
                    name='Mr. Elsa Reinger',
                ),
                quantity=7705.81,
                sub_total=3045.82,
                tax_amount=1469.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8828.6,
                    id='141aac36-6c8d-4d6b-9442-907474778a7b',
                    name='Bernard Kerluke',
                ),
                total_amount=1811.51,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c10ab3cd-ca42-4519-84e5-23c7e0bc7178',
                            name='Tom Kuhn',
                        ),
                        shared.TrackingCategoryRef(
                            id='f2a70c68-8282-4aa4-8256-2f222e9817ee',
                            name='Joy Schmidt',
                        ),
                        shared.TrackingCategoryRef(
                            id='61e6b7b9-5bc0-4ab3-820c-4f3789fd871f',
                            name='Kirk Stracke',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eveniet',
                        id='fd121aa6-f1e6-474b-9b04-f15756082d68',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='19f1d170-5133-49d0-8086-a1840394c260',
                        name='Jean Wunsch',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5f0642da-c7af-4515-8c41-3aa63aae8d67',
                        name='Cecil Grant',
                    ),
                    shared.TrackingCategoryRef(
                        id='b675fd5e-60b3-475e-94f6-fbee41f33317',
                        name='Doyle Feest',
                    ),
                    shared.TrackingCategoryRef(
                        id='60eb1ea4-2655-45ba-bc28-744ed53b88f3',
                        name='Byron Stroman',
                    ),
                    shared.TrackingCategoryRef(
                        id='5c0b2f2f-b7b1-494a-a76b-26916fe1f08f',
                        name='Tammy Medhurst',
                    ),
                ],
                unit_amount=2155.29,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='698f447f-603e-48b4-85e8-0ca55efd20e4',
                    name='Ms. Pearl Towne',
                ),
                description='praesentium',
                discount_amount=7400.98,
                discount_percentage=3868.27,
                item_ref=shared.ItemRef(
                    id='a89fbe3a-5aa8-4e48-a4d0-ab4075088e51',
                    name='Ms. Ruben Cremin',
                ),
                quantity=9061.72,
                sub_total=6222.31,
                tax_amount=85.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2790.68,
                    id='f3b1194b-8abf-4603-a79f-9dfe0ab7da8a',
                    name='Helen Schiller IV',
                ),
                total_amount=4420.36,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='86bc173d-689e-4ee9-926f-8d986e881ead',
                            name='Lela Baumbach Jr.',
                        ),
                        shared.TrackingCategoryRef(
                            id='12563f94-e29e-4973-a922-a57a15be3e06',
                            name='Lena Beier',
                        ),
                        shared.TrackingCategoryRef(
                            id='2b6e3ab8-845f-4059-ba60-ff2a54a31e94',
                            name='Carla Graham',
                        ),
                        shared.TrackingCategoryRef(
                            id='e865e795-6f92-451a-9a9d-a660ff57bfaa',
                            name='Edwin Wolf',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='sapiente',
                        id='c1b4512c-1032-4648-9c2f-615199ebfd0e',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='e6c632ca-3aed-4011-b996-312fde047717',
                        name='Irma Wuckert',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d0174763-60a1-45db-aa66-0659a1adeaab',
                        name='Dr. Cassandra Halvorson',
                    ),
                ],
                unit_amount=7758.03,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ex',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='ad',
                    currency='expedita',
                    currency_rate=299.5,
                    total_amount=5615.77,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b61891ba-a0fe-41ad-a008-e6f8c5f350d8',
                        name='Taylor Reichel',
                    ),
                    currency='dolor',
                    currency_rate=3073.76,
                    id='18143010-4218-413d-9208-ece7e253b668',
                    note='magnam',
                    paid_on_date='exercitationem',
                    reference='ab',
                    total_amount=7814.8,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='autem',
                    currency='nobis',
                    currency_rate=3883.19,
                    total_amount=9272.12,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='205e16de-ab3f-4ec9-978a-64584273a841',
                        name='Clint Carroll',
                    ),
                    currency='consectetur',
                    currency_rate=468.06,
                    id='9fb09299-21ae-4fb9-b58c-4d86e68e4be0',
                    note='ipsam',
                    paid_on_date='vel',
                    reference='alias',
                    total_amount=938.94,
                ),
            ),
        ],
        remaining_credit=2476.85,
        source_modified_date='maiores',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "sint": {
                    "deserunt": 'esse',
                    "nemo": 'reprehenderit',
                    "est": 'quis',
                    "sint": 'accusamus',
                },
                "impedit": {
                    "necessitatibus": 'asperiores',
                    "ex": 'voluptas',
                    "debitis": 'delectus',
                    "quae": 'minus',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='aa3383c2-beb4-4773-b3c8-d72f64d1db1f',
            supplier_name='quia',
        ),
        total_amount=805.78,
        total_discount=7820.9,
        total_tax_amount=3041.98,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=753.59,
                name='Dr. Gina Jaskolski',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=431994,
)

res = s.bill_credit_notes.create(req)

if res.create_bill_credit_note_response is not None:
    # handle response
```

## get

﻿Gets a single billCreditNote corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id='velit',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bill_credit_notes.get(req)

if res.bill_credit_note is not None:
    # handle response
```

## get_create_update_model

﻿Get create/update bill credit note model.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating and updating bill credit notes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBillCreditNotesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bill_credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets a list of all bill credit notes for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='ut',
)

res = s.bill_credit_notes.list(req)

if res.bill_credit_notes is not None:
    # handle response
```

## update

﻿Posts an updated billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support updating bill credit notes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='perspiciatis',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='earum',
        currency_rate=1175.25,
        discount_percentage=7722.66,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='voluptatibus',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='e06e3a43-7000-4ae6-b6bc-9b8f759eac55',
                    name='Jeremiah Koch PhD',
                ),
                description='consectetur',
                discount_amount=1124.27,
                discount_percentage=813.71,
                item_ref=shared.ItemRef(
                    id='352965bb-8a72-4026-9143-5e139dbc2259',
                    name='Gerald Ondricka',
                ),
                quantity=6374.62,
                sub_total=5546.03,
                tax_amount=8119.39,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=257.56,
                    id='70e1084c-b067-42d1-ad87-9eeb9665b85e',
                    name='Mr. Jonathon Swaniawski',
                ),
                total_amount=6841.26,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='0be2d782-259e-43ea-8b51-97f92443da7c',
                            name='Lewis Denesik',
                        ),
                        shared.TrackingCategoryRef(
                            id='95c537c6-454e-4fb0-b348-96c3ca5acfbe',
                            name='Winifred Streich',
                        ),
                        shared.TrackingCategoryRef(
                            id='07577929-177d-4eac-a46e-cb573409e3eb',
                            name='Lila Harvey',
                        ),
                        shared.TrackingCategoryRef(
                            id='b12eb07f-116d-4b99-945f-c95fa88970e1',
                            name='Nick Shields',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='velit',
                        id='0fcb33ea-055b-4197-8d44-e2f52d82d351',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='b6f48b65-6bcd-4b35-bf2e-4b27537a8cd9',
                        name='Miss Kelly Ernser',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='77d525f7-7b11-44ee-b52f-f785fc37814d',
                        name='Alexandra McLaughlin',
                    ),
                ],
                unit_amount=96.83,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='c2bb89eb-75da-4d63-ac60-0503d8bb3118',
                    name='Lana Kris',
                ),
                description='dolorum',
                discount_amount=8979.56,
                discount_percentage=5928.8,
                item_ref=shared.ItemRef(
                    id='e057eb80-9e28-4103-b1f3-981d4c700b60',
                    name='Kristie Frami',
                ),
                quantity=2313.82,
                sub_total=7532.4,
                tax_amount=4901.1,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2358.34,
                    id='b9da3f2c-eda7-4e23-b225-7411faf4b754',
                    name='Casey Gleason PhD',
                ),
                total_amount=5258.09,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2857a5b4-0463-4a7d-975f-1400e764ad73',
                            name='Bertha Ward MD',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='iusto',
                        id='81b36a08-088d-4100-afad-a200ef0422eb',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='64cf9ab8-366c-4723-bfda-9e06bee4825c',
                        name='Dr. Shari Roob Sr.',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c80bff91-8544-4ec4-adef-cce8f1977773',
                        name='Ben Durgan',
                    ),
                    shared.TrackingCategoryRef(
                        id='2a7b408f-05e3-4d48-bdaf-313a1f5fd942',
                        name='Miss Misty Ruecker',
                    ),
                ],
                unit_amount=4124.33,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='f25ea944-f3b7-456c-91f6-c37a51262438',
                    name='Annette Quitzon',
                ),
                description='sit',
                discount_amount=3634.82,
                discount_percentage=6339.87,
                item_ref=shared.ItemRef(
                    id='23a45cef-c5fd-4e10-a0ce-2169e510019c',
                    name='Doreen Schmeler',
                ),
                quantity=2467.72,
                sub_total=2991.53,
                tax_amount=4935.91,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3884.04,
                    id='2799bfbb-e694-49fb-abb4-ecae6c3d5db3',
                    name='Kristopher Walter',
                ),
                total_amount=3233.65,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='aea4c506-a8aa-494c-8264-4cf5e9d9a457',
                            name='Grant Schultz MD',
                        ),
                        shared.TrackingCategoryRef(
                            id='c600dec0-01ac-4802-a2ec-09ff8f0f816f',
                            name='Lee Gibson',
                        ),
                        shared.TrackingCategoryRef(
                            id='c13e902c-1412-45b0-960a-668151a472af',
                            name='Jeremy Douglas',
                        ),
                        shared.TrackingCategoryRef(
                            id='949f83f3-50cf-4876-bfb9-01c6ecbb4e24',
                            name='Marianne Zemlak',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='sint',
                        id='ffafeda5-3e5a-4e6e-8ac1-84c2b9c247c8',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='73a40e19-42f3-42e5-9055-756f5d56d0bd',
                        name='Amelia Williamson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e13db4f6-2cba-43f8-941a-ebc0b80a6924',
                        name='Rodney Prohaska',
                    ),
                    shared.TrackingCategoryRef(
                        id='cfcc8f89-5010-4f5d-93d6-fa1804e54c82',
                        name='Walter Jacobs',
                    ),
                    shared.TrackingCategoryRef(
                        id='363c8873-e484-4380-b1f6-b8ca275a60a0',
                        name='Jody Gutmann',
                    ),
                    shared.TrackingCategoryRef(
                        id='cc699171-b51c-41bd-b1cf-4b888ebdfc4c',
                        name='Lowell Olson',
                    ),
                ],
                unit_amount=7268.51,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='quo',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='hic',
                    currency='maxime',
                    currency_rate=366.91,
                    total_amount=7435.31,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2dce1087-3e42-4b00-ad67-8878ba8581a5',
                        name='Martin Berge',
                    ),
                    currency='enim',
                    currency_rate=2864.53,
                    id='fefa9c95-f2ea-4c55-a5d3-07cfee81206e',
                    note='sed',
                    paid_on_date='deleniti',
                    reference='sunt',
                    total_amount=2001.9,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='delectus',
                    currency='laborum',
                    currency_rate=3034.21,
                    total_amount=6442.23,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='41c480d3-f213-42af-8310-2d514f4cc6f1',
                        name='Rudolph Welch',
                    ),
                    currency='sed',
                    currency_rate=1066.82,
                    id='a6a4f77a-87ee-43e4-be75-2c65b34418e3',
                    note='expedita',
                    paid_on_date='libero',
                    reference='iste',
                    total_amount=749.21,
                ),
            ),
        ],
        remaining_credit=7924.99,
        source_modified_date='quos',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "sint": {
                    "enim": 'accusamus',
                    "aperiam": 'voluptates',
                },
                "laudantium": {
                    "quae": 'omnis',
                    "illum": 'rem',
                },
                "tenetur": {
                    "modi": 'earum',
                    "architecto": 'aliquam',
                    "labore": 'maiores',
                },
                "sequi": {
                    "consequatur": 'esse',
                    "debitis": 'facere',
                    "quisquam": 'cumque',
                    "aliquam": 'dolorum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='a5f3cabd-905a-4972-a056-728227b2d309',
            supplier_name='dolore',
        ),
        total_amount=805.78,
        total_discount=4570.63,
        total_tax_amount=380.44,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9565.45,
                name='Monique Hackett',
            ),
            shared.WithholdingTaxitems(
                amount=5314.94,
                name='Jody Wolff',
            ),
            shared.WithholdingTaxitems(
                amount=3538.19,
                name='Shane Yundt',
            ),
        ],
    ),
    bill_credit_note_id='corporis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=252567,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
