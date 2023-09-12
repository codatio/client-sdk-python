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

The *Create bill* endpoint creates a new [bill](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) for a given company's connection.

[Bills](https://docs.codat.io/sync-for-payables-api#/schemas/Bill) are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating a bill.


### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared
from decimal import Decimal

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=Decimal('2494.2'),
        currency='GBP',
        currency_rate=Decimal('1059.06'),
        due_date='2022-10-23T00:00:00.000Z',
        id='fe35b60e-b1ea-4426-955b-a3c28744ed53',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='88f3a8d8-f5c0-4b2f-afb7-b194a276b269',
                    name='Laurie Willms DVM',
                ),
                description='perferendis',
                discount_amount=Decimal('5468.85'),
                discount_percentage=Decimal('9795.74'),
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='4294e369-8f44-47f6-83e8-b445e80ca55e',
                    name='Dr. Jody Cummings',
                ),
                quantity=Decimal('3299.35'),
                sub_total=Decimal('4461.35'),
                tax_amount=Decimal('8892.34'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('1046.27'),
                    id='858b6a89-fbe3-4a5a-a8e4-824d0ab40750',
                    name='Willard Walker IV',
                ),
                total_amount=Decimal('4059.42'),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2065e904-f3b1-4194-b8ab-f603a79f9dfe',
                            name='Monique Predovic',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='fuga',
                        id='8a50ce18-7f86-4bc1-b3d6-89eee9526f8d',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.TrackingProjectReference(
                        id='6e881ead-4f0e-4101-a563-f94e29e973e9',
                        name='Beverly Olson',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a15be3e0-6080-47e2-b6e3-ab8845f0597a',
                        name='Linda Wuckert',
                    ),
                ],
                unit_amount=Decimal('6638.66'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='dolore',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('632.07'),
                    total_amount=Decimal('9257.03'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='94764a3e-865e-4795-af92-51a5a9da660f',
                        name='Dustin King',
                    ),
                    currency='USD',
                    currency_rate=Decimal('6720.41'),
                    id='d4f9efc1-b451-42c1-8326-48dc2f615199',
                    note='earum',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='hic',
                    total_amount=Decimal('8481.51'),
                ),
            ),
        ],
        purchase_order_refs=[
            shared.BillPurchaseOrderReference(
                id='0e9fe6c6-32ca-43ae-9011-7996312fde04',
                purchase_order_number='nihil',
            ),
        ],
        reference='molestiae',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.PARTIALLY_PAID,
        sub_total=Decimal('4570.59'),
        supplemental_data=shared.BillSupplementalData(
            content={
                "praesentium": {
                    "maiores": 'reiciendis',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='61d01747-6360-4a15-9b6a-660659a1adea',
            supplier_name='laborum',
        ),
        tax_amount=Decimal('7263.43'),
        total_amount=Decimal('3240.83'),
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=Decimal('5369.23'),
                name='Gloria Skiles',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=405373,
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
    2. [Push operation status endpoint](https://docs.codat.io/sync-for-payables-api#/operations/get-push-operation).

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
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteBillRequest(
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.delete(req)

if res.push_operation is not None:
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
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
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
    query='molestias',
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
    bill_id='7110701885',
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
from decimal import Decimal

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=Decimal('3996.6'),
        currency='GBP',
        currency_rate=Decimal('5308.6'),
        due_date='2022-10-23T00:00:00.000Z',
        id='1baa0fe1-ade0-408e-af8c-5f350d8cdb5a',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='41814301-0421-4813-9520-8ece7e253b66',
                    name='Miss Oscar Heller',
                ),
                description='nobis',
                discount_amount=Decimal('3883.19'),
                discount_percentage=Decimal('9272.12'),
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='205e16de-ab3f-4ec9-978a-64584273a841',
                    name='Clint Carroll',
                ),
                quantity=Decimal('2330.78'),
                sub_total=Decimal('468.06'),
                tax_amount=Decimal('5854.32'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('9707.32'),
                    id='b0929921-aefb-49f5-8c4d-86e68e4be056',
                    name='Frances Franey',
                ),
                total_amount=Decimal('5752.13'),
                tracking=shared.Tracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='da757a59-ecfe-4f66-af1c-aa3383c2beb4',
                            name='Colleen Dickinson',
                        ),
                    ],
                    customer_ref=shared.TrackingCustomerRef(
                        company_name='quo',
                        id='8d72f64d-1db1-4f2c-8310-661e96349e1c',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.TrackingProjectReference(
                        id='e06e3a43-7000-4ae6-b6bc-9b8f759eac55',
                        name='Jeremiah Koch PhD',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='31135296-5bb8-4a72-8261-1435e139dbc2',
                        name='Bernice Moen MD',
                    ),
                ],
                unit_amount=Decimal('7278.88'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='officia',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('257.56'),
                    total_amount=Decimal('4793.85'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='0e1084cb-0672-4d1a-9879-eeb9665b85ef',
                        name='Josh Abshire',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('9195.08'),
                    id='0be2d782-259e-43ea-8b51-97f92443da7c',
                    note='necessitatibus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='qui',
                    total_amount=Decimal('7088.98'),
                ),
            ),
        ],
        purchase_order_refs=[
            shared.BillPurchaseOrderReference(
                id='895c537c-6454-4efb-8b34-896c3ca5acfb',
                purchase_order_number='vero',
            ),
        ],
        reference='odit',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.DRAFT,
        sub_total=Decimal('3628.88'),
        supplemental_data=shared.BillSupplementalData(
            content={
                "reprehenderit": {
                    "aperiam": 'odio',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='57792917-7dea-4c64-aecb-573409e3eb1e',
            supplier_name='veniam',
        ),
        tax_amount=Decimal('6592.68'),
        total_amount=Decimal('1753.72'),
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=Decimal('7249.94'),
                name='Louise Tromp IV',
            ),
        ],
    ),
    bill_id='EILBDVJVNUAGVKRQ',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=87382,
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
        content='quasi'.encode(),
        request_body='laboriosam',
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

