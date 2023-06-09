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
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=201.07,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='502a94bb-4f63-4c96-9e9a-3efa77dfb14c',
                    name='Nathaniel Hyatt',
                ),
                description='non',
                discount_amount=5812.73,
                discount_percentage=3132.18,
                item_ref=shared.ItemRef(
                    id='efb9ba88-f3a6-4699-b074-ba4469b6e214',
                    name='Miriam Hermann',
                ),
                quantity=5743.25,
                sub_total=336.25,
                tax_amount=6532.01,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9689.62,
                    id='a563e251-6fe4-4c8b-b11e-5b7fd2ed0289',
                    name='Joan Satterfield',
                ),
                total_amount=8073.19,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='92601fb5-76b0-4d5f-8d30-c5fbb2587053',
                            name='Dorothy Dach',
                        ),
                        shared.TrackingCategoryRef(
                            id='3d5fe9b9-0c28-4909-b3fe-49a8d9cbf486',
                            name='Dawn Fadel',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='hic',
                        id='9b77f3a4-1006-474e-bf69-280d1ba77a89',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='f737ae42-03ce-45e6-a95d-8a0d446ce2af',
                        name='Fannie Kub',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3be453f8-70b3-426b-9a73-429cdb1a8422',
                        name='Cesar Hyatt',
                    ),
                    shared.TrackingCategoryRef(
                        id='d2322715-bf0c-4bb1-a31b-8b90f3443a11',
                        name='Miss Billie Ward',
                    ),
                    shared.TrackingCategoryRef(
                        id='cf4b9218-79fc-4e95-bf73-ef7fbc7abd74',
                        name='Gilberto Dickinson',
                    ),
                    shared.TrackingCategoryRef(
                        id='0f5d2cff-7c70-4a45-a26d-436813f16d9f',
                        name='Dixie Schamberger',
                    ),
                ],
                unit_amount=7740.48,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='556146c3-e250-4fb0-88c4-2e141aac366c',
                    name='Mack Stoltenberg',
                ),
                description='quasi',
                discount_amount=2703.28,
                discount_percentage=2561.39,
                item_ref=shared.ItemRef(
                    id='29074747-78a7-4bd4-a6d2-8c10ab3cdca4',
                    name='Brittany Bernier II',
                ),
                quantity=8920.5,
                sub_total=3708.53,
                tax_amount=1334.65,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1970.54,
                    id='c7e0bc71-78e4-4796-b2a7-0c688282aa48',
                    name='Cathy Huel',
                ),
                total_amount=1598.7,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2e9817ee-17cb-4e61-a6b7-b95bc0ab3c20',
                            name='Calvin Williamson',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='blanditiis',
                        id='9fd871f9-9dd2-4efd-921a-a6f1e674bdb0',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='15756082-d68e-4a19-b1d1-7051339d0808',
                        name='Iris Bernhard',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='394c2607-1f93-4f5f-8642-dac7af515cc4',
                        name='Josephine Paucek',
                    ),
                ],
                unit_amount=2460.63,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='aae8d678-64db-4b67-9fd5-e60b375ed4f6',
                    name='Rickey Ullrich',
                ),
                description='sunt',
                discount_amount=9920.12,
                discount_percentage=2415.45,
                item_ref=shared.ItemRef(
                    id='3317fe35-b60e-4b1e-a426-555ba3c28744',
                    name='Lionel Herman',
                ),
                quantity=5023.89,
                sub_total=5553.61,
                tax_amount=9425.84,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2015.17,
                    id='a8d8f5c0-b2f2-4fb7-b194-a276b26916fe',
                    name='Faith Aufderhar',
                ),
                total_amount=2748.23,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='94e3698f-447f-4603-a8b4-45e80ca55efd',
                            name='Deborah Turcotte',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='in',
                        id='e1858b6a-89fb-4e3a-9aa8-e4824d0ab407',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='88e51862-065e-4904-b3b1-194b8abf603a',
                        name='Lindsey Witting',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e0ab7da8-a50c-4e18-bf86-bc173d689eee',
                        name='Darrell Collier',
                    ),
                    shared.TrackingCategoryRef(
                        id='8d986e88-1ead-44f0-a101-2563f94e29e9',
                        name='Sylvia Upton',
                    ),
                    shared.TrackingCategoryRef(
                        id='2a57a15b-e3e0-4608-87e2-b6e3ab8845f0',
                        name='Katrina Kovacek',
                    ),
                    shared.TrackingCategoryRef(
                        id='0ff2a54a-31e9-4476-8a3e-865e7956f925',
                        name='Lynda Heathcote',
                    ),
                ],
                unit_amount=8217.19,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='a660ff57-bfaa-4d4f-9efc-1b4512c10326',
                    name='Deanna Swaniawski',
                ),
                description='sapiente',
                discount_amount=4332.79,
                discount_percentage=1173.2,
                item_ref=shared.ItemRef(
                    id='5199ebfd-0e9f-4e6c-a32c-a3aed0117996',
                    name='Joyce Cummings',
                ),
                quantity=8965.82,
                sub_total=585.34,
                tax_amount=2711.13,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4706.21,
                    id='71778ff6-1d01-4747-a360-a15db6a66065',
                    name='Alfonso Bernier',
                ),
                total_amount=9139.92,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ab5851d6-c645-4b08-b618-91baa0fe1ade',
                            name='Mary Leuschke',
                        ),
                        shared.TrackingCategoryRef(
                            id='f8c5f350-d8cd-4b5a-b418-143010421813',
                            name='Ms. Vernon Crooks',
                        ),
                        shared.TrackingCategoryRef(
                            id='ce7e253b-6684-451c-ac6e-205e16deab3f',
                            name='Earnest McClure',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='blanditiis',
                        id='a6458427-3a84-418d-9623-09fb0929921a',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='b9f58c4d-86e6-48e4-be05-6013f59da757',
                        name='Alvin Marquardt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ef66ef1c-aa33-483c-abeb-477373c8d72f',
                        name='Dr. Megan Spinka',
                    ),
                    shared.TrackingCategoryRef(
                        id='1f2c4310-661e-4963-89e1-cf9e06e3a437',
                        name='Sharon Adams',
                    ),
                    shared.TrackingCategoryRef(
                        id='6b6bc9b8-f759-4eac-95a9-741d31135296',
                        name='Patty Reinger',
                    ),
                    shared.TrackingCategoryRef(
                        id='72026114-35e1-439d-bc22-59b1abda8c07',
                        name='Ms. Tasha Block',
                    ),
                ],
                unit_amount=7551.06,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=1729.51,
                    total_amount=8247.98,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1ad879ee-b966-45b8-9efb-d02bae0be2d7',
                        name='Fred Champlin',
                    ),
                    currency='EUR',
                    currency_rate=2393.37,
                    id='ea4b5197-f924-443d-a7ce-52b895c537c6',
                    note='modi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='magnam',
                    total_amount=9149.71,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "aperiam": {
                    "ratione": 'labore',
                    "totam": 'occaecati',
                    "voluptas": 'quo',
                },
                "velit": {
                    "fuga": 'nostrum',
                    "est": 'impedit',
                    "delectus": 'tempore',
                    "vero": 'odit',
                },
                "repellat": {
                    "nemo": 'reprehenderit',
                    "aperiam": 'odio',
                    "minima": 'in',
                    "ducimus": 'excepturi',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='29177dea-c646-4ecb-9734-09e3eb1e5a2b',
            supplier_name='dicta',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=8998.67,
                name='Larry Kuphal Sr.',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=386447,
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
    bill_credit_note_id='pariatur',
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
    query='libero',
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
        allocated_on_date='2022-10-23T00:00:00.000Z',
        bill_credit_note_number='91fe2a83-e161-4c21-929d-c5c10c4b07e5',
        currency='USD',
        currency_rate=3679.17,
        discount_percentage=0,
        id='1509398f-98e2-436d-8a5d-c042e0c74ffc',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='fc95fa88-970e-4189-9bb3-0fcb33ea055b',
                    name='Mae Krajcik',
                ),
                description='non',
                discount_amount=2981.87,
                discount_percentage=9322.96,
                item_ref=shared.ItemRef(
                    id='2f52d82d-3513-4bb6-b48b-656bcdb35ff2',
                    name='Marcus Prohaska',
                ),
                quantity=3455.06,
                sub_total=2072.96,
                tax_amount=4800.61,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6649.65,
                    id='8cd9e731-9c17-47d5-a5f7-7b114eeb52ff',
                    name='Maxine Hilll',
                ),
                total_amount=1972.59,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='814d4c98-e0c2-4bb8-9eb7-5dad636c6005',
                            name='Wendy Stanton',
                        ),
                        shared.TrackingCategoryRef(
                            id='b31180f7-39ae-49e0-97eb-809e2810331f',
                            name='Dr. Misty Lindgren',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='minus',
                        id='700b607f-3c93-4c73-b9da-3f2ceda7e23f',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='57411faf-4b75-444e-872e-802857a5b404',
                        name='Robin O'Hara',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='75f1400e-764a-4d73-b4ec-1b781b36a080',
                        name='Mr. Dwayne Sipes PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='fada200e-f042-42eb-a164-cf9ab8366c72',
                        name='Faith Zulauf',
                    ),
                ],
                unit_amount=6176.57,
            ),
            shared.BillCreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='e06bee48-25c1-4fc0-a115-c80bff918544',
                    name='Simon Gleason',
                ),
                description='vero',
                discount_amount=9851.09,
                discount_percentage=7737.11,
                item_ref=shared.ItemRef(
                    id='ce8f1977-773e-4635-a2a7-b408f05e3d48',
                    name='Clint Ortiz',
                ),
                quantity=1105.22,
                sub_total=2010.96,
                tax_amount=6308.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=748.95,
                    id='f5fd9425-9c0b-436f-a5ea-944f3b756c11',
                    name='Charlie Schaefer',
                ),
                total_amount=6837.27,
                tracking=shared.BillCreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='12624383-5bbc-405a-a3a4-5cefc5fde10a',
                            name='Della Treutel III',
                        ),
                        shared.TrackingCategoryRef(
                            id='9e510019-c6dc-45e3-8762-799bfbbe6949',
                            name='Jonathon Collins',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='incidunt',
                        id='ecae6c3d-5db3-4ade-bd5d-aea4c506a8aa',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='c02644cf-5e9d-49a4-978a-dc1ac600dec0',
                        name='Julie Murazik',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='2e2ec09f-f8f0-4f81-aff3-477c13e902c1',
                        name='Cheryl Conn',
                    ),
                ],
                unit_amount=46.54,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='Bill Credit Note with 1 line items, totaling 805.78',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=3881.69,
                    total_amount=4016.88,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8151a472-af92-43c5-949f-83f350cf876f',
                        name='Mr. Robin Miller',
                    ),
                    currency='USD',
                    currency_rate=9087.34,
                    id='cbb4e243-cf78-49ff-afed-a53e5ae6e0ac',
                    note='quasi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eius',
                    total_amount=7861.89,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6200.54,
                    total_amount=7935.68,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='247c8837-3a40-4e19-82f3-2e55055756f5',
                        name='Maurice Hoppe MD',
                    ),
                    currency='EUR',
                    currency_rate=177.68,
                    id='af2dfe13-db4f-462c-ba3f-8941aebc0b80',
                    note='deserunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='excepturi',
                    total_amount=1674.35,
                ),
            ),
        ],
        remaining_credit=0,
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillCreditNoteStatus.PAID,
        sub_total=805.78,
        supplemental_data=shared.SupplementalData(
            content={
                "dolor": {
                    "sed": 'accusamus',
                    "optio": 'delectus',
                    "minus": 'quo',
                },
                "quos": {
                    "voluptatum": 'iste',
                    "corporis": 'accusantium',
                    "illo": 'aut',
                    "doloribus": 'nostrum',
                },
                "at": {
                    "neque": 'pariatur',
                    "vel": 'sapiente',
                    "mollitia": 'quae',
                    "quos": 'aperiam',
                },
                "non": {
                    "ad": 'aliquam',
                    "quisquam": 'quas',
                    "consequuntur": 'maiores',
                    "inventore": 'aliquid',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='8a363c88-73e4-4843-80b1-f6b8ca275a60',
            supplier_name='fuga',
        ),
        total_amount=805.78,
        total_discount=0,
        total_tax_amount=0,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2958.92,
                name='Jay Morar',
            ),
        ],
    ),
    bill_credit_note_id='placeat',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=378403,
)

res = s.bill_credit_notes.update(req)

if res.update_bill_credit_note_response is not None:
    # handle response
```
