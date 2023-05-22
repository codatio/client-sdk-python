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

﻿Posts a new billCreditNote to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-billCreditNotes-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billCreditNotes) for integrations that support creating bill credit notes.

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
        allocated_on_date='quae',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='ipsum',
        currency_rate=6924.72,
        discount_percentage=5651.89,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='excepturi',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='488e1e91-e450-4ad2-abd4-4269802d502a',
                    name='Eddie Prosacco',
                ),
                description='delectus',
                discount_amount=4332.88,
                discount_percentage=2487.53,
                item_ref=shared.ItemRef(
                    id='c969e9a3-efa7-47df-b14c-d66ae395efb9',
                    name='Lynn Kuvalis',
                ),
                quantity=2305.33,
                sub_total=6439.9,
                tax_amount=3948.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4238.55,
                    id='997074ba-4469-4b6e-a141-959890afa563',
                    name='Ms. Fred Hilll',
                ),
                total_amount=8919.24,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c8b711e5-b7fd-42ed-8289-21cddc692601',
                            name='Rickey Hintz',
                        ),
                        shared.TrackingCategoryRef(
                            id='b0d5f0d3-0c5f-4bb2-9870-53202c73d5fe',
                            name='Miss Cesar Metz',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='blanditiis',
                        id='909b3fe4-9a8d-49cb-b486-33323f9b77f3',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='100674eb-f692-480d-9ba7-7a89ebf737ae',
                        name='Judy Aufderhar',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5e6a95d8-a0d4-446c-a2af-7a73cf3be453',
                        name='Miss Jimmie Kozey',
                    ),
                    shared.TrackingCategoryRef(
                        id='26b5a734-29cd-4b1a-8422-bb679d232271',
                        name='Miss Candice Weimann',
                    ),
                    shared.TrackingCategoryRef(
                        id='b1e31b8b-90f3-4443-a110-8e0adcf4b921',
                        name='Darren McClure',
                    ),
                    shared.TrackingCategoryRef(
                        id='e953f73e-f7fb-4c7a-bd74-dd39c0f5d2cf',
                        name='Ted Romaguera MD',
                    ),
                ],
                unit_amount=2694.79,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='5626d436-813f-416d-9f5f-ce6c556146c3',
                    name='Dr. Bruce Hane',
                ),
                description='aut',
                discount_amount=114.27,
                discount_percentage=5334.66,
                item_ref=shared.ItemRef(
                    id='c42e141a-ac36-46c8-9d6b-144290747477',
                    name='Blake Kihn',
                ),
                quantity=2835.19,
                sub_total=4334.39,
                tax_amount=3799.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8268.71,
                    id='28c10ab3-cdca-4425-9904-e523c7e0bc71',
                    name='Christy Tillman',
                ),
                total_amount=5775.43,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
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
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='645b08b6-1891-4baa-8fe1-ade008e6f8c5',
                    name='Dr. Chris Hermiston',
                ),
                description='impedit',
                discount_amount=8427.77,
                discount_percentage=7205.28,
                item_ref=shared.ItemRef(
                    id='5a341814-3010-4421-813d-5208ece7e253',
                    name='Andre Kautzer',
                ),
                quantity=3494.4,
                sub_total=704.1,
                tax_amount=7814.8,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4218.44,
                    id='c6e205e1-6dea-4b3f-ac95-78a64584273a',
                    name='Randall Boyle',
                ),
                total_amount=1173.8,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2309fb09-2992-41ae-bb9f-58c4d86e68e4',
                            name='Ignacio Bartoletti',
                        ),
                        shared.TrackingCategoryRef(
                            id='013f59da-757a-459e-8fef-66ef1caa3383',
                            name='Victor Rogahn',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dolore',
                        id='77373c8d-72f6-44d1-9b1f-2c4310661e96',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='9e1cf9e0-6e3a-4437-800a-e6b6bc9b8f75',
                        name='Terence O'Keefe',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a9741d31-1352-4965-bb8a-7202611435e1',
                        name='Lindsay Stiedemann',
                    ),
                    shared.TrackingCategoryRef(
                        id='2259b1ab-da8c-4070-a108-4cb0672d1ad8',
                        name='Daisy Tillman',
                    ),
                ],
                unit_amount=5750.78,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ea',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='ipsam',
                    currency='rerum',
                    currency_rate=5156.38,
                    total_amount=3572.07,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='efbd02ba-e0be-42d7-8225-9e3ea4b5197f',
                        name='Steve Fritsch',
                    ),
                    currency='at',
                    currency_rate=6378.56,
                    id='7ce52b89-5c53-47c6-854e-fb0b34896c3c',
                    note='fuga',
                    paid_on_date='nostrum',
                    reference='est',
                    total_amount=7708.73,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='delectus',
                    currency='tempore',
                    currency_rate=8786.01,
                    total_amount=1415.06,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='fd570757-7929-4177-9eac-646ecb573409',
                        name='Earl VonRueden DVM',
                    ),
                    currency='veniam',
                    currency_rate=6592.68,
                    id='2b12eb07-f116-4db9-9545-fc95fa88970e',
                    note='architecto',
                    paid_on_date='quos',
                    reference='iste',
                    total_amount=8268.62,
                ),
            ),
        ],
        remaining_credit=7316.34,
        source_modified_date='libero',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "doloremque": {
                    "impedit": 'cum',
                    "ipsum": 'adipisci',
                    "saepe": 'deserunt',
                    "doloremque": 'quis',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='5b197cd4-4e2f-452d-82d3-513bb6f48b65',
            supplier_name='nisi',
        ),
        total_amount=805.78,
        total_discount=7277.71,
        total_tax_amount=7945.07,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=7060.61,
                name='Erin Wiza',
            ),
            shared.WithholdingTaxitems(
                amount=8915.81,
                name='Susie Davis',
            ),
            shared.WithholdingTaxitems(
                amount=2072.96,
                name='Genevieve Lebsack',
            ),
            shared.WithholdingTaxitems(
                amount=6040.78,
                name='Miss Kelly Ernser',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=111496,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBillCreditNoteRequest(
    bill_credit_note_id='dignissimos',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBillCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='esse',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateBillCreditNoteRequest(
    bill_credit_note=shared.BillCreditNote(
        allocated_on_date='fugiat',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='ad',
        currency_rate=1348.18,
        discount_percentage=3165.01,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='delectus',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7b114eeb-52ff-4785-bc37-814d4c98e0c2',
                    name='Rudolph Macejkovic',
                ),
                description='rerum',
                discount_amount=4923.61,
                discount_percentage=3609.34,
                item_ref=shared.ItemRef(
                    id='dad636c6-0050-43d8-bb31-180f739ae9e0',
                    name='Nellie Waters',
                ),
                quantity=439.75,
                sub_total=5740.92,
                tax_amount=8795.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1786.35,
                    id='810331f3-981d-44c7-80b6-07f3c93c73b9',
                    name='Luke Fay',
                ),
                total_amount=7782.76,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='da7e23f2-2574-411f-af4b-7544e472e802',
                            name='Bill Kling',
                        ),
                        shared.TrackingCategoryRef(
                            id='b40463a7-d575-4f14-80e7-64ad7334ec1b',
                            name='Tracey Bosco',
                        ),
                        shared.TrackingCategoryRef(
                            id='6a08088d-100e-4fad-a200-ef0422eb2164',
                            name='Courtney Maggio',
                        ),
                        shared.TrackingCategoryRef(
                            id='8366c723-ffda-49e0-abee-4825c1fc0e11',
                            name='Miss Marianne Leffler',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='a',
                        id='918544ec-42de-4fcc-a8f1-977773e63562',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='b408f05e-3d48-4fda-b313-a1f5fd94259c',
                        name='Yvette Dooley',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5ea944f3-b756-4c11-b6c3-7a5126243835',
                        name='Mrs. Johnathan Russel',
                    ),
                ],
                unit_amount=1593.93,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='3a45cefc-5fde-410a-8ce2-169e510019c6',
                    name='Jermaine Hettinger',
                ),
                description='magnam',
                discount_amount=4935.91,
                discount_percentage=3884.04,
                item_ref=shared.ItemRef(
                    id='2799bfbb-e694-49fb-abb4-ecae6c3d5db3',
                    name='Kristopher Walter',
                ),
                quantity=3233.65,
                sub_total=8161.51,
                tax_amount=6746.83,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9114.51,
                    id='a4c506a8-aa94-4c02-a44c-f5e9d9a4578a',
                    name='Edmund Boyle',
                ),
                total_amount=3857.39,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='0dec001a-c802-4e2e-809f-f8f0f816ff34',
                            name='Mrs. Pearl Rosenbaum',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='excepturi',
                        id='02c14125-b096-40a6-a815-1a472af923c5',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='9f83f350-cf87-46ff-b901-c6ecbb4e243c',
                        name='Claude Kutch',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='afeda53e-5ae6-4e0a-8184-c2b9c247c883',
                        name='Grace Padberg PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='1942f32e-5505-4575-af5d-56d0bd0af2df',
                        name='Joe Fisher',
                    ),
                    shared.TrackingCategoryRef(
                        id='4f62cba3-f894-41ae-bc0b-80a6924d3b2e',
                        name='Van Schiller',
                    ),
                    shared.TrackingCategoryRef(
                        id='f895010f-5dd3-4d6f-a180-4e54c82f168a',
                        name='Vicki Feeney',
                    ),
                ],
                unit_amount=5277.15,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ducimus',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='recusandae',
                    currency='tempora',
                    currency_rate=5034.49,
                    total_amount=2580.59,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='380b1f6b-8ca2-475a-a0a0-4c495cc69917',
                        name='Miss Juana Hilpert MD',
                    ),
                    currency='facere',
                    currency_rate=7079.83,
                    id='1cf4b888-ebdf-4c4c-8ca9-9bc7fc0b2dce',
                    note='veritatis',
                    paid_on_date='aut',
                    reference='laudantium',
                    total_amount=4804.21,
                ),
            ),
        ],
        remaining_credit=2198.6,
        source_modified_date='voluptates',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "magni": {
                    "doloremque": 'voluptatem',
                    "eum": 'at',
                    "eum": 'reprehenderit',
                },
                "voluptatum": {
                    "nihil": 'atque',
                    "rerum": 'deserunt',
                    "atque": 'nostrum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='81a58208-c54f-4efa-9c95-f2eac5565d30',
            supplier_name='odio',
        ),
        total_amount=805.78,
        total_discount=7943.06,
        total_tax_amount=9903.69,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9121.51,
                name='Mrs. Samuel Considine',
            ),
            shared.WithholdingTaxitems(
                amount=1489.75,
                name='Ralph Dooley',
            ),
            shared.WithholdingTaxitems(
                amount=3034.21,
                name='Edwin Cartwright',
            ),
            shared.WithholdingTaxitems(
                amount=5283.2,
                name='Cristina Ebert',
            ),
        ],
    ),
    bill_credit_note_id='inventore',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=193236,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
