# direct_incomes

## Overview

Direct incomes

### Available Operations

* [create](#create) - Create direct income
* [download_attachment](#download_attachment) - Download direct income attachment
* [get](#get) - Get direct income
* [get_attachment](#get_attachment) - Get direct income attachment
* [get_create_model](#get_create_model) - Get create direct income model
* [list](#list) - List direct incomes
* [list_attachments](#list_attachments) - List direct income attachments
* [upload_attachment](#upload_attachment) - Create direct income attachment

## create

Posts a new direct income to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct income model](https://docs.codat.io/accounting-api#/operations/get-create-directIncomes-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type='magni',
            id='cdd14fc4-3b70-4bca-88fa-70c43351c3dd',
        ),
        currency='beatae',
        currency_rate=8962.8,
        id='b8f7f75f-4f23-4f1c-8a58-6c3ae7d7b67f',
        issue_date='officiis',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='f5e142d9-5b1d-4bec-aff7-c4b156e92782',
                    name='Holly Toy',
                ),
                description='esse',
                discount_amount=3851.06,
                discount_percentage=5122.23,
                item_ref=shared.ItemRef(
                    id='17468063-f799-4b79-96c0-b0fa0bb20a40',
                    name='Roland Ryan',
                ),
                quantity=8828.41,
                sub_total=3996.96,
                tax_amount=3081.27,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=498.27,
                    id='64272657-b01a-407c-88fd-3921c257930d',
                    name='Elisa Bailey',
                ),
                total_amount=6488.15,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='efa46d36-6dfa-4101-9a09-1b3ec8b53862',
                        name='Alonzo Bins',
                    ),
                ],
                unit_amount=8706.71,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='14fe72e5-21f9-4030-bdfc-338397fffa6d',
                    name='Meredith Dickinson V',
                ),
                description='alias',
                discount_amount=9869.41,
                discount_percentage=7770.83,
                item_ref=shared.ItemRef(
                    id='157ac9fe-1961-4ce9-be41-c869dd7d9719',
                    name='Michael Kulas',
                ),
                quantity=154.46,
                sub_total=498.92,
                tax_amount=6470.89,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3619.89,
                    id='8ffd2967-df8f-4d88-aa8e-60be620cd9c5',
                    name='Darrin Schuppe II',
                ),
                total_amount=7561.02,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='752512be-ae1d-487e-8c5f-dcea8e7a8831',
                        name='Lucy Howell',
                    ),
                ],
                unit_amount=8726.91,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='a6d77c1d-8606-4623-bd42-27866db8a749',
                    name='Glenn McLaughlin',
                ),
                description='exercitationem',
                discount_amount=988.25,
                discount_percentage=1089.18,
                item_ref=shared.ItemRef(
                    id='cc75e4f0-c004-4b5b-b758-cc94562f0069',
                    name='Gwendolyn Hickle',
                ),
                quantity=8194.9,
                sub_total=955.55,
                tax_amount=6650.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1149.02,
                    id='73d84bbe-24f2-4983-8afb-0735cb6285d4',
                    name='Fred Mitchell',
                ),
                total_amount=6662.15,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e169156f-7d2e-4e20-9505-bf03a93e9448',
                        name='Myra Pfannerstill',
                    ),
                ],
                unit_amount=9771.81,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='b1078903-2ac3-4331-b2e2-dd79ec74ba7e',
                    name='Jaime Schuster',
                ),
                description='ipsum',
                discount_amount=4175.44,
                discount_percentage=9669.27,
                item_ref=shared.ItemRef(
                    id='d1ccc341-c865-4734-b4f0-a740fb4ab441',
                    name='Ms. Dale Nolan',
                ),
                quantity=4588.95,
                sub_total=4145.21,
                tax_amount=2428.43,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5966.4,
                    id='95d808bb-e794-4455-abc5-50a1c426b59c',
                    name='Rodney Jerde',
                ),
                total_amount=8142.27,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c135582c-1b85-45e8-89d9-ef932e9000a1',
                        name='Sandy Stokes Sr.',
                    ),
                    shared.TrackingCategoryRef(
                        id='4208efd2-3411-4898-a738-79efbe8baeba',
                        name='Geoffrey Kuhic',
                    ),
                    shared.TrackingCategoryRef(
                        id='536e9035-1bb9-4763-9720-b77a5a5365a7',
                        name='Timmy Bernier',
                    ),
                    shared.TrackingCategoryRef(
                        id='71f01c0d-361f-4ed8-9c5e-ffb453e9089e',
                        name='Roland Bode',
                    ),
                ],
                unit_amount=7471.07,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ut',
        note='at',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='perspiciatis',
                    currency='molestiae',
                    currency_rate=7361.58,
                    total_amount=8169.35,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='d9c985e4-3734-4a5d-b2d9-edd785be5e7a',
                        name='Sheldon Hermann',
                    ),
                    currency='occaecati',
                    currency_rate=4720.94,
                    id='ba6281f4-4e3a-4233-94a6-8cc80d30ff72',
                    note='illo',
                    paid_on_date='aliquid',
                    reference='quaerat',
                    total_amount=8368.03,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='alias',
                    currency='deserunt',
                    currency_rate=5794.14,
                    total_amount=1167.29,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='fe9d9655-3b89-4e00-89c6-692de7b35622',
                        name='Christine Nikolaus',
                    ),
                    currency='error',
                    currency_rate=7417.47,
                    id='4ae7b1a5-b908-4d4e-b049-1aa35d4a839f',
                    note='consequatur',
                    paid_on_date='ipsum',
                    reference='quidem',
                    total_amount=6785.88,
                ),
            ),
        ],
        reference='quidem',
        source_modified_date='molestiae',
        sub_total=4410.01,
        supplemental_data=shared.SupplementalData(
            content={
                "occaecati": {
                    "blanditiis": 'a',
                },
                "aut": {
                    "dicta": 'dolor',
                },
                "iste": {
                    "ut": 'exercitationem',
                    "sit": 'reprehenderit',
                    "officiis": 'accusantium',
                },
            },
        ),
        tax_amount=9159.68,
        total_amount=2348.84,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=577369,
)

res = s.direct_incomes.create(req)

if res.create_direct_income_response is not None:
    # handle response
```

## download_attachment

Downloads an attachment for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_incomes.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets the specified direct income for a given company and connection.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='impedit',
)

res = s.direct_incomes.get(req)

if res.direct_income is not None:
    # handle response
```

## get_attachment

Gets the specified direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    timeout_in_minutes=461855,
)

res = s.direct_incomes.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_model

Get create direct income model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) for integrations that support creating direct incomes.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateDirectIncomesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_incomes.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Lists the direct incomes for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListDirectIncomesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='saepe',
)

res = s.direct_incomes.list(req)

if res.direct_incomes is not None:
    # handle response
```

## list_attachments

Gets all attachments for the specified direct income for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_incomes.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_attachment

Posts a new direct income attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='odit'.encode(),
        request_body='consectetur',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='itaque',
)

res = s.direct_incomes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
