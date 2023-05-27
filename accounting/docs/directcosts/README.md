# direct_costs

## Overview

Direct costs

### Available Operations

* [create](#create) - Create direct cost
* [download_attachment](#download_attachment) - Download direct cost attachment
* [get](#get) - Get direct cost
* [get_attachment](#get_attachment) - Get direct cost attachment
* [get_create_model](#get_create_model) - Get create direct cost model
* [list](#list) - List direct costs
* [list_attachments](#list_attachments) - List direct cost attachments
* [upload_attachment](#upload_attachment) - Upload direct cost attachment

## create

Posts a new direct cost to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create direct cost model](https://docs.codat.io/accounting-api#/operations/get-create-directCosts-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) to see which integrations support this endpoint.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateDirectCostRequest(
    direct_cost=shared.DirectCost(
        contact_ref=shared.ContactRef(
            data_type='quis',
            id='93260525-1e66-4bb4-a689-7d99a2d33567',
        ),
        currency='ipsa',
        currency_rate=8842.06,
        id='93ee6cf5-9f35-48aa-aaca-e323a31bf7ba',
        issue_date='architecto',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='c97716c8-02cc-49e0-87d9-d323f1aa63ed',
                    name='Miss Earnest Zemlak',
                ),
                description='nemo',
                discount_amount=4125.09,
                discount_percentage=7425.62,
                item_ref=shared.ItemRef(
                    id='cba51ef2-454a-447f-acf1-16cdd5444a75',
                    name='Andrea Lang',
                ),
                quantity=8116.96,
                sub_total=4938,
                tax_amount=8445.24,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8127.53,
                    id='9efaf43d-c623-4620-b313-8f30df3db022',
                    name='Donnie Ondricka',
                ),
                total_amount=3413.59,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='delectus',
                        id='b8f652eb-b9d3-4838-b879-0243b293dab3',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='vero',
                            id='917f50fd-a04c-48b1-bb55-a292b0bc3bb7',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4664eb1d-0338-48b0-91bb-17afee74b6fe',
                        name='Marion Greenfelder',
                    ),
                    shared.TrackingCategoryRef(
                        id='c7edaf39-d16f-4bf7-afd1-62b303e3023b',
                        name='Manuel Tillman',
                    ),
                ],
                unit_amount=1973.88,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='16cf55b4-3135-453c-8f1c-204c4adcc990',
                    name='Ms. Jody Hamill',
                ),
                description='cum',
                discount_amount=5405.93,
                discount_percentage=3840.98,
                item_ref=shared.ItemRef(
                    id='48cefa78-f1e2-4d3b-901e-0952bbb4cbb1',
                    name='Mrs. Courtney Kuhic',
                ),
                quantity=5685.48,
                sub_total=3158.92,
                tax_amount=6366.25,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2930.95,
                    id='169c1387-271e-418e-a9e4-5118c2cc57fb',
                    name='Tyler Abernathy MD',
                ),
                total_amount=4645.41,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='molestias',
                        id='ed29a9d4-eea8-4565-8c2d-4f4c88be4f27',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='tenetur',
                            id='d9667e46-c51d-42ff-aa58-dcef234c955b',
                        ),
                        shared.InvoiceTo(
                            data_type='natus',
                            id='bdf2190a-bd9b-4bcc-a725-ec2659ce0280',
                        ),
                        shared.InvoiceTo(
                            data_type='corrupti',
                            id='40c69ef6-8e45-4c8a-9dfa-c754500430c6',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='32b4391f-df01-4c3e-91e8-f7bc69d460a7',
                        name='Alyssa Satterfield',
                    ),
                    shared.TrackingCategoryRef(
                        id='26d10f1e-f263-41c7-80f0-f873f9d5c25f',
                        name='Miss Alfred VonRueden',
                    ),
                ],
                unit_amount=6464.87,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='4a4253c3-0257-411f-82c7-e7dc548be09e',
                    name='Diane Paucek',
                ),
                description='dolores',
                discount_amount=816.73,
                discount_percentage=3686.17,
                item_ref=shared.ItemRef(
                    id='ca12a4ba-9d59-4988-992c-fd0c77c53e7e',
                    name='Chelsea Gibson',
                ),
                quantity=3952.6,
                sub_total=9251.57,
                tax_amount=5344.54,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7493.37,
                    id='90bac384-e239-4670-bfec-31c50824d189',
                    name='Curtis Keebler',
                ),
                total_amount=6908.65,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='sunt',
                        id='d27eb707-aa60-4c8f-a46e-6177db9db3b7',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='voluptatibus',
                            id='fbb6970e-e770-4e36-897e-f7c206e61b0d',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='08714c20-a3d9-4863-bca8-5c3fe65574db',
                        name='Dominick Mraz',
                    ),
                ],
                unit_amount=4622.78,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='c98f13af-28db-42cf-abf4-f3ded356d7e1',
                    name='Miss Whitney Dach',
                ),
                description='occaecati',
                discount_amount=5317.63,
                discount_percentage=1078.63,
                item_ref=shared.ItemRef(
                    id='96d55af6-9a1c-44b7-9ae3-3681c23c39a7',
                    name='Ms. Michael Torphy',
                ),
                quantity=7162.96,
                sub_total=938.38,
                tax_amount=1709.49,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7710.42,
                    id='5ba825fe-22cd-45cb-a6fb-fec932af6813',
                    name='Angel Harvey',
                ),
                total_amount=9353.01,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingRecordReference(
                        data_type='placeat',
                        id='ec2dd691-6f7f-4c7d-9a70-ec60e6075894',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='autem',
                            id='1c14cd90-227e-437c-8d97-7f1a5491abe9',
                        ),
                        shared.InvoiceTo(
                            data_type='dignissimos',
                            id='51b106d2-3e03-4e69-815a-ae99fcde9e72',
                        ),
                        shared.InvoiceTo(
                            data_type='iste',
                            id='c9d4f2d8-a446-440c-a60d-b73a2f93f467',
                        ),
                        shared.InvoiceTo(
                            data_type='at',
                            id='c0d8da56-1220-426a-b8f2-77485c1976af',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='80da7a08-9fc4-44db-a745-30e5cc7c6d0c',
                        name='Spencer Wintheiser',
                    ),
                    shared.TrackingCategoryRef(
                        id='d334b6f6-23bc-4eca-b50a-ee5e0da8b9af',
                        name='Mrs. Alberta Stoltenberg',
                    ),
                    shared.TrackingCategoryRef(
                        id='86e7b413-cbe2-4d17-adc1-c43d40f61d17',
                        name='Christine Hane',
                    ),
                ],
                unit_amount=7322.16,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='debitis',
        note='enim',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='saepe',
                    currency='non',
                    currency_rate=9407.97,
                    total_amount=4601.8,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='21184077-2f32-4e3b-89db-e0f23b7b6d99',
                        name='Dianne Simonis',
                    ),
                    currency='facere',
                    currency_rate=8999.7,
                    id='d477680f-c7a1-47a8-ae5e-82fd28d1040a',
                    note='iusto',
                    paid_on_date='debitis',
                    reference='sint',
                    total_amount=1083.49,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='ratione',
                    currency='omnis',
                    currency_rate=1850.41,
                    total_amount=6781.29,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b44cb183-5008-4f46-9ce5-3e914498a9ba',
                        name='Alma Beahan',
                    ),
                    currency='pariatur',
                    currency_rate=9692.94,
                    id='de410c37-daa9-4182-a49d-9625d3caffc1',
                    note='cupiditate',
                    paid_on_date='blanditiis',
                    reference='voluptates',
                    total_amount=9025.46,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='animi',
                    currency='modi',
                    currency_rate=3101.3,
                    total_amount=3390.36,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2792bcd4-40ea-498b-acce-0486de0d56d7',
                        name='Mrs. Verna Anderson',
                    ),
                    currency='accusantium',
                    currency_rate=2062.3,
                    id='e8dc626f-f77c-4656-b5f5-b70e3e4cfcc6',
                    note='dolorum',
                    paid_on_date='cupiditate',
                    reference='ab',
                    total_amount=8969.21,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='maxime',
                    currency='veniam',
                    currency_rate=1816.73,
                    total_amount=3974.18,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='24d00014-ef45-4cea-91ac-53ebb6587f34',
                        name='Megan Bergnaum',
                    ),
                    currency='ipsam',
                    currency_rate=7395.69,
                    id='9acee400-ae9f-492c-af1b-025f1d14718c',
                    note='nisi',
                    paid_on_date='voluptatibus',
                    reference='est',
                    total_amount=1274.87,
                ),
            ),
        ],
        reference='doloribus',
        source_modified_date='mollitia',
        sub_total=8418.47,
        supplemental_data=shared.SupplementalData(
            content={
                "cumque": {
                    "commodi": 'porro',
                },
            },
        ),
        tax_amount=3298.49,
        total_amount=8155.84,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=571303,
)

res = s.direct_costs.create(req)

if res.create_direct_cost_response is not None:
    # handle response
```

## download_attachment

Downloads an attachment for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

Gets the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetDirectCostRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.get(req)

if res.direct_cost is not None:
    # handle response
```

## get_attachment

Gets the specified direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetDirectCostAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_model

Get create direct cost model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetCreateDirectCostsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.direct_costs.get_create_model(req)

if res.push_option is not None:
    # handle response
```

## list

Gets the direct costs for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListDirectCostsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='exercitationem',
)

res = s.direct_costs.list(req)

if res.direct_costs is not None:
    # handle response
```

## list_attachments

Gets all attachments for the specified direct cost for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListDirectCostAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## upload_attachment

Posts a new direct cost attachment for a given company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UploadDirectCostAttachmentRequest(
    request_body=operations.UploadDirectCostAttachmentRequestBody(
        content='quaerat'.encode(),
        request_body='in',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
