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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=7609.42,
        additional_tax_percentage=2365.88,
        allocated_on_date='ab',
        credit_note_number='maxime',
        currency='porro',
        currency_rate=1279.53,
        customer_ref=shared.CustomerRef(
            company_name='reiciendis',
            id='1fcb51c9-a41f-4fbe-9cbd-795ee65e076c',
        ),
        discount_percentage=7903.41,
        id='7abf616e-a5c7-4164-9934-b90f2e09d19d',
        issue_date='magni',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='c2f9e2e1-0594-44b9-b5d2-37a72f90849d',
                    name='Madeline Waters',
                ),
                description='id',
                discount_amount=9081.27,
                discount_percentage=7595.37,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='b7537cd9-222c-49ff-9749-1aabfa2e761f',
                    name='Angelica O'Reilly',
                ),
                quantity=2893.42,
                sub_total=3375.7,
                tax_amount=3985.78,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8757.66,
                    id='f1031e68-99f0-4c20-81e2-2cd55cc0584a',
                    name='Lena Goyette',
                ),
                total_amount=3758.77,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='971fc820-c65b-4037-bb8e-0cc885187e4d',
                            name='William Graham',
                        ),
                        shared.TrackingCategoryRef(
                            id='28c5dddb-46aa-41cf-96d8-28da01319112',
                            name='Reginald Hackett',
                        ),
                        shared.TrackingCategoryRef(
                            id='45c1d81f-2904-42f5-a9b7-aff0ea2216cb',
                            name='Miss Larry Kunde',
                        ),
                        shared.TrackingCategoryRef(
                            id='163e279a-3b08-44da-9925-7d04f40847a7',
                            name='Lori Sipes',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eius',
                        id='96cbdeec-f6b9-49bc-a356-2ebfdf55c294',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='60b06a12-8776-44ee-b6d0-c6d6ed9c73dd',
                        name='Sheila Grant',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='509a8e87-0d3c-45a1-b9c2-42c7b66a1f30',
                        name='Cody Franey',
                    ),
                ],
                unit_amount=3480.56,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='b6719890-f42a-44bb-838d-85b260591d74',
                    name='Silvia Dietrich',
                ),
                description='quae',
                discount_amount=3298.36,
                discount_percentage=5726.33,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c9c3f567-e0e2-4527-a5b1-d62fcdace1f0',
                    name='Christina Bode',
                ),
                quantity=9210.86,
                sub_total=1621.71,
                tax_amount=1333.6,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1945.74,
                    id='9e8f25cd-0d19-4d95-9f43-9e39266cbd95',
                    name='Clinton Oberbrunner',
                ),
                total_amount=6980.88,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='4113695d-1e66-498f-8c45-96217c297767',
                            name='Edith Frami',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ad',
                        id='4038bfb5-971e-4981-9055-7389cedbac7f',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='39594d66-bc2a-4e48-8632-b9954b6fa220',
                        name='Crystal Johnson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8553cb10-006b-4ef4-921e-c2053b749366',
                        name='Wilson Ledner',
                    ),
                ],
                unit_amount=312.92,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='f2bf1958-8d40-4d03-b3de-ba297be3e90b',
                    name='Jesus Abshire',
                ),
                description='quos',
                discount_amount=4169.67,
                discount_percentage=5023.8,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='fd52405c-b331-4d49-af4f-127fb0e0bf1f',
                    name='Steve Block',
                ),
                quantity=4940.93,
                sub_total=5283.5,
                tax_amount=8602.82,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=65.17,
                    id='acca77ae-b7b7-4021-a520-46b64e99fb0e',
                    name='Ms. Delores Tromp',
                ),
                total_amount=9417.76,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='fed5540e-f53a-434a-9b8f-e99731adc05d',
                            name='Alvin Parker',
                        ),
                        shared.TrackingCategoryRef(
                            id='dfb70fb3-8742-490d-b365-61eca16ef894',
                            name='Kathleen Pollich',
                        ),
                        shared.TrackingCategoryRef(
                            id='6eeeb518-c4da-41fa-9355-12f06d4e5b72',
                            name='James Yost',
                        ),
                        shared.TrackingCategoryRef(
                            id='8568a042-4e00-4a1d-aeb9-434645d03084',
                            name='Malcolm Rempel',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='cumque',
                        id='ceff5cb0-1fe5-41e5-a8a4-5ac82b85f8bc',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='aba8da41-27dd-4597-bf47-11aa1bc74b86',
                        name='Alonzo Schaefer',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f77b4848-bd6a-46f0-841d-2c3b80809437',
                        name='Laverne Bednar II',
                    ),
                    shared.TrackingCategoryRef(
                        id='59bebbad-02f2-4586-bcf1-52558daa95be',
                        name='Mr. Robyn Stoltenberg',
                    ),
                ],
                unit_amount=3159.04,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='6c354aa4-32b4-47e1-b63c-5208c23e9802',
                    name='Willard Dibbert PhD',
                ),
                description='magnam',
                discount_amount=3401.07,
                discount_percentage=9204.88,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='b4a8b674-ee5c-4fc1-8edc-7f787e32e04b',
                    name='Freda Frami',
                ),
                quantity=614.71,
                sub_total=7685.46,
                tax_amount=3532.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4271.07,
                    id='70ef42bd-3c9f-41cc-903f-6c39bcd0a629',
                    name='Tami McClure',
                ),
                total_amount=9704.91,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='85189ad7-ef80-47aa-a03f-33ca79fb9de4',
                            name='Rita Crist',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='qui',
                        id='6fd368ba-9216-4bcb-8158-35c736417231',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='edc046bc-5163-4bbc-a492-27c42c22c553',
                        name='Donna Gottlieb',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5dbb3c57-c1e4-4981-a8aa-257ddc1912eb',
                        name='Rogelio Keebler',
                    ),
                    shared.TrackingCategoryRef(
                        id='fcc5469d-4015-4dfa-b962-06bef2b0a3e4',
                        name='Robyn Braun',
                    ),
                    shared.TrackingCategoryRef(
                        id='010e9aac-2e91-4355-86d1-8f9f97a4bfad',
                        name='Juana Zboncak',
                    ),
                    shared.TrackingCategoryRef(
                        id='67ca84ad-99b4-41d6-9243-531870cf68b0',
                        name='Kristine Shields',
                    ),
                ],
                unit_amount=1067.67,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='rerum',
        note='repellendus',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='nesciunt',
                    currency='facere',
                    currency_rate=1047.54,
                    total_amount=9646.41,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='0cb0a000-3eb2-42d9-b3a7-0d94faa741c5',
                        name='Mona Carroll',
                    ),
                    currency='quibusdam',
                    currency_rate=8045.25,
                    id='2050d38d-c3ce-4185-872f-9ee69166a8be',
                    note='adipisci',
                    paid_on_date='dolore',
                    reference='tempora',
                    total_amount=3088.64,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='debitis',
                    currency='similique',
                    currency_rate=7807.03,
                    total_amount=5051.92,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b3a2875c-6c1f-4e60-ad07-d2a9c87ae50c',
                        name='Jessie Hirthe V',
                    ),
                    currency='veritatis',
                    currency_rate=8360.84,
                    id='9136a7e8-d532-413f-bf65-8752db764c59',
                    note='asperiores',
                    paid_on_date='doloremque',
                    reference='id',
                    total_amount=3349.54,
                ),
            ),
        ],
        remaining_credit=4096.77,
        source_modified_date='placeat',
        status=shared.CreditNoteStatus.PARTIALLY_PAID,
        sub_total=6881.14,
        supplemental_data=shared.SupplementalData(
            content={
                "culpa": {
                    "laborum": 'consequuntur',
                    "omnis": 'maxime',
                    "officia": 'iusto',
                    "natus": 'ab',
                },
                "deleniti": {
                    "eligendi": 'sint',
                },
                "ipsam": {
                    "molestiae": 'ab',
                    "ex": 'iure',
                },
                "dolorem": {
                    "ad": 'ipsum',
                    "ipsa": 'nam',
                    "minima": 'vel',
                    "nisi": 'minima',
                },
            },
        ),
        total_amount=933.84,
        total_discount=4177.55,
        total_tax_amount=2204.55,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2495.41,
                name='Grace Lesch Sr.',
            ),
            shared.WithholdingTaxitems(
                amount=6639.81,
                name='Billy Heathcote MD',
            ),
            shared.WithholdingTaxitems(
                amount=5936,
                name='Ms. Craig Turner',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=302814,
)

res = s.credit_notes.create(req)

if res.create_credit_note_response is not None:
    # handle response
```

## get

﻿Gets a single creditNote corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreditNoteRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    credit_note_id='autem',
)

res = s.credit_notes.get(req)

if res.credit_note is not None:
    # handle response
```

## get_create_update_model

﻿Get create/update credit note model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating and updating a credit note.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateCreditNotesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.credit_notes.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets a list of all credit notes for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCreditNotesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='reprehenderit',
)

res = s.credit_notes.list(req)

if res.credit_notes is not None:
    # handle response
```

## update

﻿Posts an updated credit note to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support updating a credit note.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=6935.09,
        additional_tax_percentage=5597.16,
        allocated_on_date='officia',
        credit_note_number='modi',
        currency='alias',
        currency_rate=7216.91,
        customer_ref=shared.CustomerRef(
            company_name='minus',
            id='05fab0d6-50ed-4f22-a94d-20ec90ea41d1',
        ),
        discount_percentage=9416.83,
        id='465e8515-6fff-473f-9f54-fdd5ea954339',
        issue_date='voluptatum',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='afb42a8d-6338-48e4-9803-9ea5f9b18a24',
                    name='Jeannie Schuppe V',
                ),
                description='aut',
                discount_amount=2158.13,
                discount_percentage=6113.61,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='dacd38ed-0dc6-471d-87f1-e3af15920c90',
                    name='Stephen Robel',
                ),
                quantity=474.01,
                sub_total=1205.48,
                tax_amount=9957.13,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1728.07,
                    id='bd89c8a3-2639-4da5-b7b6-902b881a94f6',
                    name='Annie Huel',
                ),
                total_amount=6534.92,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f0af8c69-1d73-42d9-bbaf-9476a2ae8dcc',
                            name='Angela Schroeder',
                        ),
                        shared.TrackingCategoryRef(
                            id='3512c737-8489-4307-90a0-0e966ec736d4',
                            name='Stephanie Moen',
                        ),
                        shared.TrackingCategoryRef(
                            id='98c783c9-2398-4ed3-93ab-7ca3c5ca8649',
                            name='Kurt Auer',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quibusdam',
                        id='5d6989b7-2064-4510-b7d1-9ea83d492ed1',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='8a2c1954-545e-4955-9cc1-85ea4901c7c4',
                        name='Harriet Schultz',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a784aba3-d230-4edf-b381-1a115382bd7e',
                        name='Jon Hodkiewicz IV',
                    ),
                    shared.TrackingCategoryRef(
                        id='621c58f4-d739-4656-8c20-a0711a961d24',
                        name='Lance Stokes',
                    ),
                    shared.TrackingCategoryRef(
                        id='8f532d89-2cf7-4812-8b51-2c878240bf54',
                        name='Randal Lockman',
                    ),
                ],
                unit_amount=5030.15,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='f1bf0bc8-e1f2-406d-9d83-1d0081090f67',
                    name='Loretta Howe',
                ),
                description='doloribus',
                discount_amount=1877.7,
                discount_percentage=6638.67,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='681c5768-dce7-4424-89a2-15e08601489a',
                    name='Ora Homenick',
                ),
                quantity=2072.02,
                sub_total=6489.85,
                tax_amount=9474.2,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2479.72,
                    id='dd9dda33-dcd6-4348-be4a-7a98e4df37e4',
                    name='Pam Leannon',
                ),
                total_amount=3422.41,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='413e13a4-8231-4090-bbd3-54c092bd734f',
                            name='Louise Funk',
                        ),
                        shared.TrackingCategoryRef(
                            id='d86f4bb2-0fe5-4d91-9cbf-e749caf45a27',
                            name='Ruben Muller',
                        ),
                        shared.TrackingCategoryRef(
                            id='c9e6d10e-9db3-4ad4-86b0-3108d9c33747',
                            name='Jennifer Ledner',
                        ),
                        shared.TrackingCategoryRef(
                            id='94f2ab1f-d567-41e9-8326-350a46714378',
                            name='Dr. Devin Waters',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='error',
                        id='1594d93a-74c0-4252-be3b-4b4db8b778eb',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='e1d2cf50-2baf-4b2c-bc46-35d5e65da028',
                        name='Curtis Thompson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a1e30fda-9664-489d-bb78-673e13a12a6b',
                        name='Marshall Corkery',
                    ),
                ],
                unit_amount=2959.53,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='594487f5-c843-4836-b86b-3cdf6415b044',
                    name='Terrell Muller',
                ),
                description='dicta',
                discount_amount=1911.01,
                discount_percentage=9646.4,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='4eedbe78-bf60-4682-9894-ea763d5c7279',
                    name='Lula Koepp',
                ),
                quantity=1139.47,
                sub_total=3005.84,
                tax_amount=5032.47,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8612.36,
                    id='6d549e56-35b3-43bc-8f97-0c42fc9f4844',
                    name='Andrea Harris',
                ),
                total_amount=3245.72,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='796065c0-efa6-4f93-b90a-1b8c95be1254',
                            name='Jessie Fisher',
                        ),
                        shared.TrackingCategoryRef(
                            id='4fe77210-d1f6-4558-899c-722d2bc0f940',
                            name='Kurt Schuppe',
                        ),
                        shared.TrackingCategoryRef(
                            id='aae042dd-7caa-4c9b-8caa-1cfe9e15df90',
                            name='Faye Bayer',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='amet',
                        id='7831983d-42e5-44a8-9466-597c50233c14',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='d51aaa6d-df5a-4bd6-887c-5fc2b862a00b',
                        name='Cary Jones',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='00157630-bda7-4afd-ad84-a35a41238e1a',
                        name='Emily Hand',
                    ),
                ],
                unit_amount=1866.88,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='6ae33bef-971a-48f4-abca-1106fe965b71',
                    name='Meredith Barrows',
                ),
                description='tenetur',
                discount_amount=5358.76,
                discount_percentage=5373.21,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ec9f7b99-a550-4a65-aed3-33bb0ce8aa65',
                    name='Victoria Denesik',
                ),
                quantity=5250.89,
                sub_total=4102.39,
                tax_amount=8917.7,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7430.23,
                    id='7e14ca56-4089-4150-8970-19a48f88ece7',
                    name='Mrs. Terrell Mayert',
                ),
                total_amount=81.62,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='105d3890-8162-4c6b-ab68-a0f657b7d03a',
                            name='Dr. Carrie Lang',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='at',
                        id='e30f069d-8106-418d-97e1-52297510da80',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='2292cc61-c2a7-402b-b97e-e102da2de35f',
                        name='Miss Frankie Bailey',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3eaab454-02ac-4170-8bf1-cc9fc61aae5e',
                        name='Miss Jon Willms',
                    ),
                ],
                unit_amount=5655.59,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='qui',
        note='soluta',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='nihil',
                    currency='ut',
                    currency_rate=2799.45,
                    total_amount=8430.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='08a2267a-aee7-49e3-871a-d31becb83d23',
                        name='Cassandra O'Conner',
                    ),
                    currency='facilis',
                    currency_rate=9571.11,
                    id='c23d9450-a986-4a49-9bac-707f06b28ecc',
                    note='atque',
                    paid_on_date='autem',
                    reference='eius',
                    total_amount=5999.15,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sunt',
                    currency='amet',
                    currency_rate=5118.79,
                    total_amount=4131.3,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f62c969c-4cc6-4b78-890a-3fd3c81da10f',
                        name='Earnest Crooks',
                    ),
                    currency='voluptatibus',
                    currency_rate=6148.15,
                    id='31da3edb-51fa-4d94-acc9-435137726d15',
                    note='velit',
                    paid_on_date='quia',
                    reference='dicta',
                    total_amount=7214.48,
                ),
            ),
        ],
        remaining_credit=5545.08,
        source_modified_date='velit',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=6851.1,
        supplemental_data=shared.SupplementalData(
            content={
                "aliquid": {
                    "laboriosam": 'sint',
                    "architecto": 'totam',
                    "alias": 'hic',
                    "tenetur": 'iure',
                },
                "consequatur": {
                    "cum": 'occaecati',
                    "fuga": 'ex',
                    "autem": 'nostrum',
                    "atque": 'saepe',
                },
            },
        ),
        total_amount=4320.55,
        total_discount=5652.45,
        total_tax_amount=6841.96,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=7212.15,
                name='Alexander Friesen',
            ),
            shared.WithholdingTaxitems(
                amount=5197.99,
                name='Rosemarie Pollich',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='ducimus',
    force_update=False,
    timeout_in_minutes=323612,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```
