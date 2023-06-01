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
        allocated_on_date='omnis',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='molestiae',
        currency_rate=191.93,
        discount_percentage=4701.32,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='magnam',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='a4469b6e-2141-4959-890a-fa563e2516fe',
                    name='Jasmine Lind',
                ),
                description='architecto',
                discount_amount=995.69,
                discount_percentage=9194.83,
                item_ref=shared.ItemRef(
                    id='5b7fd2ed-0289-421c-9dc6-92601fb576b0',
                    name='Dr. Herman Wolf',
                ),
                quantity=117.14,
                sub_total=7649.12,
                tax_amount=3599.78,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9441.24,
                    id='bb258705-3202-4c73-95fe-9b90c28909b3',
                    name='Merle Gleichner',
                ),
                total_amount=5356.33,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='9cbf4863-3323-4f9b-b7f3-a4100674ebf6',
                            name='Dr. Craig Littel DDS',
                        ),
                        shared.TrackingCategoryRef(
                            id='a77a89eb-f737-4ae4-a03c-e5e6a95d8a0d',
                            name='Rhonda Kautzer',
                        ),
                        shared.TrackingCategoryRef(
                            id='2af7a73c-f3be-4453-b870-b326b5a73429',
                            name='Miss Jody Rogahn',
                        ),
                        shared.TrackingCategoryRef(
                            id='422bb679-d232-4271-9bf0-cbb1e31b8b90',
                            name='Mike Greenholt',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dolorum',
                        id='1108e0ad-cf4b-4921-879f-ce953f73ef7f',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='7abd74dd-39c0-4f5d-acff-7c70a45626d4',
                        name='Mrs. Vicki Langosh',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6d9f5fce-6c55-4614-ac3e-250fb008c42e',
                        name='Ellen Borer',
                    ),
                ],
                unit_amount=8104.24,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='366c8dd6-b144-4290-b474-778a7bd466d2',
                    name='Miss Devin Bogan',
                ),
                description='neque',
                discount_amount=7786.96,
                discount_percentage=8472.76,
                item_ref=shared.ItemRef(
                    id='ca425190-4e52-43c7-a0bc-7178e4796f2a',
                    name='Carol Sawayn',
                ),
                quantity=5100.17,
                sub_total=1598.67,
                tax_amount=5361.78,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1438.29,
                    id='aa482562-f222-4e98-97ee-17cbe61e6b7b',
                    name='Warren Rau V',
                ),
                total_amount=7313.98,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c20c4f37-89fd-4871-b99d-d2efd121aa6f',
                            name='Lila Kassulke',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='libero',
                        id='db04f157-5608-42d6-8ea1-9f1d17051339',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='8086a184-0394-4c26-871f-93f5f0642dac',
                        name='Blanche Yundt II',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c413aa63-aae8-4d67-864d-bb675fd5e60b',
                        name='Arlene Heidenreich',
                    ),
                    shared.TrackingCategoryRef(
                        id='4f6fbee4-1f33-4317-be35-b60eb1ea4265',
                        name='Cathy Rohan',
                    ),
                    shared.TrackingCategoryRef(
                        id='c28744ed-53b8-48f3-a8d8-f5c0b2f2fb7b',
                        name='Margarita Greenholt',
                    ),
                    shared.TrackingCategoryRef(
                        id='76b26916-fe1f-408f-8294-e3698f447f60',
                        name='Cecelia Lakin',
                    ),
                ],
                unit_amount=2777.73,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='5e80ca55-efd2-40e4-97e1-858b6a89fbe3',
                    name='Wesley Nikolaus',
                ),
                description='accusamus',
                discount_amount=2726.83,
                discount_percentage=5436.78,
                item_ref=shared.ItemRef(
                    id='24d0ab40-7508-48e5-9862-065e904f3b11',
                    name='Francisco Powlowski',
                ),
                quantity=7241.48,
                sub_total=9488.61,
                tax_amount=3888.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=27.03,
                    id='3a79f9df-e0ab-47da-8a50-ce187f86bc17',
                    name='Angelina Jenkins',
                ),
                total_amount=8872.65,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e9526f8d-986e-4881-aad4-f0e1012563f9',
                            name='Tricia Cronin',
                        ),
                        shared.TrackingCategoryRef(
                            id='973e922a-57a1-45be-be06-0807e2b6e3ab',
                            name='Jordan Haag',
                        ),
                        shared.TrackingCategoryRef(
                            id='0597a60f-f2a5-44a3-9e94-764a3e865e79',
                            name='Natalie Witting',
                        ),
                        shared.TrackingCategoryRef(
                            id='51a5a9da-660f-4f57-bfaa-d4f9efc1b451',
                            name='Mrs. Erma Berge',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eum',
                        id='48dc2f61-5199-4ebf-90e9-fe6c632ca3ae',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='11799631-2fde-4047-b177-8ff61d017476',
                        name='Jeanne Beer II',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='b6a66065-9a1a-4dea-ab58-51d6c645b08b',
                        name='Doris Lemke MD',
                    ),
                    shared.TrackingCategoryRef(
                        id='aa0fe1ad-e008-4e6f-8c5f-350d8cdb5a34',
                        name='Cassandra Bogan',
                    ),
                    shared.TrackingCategoryRef(
                        id='01042181-3d52-408e-8e7e-253b668451c6',
                        name='Brent Walter II',
                    ),
                    shared.TrackingCategoryRef(
                        id='e16deab3-fec9-4578-a645-84273a8418d1',
                        name='Ms. Marilyn Feest',
                    ),
                ],
                unit_amount=7468.37,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='alias',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='eos',
                    currency='occaecati',
                    currency_rate=6128.67,
                    total_amount=1700.99,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1aefb9f5-8c4d-486e-a8e4-be056013f59d',
                        name='Claude Hickle',
                    ),
                    currency='quis',
                    currency_rate=5718.44,
                    id='ecfef66e-f1ca-4a33-83c2-beb477373c8d',
                    note='iure',
                    paid_on_date='odit',
                    reference='voluptatibus',
                    total_amount=4269.04,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='magnam',
                    currency='quibusdam',
                    currency_rate=789.69,
                    total_amount=8180.34,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b1f2c431-0661-4e96-b49e-1cf9e06e3a43',
                        name='Miss Karen Batz',
                    ),
                    currency='ea',
                    currency_rate=6931.53,
                    id='6bc9b8f7-59ea-4c55-a974-1d311352965b',
                    note='libero',
                    paid_on_date='rem',
                    reference='dolorum',
                    total_amount=4876.76,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='fugit',
                    currency='alias',
                    currency_rate=1680.42,
                    total_amount=4254.02,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='11435e13-9dbc-4225-9b1a-bda8c070e108',
                        name='Ms. Lynne Rau',
                    ),
                    currency='dolores',
                    currency_rate=8247.98,
                    id='1ad879ee-b966-45b8-9efb-d02bae0be2d7',
                    note='praesentium',
                    paid_on_date='odit',
                    reference='explicabo',
                    total_amount=3589.95,
                ),
            ),
        ],
        remaining_credit=6214.73,
        source_modified_date='earum',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "recusandae": {
                    "ut": 'quidem',
                    "quis": 'beatae',
                    "unde": 'molestiae',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='f92443da-7ce5-42b8-95c5-37c6454efb0b',
            supplier_name='ratione',
        ),
        total_amount=805.78,
        total_discount=2899.13,
        total_tax_amount=5208.75,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=3759.94,
                name='Jacob Schinner',
            ),
            shared.WithholdingTaxitems(
                amount=6692.37,
                name='Brendan Rippin',
            ),
            shared.WithholdingTaxitems(
                amount=9974.37,
                name='Ms. Corey Kiehn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=448369,
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
    bill_credit_note_id='ducimus',
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
    query='excepturi',
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
        allocated_on_date='dolores',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='error',
        currency_rate=850.76,
        discount_percentage=4981.8,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='voluptate',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='eac646ec-b573-4409-a3eb-1e5a2b12eb07',
                    name='Harold Boyer',
                ),
                description='libero',
                discount_amount=5665.06,
                discount_percentage=5782.1,
                item_ref=shared.ItemRef(
                    id='545fc95f-a889-470e-989d-bb30fcb33ea0',
                    name='Ms. Sally Rempel',
                ),
                quantity=7566.54,
                sub_total=8200.23,
                tax_amount=2514.64,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2981.87,
                    id='e2f52d82-d351-43bb-af48-b656bcdb35ff',
                    name='Raquel Greenfelder',
                ),
                total_amount=4407.77,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='37a8cd9e-7319-4c17-bd52-5f77b114eeb5',
                            name='Johanna Weimann',
                        ),
                        shared.TrackingCategoryRef(
                            id='5fc37814-d4c9-48e0-82bb-89eb75dad636',
                            name='Mrs. Leslie Anderson I',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='illum',
                        id='8bb31180-f739-4ae9-a057-eb809e281033',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='3981d4c7-00b6-407f-bc93-c73b9da3f2ce',
                        name='Cameron Kuhn',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f2257411-faf4-4b75-84e4-72e802857a5b',
                        name='Karen Gleichner',
                    ),
                ],
                unit_amount=6521.25,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7d575f14-00e7-464a-9733-4ec1b781b36a',
                    name='Gwendolyn Anderson',
                ),
                description='repellendus',
                discount_amount=832.91,
                discount_percentage=607.78,
                item_ref=shared.ItemRef(
                    id='0efada20-0ef0-4422-ab21-64cf9ab8366c',
                    name='Kathy Frami',
                ),
                quantity=8611.23,
                sub_total=6711.16,
                tax_amount=6176.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8837.8,
                    id='06bee482-5c1f-4c0e-915c-80bff918544e',
                    name='Joel Cruickshank',
                ),
                total_amount=9851.09,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ce8f1977-773e-4635-a2a7-b408f05e3d48',
                            name='Clint Ortiz',
                        ),
                        shared.TrackingCategoryRef(
                            id='13a1f5fd-9425-49c0-b36f-25ea944f3b75',
                            name='Dr. Alexandra Bernhard',
                        ),
                        shared.TrackingCategoryRef(
                            id='c37a5126-2438-435b-bc05-a23a45cefc5f',
                            name='Miss Frankie Braun DDS',
                        ),
                        shared.TrackingCategoryRef(
                            id='e2169e51-0019-4c6d-85e3-4762799bfbbe',
                            name='Lindsey Gislason',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='cum',
                        id='2bb4ecae-6c3d-45db-bade-bd5daea4c506',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='aa94c026-44cf-45e9-99a4-578adc1ac600',
                        name='Mr. Alonzo Schoen V',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='802e2ec0-9ff8-4f0f-816f-f3477c13e902',
                        name='Mr. Jack Gottlieb',
                    ),
                    shared.TrackingCategoryRef(
                        id='b0960a66-8151-4a47-aaf9-23c5949f83f3',
                        name='Angela Schaefer',
                    ),
                    shared.TrackingCategoryRef(
                        id='76ffb901-c6ec-4bb4-a243-cf789ffafeda',
                        name='Sheila Torphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='e6e0ac18-4c2b-49c2-87c8-8373a40e1942',
                        name='Tony Connelly',
                    ),
                ],
                unit_amount=3731.06,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='055756f5-d56d-40bd-8af2-dfe13db4f62c',
                    name='Lorenzo Flatley',
                ),
                description='error',
                discount_amount=2524.73,
                discount_percentage=978.1,
                item_ref=shared.ItemRef(
                    id='aebc0b80-a692-44d3-b2ec-fcc8f895010f',
                    name='Lynette Senger',
                ),
                quantity=4248.53,
                sub_total=9608.13,
                tax_amount=6525.15,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=651.21,
                    id='804e54c8-2f16-48a3-a3c8-873e484380b1',
                    name='Milton Powlowski',
                ),
                total_amount=6464.91,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='75a60a04-c495-4cc6-9917-1b51c1bdb1cf',
                            name='Lula Lowe',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='officiis',
                        id='bdfc4ccc-a99b-4c7f-80b2-dce10873e42b',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='6d678878-ba85-481a-9820-8c54fefa9c95',
                        name='Howard Torphy',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='565d307c-fee8-4120-ae28-13fa4a41c480',
                        name='Mike Zulauf I',
                    ),
                    shared.TrackingCategoryRef(
                        id='2af03102-d514-4f4c-86f1-8bf9621a6a4f',
                        name='Tamara O'Kon',
                    ),
                ],
                unit_amount=9085.39,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='e3e4be75-2c65-4b34-818e-3bb91c8d975e',
                    name='Silvia Langworth V',
                ),
                description='illum',
                discount_amount=5265.84,
                discount_percentage=9493.7,
                item_ref=shared.ItemRef(
                    id='84f144f3-e07e-4dcc-8aa5-f3cabd905a97',
                    name='Kelley Bashirian',
                ),
                quantity=4741.85,
                sub_total=1541.3,
                tax_amount=5147.67,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1527.42,
                    id='27b2d309-470b-4f7a-8fa8-7cf535a6fae5',
                    name='Gwen Reichel',
                ),
                total_amount=304.26,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='321f023b-75d2-4367-be1a-0cc8df79f0a3',
                            name='Ruben Sipes DDS',
                        ),
                        shared.TrackingCategoryRef(
                            id='364b7c15-dfba-4ce1-88b1-c4ee2c8c6ce6',
                            name='Marie Wunsch',
                        ),
                        shared.TrackingCategoryRef(
                            id='b1c7cbdb-6eec-4743-b8ba-25317747dc91',
                            name='Janie Stanton',
                        ),
                        shared.TrackingCategoryRef(
                            id='af5dd672-3dc0-4f5a-a2f3-a6b700878756',
                            name='Gail Fay',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='est',
                        id='6c98b555-5408-40d4-8bca-cc6cbd6b5f3e',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='09304f92-6bad-4255-b819-b474b0ed20e5',
                        name='Ruby Haag',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f639a910-abdc-4ab6-a676-696e1ec00221',
                        name='Johnny Farrell',
                    ),
                    shared.TrackingCategoryRef(
                        id='89acb3ec-fda8-4d0c-949e-f03004978a61',
                        name='Neal Boehm',
                    ),
                    shared.TrackingCategoryRef(
                        id='20688f77-c1ff-4c71-9ca1-63f2a3c80a97',
                        name='Darrin Flatley',
                    ),
                    shared.TrackingCategoryRef(
                        id='cddf857a-9e61-4876-86ab-21d29dfc94d6',
                        name='Clay Schaefer',
                    ),
                ],
                unit_amount=6143.46,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='provident',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sint',
                    currency='aperiam',
                    currency_rate=494.56,
                    total_amount=4312.58,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6a6d2d00-0355-4338-8ec0-86fa21e9152c',
                        name='Ms. Melvin Brekke III',
                    ),
                    currency='ducimus',
                    currency_rate=7284.74,
                    id='8e3c8db0-3408-4d6d-b64f-fd455906d126',
                    note='neque',
                    paid_on_date='quibusdam',
                    reference='numquam',
                    total_amount=5231.09,
                ),
            ),
        ],
        remaining_credit=8846.22,
        source_modified_date='omnis',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "corporis": {
                    "dolores": 'placeat',
                    "excepturi": 'recusandae',
                    "quos": 'dicta',
                    "sapiente": 'ipsum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='0be3e432-02d7-4216-9765-06641870d9d2',
            supplier_name='inventore',
        ),
        total_amount=805.78,
        total_discount=9764.03,
        total_tax_amount=6012.28,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=8345.87,
                name='Sherry Batz',
            ),
            shared.WithholdingTaxitems(
                amount=8907.65,
                name='Miss Simon Bosco V',
            ),
            shared.WithholdingTaxitems(
                amount=1917.24,
                name='Anita Dare III',
            ),
        ],
    ),
    bill_credit_note_id='laudantium',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=703407,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
