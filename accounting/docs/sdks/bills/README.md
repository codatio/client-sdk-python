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
        amount_due=6704.3,
        currency='EUR',
        currency_rate=1479.89,
        due_date='2022-10-23T00:00:00.000Z',
        id='af5dd672-3dc0-4f5a-a2f3-a6b700878756',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='3f5a6c98-b555-4540-80d4-0bcacc6cbd6b',
                    name='Shawna Feil',
                ),
                description='cupiditate',
                discount_amount=290.8,
                discount_percentage=5881.58,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='304f926b-ad25-4538-99b4-74b0ed20e562',
                    name='Vickie Welch',
                ),
                quantity=4209.85,
                sub_total=1988.92,
                tax_amount=5856.28,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6568.39,
                    id='910abdca-b626-4766-96e1-ec00221b335d',
                    name='Austin Murphy',
                ),
                total_amount=2258.09,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='cfda8d0c-549e-4f03-8049-78a61fa1cf20',
                            name='Leah Leannon',
                        ),
                        shared.TrackingCategoryRef(
                            id='7c1ffc71-dca1-463f-aa3c-80a97ff334cd',
                            name='Irvin MacGyver',
                        ),
                        shared.TrackingCategoryRef(
                            id='a9e61876-c6ab-421d-a9df-c94d6fecd799',
                            name='Ms. Becky Baumbach',
                        ),
                        shared.TrackingCategoryRef(
                            id='a6d2d000-3553-438c-ac08-6fa21e9152cb',
                            name='Doris Casper III',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ducimus',
                        id='b8e3c8db-0340-48d6-9364-ffd455906d12',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='d48e935c-2c9e-481f-b0be-3e43202d7216',
                        name='Colleen Kautzer III',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='41870d9d-21f9-4ad0-b0c4-ecc11a083642',
                        name='Kenneth Hoppe',
                    ),
                    shared.TrackingCategoryRef(
                        id='8502a55e-7f73-4bc8-85e3-20a319f4badf',
                        name='Jesus Kreiger',
                    ),
                ],
                unit_amount=6561.59,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='867bc424-2666-4581-addc-a8ef51fcb4c5',
                    name='Manuel Thiel Sr.',
                ),
                description='quo',
                discount_amount=8400.17,
                discount_percentage=6520.92,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='ad0ec7af-edbd-480d-b448-a47f9390c588',
                    name='Donald McLaughlin',
                ),
                quantity=8742.83,
                sub_total=6834.9,
                tax_amount=7047.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9830.6,
                    id='9ef3ffdd-9f7f-4079-af4d-35724cdb0f4d',
                    name='Ms. Billie Boyle',
                ),
                total_amount=8548,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='6844eded-85a9-4065-a628-bdfc2032b6c8',
                            name='Guadalupe Monahan',
                        ),
                        shared.TrackingCategoryRef(
                            id='b7e13584-f7ae-412c-a891-f82ce1157172',
                            name='Shirley Heidenreich',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='voluptate',
                        id='dcfa89df-975e-4356-a860-92e9c3ddc5f1',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='dea1026d-541a-44d1-90fe-b21780bccc0d',
                        name='Kelvin Shanahan',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='84708fb4-e391-4e6b-8158-c4c4e54599ea',
                        name='Juanita Collier',
                    ),
                    shared.TrackingCategoryRef(
                        id='0e9b200c-e78a-41bd-8fb7-a0a116ce723d',
                        name='Susan Mraz',
                    ),
                ],
                unit_amount=6443.97,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ipsa',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=9444.05,
                    total_amount=4974.8,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='25b29122-030d-483f-9aeb-7799d22e8c1f',
                        name='Clifford Mertz',
                    ),
                    currency='GBP',
                    currency_rate=3642.84,
                    id='fdc42c87-6c2c-42df-b4cf-c1c76230f841',
                    note='maiores',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='architecto',
                    total_amount=6981.17,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=2115.18,
                    total_amount=9417.43,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='db14db6b-e5a6-4859-98e2-2ae20da16fc2',
                        name='Miss Randy Kshlerin',
                    ),
                    currency='USD',
                    currency_rate=5739.94,
                    id='c57e854e-9043-49d2-a246-569462407084',
                    note='delectus',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='dolorum',
                    total_amount=7262.44,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=7613.31,
                    total_amount=9040.51,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='f0222519-4db5-4541-8adc-669af90a26c7',
                        name='Carroll Runte',
                    ),
                    currency='GBP',
                    currency_rate=9788.57,
                    id='068981d6-bb33-4cfa-a348-c31bf407ee4f',
                    note='eligendi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='alias',
                    total_amount=7704.67,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=7491.01,
                    total_amount=4679.47,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8f156263-98a0-4dc7-a632-4ccb06c8ca12',
                        name='Mark D'Amore',
                    ),
                    currency='USD',
                    currency_rate=1664.01,
                    id='70b8d572-2dd8-495b-8bcf-24db95969335',
                    note='qui',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='molestiae',
                    total_amount=2925.71,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='33994d78-de3b-46e9-b89f-5abb7f662550',
                purchase_order_number='est',
            ),
            shared.PurchaseOrderRef(
                id='28382ac4-83af-4d23-95bb-a650164e06f5',
                purchase_order_number='quidem',
            ),
        ],
        reference='asperiores',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.PAID,
        sub_total=9197.3,
        supplemental_data=shared.BillSupplementalData(
            content={
                "molestias": {
                    "expedita": 'quisquam',
                },
                "praesentium": {
                    "assumenda": 'repudiandae',
                    "maiores": 'ipsum',
                    "commodi": 'vitae',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='2b63c205-fda8-4407-b4a6-8a9a35d086b6',
            supplier_name='maiores',
        ),
        tax_amount=4120.24,
        total_amount=4281.99,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=8810.67,
                name='Dr. Michael Cormier',
            ),
            shared.BillWithholdingTax(
                amount=9784.6,
                name='Carrie Franey',
            ),
            shared.BillWithholdingTax(
                amount=1754.55,
                name='Marcia Rempel',
            ),
            shared.BillWithholdingTax(
                amount=1795.88,
                name='Sidney Simonis',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=667418,
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadBillAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    bill_id='7110701885',
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
from codataccounting.models import operations

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
from codataccounting.models import operations

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
from codataccounting.models import operations

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
from codataccounting.models import operations

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
    query='recusandae',
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
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
        amount_due=6617.64,
        currency='GBP',
        currency_rate=804.67,
        due_date='2022-10-23T00:00:00.000Z',
        id='8258fd0a-9eba-447f-bd3e-f049640d6a18',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='c87adf59-6fdf-41ad-837a-e80c1c19c95b',
                    name='Jackie Mitchell',
                ),
                description='ducimus',
                discount_amount=5315.68,
                discount_percentage=9575.1,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='a3f69699-1af3-488c-a036-14448c7977a0',
                    name='Toby Denesik',
                ),
                quantity=2175.52,
                sub_total=3851.65,
                tax_amount=413.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1533.7,
                    id='8efeef93-4152-4ed7-a253-f4c157deaa71',
                    name='Linda Windler',
                ),
                total_amount=3626.93,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='ccf667aa-f9bb-4ad1-85fe-431d6bf5c838',
                            name='Kelvin Prosacco',
                        ),
                        shared.TrackingCategoryRef(
                            id='20cb67fc-4b42-45e9-9e62-34c9f7b79dfe',
                            name='Mathew Klocko',
                        ),
                        shared.TrackingCategoryRef(
                            id='c38d4baf-91e5-406e-b890-a54b475f16f5',
                            name='Marcella Dooley',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='fuga',
                        id='3c4ac631-b99e-426c-ad8f-9fdb9410f63b',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='817837b0-1afd-4d78-8624-189eb44873f5',
                        name='Diana Feil V',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='bf125ce4-152e-4ab9-8d7e-5224a6a0e123',
                        name='Mathew Lockman',
                    ),
                    shared.TrackingCategoryRef(
                        id='ec59e1f6-7f3c-44cc-a4b6-d7696ff3c574',
                        name='Mrs. Ana Armstrong',
                    ),
                    shared.TrackingCategoryRef(
                        id='7e44f51f-8b08-44c3-997e-193a245467f9',
                        name='Naomi Kozey',
                    ),
                    shared.TrackingCategoryRef(
                        id='2d5cc497-2233-4e66-bd8f-e5d00b979ef2',
                        name='Thelma Lemke',
                    ),
                ],
                unit_amount=1357.75,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='corporis',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=8017.81,
                    total_amount=7748.66,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='10964003-13b3-4e50-84f6-5fe72dc4077d',
                        name='Myra Schroeder',
                    ),
                    currency='GBP',
                    currency_rate=351.07,
                    id='8efc15ce-b4d6-4e1e-ae0f-75aedf2acab5',
                    note='quas',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='cupiditate',
                    total_amount=6025.61,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=6004.71,
                    total_amount=1535.13,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6ddb5894-61e7-4421-8be6-d9502f0ea930',
                        name='Hector Mayer',
                    ),
                    currency='EUR',
                    currency_rate=7675.4,
                    id='2f72f885-0090-4491-9608-207888ec6618',
                    note='consectetur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='tenetur',
                    total_amount=8971.46,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=3553.42,
                    total_amount=6016.34,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='eb40ec16-faf7-45b0-b532-a4da37cbaaf4',
                        name='Lauren Cremin',
                    ),
                    currency='USD',
                    currency_rate=2579.59,
                    id='2c9b2ad3-2daf-4e81-a88f-4444573fecd4',
                    note='quam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='nemo',
                    total_amount=1986.16,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='63c82093-79aa-469c-95fb-cf79da18a782',
                purchase_order_number='eos',
            ),
            shared.PurchaseOrderRef(
                id='bf95894e-6861-4adb-95f9-e5d751c9fe8f',
                purchase_order_number='nihil',
            ),
            shared.PurchaseOrderRef(
                id='502bfdc3-4508-441f-9764-456379f3fb27',
                purchase_order_number='accusamus',
            ),
            shared.PurchaseOrderRef(
                id='21f86265-7b36-4fc6-b9f5-87ce525c6764',
                purchase_order_number='architecto',
            ),
        ],
        reference='fuga',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.OPEN,
        sub_total=968.03,
        supplemental_data=shared.BillSupplementalData(
            content={
                "officiis": {
                    "quae": 'dolore',
                    "in": 'libero',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='4c21ccb4-23ab-4cdc-91fa-abdd88e71f6c',
            supplier_name='labore',
        ),
        tax_amount=5587.31,
        total_amount=1492.35,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=1494.14,
                name='Mitchell Klocko DVM',
            ),
            shared.BillWithholdingTax(
                amount=4549.04,
                name='Wilfred Aufderhar',
            ),
        ],
    ),
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=8446,
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
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadBillAttachmentRequest(
    request_body=operations.UploadBillAttachmentRequestBody(
        content='iste'.encode(),
        request_body='accusamus',
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

