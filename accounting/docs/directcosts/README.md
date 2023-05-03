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

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

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
            data_type='tempore',
            id='e3444eac-8b3a-4287-9c6c-1fe606d07d2a',
        ),
        currency='error',
        currency_rate=7699.22,
        id='87ae50c1-6661-4a1d-9136-a7e8d53213f3',
        issue_date='asperiores',
        line_items=[
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='58752db7-64c5-49f0-a56c-ebcada29ca79',
                    name='Margie Bosco',
                ),
                description='ipsam',
                discount_amount=3887.15,
                discount_percentage=4752.38,
                item_ref=shared.ItemRef(
                    id='1663c530-b566-4516-ba36-38512ab2521b',
                    name='Emmett Daugherty IV',
                ),
                quantity=1632.92,
                sub_total=3028.14,
                tax_amount=4199.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4450.23,
                    id='b8a40bc0-5fab-40d6-90ed-f22a94d20ec9',
                    name='Raquel O'Keefe PhD',
                ),
                total_amount=1004.36,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type='hic',
                        id='465e8515-6fff-473f-9f54-fdd5ea954339',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='illum',
                            id='afb42a8d-6338-48e4-9803-9ea5f9b18a24',
                        ),
                        shared.InvoiceTo(
                            data_type='modi',
                            id='fd619039-dacd-438e-90dc-671dc7f1e3af',
                        ),
                        shared.InvoiceTo(
                            data_type='quasi',
                            id='5920c90d-1b49-401f-abd8-9c8a32639da5',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='7b6902b8-81a9-44f6-8366-4a8f0af8c691',
                        name='Clinton Ernser',
                    ),
                    shared.TrackingCategoryRef(
                        id='9fbaf947-6a2a-4e8d-8c50-c8a3512c7378',
                        name='Gwendolyn McLaughlin IV',
                    ),
                    shared.TrackingCategoryRef(
                        id='50a00e96-6ec7-436d-8319-4398c783c923',
                        name='Max Tillman',
                    ),
                ],
                unit_amount=8639.57,
            ),
            shared.DirectCostLineItem(
                account_ref=shared.AccountRef(
                    id='3ab7ca3c-5ca8-4649-a70c-fd5d6989b720',
                    name='Mr. Danielle Hamill',
                ),
                description='voluptate',
                discount_amount=8494.86,
                discount_percentage=879.6,
                item_ref=shared.ItemRef(
                    id='9ea83d49-2ed1-44b8-a2c1-954545e955dc',
                    name='Henry Langosh',
                ),
                quantity=6691.93,
                sub_total=3007.59,
                tax_amount=6029.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=65.39,
                    id='1c7c43ad-2daa-4784-aba3-d230edf73811',
                    name='Albert Bruen',
                ),
                total_amount=5162.31,
                tracking=shared.Tracking(
                    invoice_to=shared.TrackingInvoiceTo(
                        data_type='consequuntur',
                        id='bd7ed565-0762-41c5-8f4d-7396564c20a0',
                    ),
                    record_refs=[
                        shared.InvoiceTo(
                            data_type='dicta',
                            id='1a961d24-a7db-4b8f-932d-892cf7812cb5',
                        ),
                        shared.InvoiceTo(
                            data_type='architecto',
                            id='2c878240-bf54-48f8-8f8f-1bf0bc8e1f20',
                        ),
                    ],
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d5d831d0-0810-490f-a706-673f3a681c57',
                        name='Vickie Simonis',
                    ),
                    shared.TrackingCategoryRef(
                        id='742409a2-15e0-4860-9489-a5f63e3af3dd',
                        name='Marty Spencer',
                    ),
                ],
                unit_amount=2439.65,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='vero',
        note='placeat',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='vel',
                    currency='non',
                    currency_rate=2799.65,
                    total_amount=5083.73,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3e4a7a98-e4df-437e-85b8-955d413e13a4',
                        name='Mr. Todd Feil',
                    ),
                    currency='perferendis',
                    currency_rate=4391.35,
                    id='bd354c09-2bd7-434f-8244-9d86f4bb20fe',
                    note='nostrum',
                    paid_on_date='quibusdam',
                    reference='provident',
                    total_amount=857.97,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sunt',
                    currency='quod',
                    currency_rate=7101.48,
                    total_amount=9611.71,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='e749caf4-5a27-4f69-a2c9-e6d10e9db3ad',
                        name='Rosalie Kautzer I',
                    ),
                    currency='quasi',
                    currency_rate=374.55,
                    id='8d9c3374-7308-42b9-8f2a-b1fd5671e9c3',
                    note='dolores',
                    paid_on_date='commodi',
                    reference='neque',
                    total_amount=3182.94,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='eaque',
                    currency='officia',
                    currency_rate=2702.53,
                    total_amount=4310.35,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='7143789c-e0e9-4915-94d9-3a74c0252fe3',
                        name='Alex Rippin',
                    ),
                    currency='rerum',
                    currency_rate=5394.26,
                    id='b778ebb6-e1d2-4cf5-82ba-fb2cbc4635d5',
                    note='eveniet',
                    paid_on_date='eum',
                    reference='exercitationem',
                    total_amount=8718.88,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='culpa',
                    currency='alias',
                    currency_rate=1759.37,
                    total_amount=5500.66,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c3e951a1-e30f-4da9-a648-9d7b78673e13',
                        name='Arthur Dare',
                    ),
                    currency='rerum',
                    currency_rate=5872.48,
                    id='92494594-487f-45c8-8383-6b86b3cdf641',
                    note='minima',
                    paid_on_date='facilis',
                    reference='sit',
                    total_amount=2799.72,
                ),
            ),
        ],
        reference='magnam',
        source_modified_date='molestias',
        sub_total=9417.1,
        supplemental_data=shared.SupplementalData(
            content={
                "repellendus": {
                    "dicta": 'ratione',
                    "delectus": 'ut',
                    "officiis": 'itaque',
                    "nulla": 'distinctio',
                },
                "recusandae": {
                    "deleniti": 'tempore',
                    "reiciendis": 'commodi',
                },
                "sit": {
                    "molestias": 'quia',
                    "ipsam": 'rem',
                },
            },
        ),
        tax_amount=5640.67,
        total_amount=2626.64,
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=898366,
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
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=directCosts) for integrations that support creating direct costs.

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
    query='culpa',
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
        content='in'.encode(),
        request_body='aliquid',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    direct_cost_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.direct_costs.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
