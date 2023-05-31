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
        additional_tax_amount=4169.63,
        additional_tax_percentage=5118.07,
        allocated_on_date='est',
        credit_note_number='consequatur',
        currency='incidunt',
        currency_rate=1748.36,
        customer_ref=shared.CustomerRef(
            company_name='labore',
            id='e00a1d6e-b943-4464-9d03-084fbba5ccef',
        ),
        discount_percentage=9488.1,
        id='5cb01fe5-1e52-48a4-9ac8-2b85f8bc2cab',
        issue_date='laborum',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='da4127dd-597f-4f47-91aa-1bc74b86cecc',
                    name='Eva Wolf',
                ),
                description='nam',
                discount_amount=2787.91,
                discount_percentage=5341.75,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='48bd6a6f-0441-4d2c-bb80-8094373e0604',
                    name='Velma Rogahn',
                ),
                quantity=7386.39,
                sub_total=6653.11,
                tax_amount=8566.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=214.7,
                    id='2f2586bc-f152-4558-9aa9-5be6cd02756c',
                    name='Regina Grady',
                ),
                total_amount=2877.97,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2b47e176-3c52-408c-a3e9-802d82f0d45e',
                            name='Ray Pfannerstill',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ea',
                        id='74ee5cfc-18ed-4c7f-b87e-32e04b3d3ed0',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='670ef42b-d3c9-4f1c-8503-f6c39bcd0a62',
                        name='Edward Wolf',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f385189a-d7ef-4807-aae0-3f33ca79fb9d',
                        name='Francis Anderson',
                    ),
                    shared.TrackingCategoryRef(
                        id='ba26fd36-8ba9-4216-bcb4-15835c736417',
                        name='Diana Bogisich',
                    ),
                ],
                unit_amount=9262.29,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='dc046bc5-163b-4bca-8922-7c42c22c5535',
                    name='Eva McDermott',
                ),
                description='quis',
                discount_amount=8177.29,
                discount_percentage=6963.68,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='b3c57c1e-4981-4e8a-a257-ddc1912ebde6',
                    name='Juana Williamson',
                ),
                quantity=3303.58,
                sub_total=3003.21,
                tax_amount=4362.35,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6168.21,
                    id='d4015dfa-7962-406b-af2b-0a3e42c1aa01',
                    name='Laverne Mante',
                ),
                total_amount=7755.85,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e9135586-d18f-49f9-ba4b-fad2bf7d67ca',
                            name='Edwin Olson',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='unde',
                        id='b41d6124-3531-4870-8f68-b03ad421bd43',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='f0cb0a00-03eb-422d-9b3a-70d94faa741c',
                        name='Dr. Lydia Spencer',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c2050d38-dc3c-4e18-9472-f9ee69166a8b',
                        name='Jeff Grimes',
                    ),
                    shared.TrackingCategoryRef(
                        id='eac8b3a2-875c-46c1-be60-6d07d2a9c87a',
                        name='Herman Barrows III',
                    ),
                    shared.TrackingCategoryRef(
                        id='661a1d91-36a7-4e8d-9321-3f3f658752db',
                        name='Stacey Haag',
                    ),
                    shared.TrackingCategoryRef(
                        id='9f0a56ce-bcad-4a29-8a79-181c95671663',
                        name='Miss Tommy Emard',
                    ),
                ],
                unit_amount=4263.08,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='65163a36-3851-42ab-a521-b9f2e072467b',
                    name='Miss Homer Gislason',
                ),
                description='sit',
                discount_amount=3356.88,
                discount_percentage=9426.04,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ab0d650e-df22-4a94-920e-c90ea41d1f46',
                    name='Jenna Lakin II',
                ),
                quantity=3916.67,
                sub_total=9957.33,
                tax_amount=9573.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9524.11,
                    id='73fdf54f-dd5e-4a95-8339-8dafb42a8d63',
                    name='Marsha Lueilwitz',
                ),
                total_amount=8648.87,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='039ea5f9-b18a-4244-bd61-9039dacd38ed',
                            name='Krystal Rolfson',
                        ),
                        shared.TrackingCategoryRef(
                            id='1dc7f1e3-af15-4920-890d-1b4901f2bd89',
                            name='Everett Ondricka',
                        ),
                        shared.TrackingCategoryRef(
                            id='639da5b7-b690-42b8-81a9-4f643664a8f0',
                            name='Marlon Leffler',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='natus',
                        id='1d732d9f-baf9-4476-a2ae-8dcc50c8a351',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='73784893-0750-4a00-a966-ec736d431943',
                        name='Sidney Ruecker',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c92398ed-3d3a-4b7c-a3c5-ca8649a70cfd',
                        name='Freda Johnson',
                    ),
                ],
                unit_amount=6125.84,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='distinctio',
        note='in',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='voluptatem',
                    currency='voluptas',
                    currency_rate=2991.8,
                    total_amount=3189,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1077d19e-a83d-4492-ad14-b8a2c1954545',
                        name='Austin Hermann',
                    ),
                    currency='cumque',
                    currency_rate=7659,
                    id='185ea490-1c7c-443a-92da-a784aba3d230',
                    note='voluptates',
                    paid_on_date='nulla',
                    reference='tenetur',
                    total_amount=4923.66,
                ),
            ),
        ],
        remaining_credit=2200.49,
        source_modified_date='totam',
        status=shared.CreditNoteStatus.UNKNOWN,
        sub_total=1147.62,
        supplemental_data=shared.SupplementalData(
            content={
                "beatae": {
                    "veniam": 'non',
                },
                "laudantium": {
                    "rerum": 'nulla',
                },
                "ducimus": {
                    "repellendus": 'enim',
                    "voluptas": 'veniam',
                    "voluptatem": 'quam',
                    "vel": 'aspernatur',
                },
            },
        ),
        total_amount=850.02,
        total_discount=7810.03,
        total_tax_amount=3220.54,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9851.55,
                name='Janis Kshlerin',
            ),
            shared.WithholdingTaxitems(
                amount=3759.62,
                name='Natalie Gleichner',
            ),
            shared.WithholdingTaxitems(
                amount=334.57,
                name='Mr. Brian Kihn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=608208,
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
    credit_note_id='commodi',
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
    query='dicta',
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
        additional_tax_amount=8489.26,
        additional_tax_percentage=1334.52,
        allocated_on_date='ut',
        credit_note_number='deserunt',
        currency='dignissimos',
        currency_rate=8604.11,
        customer_ref=shared.CustomerRef(
            company_name='facilis',
            id='b8f532d8-92cf-4781-acb5-12c878240bf5',
        ),
        discount_percentage=2743.68,
        id='8f88f8f1-bf0b-4c8e-9f20-6d5d831d0081',
        issue_date='voluptatem',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='0f670667-3f3a-4681-8576-8dce742409a2',
                    name='Ms. Annette Towne',
                ),
                description='aut',
                discount_amount=1141.51,
                discount_percentage=2710.98,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='89a5f63e-3af3-4dd9-9da3-3dcd63483e4a',
                    name='Amelia Morissette',
                ),
                quantity=2688.31,
                sub_total=8278.13,
                tax_amount=9784.16,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2045.17,
                    id='7e45b895-5d41-43e1-ba48-2310907bd354',
                    name='Charles McGlynn',
                ),
                total_amount=8744.46,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='34f02449-d86f-44bb-a0fe-5d911cbfe749',
                            name='Omar Wolf',
                        ),
                        shared.TrackingCategoryRef(
                            id='a27f69e2-c9e6-4d10-a9db-3ad4c6b03108',
                            name='Seth Schaefer',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='in',
                        id='473082b9-4f2a-4b1f-9567-1e9c326350a4',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='143789ce-0e99-4159-8d93-a74c0252fe3b',
                        name='Bridget Greenholt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='b778ebb6-e1d2-4cf5-82ba-fb2cbc4635d5',
                        name='Andre Heidenreich',
                    ),
                    shared.TrackingCategoryRef(
                        id='028c3e95-1a1e-430f-9a96-6489d7b78673',
                        name='Peter Feeney Sr.',
                    ),
                    shared.TrackingCategoryRef(
                        id='a6b99249-4594-4487-b5c8-43836b86b3cd',
                        name='Mrs. Marc Grimes',
                    ),
                ],
                unit_amount=223.76,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='449f9df1-3f4e-4edb-a78b-f606825894ea',
                    name='Jeanne Farrell',
                ),
                description='impedit',
                discount_amount=4457.32,
                discount_percentage=1479.33,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='795b7851-48d6-4d54-9e56-35b33bc0f970',
                    name='Micheal Cummings',
                ),
                quantity=5918.35,
                sub_total=9624.68,
                tax_amount=2930.13,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5170.23,
                    id='44225e75-b796-4065-80ef-a6f93b90a1b8',
                    name='Austin Hartmann',
                ),
                total_amount=1147.52,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='54b739f4-fe77-4210-91f6-558c99c722d2',
                            name='Lucas Barton',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='numquam',
                        id='087d9caa-e042-4dd7-8aac-9b4caa1cfe9e',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='df903907-f378-4319-83d4-2e54a8546659',
                        name='Mr. Kara Hintz',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c1471d51-aaa6-4ddf-9abd-6487c5fc2b86',
                        name='Miss Monique Bartell',
                    ),
                ],
                unit_amount=9832.72,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='69e10015-7630-4bda-bafd-ed84a35a4123',
                    name='Stewart Bode',
                ),
                description='sequi',
                discount_amount=3217.24,
                discount_percentage=6847.17,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c26ae33b-ef97-41a8-b46b-ca1106fe965b',
                    name='Evelyn Braun IV',
                ),
                quantity=7565.71,
                sub_total=9475.73,
                tax_amount=5358.76,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5373.21,
                    id='ec9f7b99-a550-4a65-aed3-33bb0ce8aa65',
                    name='Victoria Denesik',
                ),
                total_amount=5250.89,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='eb7e14ca-5640-4891-9009-7019a48f88ec',
                            name='Ron Ratke',
                        ),
                        shared.TrackingCategoryRef(
                            id='04e01105-d389-4081-a2c6-beb68a0f657b',
                            name='Teri Abshire',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='beatae',
                        id='480f8de3-0f06-49d8-9061-8d97e1522975',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='da803122-92cc-461c-aa70-2bb97ee102da',
                        name='Hope Walsh',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8e01bf33-eaab-4454-82ac-1704bf1cc9fc',
                        name='Katherine Oberbrunner',
                    ),
                    shared.TrackingCategoryRef(
                        id='5eb5f0c4-92b5-4744-908a-2267aaee79e3',
                        name='Fernando Blanda',
                    ),
                    shared.TrackingCategoryRef(
                        id='31becb83-d237-48ae-bbfc-23d9450a986a',
                        name='Faye Hammes',
                    ),
                    shared.TrackingCategoryRef(
                        id='c707f06b-28ec-4c86-8923-86f62c969c4c',
                        name='Rick Predovic',
                    ),
                ],
                unit_amount=5207.16,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='error',
        note='alias',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sequi',
                    currency='sapiente',
                    currency_rate=8471.37,
                    total_amount=2026.93,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c81da10f-8c23-4df9-b1da-3edb51fad94a',
                        name='Roosevelt Marvin',
                    ),
                    currency='ullam',
                    currency_rate=1158.79,
                    id='37726d15-321b-4832-a56d-69180ff60eb9',
                    note='fuga',
                    paid_on_date='ex',
                    reference='autem',
                    total_amount=3460.72,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='atque',
                    currency='saepe',
                    currency_rate=4320.55,
                    total_amount=5652.45,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a4b843d3-82db-4ec7-9c68-c60659468ce3',
                        name='Anita Spinka',
                    ),
                    currency='magnam',
                    currency_rate=5876.67,
                    id='bf8214c3-37f9-46bb-8c69-e372db1344ba',
                    note='error',
                    paid_on_date='doloribus',
                    reference='reprehenderit',
                    total_amount=5256.79,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='est',
                    currency='quis',
                    currency_rate=7709.69,
                    total_amount=343.42,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='ed7aab62-e972-461f-b0c5-8d27b51996b5',
                        name='Joel Rath DVM',
                    ),
                    currency='saepe',
                    currency_rate=9596.73,
                    id='712b7a7a-b034-44b1-b106-88deebef897f',
                    note='velit',
                    paid_on_date='fugiat',
                    reference='pariatur',
                    total_amount=276.76,
                ),
            ),
        ],
        remaining_credit=7998.57,
        source_modified_date='minus',
        status=shared.CreditNoteStatus.PARTIALLY_PAID,
        sub_total=2232.35,
        supplemental_data=shared.SupplementalData(
            content={
                "tenetur": {
                    "dicta": 'rerum',
                },
            },
        ),
        total_amount=2054.73,
        total_discount=9131.52,
        total_tax_amount=3033.65,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=30.91,
                name='Richard Nitzsche Jr.',
            ),
            shared.WithholdingTaxitems(
                amount=2752.88,
                name='Cassandra Kerluke',
            ),
            shared.WithholdingTaxitems(
                amount=4841.4,
                name='Mr. Sherri Torphy',
            ),
            shared.WithholdingTaxitems(
                amount=2244.51,
                name='Laura Cronin',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='cumque',
    force_update=False,
    timeout_in_minutes=513307,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```
