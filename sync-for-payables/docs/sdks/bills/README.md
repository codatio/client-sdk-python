# bills

## Overview

Bills

### Available Operations

* [create](#create) - Create bill
* [download_attachment](#download_attachment) - Download bill attachment
* [get](#get) - Get bill
* [get_attachment](#get_attachment) - Get bill attachment
* [get_create_update_model](#get_create_update_model) - Get create/update bill model
* [list](#list) - List bills
* [list_attachments](#list_attachments) - List bill attachments
* [update](#update) - Update bill
* [upload_attachment](#upload_attachment) - Upload bill attachment

## create

The *Create bill* endpoint creates a new [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=2986.13,
        currency='USD',
        currency_rate=4609.09,
        due_date='2022-10-23T00:00:00.000Z',
        id='adc1ac60-0dec-4001-ac80-2e2ec09ff8f0',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='16ff3477-c13e-4902-8141-25b0960a6681',
                    name='Amy Murray',
                ),
                description='magni',
                discount_amount=6463.29,
                discount_percentage=9650.95,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='923c5949-f83f-4350-8f87-6ffb901c6ecb',
                    name='Joel Von',
                ),
                quantity=1940.58,
                sub_total=7581.94,
                tax_amount=9928.87,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4598.75,
                    id='89ffafed-a53e-45ae-ae0a-c184c2b9c247',
                    name='Isaac Lowe',
                ),
                total_amount=2271.56,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='40e1942f-32e5-4505-9756-f5d56d0bd0af',
                            name='Elena Zieme I',
                        ),
                        shared.TrackingCategoryRef(
                            id='db4f62cb-a3f8-4941-aebc-0b80a6924d3b',
                            name='Eloise Rowe',
                        ),
                        shared.TrackingCategoryRef(
                            id='c8f89501-0f5d-4d3d-afa1-804e54c82f16',
                            name='Rex Ernser',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='cumque',
                        id='8873e484-380b-41f6-b8ca-275a60a04c49',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.TrackingProjectRef(
                        id='c699171b-51c1-4bdb-9cf4-b888ebdfc4cc',
                        name='Lynn Marks',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='7fc0b2dc-e108-473e-82b0-06d678878ba8',
                        name='Kay Bradtke',
                    ),
                    shared.TrackingCategoryRef(
                        id='8208c54f-efa9-4c95-b2ea-c5565d307cfe',
                        name='Hugh Carroll III',
                    ),
                    shared.TrackingCategoryRef(
                        id='e2813fa4-a41c-4480-93f2-132af03102d5',
                        name='Danielle Willms',
                    ),
                    shared.TrackingCategoryRef(
                        id='c6f18bf9-621a-46a4-b77a-87ee3e4be752',
                        name='Gilbert Hayes',
                    ),
                ],
                unit_amount=2848.85,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='418e3bb9-1c8d-4975-a0e8-419d8f84f144',
                    name='Ms. Jimmy Turcotte',
                ),
                description='facere',
                discount_amount=7890.16,
                discount_percentage=7690.47,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='4aa5f3ca-bd90-45a9-b2e0-56728227b2d3',
                    name='Bobbie Greenfelder MD',
                ),
                quantity=9565.45,
                sub_total=4630.5,
                tax_amount=6671.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3073.06,
                    id='fa87cf53-5a6f-4ae5-8ebf-60c321f023b7',
                    name='Paulette Dibbert',
                ),
                total_amount=4939.45,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e1a0cc8d-f79f-40a3-96d9-0c364b7c15df',
                            name='Hubert Russel V',
                        ),
                        shared.TrackingCategoryRef(
                            id='8b1c4ee2-c8c6-4ce6-91fe-eb1c7cbdb6ee',
                            name='Jessie Hahn',
                        ),
                        shared.TrackingCategoryRef(
                            id='8ba25317-747d-4c91-9ad2-caf5dd6723dc',
                            name='Shawna Heller',
                        ),
                        shared.TrackingCategoryRef(
                            id='2f3a6b70-0878-4756-943f-5a6c98b55554',
                            name='Naomi Bauch',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='doloremque',
                        id='bcacc6cb-d6b5-4f3e-8909-304f926bad25',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.TrackingProjectRef(
                        id='819b474b-0ed2-40e5-a248-fff639a910ab',
                        name='Salvatore Paucek',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='676696e1-ec00-4221-b335-d89acb3ecfda',
                        name='Ellis Balistreri',
                    ),
                ],
                unit_amount=3075.32,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='9ef03004-978a-461f-a1cf-20688f77c1ff',
                    name='Jared Blick',
                ),
                description='fuga',
                discount_amount=665.96,
                discount_percentage=4057.89,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='3f2a3c80-a97f-4f33-8cdd-f857a9e61876',
                    name='Marc O'Connell Sr.',
                ),
                quantity=8600.27,
                sub_total=1665.42,
                tax_amount=6180.73,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8511.99,
                    id='fc94d6fe-cd79-4939-8066-a6d2d0003553',
                    name='Billie Schmitt',
                ),
                total_amount=390.47,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='6fa21e91-52cb-4311-9167-b8e3c8db0340',
                            name='Levi Johns',
                        ),
                        shared.TrackingCategoryRef(
                            id='64ffd455-906d-4126-bd48-e935c2c9e81f',
                            name='Elizabeth Roberts',
                        ),
                        shared.TrackingCategoryRef(
                            id='e43202d7-2165-4765-8664-1870d9d21f9a',
                            name='Miss Michael Ferry',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='debitis',
                        id='cc11a083-6429-4068-b850-2a55e7f73bc8',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.TrackingProjectRef(
                        id='e320a319-f4ba-4df9-87c9-a867bc424266',
                        name='Mrs. Geraldine Lueilwitz',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ca8ef51f-cb4c-4593-ac12-cdaad0ec7afe',
                        name='Robin Strosin PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='f448a47f-9390-4c58-8809-83dabf9ef3ff',
                        name='Levi Mohr',
                    ),
                    shared.TrackingCategoryRef(
                        id='f079af4d-3572-44cd-b0f4-d281187d5684',
                        name='Eloise Stoltenberg',
                    ),
                    shared.TrackingCategoryRef(
                        id='85a9065e-628b-4dfc-a032-b6c879923b7e',
                        name='Rosa Hand',
                    ),
                ],
                unit_amount=9897.65,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='deserunt',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=7733.55,
                    total_amount=4013.88,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='891f82ce-1157-4172-b053-77dcfa89df97',
                        name='Tasha Dickinson',
                    ),
                    currency='USD',
                    currency_rate=5228.24,
                    id='6092e9c3-ddc5-4f11-9dea-1026d541a4d1',
                    note='omnis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='sapiente',
                    total_amount=8876,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=1127.51,
                    total_amount=4878.39,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='80bccc0d-bbdd-4b48-8708-fb4e391e6bc1',
                        name='Vickie Sauer',
                    ),
                    currency='GBP',
                    currency_rate=9365.18,
                    id='54599ea3-4226-40e9-b200-ce78a1bd8fb7',
                    note='culpa',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='fuga',
                    total_amount=1175.46,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=7574.38,
                    total_amount=8855.23,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='723d4097-fa30-4e9a-b725-b29122030d83',
                        name='Dan Nolan',
                    ),
                    currency='USD',
                    currency_rate=4938.65,
                    id='99d22e8c-1f84-4938-a5fd-c42c876c2c2d',
                    note='delectus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='aliquam',
                    total_amount=7579.62,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=756.1,
                    total_amount=7513.47,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='76230f84-1fb1-4bd2-bfdb-14db6be5a685',
                        name='Luther Leuschke',
                    ),
                    currency='GBP',
                    currency_rate=6715.68,
                    id='e20da16f-c2b2-471a-a89c-57e854e90439',
                    note='quibusdam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='consequuntur',
                    total_amount=1594.69,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.BillPurchaseOrderReference(
                id='65694624-0708-44f7-ab37-cef02225194d',
                purchase_order_number='quidem',
            ),
            shared.BillPurchaseOrderReference(
                id='55410adc-669a-4f90-a26c-7cdc981f0689',
                purchase_order_number='corrupti',
            ),
        ],
        reference='quae',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.PARTIALLY_PAID,
        sub_total=7304.37,
        supplemental_data=shared.BillSupplementalData(
            content={
                "amet": {
                    "minus": 'hic',
                },
                "similique": {
                    "consectetur": 'labore',
                    "laudantium": 'cumque',
                    "adipisci": 'veritatis',
                },
                "nam": {
                    "magnam": 'aperiam',
                    "ducimus": 'itaque',
                    "necessitatibus": 'numquam',
                    "doloribus": 'eligendi',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='f0c42b78-f156-4263-98a0-dc766324ccb0',
            supplier_name='ea',
        ),
        tax_amount=7713.21,
        total_amount=5184.32,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=6651.83,
                name='Mr. Louise Sipes',
            ),
            shared.BillWithholdingTax(
                amount=1364.32,
                name='Miss Victor Kuhlman',
            ),
            shared.BillWithholdingTax(
                amount=8196.9,
                name='Courtney Conroy',
            ),
            shared.BillWithholdingTax(
                amount=8506.28,
                name='Kirk Heidenreich',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=704665,
)

res = s.bills.create(req)

if res.create_bill_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateBillRequest](../../models/operations/createbillrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.CreateBillResponse](../../models/operations/createbillresponse.md)**


## download_attachment

The *Download bill attachment* endpoint downloads a specific attachment for a given `billId` and `attachmentId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support downloading a bill attachment.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadBillAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    bill_id='EILBDVJVNUAGVKRQ',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.download_attachment(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DownloadBillAttachmentRequest](../../models/operations/downloadbillattachmentrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.DownloadBillAttachmentResponse](../../models/operations/downloadbillattachmentresponse.md)**


## get

The *Get bill* endpoint returns a single bill for a given `billId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a specific bill.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillRequest(
    bill_id='EILBDVJVNUAGVKRQ',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bills.get(req)

if res.bill is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetBillRequest](../../models/operations/getbillrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |


### Response

**[operations.GetBillResponse](../../models/operations/getbillresponse.md)**


## get_attachment

The *Get bill attachment* endpoint returns a specific attachment for a given `billId` and `attachmentId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a bill attachment.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetBillAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.get_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetBillAttachmentRequest](../../models/operations/getbillattachmentrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |


### Response

**[operations.GetBillAttachmentResponse](../../models/operations/getbillattachmentresponse.md)**


## get_create_update_model

﻿The *Get create/update bill model* endpoint returns the expected data for the request payload when creating and updating a [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company and integration.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBillModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetCreateUpdateBillModelRequest](../../models/operations/getcreateupdatebillmodelrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.GetCreateUpdateBillModelResponse](../../models/operations/getcreateupdatebillmodelresponse.md)**


## list

The *List bills* endpoint returns a list of [bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='dolore',
)

res = s.bills.list(req)

if res.bills is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListBillsRequest](../../models/operations/listbillsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListBillsResponse](../../models/operations/listbillsresponse.md)**


## list_attachments

The *List bill attachments* endpoint returns a list of attachments available to download for a given `billId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support listing bill attachments.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillAttachmentsRequest(
    bill_id='EILBDVJVNUAGVKRQ',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.list_attachments(req)

if res.attachments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListBillAttachmentsRequest](../../models/operations/listbillattachmentsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.ListBillAttachmentsResponse](../../models/operations/listbillattachmentsresponse.md)**


## update

The *Update bill* endpoint updates an existing [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=7053.07,
        currency='USD',
        currency_rate=3656.76,
        due_date='2022-10-23T00:00:00.000Z',
        id='693352f7-4533-4994-978d-e3b6e9389f5a',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='7f662550-a283-482a-8483-afd2315bba65',
                    name='Debra Kerluke',
                ),
                description='quae',
                discount_amount=4090.21,
                discount_percentage=9891.22,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='5bf6ae59-1bc8-4bde-b361-2b63c205fda8',
                    name='Sarah Kuhn',
                ),
                quantity=6839.8,
                sub_total=4359.31,
                tax_amount=5383.68,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6382.19,
                    id='9a35d086-b6f6-46fe-b020-e9f443b4257b',
                    name='Marshall Daugherty',
                ),
                total_amount=8301.97,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='da6a61ef-a219-4825-8fd0-a9eba47f7d3e',
                            name='Thomas Hahn',
                        ),
                        shared.TrackingCategoryRef(
                            id='40d6a183-1c87-4adf-996f-df1ad837ae80',
                            name='Ms. Terry Runolfsson',
                        ),
                        shared.TrackingCategoryRef(
                            id='95ba9986-78fa-43f6-9699-1af388ce0361',
                            name='Eva Gleichner',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='voluptate',
                        id='977a0ef2-f536-4028-afee-f934152ed7e2',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.TrackingProjectRef(
                        id='f4c157de-aa71-470f-845a-ccf667aaf9bb',
                        name='Laurence Blick',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e431d6bf-5c83-48fb-b8c2-0cb67fc4b425',
                        name='Perry Mayert',
                    ),
                    shared.TrackingCategoryRef(
                        id='234c9f7b-79df-4eb7-ba5c-38d4baf91e50',
                        name='Olive Windler',
                    ),
                    shared.TrackingCategoryRef(
                        id='0a54b475-f16f-456d-b85a-3c4ac631b99e',
                        name='Ella Runolfsdottir',
                    ),
                    shared.TrackingCategoryRef(
                        id='8f9fdb94-10f6-43bb-b817-837b01afdd78',
                        name='Chester Daugherty IV',
                    ),
                ],
                unit_amount=6138.48,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='eb44873f-5033-4f19-9bf1-25ce4152eab9',
                    name='Lionel Klocko',
                ),
                description='odit',
                discount_amount=1383.06,
                discount_percentage=2593.74,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='a6a0e123-b784-47ec-99e1-f67f3c4cce4b',
                    name='Angel Kris',
                ),
                quantity=4001.45,
                sub_total=9961.01,
                tax_amount=9570.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2322.09,
                    id='c5747501-357e-444f-91f8-b084c3197e19',
                    name='Rosie Conroy',
                ),
                total_amount=3088.66,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7f94874c-2d5c-4c49-b223-3e66bd8fe5d0',
                            name='Jeannette Mante',
                        ),
                        shared.TrackingCategoryRef(
                            id='ef203873-2059-40cc-8109-6400313b3e50',
                            name='Debbie Windler',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='maiores',
                        id='e72dc407-7d0c-4c3f-808e-fc15ceb4d6e1',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.TrackingProjectRef(
                        id='e0f75aed-f2ac-4ab5-8b99-1c926ddb5894',
                        name='Joyce Terry',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1cbe6d95-02f0-4ea9-b0b6-9f7ac2f72f88',
                        name='Karen Barrows I',
                    ),
                ],
                unit_amount=5776.22,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='11608207-888e-4c66-983b-fe9659eb40ec',
                    name='Loretta Wehner',
                ),
                description='nihil',
                discount_amount=3452.7,
                discount_percentage=7023.39,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='0b532a4d-a37c-4baa-b445-2c4842c9b2ad',
                    name='Rose Stoltenberg',
                ),
                quantity=8968.11,
                sub_total=5316.06,
                tax_amount=981.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6493.73,
                    id='88f44445-73fe-4cd4-b353-f63c8209379a',
                    name='Reginald McClure',
                ),
                total_amount=3210.07,
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='bcf79da1-8a78-422b-b958-94e6861adb55',
                            name='Nick Torp',
                        ),
                        shared.TrackingCategoryRef(
                            id='751c9fe8-f750-42bf-9c34-50841f176445',
                            name='Wendy Kling',
                        ),
                        shared.TrackingCategoryRef(
                            id='3fb27e21-f862-4657-b36f-c6b9f587ce52',
                            name='Brooke Jacobs',
                        ),
                        shared.TrackingCategoryRef(
                            id='41a8312e-5047-4b4c-a1cc-b423abcdc91f',
                            name='Rex Rau',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='totam',
                        id='8e71f6c4-8252-4d77-b1e7-fd074009ef8d',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.TrackingProjectRef(
                        id='de1dd709-7b5d-4a08-857f-a6c78a216e19',
                        name='Pablo Wilkinson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='61914981-40b6-44ff-8ae1-70ef03b5f37e',
                        name='Angie O'Hara',
                    ),
                    shared.TrackingCategoryRef(
                        id='85559667-32aa-45dc-b668-2cb70f8cfd5f',
                        name='Brent Weber MD',
                    ),
                    shared.TrackingCategoryRef(
                        id='9a9f7484-6e2c-4330-9db0-536d9e75ca00',
                        name='Lana Hauck',
                    ),
                ],
                unit_amount=1500.91,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='et',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=3322.37,
                    total_amount=6650.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8bf92f97-428a-4d9a-9f8b-f8221125359d',
                        name='Guy Feest',
                    ),
                    currency='EUR',
                    currency_rate=4820.62,
                    id='a79cd72c-d248-44da-a172-9f2ac41ef572',
                    note='quis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='dicta',
                    total_amount=1158.49,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.BillPurchaseOrderReference(
                id='9ac1e41d-8a23-4c23-a34f-2dfa4a197f6d',
                purchase_order_number='recusandae',
            ),
            shared.BillPurchaseOrderReference(
                id='922151fe-1712-4099-853e-9f543d854439',
                purchase_order_number='accusamus',
            ),
        ],
        reference='voluptates',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.UNKNOWN,
        sub_total=2805.9,
        supplemental_data=shared.BillSupplementalData(
            content={
                "laboriosam": {
                    "tempora": 'aliquam',
                },
                "dolorem": {
                    "impedit": 'architecto',
                    "minima": 'magnam',
                    "vitae": 'quos',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='8c2f56e8-5da7-4832-aabd-617c3b0d51a4',
            supplier_name='ut',
        ),
        tax_amount=6942.92,
        total_amount=9852.65,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=1013.18,
                name='Doug Stiedemann',
            ),
        ],
    ),
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=434330,
)

res = s.bills.update(req)

if res.update_bill_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateBillRequest](../../models/operations/updatebillrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.UpdateBillResponse](../../models/operations/updatebillresponse.md)**


## upload_attachment

The *Upload bill attachment* endpoint uploads an attachment and assigns it against a specific `billId`.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/sync-for-payables-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support uploading a bill attachment.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadBillAttachmentRequest(
    request_body=operations.UploadBillAttachmentRequestBody(
        content='temporibus'.encode(),
        request_body='incidunt',
    ),
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.upload_attachment(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UploadBillAttachmentRequest](../../models/operations/uploadbillattachmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.UploadBillAttachmentResponse](../../models/operations/uploadbillattachmentresponse.md)**

