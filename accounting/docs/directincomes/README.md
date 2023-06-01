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

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directIncomes) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateDirectIncomeRequest(
    direct_income=shared.DirectIncome(
        contact_ref=shared.ContactRef(
            data_type='placeat',
            id='9b4caa1c-fe9e-415d-b903-907f37831983',
        ),
        currency='fugiat',
        currency_rate=2628.24,
        id='2e54a854-6659-47c5-8233-c1471d51aaa6',
        issue_date='illum',
        line_items=[
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='f5abd648-7c5f-4c2b-862a-00bef69e1001',
                    name='Jo Homenick DDS',
                ),
                description='quibusdam',
                discount_amount=6828.88,
                discount_percentage=4685.8,
                item_ref=shared.ItemRef(
                    id='afded84a-35a4-4123-8e1a-735ac26ae33b',
                    name='Cary Medhurst MD',
                ),
                quantity=5021.5,
                sub_total=9993.15,
                tax_amount=2679.18,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4014.66,
                    id='bca1106f-e965-4b71-9d08-cf88ec9f7b99',
                    name='Miss Maurice Hauck',
                ),
                total_amount=3393.33,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ed333bb0-ce8a-4a65-832a-986eb7e14ca5',
                        name='Ellen Baumbach',
                    ),
                    shared.TrackingCategoryRef(
                        id='15009701-9a48-4f88-ace7-bf904e01105d',
                        name='Ms. Marsha Marks III',
                    ),
                ],
                unit_amount=1337.9,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='c6beb68a-0f65-47b7-903a-1480f8de30f0',
                    name='Shelly Steuber Jr.',
                ),
                description='commodi',
                discount_amount=1030.68,
                discount_percentage=5433.17,
                item_ref=shared.ItemRef(
                    id='d97e1522-9751-40da-8031-2292cc61c2a7',
                    name='Kathy Reichel',
                ),
                quantity=4877.46,
                sub_total=9182.86,
                tax_amount=8796.44,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=935.56,
                    id='02da2de3-5f8e-401b-b33e-aab45402ac17',
                    name='Amber Rogahn DDS',
                ),
                total_amount=8111.67,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fc61aae5-eb5f-40c4-92b5-744d08a2267a',
                        name='Sheldon Toy',
                    ),
                    shared.TrackingCategoryRef(
                        id='e3c71ad3-1bec-4b83-9237-8ae3bfc23d94',
                        name='Sarah Okuneva',
                    ),
                    shared.TrackingCategoryRef(
                        id='6a495bac-707f-406b-a8ec-c86492386f62',
                        name='Wade Kemmer',
                    ),
                ],
                unit_amount=2765.07,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='cc6b7889-0a3f-4d3c-81da-10f8c23df931',
                    name='Homer Franecki',
                ),
                description='tempore',
                discount_amount=3267.12,
                discount_percentage=1152.02,
                item_ref=shared.ItemRef(
                    id='fad94acc-9435-4137-b26d-15321b832a56',
                    name='Ms. Brent Marquardt DVM',
                ),
                quantity=9463.17,
                sub_total=4373.51,
                tax_amount=84.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8836.41,
                    id='b9a6658e-69a4-4b84-bd38-2dbec75c68c6',
                    name='Alma Hartmann',
                ),
                total_amount=3818.37,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ce304d88-49bf-4821-8c33-7f96bb0c69e3',
                        name='Theresa Schumm I',
                    ),
                    shared.TrackingCategoryRef(
                        id='44ba9f78-a5c0-4ed7-aab6-2e97261fb0c5',
                        name='Lionel Connelly',
                    ),
                    shared.TrackingCategoryRef(
                        id='51996b5b-4b50-4eef-b12b-7a7ab0344b17',
                        name='Nancy Johnson',
                    ),
                ],
                unit_amount=8478.05,
            ),
            shared.DirectIncomeLineItem(
                account_ref=shared.AccountRef(
                    id='eebef897-f3dd-40cc-933f-11b3e4e080aa',
                    name='Ms. Cynthia Gorczany',
                ),
                description='accusamus',
                discount_amount=7590.59,
                discount_percentage=4841.4,
                item_ref=shared.ItemRef(
                    id='59e02f37-02c5-4c8e-ad30-ead3104fa447',
                    name='Tanya Prohaska',
                ),
                quantity=4960.06,
                sub_total=3249.55,
                tax_amount=7261.44,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2839.36,
                    id='4282821f-db2f-469e-9926-7c71cc8d3cd4',
                    name='Dolores Lehner I',
                ),
                total_amount=3691.81,
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a82c808f-e275-41a2-847c-0449e143f961',
                        name='Kelvin Robel',
                    ),
                    shared.TrackingCategoryRef(
                        id='40d5a11f-a436-4e62-9923-3f95c9d23739',
                        name='Leticia Kris',
                    ),
                    shared.TrackingCategoryRef(
                        id='b5db4f50-0183-4feb-9f67-6b7206dab750',
                        name='Jill Davis',
                    ),
                ],
                unit_amount=3951.94,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='dolore',
        note='in',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='fugiat',
                    currency='minus',
                    currency_rate=2693.91,
                    total_amount=1928.71,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='9ed8c432-0f41-4240-9448-7ac693b94c3b',
                        name='Ismael Cummings',
                    ),
                    currency='blanditiis',
                    currency_rate=8422.41,
                    id='795aa42f-c405-4669-b69a-006d21249450',
                    note='atque',
                    paid_on_date='quasi',
                    reference='natus',
                    total_amount=8518.84,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='odio',
                    currency='quo',
                    currency_rate=2153.91,
                    total_amount=7379.94,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='1b418440-60e0-4031-8d02-3dc901f5afd2',
                        name='Rafael Sanford',
                    ),
                    currency='praesentium',
                    currency_rate=2573.24,
                    id='6ae9d892-53c8-4962-b489-6bf51e4652d3',
                    note='cumque',
                    paid_on_date='nesciunt',
                    reference='aliquam',
                    total_amount=2338.04,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='at',
                    currency='suscipit',
                    currency_rate=625.56,
                    total_amount=4649.44,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='78af4912-4772-45e6-a190-9e91044a5de5',
                        name='Shaun Schowalter',
                    ),
                    currency='eaque',
                    currency_rate=3973.05,
                    id='670cf1cf-5932-4605-a51e-66bb426897d9',
                    note='omnis',
                    paid_on_date='dolorum',
                    reference='qui',
                    total_amount=8610.2,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='velit',
                    currency='amet',
                    currency_rate=3714.09,
                    total_amount=3815.34,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='70e93ee6-cf59-4f35-8aae-acae323a31bf',
                        name='Miss Luz Osinski',
                    ),
                    currency='molestias',
                    currency_rate=4623.08,
                    id='716c802c-c9e0-4c7d-9d32-3f1aa63ed9cf',
                    note='et',
                    paid_on_date='nobis',
                    reference='quas',
                    total_amount=3675.11,
                ),
            ),
        ],
        reference='commodi',
        source_modified_date='soluta',
        sub_total=7787.26,
        supplemental_data=shared.SupplementalData(
            content={
                "id": {
                    "inventore": 'accusamus',
                    "maiores": 'odit',
                },
                "numquam": {
                    "numquam": 'culpa',
                    "aliquam": 'iusto',
                },
                "voluptatibus": {
                    "maxime": 'repellat',
                    "veritatis": 'inventore',
                    "autem": 'optio',
                },
            },
        ),
        tax_amount=8552.86,
        total_amount=8174.25,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=349223,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='ut',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='dolore',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDirectIncomeAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='numquam',
    timeout_in_minutes=639401,
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='reprehenderit',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDirectIncomeAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='nemo',
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
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadDirectIncomeAttachmentRequest(
    request_body=operations.UploadDirectIncomeAttachmentRequestBody(
        content='nisi'.encode(),
        request_body='consequuntur',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_income_id='praesentium',
)

res = s.direct_incomes.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
