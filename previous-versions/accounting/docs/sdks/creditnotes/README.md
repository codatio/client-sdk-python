# CreditNotes
(*credit_notes*)

## Overview

Credit notes

### Available Operations

* [create](#create) - Create credit note
* [get](#get) - Get credit note
* [get_create_update_model](#get_create_update_model) - Get create/update credit note model
* [list](#list) - List credit notes
* [update](#update) - Update credit note

## create

The *Create credit note* endpoint creates a new [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=Decimal('7239.42'),
        additional_tax_percentage=Decimal('7119.91'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='provident',
        currency='EUR',
        currency_rate=Decimal('7000.45'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='dignissimos',
            id='5dad636c-6005-403d-8bb3-1180f739ae9e',
        ),
        discount_percentage=Decimal('100.63'),
        id='57eb809e-2810-4331-b398-1d4c700b607f',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='c93c73b9-da3f-42ce-9a7e-23f2257411fa',
                    name='Kyle Reichel',
                ),
                description='labore',
                discount_amount=Decimal('2543.82'),
                discount_percentage=Decimal('9211.93'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='472e8028-57a5-4b40-863a-7d575f1400e7',
                    name='Carrie Pagac',
                ),
                quantity=Decimal('2327.72'),
                sub_total=Decimal('2006.37'),
                tax_amount=Decimal('3106.29'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('9294.76'),
                    id='c1b781b3-6a08-4088-9100-efada200ef04',
                    name='Phyllis Tremblay Sr.',
                ),
                total_amount=Decimal('3979.88'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='4cf9ab83-66c7-423f-bda9-e06bee4825c1',
                            name='Colin Berge Sr.',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='enim',
                        id='c80bff91-8544-4ec4-adef-cce8f1977773',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='3562a7b4-08f0-45e3-948f-daf313a1f5fd',
                        name='Troy Champlin',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='0b36f25e-a944-4f3b-b56c-11f6c37a5126',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='243835bb-c05a-423a-85ce-fc5fde10a0ce',
                        name='Mildred Kautzer',
                    ),
                ],
                unit_amount=Decimal('3548.21'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='accusantium',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('5905.85'),
                    total_amount=Decimal('7658.33'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6dc5e347-6279-49bf-bbe6-949fb2bb4eca',
                        name='Ben Satterfield',
                    ),
                    currency='USD',
                    currency_rate=Decimal('8487.22'),
                    id='b3adebd5-daea-44c5-86a8-aa94c02644cf',
                    note='nostrum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='unde',
                    total_amount=Decimal('8603.11'),
                ),
            ),
        ],
        remaining_credit=Decimal('6213.93'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.DRAFT,
        sub_total=Decimal('3442.89'),
        supplemental_data=shared.SupplementalData(
            content={
                "esse": {
                    "corrupti": 'fuga',
                },
            },
        ),
        total_amount=Decimal('8152.25'),
        total_discount=Decimal('7736.59'),
        total_tax_amount=Decimal('986.1'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('6472.18'),
                name='Dr. Rick Bauch',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=807564,
)

res = s.credit_notes.create(req)

if res.create_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateCreditNoteRequest](../../models/operations/createcreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.CreateCreditNoteResponse](../../models/operations/createcreditnoteresponse.md)**


## get

The *Get credit note* endpoint returns a single credit note for a given creditNoteId.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support getting a specific credit note.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreditNoteRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    credit_note_id='consequatur',
)

res = s.credit_notes.get(req)

if res.credit_note is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetCreditNoteRequest](../../models/operations/getcreditnoterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetCreditNoteResponse](../../models/operations/getcreditnoteresponse.md)**


## get_create_update_model

﻿The *Get create/update credit note model* endpoint returns the expected data for the request payload when creating and updating a [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company and integration.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating and updating a credit note.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetCreateUpdateCreditNotesModelRequest](../../models/operations/getcreateupdatecreditnotesmodelrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetCreateUpdateCreditNotesModelResponse](../../models/operations/getcreateupdatecreditnotesmodelresponse.md)**


## list

The *List credit notes* endpoint returns a list of [credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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
    query='eaque',
)

res = s.credit_notes.list(req)

if res.credit_notes is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListCreditNotesRequest](../../models/operations/listcreditnotesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[operations.ListCreditNotesResponse](../../models/operations/listcreditnotesresponse.md)**


## update

The *Update credit note* endpoint updates an existing [credit note](https://docs.codat.io/accounting-api#/schemas/CreditNote) for a given company's connection.

[Credit notes](https://docs.codat.io/accounting-api#/schemas/CreditNote) are issued to a customer to indicate debt, typically with reference to a previously issued invoice and/or purchase.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update credit note model](https://docs.codat.io/accounting-api#/operations/get-create-update-creditNotes-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=creditNotes) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCreditNoteRequest(
    credit_note=shared.CreditNote(
        additional_tax_amount=Decimal('1023.9'),
        additional_tax_percentage=Decimal('6271.61'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='blanditiis',
        currency='GBP',
        currency_rate=Decimal('1698.19'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='officiis',
            id='2ec09ff8-f0f8-416f-b347-7c13e902c141',
        ),
        discount_percentage=Decimal('1391.33'),
        id='5b0960a6-6815-41a4-b2af-923c5949f83f',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='50cf876f-fb90-41c6-acbb-4e243cf789ff',
                    name='Emilio Waters',
                ),
                description='corporis',
                discount_amount=Decimal('2465.77'),
                discount_percentage=Decimal('8877.01'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='5ae6e0ac-184c-42b9-8247-c88373a40e19',
                    name='Ashley Wunsch',
                ),
                quantity=Decimal('9368.45'),
                sub_total=Decimal('3305.96'),
                tax_amount=Decimal('3731.06'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('510.53'),
                    id='55756f5d-56d0-4bd0-af2d-fe13db4f62cb',
                    name='Jacob Wehner',
                ),
                total_amount=Decimal('2524.73'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='1aebc0b8-0a69-424d-bb2e-cfcc8f895010',
                            name='Gordon Strosin',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='pariatur',
                        id='6fa1804e-54c8-42f1-a8a3-63c8873e4843',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='b1f6b8ca-275a-460a-84c4-95cc699171b5',
                        name='Blanca Carroll',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='accountTransaction',
                        id='1cf4b888-ebdf-4c4c-8ca9-9bc7fc0b2dce',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='10873e42-b006-4d67-8878-ba8581a58208',
                        name='Lloyd Grant',
                    ),
                ],
                unit_amount=Decimal('9657.35'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='natus',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=Decimal('3125.11'),
                    total_amount=Decimal('9853.79'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2eac5565-d307-4cfe-a812-06e2813fa4a4',
                        name='Leticia Gerlach PhD',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('9998.54'),
                    id='2132af03-102d-4514-b4cc-6f18bf9621a6',
                    note='animi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='tenetur',
                    total_amount=Decimal('4934.07'),
                ),
            ),
        ],
        remaining_credit=Decimal('4578.35'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.PAID,
        sub_total=Decimal('4610.5'),
        supplemental_data=shared.SupplementalData(
            content={
                "eveniet": {
                    "earum": 'velit',
                },
            },
        ),
        total_amount=Decimal('8847.65'),
        total_discount=Decimal('2633.46'),
        total_tax_amount=Decimal('7019.78'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('9301.11'),
                name='Brittany Cole',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    credit_note_id='quis',
    force_update=False,
    timeout_in_minutes=704402,
)

res = s.credit_notes.update(req)

if res.update_credit_note_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateCreditNoteRequest](../../models/operations/updatecreditnoterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.UpdateCreditNoteResponse](../../models/operations/updatecreditnoteresponse.md)**

