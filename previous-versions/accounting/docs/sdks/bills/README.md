# bills

## Overview

Bills

### Available Operations

* [create](#create) - Create bill
* [delete](#delete) - Delete bill
* [download_attachment](#download_attachment) - Download bill attachment
* [get](#get) - Get bill
* [get_attachment](#get_attachment) - Get bill attachment
* [get_create_update_model](#get_create_update_model) - Get create/update bill model
* [list](#list) - List bills
* [list_attachments](#list_attachments) - List bill attachments
* [update](#update) - Update bill
* [upload_attachment](#upload_attachment) - Upload bill attachment

## create

The *Create bill* endpoint creates a new [bill](https://docs.codat.io/accounting-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=1017.7,
        currency='EUR',
        currency_rate=6730.1,
        due_date='2022-10-23T00:00:00.000Z',
        id='cf20688f-77c1-4ffc-b1dc-a163f2a3c80a',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='ff334cdd-f857-4a9e-a187-6c6ab21d29df',
                    name='Austin Grady',
                ),
                description='doloribus',
                discount_amount=9260.27,
                discount_percentage=7874.52,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='d7993900-66a6-4d2d-8003-55338cec086f',
                    name='Billy Boehm',
                ),
                quantity=1164.63,
                sub_total=3690.99,
                tax_amount=1631.81,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7652.71,
                    id='b3119167-b8e3-4c8d-b034-08d6d364ffd4',
                    name='Ms. Samantha Metz',
                ),
                total_amount=1168.67,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='63d48e93-5c2c-49e8-9f30-be3e43202d72',
                            name='Beth Hand',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='minima',
                        id='06641870-d9d2-41f9-ad03-0c4ecc11a083',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='29068b85-02a5-45e7-b73b-c845e320a319',
                        name='Herbert Prohaska',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='947c9a86-7bc4-4242-a665-816ddca8ef51',
                        name='Spencer Rath',
                    ),
                    shared.TrackingCategoryRef(
                        id='593ec12c-daad-40ec-bafe-dbd80df448a4',
                        name='Lela Moore',
                    ),
                    shared.TrackingCategoryRef(
                        id='0c588809-83da-4bf9-af3f-fdd9f7f079af',
                        name='Muriel Durgan',
                    ),
                    shared.TrackingCategoryRef(
                        id='24cdb0f4-d281-4187-9568-44eded85a906',
                        name='Laverne Hudson',
                    ),
                ],
                unit_amount=6977.29,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='dfc2032b-6c87-4992-bb7e-13584f7ae12c',
                    name='Dr. Maxine Morissette',
                ),
                description='aspernatur',
                discount_amount=7552.4,
                discount_percentage=9178.77,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='11571723-0537-47dc-ba89-df975e356686',
                    name='Katrina Considine',
                ),
                quantity=7677.78,
                sub_total=2250.01,
                tax_amount=8339.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8373.27,
                    id='c5f111de-a102-46d5-81a4-d190feb21780',
                    name='Clark Schmitt PhD',
                ),
                total_amount=7188.79,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ddb48470-8fb4-4e39-9e6b-c158c4c4e545',
                            name='Marion Ward',
                        ),
                        shared.TrackingCategoryRef(
                            id='42260e9b-200c-4e78-a1bd-8fb7a0a116ce',
                            name='Tammy Dickens',
                        ),
                        shared.TrackingCategoryRef(
                            id='097fa30e-9af7-425b-a912-2030d83f5aeb',
                            name='Stella Medhurst',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='sunt',
                        id='2e8c1f84-9382-45fd-842c-876c2c2dfb4c',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='1c76230f-841f-4b1b-923f-db14db6be5a6',
                        name='Lewis Mante',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='22ae20da-16fc-42b2-b1a2-89c57e854e90',
                        name='Tiffany Mayert',
                    ),
                    shared.TrackingCategoryRef(
                        id='22465694-6240-4708-8f7a-b37cef022251',
                        name='Marcus Stehr',
                    ),
                    shared.TrackingCategoryRef(
                        id='5410adc6-69af-490a-a6c7-cdc981f06898',
                        name='Ernestine Jast',
                    ),
                    shared.TrackingCategoryRef(
                        id='33cfaa34-8c31-4bf4-87ee-4fcf0c42b78f',
                        name='Samantha Huels',
                    ),
                ],
                unit_amount=1913.12,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corrupti',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=7702.62,
                    total_amount=4972.31,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='66324ccb-06c8-4ca1-ad02-529270b8d572',
                        name='Lynette Stark',
                    ),
                    currency='USD',
                    currency_rate=7399.38,
                    id='8bcf24db-9596-4933-92f7-4533994d78de',
                    note='amet',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='vel',
                    total_amount=9004.38,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=5456.29,
                    total_amount=5873.37,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f5abb7f6-6255-40a2-8382-ac483afd2315',
                        name='Malcolm O'Connell',
                    ),
                    currency='GBP',
                    currency_rate=767.86,
                    id='64e06f5b-f6ae-4591-bc8b-def3612b63c2',
                    note='alias',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='a',
                    total_amount=8168.25,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=3106.48,
                    total_amount=458.5,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='774a68a9-a35d-4086-b6f6-6fef020e9f44',
                        name='Celia Gottlieb',
                    ),
                    currency='USD',
                    currency_rate=7289.48,
                    id='992c8dbd-a6a6-41ef-a219-8258fd0a9eba',
                    note='labore',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='voluptatibus',
                    total_amount=4668.62,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='3ef04964-0d6a-4183-9c87-adf596fdf1ad',
                purchase_order_number='praesentium',
            ),
            shared.PurchaseOrderRef(
                id='37ae80c1-c19c-495b-a998-678fa3f69699',
                purchase_order_number='ab',
            ),
            shared.PurchaseOrderRef(
                id='af388ce0-3614-4448-8797-7a0ef2f53602',
                purchase_order_number='voluptatum',
            ),
            shared.PurchaseOrderRef(
                id='efeef934-152e-4d7e-a53f-4c157deaa717',
                purchase_order_number='consequatur',
            ),
        ],
        reference='delectus',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.OPEN,
        sub_total=3626.93,
        supplemental_data=shared.BillSupplementalData(
            content={
                "quo": {
                    "delectus": 'laboriosam',
                    "laboriosam": 'quam',
                    "fuga": 'officia',
                    "repellat": 'cupiditate',
                },
                "soluta": {
                    "culpa": 'fugiat',
                    "inventore": 'atque',
                    "ad": 'sapiente',
                },
                "voluptates": {
                    "nesciunt": 'ab',
                    "quibusdam": 'suscipit',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='bf5c838f-bb8c-420c-b67f-c4b425e99e62',
            supplier_name='amet',
        ),
        tax_amount=2796.79,
        total_amount=7835.39,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=9707.03,
                name='Whitney King',
            ),
            shared.BillWithholdingTax(
                amount=9503.37,
                name='Rudolph Kshlerin',
            ),
            shared.BillWithholdingTax(
                amount=3216.54,
                name='Philip Leannon',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=722889,
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


## delete

﻿The *Delete bill* endpoint allows you to delete a specified bill from an accounting platform. 

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are itemized records of goods received or services provided to the SMB.

### Process 
1. Pass the `{billId}` to the *Delete bill* endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](https://docs.codat.io/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the bill object was deleted from the accounting platform.
3. (Optional) Check that the bill was deleted from the accounting platform.

### Effect on related objects

Be aware that deleting a bill from an accounting platform might cause related objects to be modified. For example, if you delete a paid bill in QuickBooks Online, the bill is deleted but the bill payment against that bill is not. The bill payment is converted to a payment on account.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Delete | Details                                                                                                      |  
|-------------|-------------|--------------------------------------------------------------------------------------------------------------|
| QuickBooks Online | No          | -                                                                                                            |
| Oracle NetSuite   | No          | When deleting a bill that's already linked to a bill payment, you must delete the linked bill payment first. |

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteBillRequest(
    bill_id='7110701885',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteBillRequest](../../models/operations/deletebillrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.DeleteBillResponse](../../models/operations/deletebillresponse.md)**


## download_attachment

The *Download bill attachment* endpoint downloads a specific attachment for a given `billId` and `attachmentId`.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support downloading a bill attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
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

The *Get bill* endpoint returns a single bill for a given billId.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a specific bill.

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

req = operations.GetBillRequest(
    bill_id='7110701885',
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

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support getting a bill attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
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

﻿The *Get create/update bill model* endpoint returns the expected data for the request payload when creating and updating a [bill](https://docs.codat.io/accounting-api#/schemas/Bill) for a given company and integration.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateBillsModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCreateUpdateBillsModelRequest](../../models/operations/getcreateupdatebillsmodelrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetCreateUpdateBillsModelResponse](../../models/operations/getcreateupdatebillsmodelresponse.md)**


## list

The *List bills* endpoint returns a list of [bills](https://docs.codat.io/accounting-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

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

req = operations.ListBillsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='saepe',
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

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support listing bill attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListBillAttachmentsRequest(
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.list_attachments(req)

if res.attachments_dataset is not None:
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

The *Update bill* endpoint updates an existing [bill](https://docs.codat.io/accounting-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating an account.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=524.07,
        currency='USD',
        currency_rate=9101.32,
        due_date='2022-10-23T00:00:00.000Z',
        id='890a54b4-75f1-46f5-ad38-5a3c4ac631b9',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='26ced8f9-fdb9-4410-b63b-bf817837b01a',
                    name='Josh Sporer',
                ),
                description='rem',
                discount_amount=4245.53,
                discount_percentage=1777.9,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='4189eb44-873f-4503-bf19-dbf125ce4152',
                    name='Julius Ratke',
                ),
                quantity=8382.27,
                sub_total=4547.61,
                tax_amount=9354.93,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3272.63,
                    id='224a6a0e-123b-4784-bec5-9e1f67f3c4cc',
                    name='Ricky Rempel',
                ),
                total_amount=4785.76,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='96ff3c57-4750-4135-be44-f51f8b084c31',
                            name='Ms. Jamie Torphy',
                        ),
                        shared.TrackingCategoryRef(
                            id='a245467f-9487-44c2-95cc-4972233e66bd',
                            name='Jan Torphy',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='aut',
                        id='0b979ef2-0387-4320-990c-cc1096400313',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='e5044f65-fe72-4dc4-877d-0cc3f408efc1',
                        name='Pat Upton',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6e1eae0f-75ae-4df2-acab-58b991c926dd',
                        name='Jon Lockman',
                    ),
                    shared.TrackingCategoryRef(
                        id='61e7421c-be6d-4950-af0e-a930b69f7ac2',
                        name='Erik Champlin',
                    ),
                    shared.TrackingCategoryRef(
                        id='85009049-1160-4820-b888-ec66183bfe96',
                        name='Lindsey Trantow',
                    ),
                    shared.TrackingCategoryRef(
                        id='0ec16faf-75b0-4b53-aa4d-a37cbaaf4452',
                        name='Jon Lemke DDS',
                    ),
                ],
                unit_amount=5867.23,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='b2ad32da-fe81-4a88-b444-4573fecd4735',
                    name='Lana Keeling',
                ),
                description='quos',
                discount_amount=1523.02,
                discount_percentage=544.98,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='9379aa69-cd5f-4bcf-b9da-18a7822bf958',
                    name='Tom Thiel',
                ),
                quantity=4331.94,
                sub_total=1151.37,
                tax_amount=6574.85,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8187.39,
                    id='b55f9e5d-751c-49fe-8f75-02bfdc345084',
                    name='Josefina Borer',
                ),
                total_amount=2943.14,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='56379f3f-b27e-421f-8626-57b36fc6b9f5',
                            name='Mathew Schmitt',
                        ),
                        shared.TrackingCategoryRef(
                            id='25c67641-a831-42e5-847b-4c21ccb423ab',
                            name='Josh Rutherford DVM',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='fuga',
                        id='abdd88e7-1f6c-4482-92d7-771e7fd07400',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='f8d29de1-dd70-497b-9da0-8c57fa6c78a2',
                        name='Ms. Eileen Thompson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='feca6191-4981-440b-a4ff-8ae170ef03b5',
                        name='Mike Kovacek',
                    ),
                    shared.TrackingCategoryRef(
                        id='aa868555-9667-432a-a5dc-b6682cb70f8c',
                        name='Kristopher Herman',
                    ),
                    shared.TrackingCategoryRef(
                        id='6e91b9a9-f748-446e-ac33-09db0536d9e7',
                        name='Mr. Vicky Parker',
                    ),
                ],
                unit_amount=9386.72,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='5392c11a-25a8-4bf9-af97-428ad9a9f8bf',
                    name='Mr. Roy Conn',
                ),
                description='ad',
                discount_amount=2449.9,
                discount_percentage=3556.85,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='9d98387f-7a79-4cd7-acd2-484da21729f2',
                    name='Dr. Guillermo Funk',
                ),
                quantity=3495.58,
                sub_total=4682.21,
                tax_amount=1547.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3361.23,
                    id='f1169ac1-e41d-48a2-bc23-e34f2dfa4a19',
                    name='Elsa Kerluke',
                ),
                total_amount=6107.22,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2151fe17-1209-4985-be9f-543d854439ee',
                            name='Nicole Goyette',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='accusantium',
                        id='443bc154-188c-42f5-ae85-da7832eabd61',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='3b0d51a4-4bf0-41ba-9870-6d46082bfbdc',
                        name='Jean Windler',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4e2ae4fb-5cb3-45d1-b638-f1edb78359ec',
                        name='Warren Runolfsson',
                    ),
                    shared.TrackingCategoryRef(
                        id='60f8cd58-0ba7-4381-8e4f-e4447297cd3b',
                        name='Angel Stokes',
                    ),
                    shared.TrackingCategoryRef(
                        id='bce247b7-684e-4ff5-8126-d71cffbd0eb7',
                        name='Beulah Kuvalis',
                    ),
                    shared.TrackingCategoryRef(
                        id='1953b44b-d3c4-4315-9d33-e5953c001139',
                        name='Gilbert Dickinson',
                    ),
                ],
                unit_amount=2664.61,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='1e6c31cc-2f1f-4cb5-9c9a-41ffbe9cbd79',
                    name='Casey Weber',
                ),
                description='debitis',
                discount_amount=414.36,
                discount_percentage=4582.74,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='6cc7abf6-16ea-45c7-9641-934b90f2e09d',
                    name='Faye Senger',
                ),
                quantity=7687.72,
                sub_total=1277.84,
                tax_amount=9668.01,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6189.9,
                    id='e2e10594-4b93-45d2-b7a7-2f90849d6aed',
                    name='Amelia Upton',
                ),
                total_amount=4929.22,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='37cd9222-c9ff-4574-91aa-bfa2e761f0ca',
                            name='Meredith Green',
                        ),
                        shared.TrackingCategoryRef(
                            id='ef1031e6-899f-40c2-801e-22cd55cc0584',
                            name='Carl Larson',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='nihil',
                        id='6d971fc8-20c6-45b0-b7bb-8e0cc885187e',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='e04af28c-5ddd-4b46-aa1c-fd6d828da013',
                        name='Mr. Sabrina Blick',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='46645c1d-81f2-4904-af56-9b7aff0ea221',
                        name='Nichole Renner IV',
                    ),
                    shared.TrackingCategoryRef(
                        id='1bc163e2-79a3-4b08-8da9-9257d04f4084',
                        name='Kayla Kilback',
                    ),
                ],
                unit_amount=8310.89,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ut',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=8124.31,
                    total_amount=7335.71,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='deecf6b9-9bc6-4356-aebf-df55c294c060',
                        name='Steven Jast Sr.',
                    ),
                    currency='USD',
                    currency_rate=4767.7,
                    id='764eef6d-0c6d-46ed-9c73-dd634571509a',
                    note='blanditiis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='deleniti',
                    total_amount=4930.17,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=2381.67,
                    total_amount=7937.52,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5a1f9c24-2c7b-466a-9f30-c73df5b67198',
                        name='Gary Wisozk',
                    ),
                    currency='EUR',
                    currency_rate=2723.96,
                    id='bb438d85-b260-4591-9745-e3c2059c9c3f',
                    note='veniam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='esse',
                    total_amount=8871.67,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='e252765b-1d62-4fcd-ace1-f01216ce2239',
                purchase_order_number='accusamus',
            ),
        ],
        reference='deleniti',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.UNKNOWN,
        sub_total=3184.71,
        supplemental_data=shared.BillSupplementalData(
            content={
                "quibusdam": {
                    "nulla": 'inventore',
                },
                "omnis": {
                    "excepturi": 'nostrum',
                    "sint": 'doloribus',
                    "magnam": 'adipisci',
                    "natus": 'necessitatibus',
                },
                "velit": {
                    "eos": 'nisi',
                    "commodi": 'impedit',
                    "facilis": 'temporibus',
                },
                "error": {
                    "delectus": 'molestiae',
                    "deserunt": 'laborum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='2b241136-95d1-4e66-98fc-c4596217c297',
            supplier_name='molestiae',
        ),
        tax_amount=3968.2,
        total_amount=4547.05,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=2325.57,
                name='Rhonda Collins',
            ),
            shared.BillWithholdingTax(
                amount=17.82,
                name='Penny Rice',
            ),
        ],
    ),
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=584483,
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

[Bills](https://docs.codat.io/accounting-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/accounting-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support uploading a bill attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadBillAttachmentRequest(
    request_body=operations.UploadBillAttachmentRequestBody(
        content='molestiae'.encode(),
        request_body='et',
    ),
    bill_id='EILBDVJVNUAGVKRQ',
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

