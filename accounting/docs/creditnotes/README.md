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
        additional_tax_amount=922.79,
        additional_tax_percentage=9391.31,
        allocated_on_date='fuga',
        credit_note_number='est',
        currency='distinctio',
        currency_rate=8546.46,
        customer_ref=shared.CustomerRef(
            company_name='nulla',
            id='88e71f6c-4825-42d7-b71e-7fd074009ef8',
        ),
        discount_percentage=8172.49,
        id='29de1dd7-097b-45da-88c5-7fa6c78a216e',
        issue_date='illo',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='bafeca61-9149-4814-8b64-ff8ae170ef03',
                    name='Jon Wilkinson',
                ),
                description='recusandae',
                discount_amount=2538.55,
                discount_percentage=6520.13,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='a8685559-6673-42aa-9dcb-6682cb70f8cf',
                    name='Dustin Wilkinson',
                ),
                quantity=9347.07,
                sub_total=5800.8,
                tax_amount=1161.7,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6935.92,
                    id='9a9f7484-6e2c-4330-9db0-536d9e75ca00',
                    name='Lana Hauck',
                ),
                total_amount=1500.91,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='11a25a8b-f92f-4974-a8ad-9a9f8bf82211',
                            name='Erin Frami',
                        ),
                        shared.TrackingCategoryRef(
                            id='d98387f7-a79c-4d72-8d24-84da21729f2a',
                            name='Francis Block',
                        ),
                        shared.TrackingCategoryRef(
                            id='5725f116-9ac1-4e41-98a2-3c23e34f2dfa',
                            name='Blanche Cassin',
                        ),
                        shared.TrackingCategoryRef(
                            id='f6de9221-51fe-4171-a099-853e9f543d85',
                            name='Elaine Fadel',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='voluptates',
                        id='22446044-3bc1-4541-88c2-f56e85da7832',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='bd617c3b-0d51-4a44-bf01-bad8706d4608',
                        name='Juana Wuckert',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='41ff5d4e-2ae4-4fb5-8b35-d17638f1edb7',
                        name='Jeffery Hilll',
                    ),
                    shared.TrackingCategoryRef(
                        id='cc5cb860-f8cd-4580-ba73-810e4fe44472',
                        name='Cory Runolfsson',
                    ),
                    shared.TrackingCategoryRef(
                        id='b1dd3bbc-e247-4b76-84ef-f50126d71cff',
                        name='Bryant Anderson',
                    ),
                    shared.TrackingCategoryRef(
                        id='74b84219-53b4-44bd-bc43-159d33e5953c',
                        name='Mrs. Ruth Carroll',
                    ),
                ],
                unit_amount=5525.12,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='63aa41e6-c31c-4c2f-9fcb-51c9a41ffbe9',
                    name='Willis Smitham',
                ),
                description='ipsam',
                discount_amount=9200.57,
                discount_percentage=9358,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='65e076cc-7abf-4616-aa5c-71641934b90f',
                    name='Rochelle Bailey',
                ),
                quantity=683,
                sub_total=6173.25,
                tax_amount=8228.62,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1699.28,
                    id='fc2f9e2e-1059-444b-935d-237a72f90849',
                    name='Rick Olson',
                ),
                total_amount=3105.08,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ecb7537c-d922-42c9-bf57-491aabfa2e76',
                            name='Essie Barton',
                        ),
                        shared.TrackingCategoryRef(
                            id='4d456ef1-031e-4689-9f0c-2001e22cd55c',
                            name='Robert Hickle',
                        ),
                        shared.TrackingCategoryRef(
                            id='a184d76d-971f-4c82-8c65-b037bb8e0cc8',
                            name='Dan Boehm',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='officiis',
                        id='4de04af2-8c5d-4ddb-86aa-1cfd6d828da0',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='19112964-6645-4c1d-81f2-9042f569b7af',
                        name='David Volkman',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='16cbe071-bc16-43e2-b9a3-b084da99257d',
                        name='Amber Ziemann V',
                    ),
                ],
                unit_amount=2756.61,
            ),
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='7a742d84-496c-4bde-acf6-b99bc63562eb',
                    name='Lionel Wisoky',
                ),
                description='porro',
                discount_amount=1748.97,
                discount_percentage=6102.13,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='4c060b06-a128-4776-8eef-6d0c6d6ed9c7',
                    name='Paulette Smitham',
                ),
                quantity=2855.44,
                sub_total=3419.34,
                tax_amount=4922.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=768.18,
                    id='509a8e87-0d3c-45a1-b9c2-42c7b66a1f30',
                    name='Cody Franey',
                ),
                total_amount=3480.56,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='6719890f-42a4-4bb4-b8d8-5b260591d745',
                            name='Earl Rosenbaum II',
                        ),
                        shared.TrackingCategoryRef(
                            id='9c9c3f56-7e0e-4252-b65b-1d62fcdace1f',
                            name='Mrs. Ashley Connelly',
                        ),
                        shared.TrackingCategoryRef(
                            id='e2239e8f-25cd-40d1-9d95-9f439e39266c',
                            name='Lionel Mraz',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='molestiae',
                        id='aa2b2411-3695-4d1e-a698-fcc4596217c2',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='76763342-5403-48bf-b597-1e9819055738',
                        name='Benny Ward',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c7fda395-94d6-46bc-aae4-80632b9954b6',
                        name='Mr. Alfonso Dibbert',
                    ),
                    shared.TrackingCategoryRef(
                        id='36982855-3cb1-4000-abef-4921ec2053b7',
                        name='Claire Fay',
                    ),
                    shared.TrackingCategoryRef(
                        id='ac8ee0f2-bf19-4588-940d-03f3deba297b',
                        name='Nathan Watsica MD',
                    ),
                ],
                unit_amount=7524.92,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='numquam',
        note='consequatur',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='doloribus',
                    currency='quos',
                    currency_rate=4169.67,
                    total_amount=5023.8,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='fd52405c-b331-4d49-af4f-127fb0e0bf1f',
                        name='Steve Block',
                    ),
                    currency='dignissimos',
                    currency_rate=5283.5,
                    id='d0acca77-aeb7-4b70-a1a5-2046b64e99fb',
                    note='doloremque',
                    paid_on_date='officiis',
                    reference='nisi',
                    total_amount=4421.29,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='necessitatibus',
                    currency='alias',
                    currency_rate=5898.68,
                    total_amount=2853.36,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='fdfed554-0ef5-43a3-8a1b-8fe99731adc0',
                        name='Hope Macejkovic',
                    ),
                    currency='eveniet',
                    currency_rate=1603.53,
                    id='dfb70fb3-8742-490d-b365-61eca16ef894',
                    note='ad',
                    paid_on_date='ab',
                    reference='harum',
                    total_amount=8177.91,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='ducimus',
                    currency='nisi',
                    currency_rate=8811.68,
                    total_amount=8848.3,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='eb518c4d-a1fa-4d35-912f-06d4e5b72f0f',
                        name='Valerie Little',
                    ),
                    currency='laudantium',
                    currency_rate=6675.59,
                    id='0424e00a-1d6e-4b94-b464-5d03084fbba5',
                    note='cumque',
                    paid_on_date='cumque',
                    reference='vero',
                    total_amount=9539.16,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='tenetur',
                    currency='ipsam',
                    currency_rate=7981.22,
                    total_amount=7080.11,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='01fe51e5-28a4-45ac-82b8-5f8bc2caba8d',
                        name='Clifford Bogisich',
                    ),
                    currency='illum',
                    currency_rate=8601.44,
                    id='597ff471-1aa1-4bc7-8b86-cecc74f77b48',
                    note='aliquam',
                    paid_on_date='totam',
                    reference='soluta',
                    total_amount=8425.39,
                ),
            ),
        ],
        remaining_credit=4371.07,
        source_modified_date='mollitia',
        status=shared.CreditNoteStatus.SUBMITTED,
        sub_total=9404.72,
        supplemental_data=shared.SupplementalData(
            content={
                "tempora": {
                    "architecto": 'nulla',
                    "qui": 'maxime',
                },
            },
        ),
        total_amount=1898.27,
        total_discount=7465.11,
        total_tax_amount=5541.99,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5119.21,
                name='Erika Hahn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=239283,
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
    credit_note_id='eveniet',
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
    query='ipsa',
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
        additional_tax_amount=3846.3,
        additional_tax_percentage=253.21,
        allocated_on_date='labore',
        credit_note_number='ullam',
        currency='excepturi',
        currency_rate=7463.15,
        customer_ref=shared.CustomerRef(
            company_name='voluptates',
            id='bbad02f2-586b-4cf1-9255-8daa95be6cd0',
        ),
        discount_percentage=1829.75,
        id='756c354a-a432-4b47-a176-3c5208c23e98',
        issue_date='sit',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='d82f0d45-eb4a-48b6-b4ee-5cfc18edc7f7',
                    name='Julio Wehner',
                ),
                description='recusandae',
                discount_amount=298.97,
                discount_percentage=2587.5,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='b3d3ed0c-5670-4ef4-abd3-c9f1cc503f6c',
                    name='Sheryl Reichel',
                ),
                quantity=30.26,
                sub_total=6464.39,
                tax_amount=4283.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1860.92,
                    id='90f957f3-8518-49ad-bef8-07aae03f33ca',
                    name='Lindsay Zemlak',
                ),
                total_amount=8535.32,
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='4032ba26-fd36-48ba-9216-bcb415835c73',
                            name='Anita Braun',
                        ),
                        shared.TrackingCategoryRef(
                            id='3133edc0-46bc-4516-bbbc-a49227c42c22',
                            name='Warren Hills',
                        ),
                        shared.TrackingCategoryRef(
                            id='0495c5db-b3c5-47c1-a498-1e8aa257ddc1',
                            name='Dennis Considine',
                        ),
                        shared.TrackingCategoryRef(
                            id='de64bfcc-5469-4d40-95df-a796206bef2b',
                            name='Lynda Dicki',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quia',
                        id='c1aa010e-9aac-42e9-9355-86d18f9f97a4',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='ad2bf7d6-7ca8-44ad-99b4-1d6124353187',
                        name='Erma Windler',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='03ad421b-d43d-41f0-8b0a-0003eb22d9b3',
                        name='Harvey Beahan',
                    ),
                    shared.TrackingCategoryRef(
                        id='4faa741c-57d1-4fed-8205-0d38dc3ce185',
                        name='Marlene Cassin',
                    ),
                    shared.TrackingCategoryRef(
                        id='ee69166a-8be3-4444-aac8-b3a2875c6c1f',
                        name='Sam Aufderhar',
                    ),
                ],
                unit_amount=18.19,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='voluptate',
        note='repellendus',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='deserunt',
                    currency='error',
                    currency_rate=7699.22,
                    total_amount=5131.41,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7ae50c16-661a-41d9-936a-7e8d53213f3f',
                        name='Melanie Lueilwitz',
                    ),
                    currency='fugit',
                    currency_rate=8256.43,
                    id='b764c59f-0a56-4ceb-8ada-29ca79181c95',
                    note='laboriosam',
                    paid_on_date='molestiae',
                    reference='ab',
                    total_amount=4014.49,
                ),
            ),
        ],
        remaining_credit=4363.67,
        source_modified_date='dolorem',
        status=shared.CreditNoteStatus.VOID,
        sub_total=3218.89,
        supplemental_data=shared.SupplementalData(
            content={
                "ipsa": {
                    "minima": 'vel',
                    "nisi": 'minima',
                    "et": 'autem',
                },
            },
        ),
        total_amount=2204.55,
        total_discount=6359.03,
        total_tax_amount=2495.41,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2274.7,
                name='Dustin Blanda',
            ),
            shared.WithholdingTaxitems(
                amount=7315.02,
                name='Miss Bernice Cummings',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='asperiores',
    force_update=False,
    timeout_in_minutes=179648,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```
