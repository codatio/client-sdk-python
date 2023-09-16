# CreditNotes

## Overview

Credit notes

### Available Operations

* [create](#create) - Create credit note
* [get](#get) - Get credit note
* [get_create_update_model](#get_create_update_model) - Get create/update credit note model
* [list](#list) - List credit notes
* [update](#update) - Update creditNote

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
        additional_tax_amount=Decimal('1363.57'),
        additional_tax_percentage=Decimal('7239.42'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='quas',
        currency='USD',
        currency_rate=Decimal('9222.99'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='rerum',
            id='75dad636-c600-4503-98bb-31180f739ae9',
        ),
        discount_percentage=Decimal('9202.72'),
        id='057eb809-e281-4033-9f39-81d4c700b607',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='3c93c73b-9da3-4f2c-ada7-e23f2257411f',
                    name='Toby Friesen',
                ),
                description='exercitationem',
                discount_amount=Decimal('2883'),
                discount_percentage=Decimal('2543.82'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='e472e802-857a-45b4-8463-a7d575f1400e',
                    name='Gertrude Gerhold',
                ),
                quantity=Decimal('4523.99'),
                sub_total=Decimal('2327.72'),
                tax_amount=Decimal('2006.37'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('3106.29'),
                    id='ec1b781b-36a0-4808-8d10-0efada200ef0',
                    name='Phyllis Denesik',
                ),
                total_amount=Decimal('1267.27'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='164cf9ab-8366-4c72-bffd-a9e06bee4825',
                            name='Willie Wiza PhD',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='architecto',
                        id='15c80bff-9185-444e-842d-efcce8f19777',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='e63562a7-b408-4f05-a3d4-8fdaf313a1f5',
                        name='Woodrow Mitchell III',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='accountTransaction',
                        id='c0b36f25-ea94-44f3-b756-c11f6c37a512',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6243835b-bc05-4a23-a45c-efc5fde10a0c',
                        name='Randy Carter',
                    ),
                ],
                unit_amount=Decimal('8927.08'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='architecto',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('828.76'),
                    total_amount=Decimal('5905.85'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c6dc5e34-7627-499b-bbbe-6949fb2bb4ec',
                        name='Bert Kassulke',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('3674.75'),
                    id='db3adebd-5dae-4a4c-906a-8aa94c02644c',
                    note='hic',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='officiis',
                    total_amount=Decimal('6036.5'),
                ),
            ),
        ],
        remaining_credit=Decimal('8603.11'),
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.CreditNoteStatus.PAID,
        sub_total=Decimal('2986.13'),
        supplemental_data=shared.SupplementalData(
            content={
                "nostrum": {
                    "esse": 'corrupti',
                },
            },
        ),
        total_amount=Decimal('6847.99'),
        total_discount=Decimal('8152.25'),
        total_tax_amount=Decimal('7736.59'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('986.1'),
                name='Mr. Forrest Howe',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=901008,
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
    credit_note_id='maxime',
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
    query='consequatur',
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
        additional_tax_amount=Decimal('510.07'),
        additional_tax_percentage=Decimal('1023.9'),
        allocated_on_date='2022-10-23T00:00:00.000Z',
        credit_note_number='porro',
        currency='USD',
        currency_rate=Decimal('608.92'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='magni',
            id='e2ec09ff-8f0f-4816-bf34-77c13e902c14',
        ),
        discount_percentage=Decimal('1165.58'),
        id='25b0960a-6681-451a-872a-f923c5949f83',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.CreditNoteLineItem(
                account_ref=shared.AccountRef(
                    id='350cf876-ffb9-401c-aecb-b4e243cf789f',
                    name='Lynn Wuckert',
                ),
                description='deserunt',
                discount_amount=Decimal('3590.97'),
                discount_percentage=Decimal('2465.77'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='e5ae6e0a-c184-4c2b-9c24-7c88373a40e1',
                    name='Micheal Cassin',
                ),
                quantity=Decimal('1397.45'),
                sub_total=Decimal('9368.45'),
                tax_amount=Decimal('3305.96'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('3731.06'),
                    id='055756f5-d56d-40bd-8af2-dfe13db4f62c',
                    name='Lorenzo Flatley',
                ),
                total_amount=Decimal('6211.4'),
                tracking=shared.CreditNoteLineItemTracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='41aebc0b-80a6-4924-93b2-ecfcc8f89501',
                            name='Melba Heaney',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='neque',
                        id='d6fa1804-e54c-482f-968a-363c8873e484',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='0b1f6b8c-a275-4a60-a04c-495cc699171b',
                        name='Miss Joyce Runolfsson',
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

