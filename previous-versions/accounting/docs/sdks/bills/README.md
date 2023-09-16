# Bills

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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=Decimal('5436.78'),
        currency='GBP',
        currency_rate=Decimal('2826.99'),
        due_date='2022-10-23T00:00:00.000Z',
        id='0ab40750-88e5-4186-a065-e904f3b1194b',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='abf603a7-9f9d-4fe0-ab7d-a8a50ce187f8',
                    name='Ms. Alison Schoen',
                ),
                description='assumenda',
                discount_amount=Decimal('4103.01'),
                discount_percentage=Decimal('5391.18'),
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='9eee9526-f8d9-486e-881e-ad4f0e101256',
                    name='Elsa Maggio',
                ),
                quantity=Decimal('1604.67'),
                sub_total=Decimal('5801.07'),
                tax_amount=Decimal('8863.05'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('5979.37'),
                    id='73e922a5-7a15-4be3-a060-807e2b6e3ab8',
                    name='Jim Hammes II',
                ),
                total_amount=Decimal('5973.03'),
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7a60ff2a-54a3-41e9-8764-a3e865e7956f',
                            name='Miss Bruce Hermann',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='mollitia',
                        id='9da660ff-57bf-4aad-8f9e-fc1b4512c103',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='48dc2f61-5199-4ebf-90e9-fe6c632ca3ae',
                        name='Ms. William Boyle',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='96312fde-0477-4177-8ff6-1d017476360a',
                        name='Audrey Stiedemann',
                    ),
                ],
                unit_amount=Decimal('6391.87'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='aliquid',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=Decimal('3747.53'),
                    total_amount=Decimal('6145.28'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a1adeaab-5851-4d6c-a45b-08b61891baa0',
                        name='Stewart Brakus',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('291.9'),
                    id='08e6f8c5-f350-4d8c-9b5a-341814301042',
                    note='ab',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='quae',
                    total_amount=Decimal('2226.58'),
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='d5208ece-7e25-43b6-a845-1c6c6e205e16',
                purchase_order_number='at',
            ),
        ],
        reference='vero',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.VOID,
        sub_total=Decimal('1927.18'),
        supplemental_data=shared.BillSupplementalData(
            content={
                "doloribus": {
                    "repudiandae": 'optio',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='9578a645-8427-43a8-818d-162309fb0929',
            supplier_name='iste',
        ),
        tax_amount=Decimal('1700.99'),
        total_amount=Decimal('813.69'),
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=Decimal('6863.62'),
                name='Jan Reichel',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=328379,
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
    bill_id='9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
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
    bill_id='EILBDVJVNUAGVKRQ',
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
    query='quos',
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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=Decimal('9308.19'),
        currency='USD',
        currency_rate=Decimal('5207.61'),
        due_date='2022-10-23T00:00:00.000Z',
        id='4be05601-3f59-4da7-97a5-9ecfef66ef1c',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='a3383c2b-eb47-4737-bc8d-72f64d1db1f2',
                    name='Mr. Jim Franecki',
                ),
                description='ea',
                discount_amount=Decimal('1076.17'),
                discount_percentage=Decimal('8777.51'),
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='96349e1c-f9e0-46e3-a437-000ae6b6bc9b',
                    name='Tommie Klocko',
                ),
                quantity=Decimal('8975.43'),
                sub_total=Decimal('6540.82'),
                tax_amount=Decimal('7699.67'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('3730.4'),
                    id='5a9741d3-1135-4296-9bb8-a7202611435e',
                    name='Tracy Mills',
                ),
                total_amount=Decimal('8028.94'),
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='2259b1ab-da8c-4070-a108-4cb0672d1ad8',
                            name='Daisy Tillman',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='sint',
                        id='665b85ef-bd02-4bae-8be2-d782259e3ea4',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='197f9244-3da7-4ce5-ab89-5c537c6454ef',
                        name='Jason Rempel',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='896c3ca5-acfb-4e2f-9570-7577929177de',
                        name='Benny Jacobs',
                    ),
                ],
                unit_amount=Decimal('8886.16'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quidem',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=Decimal('2114.55'),
                    total_amount=Decimal('2646.19'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='09e3eb1e-5a2b-412e-b07f-116db99545fc',
                        name='Ronnie Welch',
                    ),
                    currency='USD',
                    currency_rate=Decimal('5646.67'),
                    id='70e189db-b30f-4cb3-bea0-55b197cd44e2',
                    note='asperiores',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='consequuntur',
                    total_amount=Decimal('8138.8'),
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='82d3513b-b6f4-48b6-96bc-db35ff2e4b27',
                purchase_order_number='nostrum',
            ),
        ],
        reference='neque',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.PAID,
        sub_total=Decimal('5221.76'),
        supplemental_data=shared.BillSupplementalData(
            content={
                "eligendi": {
                    "fugiat": 'unde',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='e7319c17-7d52-45f7-bb11-4eeb52ff785f',
            supplier_name='quisquam',
        ),
        tax_amount=Decimal('1972.59'),
        total_amount=Decimal('4671.19'),
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=Decimal('5349.08'),
                name='Jamie Simonis',
            ),
        ],
    ),
    bill_id='7110701885',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=514993,
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
        content='repudiandae'.encode(),
        request_body='consequatur',
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

