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
        amount_due=9453.2,
        currency='USD',
        currency_rate=3712.95,
        due_date='2022-10-23T00:00:00.000Z',
        id='a9e61876-c6ab-421d-a9df-c94d6fecd799',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='0066a6d2-d000-4355-b38c-ec086fa21e91',
                    name='Kathryn Runolfsdottir',
                ),
                description='beatae',
                discount_amount=1234.95,
                discount_percentage=5658.45,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='167b8e3c-8db0-4340-8d6d-364ffd455906',
                    name='Keith Crist',
                ),
                quantity=8436.59,
                sub_total=2552.64,
                tax_amount=5231.09,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8846.22,
                    id='935c2c9e-81f3-40be-be43-202d72165765',
                    name='Kristin Howell IV',
                ),
                total_amount=4935.79,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d9d21f9a-d030-4c4e-8c11-a0836429068b',
                            name='Pedro Armstrong',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quaerat',
                        id='5e7f73bc-845e-4320-a319-f4badf947c9a',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='7bc42426-6658-416d-9ca8-ef51fcb4c593',
                        name='Devin Boyle',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='aad0ec7a-fedb-4d80-9f44-8a47f9390c58',
                        name='Willard Barrows',
                    ),
                    shared.TrackingCategoryRef(
                        id='3dabf9ef-3ffd-4d9f-bf07-9af4d35724cd',
                        name='Jeffrey Wisoky',
                    ),
                    shared.TrackingCategoryRef(
                        id='281187d5-6844-4ede-985a-9065e628bdfc',
                        name='Elizabeth Douglas',
                    ),
                    shared.TrackingCategoryRef(
                        id='6c879923-b7e1-4358-8f7a-e12c6891f82c',
                        name='Keith Bode',
                    ),
                ],
                unit_amount=823.96,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='72305377-dcfa-489d-b975-e356686092e9',
                    name='Norman Skiles',
                ),
                description='minima',
                discount_amount=9519.01,
                discount_percentage=1048.34,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='11dea102-6d54-41a4-9190-feb21780bccc',
                    name='Muriel Reichel',
                ),
                quantity=8504.06,
                sub_total=7468.34,
                tax_amount=2973.25,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5123.49,
                    id='4708fb4e-391e-46bc-958c-4c4e54599ea3',
                    name='Nicole Christiansen DVM',
                ),
                total_amount=5757.53,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='200ce78a-1bd8-4fb7-a0a1-16ce723d4097',
                            name='Dr. Doug Dibbert',
                        ),
                        shared.TrackingCategoryRef(
                            id='af725b29-1220-430d-83f5-aeb7799d22e8',
                            name='Roger Zulauf',
                        ),
                        shared.TrackingCategoryRef(
                            id='93825fdc-42c8-476c-ac2d-fb4cfc1c7623',
                            name='Johanna Lueilwitz DVM',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='nam',
                        id='1bd23fdb-14db-46be-9a68-5998e22ae20d',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='6fc2b271-a289-4c57-a854-e90439d22246',
                        name='Kristin McDermott',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='407084f7-ab37-4cef-8222-5194db55410a',
                        name='Garrett Hoeger',
                    ),
                ],
                unit_amount=6668.17,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='f90a26c7-cdc9-481f-8689-81d6bb33cfaa',
                    name='Clara Larson',
                ),
                description='veritatis',
                discount_amount=7217.23,
                discount_percentage=9747.75,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='407ee4fc-f0c4-42b7-8f15-626398a0dc76',
                    name='Rosa Considine',
                ),
                quantity=8031.44,
                sub_total=7133.71,
                tax_amount=371.81,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4086.77,
                    id='c8ca12d0-2529-4270-b8d5-722dd895b8bc',
                    name='Ernest Grimes',
                ),
                total_amount=5854.45,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='9693352f-7453-4399-8d78-de3b6e9389f5',
                            name='Gerardo Ritchie',
                        ),
                        shared.TrackingCategoryRef(
                            id='662550a2-8382-4ac4-83af-d2315bba6501',
                            name='Ms. Eva Upton',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='veniam',
                        id='bf6ae591-bc8b-4def-b612-b63c205fda84',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='74a68a9a-35d0-486b-af66-fef020e9f443',
                        name='Randall Daniel',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='992c8dbd-a6a6-41ef-a219-8258fd0a9eba',
                        name='Allison Wiza',
                    ),
                    shared.TrackingCategoryRef(
                        id='3ef04964-0d6a-4183-9c87-adf596fdf1ad',
                        name='Tony Konopelski',
                    ),
                    shared.TrackingCategoryRef(
                        id='80c1c19c-95ba-4998-a78f-a3f696991af3',
                        name='Daryl Schmitt I',
                    ),
                ],
                unit_amount=4209.1,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='numquam',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=7914.54,
                    total_amount=4524.81,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='977a0ef2-f536-4028-afee-f934152ed7e2',
                        name='Ethel Windler',
                    ),
                    currency='GBP',
                    currency_rate=3534.93,
                    id='7deaa717-0f44-45ac-8f66-7aaf9bbad185',
                    note='sapiente',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ut',
                    total_amount=2010.05,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=3843.54,
                    total_amount=6963.24,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f5c838fb-b8c2-40cb-a7fc-4b425e99e623',
                        name='Robyn McCullough',
                    ),
                    currency='EUR',
                    currency_rate=4473.23,
                    id='9dfeb77a-5c38-4d4b-af91-e506ef890a54',
                    note='nam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='odio',
                    total_amount=3427.72,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='16f56d38-5a3c-44ac-a31b-99e26ced8f9f',
                purchase_order_number='repellendus',
            ),
            shared.PurchaseOrderRef(
                id='b9410f63-bbf8-4178-b7b0-1afdd7886241',
                purchase_order_number='blanditiis',
            ),
            shared.PurchaseOrderRef(
                id='9eb44873-f503-43f1-9dbf-125ce4152eab',
                purchase_order_number='error',
            ),
            shared.PurchaseOrderRef(
                id='cd7e5224-a6a0-4e12-bb78-47ec59e1f67f',
                purchase_order_number='amet',
            ),
        ],
        reference='cumque',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.VOID,
        sub_total=7763.34,
        supplemental_data=shared.BillSupplementalData(
            content={
                "tempora": {
                    "suscipit": 'illum',
                    "iusto": 'aliquid',
                    "sint": 'aliquid',
                },
                "repellat": {
                    "consectetur": 'eligendi',
                    "ullam": 'nihil',
                    "eius": 'dignissimos',
                    "corporis": 'perferendis',
                },
                "architecto": {
                    "corporis": 'nihil',
                },
                "officiis": {
                    "magnam": 'maiores',
                    "ipsam": 'dicta',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='f8b084c3-197e-4193-a245-467f94874c2d',
            supplier_name='ipsam',
        ),
        tax_amount=7503.43,
        total_amount=7841.2,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=5961.33,
                name='Lois Dibbert',
            ),
            shared.BillWithholdingTax(
                amount=9041.93,
                name='Beth Ritchie',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=977472,
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
    bill_id='EILBDVJVNUAGVKRQ',
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
    query='voluptatem',
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
    bill_id='7110701885',
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
        amount_due=5684.19,
        currency='USD',
        currency_rate=6091.61,
        due_date='2022-10-23T00:00:00.000Z',
        id='f2038732-0590-4ccc-9096-400313b3e504',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='65fe72dc-4077-4d0c-83f4-08efc15ceb4d',
                    name='Cecelia Boyer',
                ),
                description='necessitatibus',
                discount_amount=296,
                discount_percentage=9807.05,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='75aedf2a-cab5-48b9-91c9-26ddb589461e',
                    name='Miss Elaine Considine',
                ),
                quantity=9245.59,
                sub_total=4128.97,
                tax_amount=8203.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5890.98,
                    id='502f0ea9-30b6-49f7-ac2f-72f885009049',
                    name='Ms. Carolyn Jacobson',
                ),
                total_amount=170.4,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='888ec661-83bf-4e96-99eb-40ec16faf75b',
                            name='Juana Herman',
                        ),
                        shared.TrackingCategoryRef(
                            id='a4da37cb-aaf4-4452-8484-2c9b2ad32daf',
                            name='Bob Boyle',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='blanditiis',
                        id='f4444573-fecd-4473-93f6-3c8209379aa6',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='d5fbcf79-da18-4a78-a2bf-95894e6861ad',
                        name='Pedro Haley',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5d751c9f-e8f7-4502-bfdc-3450841f1764',
                        name='Bernice Jaskolski',
                    ),
                    shared.TrackingCategoryRef(
                        id='9f3fb27e-21f8-4626-97b3-6fc6b9f587ce',
                        name='Sara Hegmann',
                    ),
                    shared.TrackingCategoryRef(
                        id='7641a831-2e50-447b-8c21-ccb423abcdc9',
                        name='Lana Pfannerstill',
                    ),
                    shared.TrackingCategoryRef(
                        id='dd88e71f-6c48-4252-9777-1e7fd074009e',
                        name='Jaime Schumm',
                    ),
                ],
                unit_amount=8304.73,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='e1dd7097-b5da-408c-97fa-6c78a216e19b',
                    name='Randal Walker',
                ),
                description='laboriosam',
                discount_amount=717.34,
                discount_percentage=5842.92,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='1498140b-64ff-48ae-970e-f03b5f37e4aa',
                    name='Ricardo Lynch',
                ),
                quantity=3573.88,
                sub_total=6141.75,
                tax_amount=4116.69,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4196,
                    id='732aa5dc-b668-42cb-b0f8-cfd5fb6e91b9',
                    name='Ross Wilderman',
                ),
                total_amount=5110.54,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='6e2c3309-db05-436d-9e75-ca006f5392c1',
                            name='Jodi Crona',
                        ),
                        shared.TrackingCategoryRef(
                            id='8bf92f97-428a-4d9a-9f8b-f8221125359d',
                            name='Guy Feest',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='repellat',
                        id='7a79cd72-cd24-484d-a217-29f2ac41ef57',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='f1169ac1-e41d-48a2-bc23-e34f2dfa4a19',
                        name='Elsa Kerluke',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='22151fe1-7120-4998-93e9-f543d854439e',
                        name='Randy Collier',
                    ),
                    shared.TrackingCategoryRef(
                        id='60443bc1-5418-48c2-b56e-85da7832eabd',
                        name='Frances Kuhlman',
                    ),
                    shared.TrackingCategoryRef(
                        id='b0d51a44-bf01-4bad-8706-d46082bfbdc4',
                        name='Lucia Wintheiser',
                    ),
                ],
                unit_amount=2975.85,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='e2ae4fb5-cb35-4d17-a38f-1edb78359ecc',
                    name='Blanca Prohaska',
                ),
                description='doloremque',
                discount_amount=9640.52,
                discount_percentage=5582.01,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='cd580ba7-3810-4e4f-a444-7297cd3b1dd3',
                    name='Randolph Russel',
                ),
                quantity=2814.16,
                sub_total=4724.44,
                tax_amount=6906.54,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4559.58,
                    id='684eff50-126d-471c-bfbd-0eb74b842195',
                    name='Melody Grady',
                ),
                total_amount=8614.06,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c43159d3-3e59-453c-8011-39863aa41e6c',
                            name='Rebecca Schmitt DVM',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dicta',
                        id='fcb51c9a-41ff-4be9-8bd7-95ee65e076cc',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='bf616ea5-c716-4419-b4b9-0f2e09d19d2f',
                        name='Nicholas Wisoky',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='e105944b-935d-4237-a72f-90849d6aed4a',
                        name='Earnest Rogahn',
                    ),
                ],
                unit_amount=2048.77,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='7cd9222c-9ff5-4749-9aab-fa2e761f0ca4',
                    name='Francisco Hauck',
                ),
                description='reiciendis',
                discount_amount=1170.53,
                discount_percentage=234.1,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='31e6899f-0c20-401e-a2cd-55cc0584a184',
                    name='Christian Hirthe',
                ),
                quantity=4525.15,
                sub_total=1150.77,
                tax_amount=9714.36,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7665.01,
                    id='820c65b0-37bb-48e0-8c88-5187e4de04af',
                    name='Naomi Schneider',
                ),
                total_amount=8135.45,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b46aa1cf-d6d8-428d-a013-191129646645',
                            name='Raymond Sporer DVM',
                        ),
                        shared.TrackingCategoryRef(
                            id='29042f56-9b7a-4ff0-aa22-16cbe071bc16',
                            name='Rochelle Cormier',
                        ),
                        shared.TrackingCategoryRef(
                            id='a3b084da-9925-47d0-8f40-847a742d8449',
                            name='Chelsea Reynolds',
                        ),
                        shared.TrackingCategoryRef(
                            id='ecf6b99b-c635-462e-bfdf-55c294c060b0',
                            name='Janie Bogisich',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='molestiae',
                        id='764eef6d-0c6d-46ed-9c73-dd634571509a',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='870d3c5a-1f9c-4242-87b6-6a1f30c73df5',
                        name='Ms. Angel Kreiger',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='0f42a4bb-438d-485b-a605-91d745e3c205',
                        name='Sylvester Mante',
                    ),
                    shared.TrackingCategoryRef(
                        id='f567e0e2-5276-45b1-962f-cdace1f01216',
                        name='Cornelius Crooks',
                    ),
                    shared.TrackingCategoryRef(
                        id='9e8f25cd-0d19-4d95-9f43-9e39266cbd95',
                        name='Clinton Oberbrunner',
                    ),
                ],
                unit_amount=6980.88,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='magnam',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=3911.05,
                    total_amount=5979.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5d1e6698-fcc4-4596-a17c-297767633425',
                        name='Mary Fisher',
                    ),
                    currency='EUR',
                    currency_rate=7169.75,
                    id='5971e981-9055-4738-9ced-bac7fda39594',
                    note='pariatur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='laboriosam',
                    total_amount=7444.74,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='2ae48063-2b99-454b-afa2-206369828553',
                purchase_order_number='optio',
            ),
            shared.PurchaseOrderRef(
                id='b10006be-f492-41ec-a053-b749366ac8ee',
                purchase_order_number='voluptatem',
            ),
            shared.PurchaseOrderRef(
                id='f2bf1958-8d40-4d03-b3de-ba297be3e90b',
                purchase_order_number='nobis',
            ),
            shared.PurchaseOrderRef(
                id='40df868f-d524-405c-b331-d492f4f127fb',
                purchase_order_number='aperiam',
            ),
        ],
        reference='saepe',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.VOID,
        sub_total=9438.65,
        supplemental_data=shared.BillSupplementalData(
            content={
                "delectus": {
                    "fugit": 'inventore',
                    "reprehenderit": 'sint',
                    "dignissimos": 'voluptatum',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='d0acca77-aeb7-4b70-a1a5-2046b64e99fb',
            supplier_name='doloremque',
        ),
        tax_amount=8871.99,
        total_amount=3942.08,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=8997.35,
                name='Daisy Graham',
            ),
            shared.BillWithholdingTax(
                amount=9504.65,
                name='Kristopher Herman',
            ),
        ],
    ),
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=924506,
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
        content='a'.encode(),
        request_body='exercitationem',
    ),
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
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

