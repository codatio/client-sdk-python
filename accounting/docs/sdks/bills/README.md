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
        amount_due=3759.94,
        currency='EUR',
        currency_rate=2420.99,
        due_date='2022-10-23T00:00:00.000Z',
        id='a5acfbe2-fd57-4075-b792-9177deac646e',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='573409e3-eb1e-45a2-b12e-b07f116db995',
                    name='Bernice Yundt',
                ),
                description='enim',
                discount_amount=9449.5,
                discount_percentage=6573.19,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='88970e18-9dbb-430f-8b33-ea055b197cd4',
                    name='Kellie Corwin',
                ),
                quantity=1645.32,
                sub_total=8138.8,
                tax_amount=5129.05,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1403.84,
                    id='d3513bb6-f48b-4656-bcdb-35ff2e4b2753',
                    name='Genevieve Lebsack',
                ),
                total_amount=6040.78,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7319c177-d525-4f77-b114-eeb52ff785fc',
                            name='Mrs. Claudia Leuschke',
                        ),
                        shared.TrackingCategoryRef(
                            id='4c98e0c2-bb89-4eb7-9dad-636c600503d8',
                            name='Mr. Jonathon Fay',
                        ),
                        shared.TrackingCategoryRef(
                            id='0f739ae9-e057-4eb8-89e2-810331f3981d',
                            name='Mr. Bethany Koch',
                        ),
                        shared.TrackingCategoryRef(
                            id='607f3c93-c73b-49da-bf2c-eda7e23f2257',
                            name='Virginia Bins',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='delectus',
                        id='4b7544e4-72e8-4028-97a5-b40463a7d575',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='400e764a-d733-44ec-9b78-1b36a08088d1',
                        name='Jessica Turner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a200ef04-22eb-4216-8cf9-ab8366c723ff',
                        name='Cameron Mosciski III',
                    ),
                    shared.TrackingCategoryRef(
                        id='bee4825c-1fc0-4e11-9c80-bff918544ec4',
                        name='Nadine Terry',
                    ),
                    shared.TrackingCategoryRef(
                        id='ce8f1977-773e-4635-a2a7-b408f05e3d48',
                        name='Clint Ortiz',
                    ),
                    shared.TrackingCategoryRef(
                        id='13a1f5fd-9425-49c0-b36f-25ea944f3b75',
                        name='Dr. Alexandra Bernhard',
                    ),
                ],
                unit_amount=7869.54,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='37a51262-4383-45bb-805a-23a45cefc5fd',
                    name='Juan Abshire DDS',
                ),
                description='necessitatibus',
                discount_amount=1559.78,
                discount_percentage=1189.32,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='69e51001-9c6d-4c5e-b476-2799bfbbe694',
                    name='Irvin Rippin',
                ),
                quantity=7202.66,
                sub_total=2791.72,
                tax_amount=9253.95,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7972.54,
                    id='ae6c3d5d-b3ad-4ebd-9dae-a4c506a8aa94',
                    name='Thomas Conroy',
                ),
                total_amount=3085.28,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f5e9d9a4-578a-4dc1-ac60-0dec001ac802',
                            name='Louis Treutel V',
                        ),
                        shared.TrackingCategoryRef(
                            id='ff8f0f81-6ff3-4477-813e-902c14125b09',
                            name='Carol O'Reilly',
                        ),
                        shared.TrackingCategoryRef(
                            id='8151a472-af92-43c5-949f-83f350cf876f',
                            name='Mr. Robin Miller',
                        ),
                        shared.TrackingCategoryRef(
                            id='6ecbb4e2-43cf-4789-bfaf-eda53e5ae6e0',
                            name='Myron Boyle',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quisquam',
                        id='2b9c247c-8837-43a4-8e19-42f32e550557',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='f5d56d0b-d0af-42df-a13d-b4f62cba3f89',
                        name='Joyce O'Connell',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='0b80a692-4d3b-42ec-bcc8-f895010f5dd3',
                        name='Chester Willms V',
                    ),
                    shared.TrackingCategoryRef(
                        id='04e54c82-f168-4a36-bc88-73e484380b1f',
                        name='Yvette Larson',
                    ),
                    shared.TrackingCategoryRef(
                        id='275a60a0-4c49-45cc-a991-71b51c1bdb1c',
                        name='Leroy Ratke',
                    ),
                    shared.TrackingCategoryRef(
                        id='8ebdfc4c-cca9-49bc-bfc0-b2dce10873e4',
                        name='Ms. Susie Batz',
                    ),
                ],
                unit_amount=4312.53,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='78878ba8-581a-4582-88c5-4fefa9c95f2e',
                    name='Noel Hauck',
                ),
                description='nemo',
                discount_amount=8493.37,
                discount_percentage=2012.66,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='07cfee81-206e-4281-bfa4-a41c480d3f21',
                    name='Theresa Pfannerstill I',
                ),
                quantity=1018.54,
                sub_total=449.29,
                tax_amount=1341.73,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8603.62,
                    id='514f4cc6-f18b-4f96-a1a6-a4f77a87ee3e',
                    name='Susie Ward',
                ),
                total_amount=1316.87,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='65b34418-e3bb-491c-8d97-5e0e8419d8f8',
                            name='Lila Bradtke',
                        ),
                        shared.TrackingCategoryRef(
                            id='f3e07edc-c4aa-45f3-8abd-905a972e0567',
                            name='Myrtle Cremin',
                        ),
                        shared.TrackingCategoryRef(
                            id='b2d30947-0bf7-4a4f-a87c-f535a6fae54e',
                            name='Miss Cary Howe',
                        ),
                        shared.TrackingCategoryRef(
                            id='21f023b7-5d23-467f-a1a0-cc8df79f0a39',
                            name='Miss Estelle Mills',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='commodi',
                        id='4b7c15df-bace-4188-b1c4-ee2c8c6ce611',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='eb1c7cbd-b6ee-4c74-b78b-a25317747dc9',
                        name='Annette Osinski',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='af5dd672-3dc0-4f5a-a2f3-a6b700878756',
                        name='Gail Fay',
                    ),
                    shared.TrackingCategoryRef(
                        id='a6c98b55-5540-480d-80bc-acc6cbd6b5f3',
                        name='Ms. Wilbert McGlynn',
                    ),
                    shared.TrackingCategoryRef(
                        id='04f926ba-d255-4381-9b47-4b0ed20e5624',
                        name='Moses Wuckert',
                    ),
                    shared.TrackingCategoryRef(
                        id='39a910ab-dcab-4626-b669-6e1ec00221b3',
                        name='Yvonne Stamm',
                    ),
                ],
                unit_amount=6294.61,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='tempore',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=9890.89,
                    total_amount=8360.53,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a8d0c549-ef03-4004-978a-61fa1cf20688',
                        name='Jared Koepp DVM',
                    ),
                    currency='EUR',
                    currency_rate=7989.53,
                    id='71dca163-f2a3-4c80-a97f-f334cddf857a',
                    note='perspiciatis',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eum',
                    total_amount=951.23,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='76c6ab21-d29d-4fc9-8d6f-ecd799390066',
                purchase_order_number='laborum',
            ),
            shared.PurchaseOrderRef(
                id='6d2d0003-5533-48ce-8086-fa21e9152cb3',
                purchase_order_number='beatae',
            ),
            shared.PurchaseOrderRef(
                id='19167b8e-3c8d-4b03-808d-6d364ffd4559',
                purchase_order_number='alias',
            ),
        ],
        reference='ex',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.UNKNOWN,
        sub_total=1548.4,
        supplemental_data=shared.BillSupplementalData(
            content={
                "neque": {
                    "numquam": 'rem',
                    "officiis": 'omnis',
                    "neque": 'corporis',
                    "quod": 'dolores',
                },
                "placeat": {
                    "recusandae": 'quos',
                    "dicta": 'sapiente',
                    "ipsum": 'consequatur',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='be3e4320-2d72-4165-b650-6641870d9d21',
            supplier_name='voluptatibus',
        ),
        tax_amount=6012.28,
        total_amount=6456.09,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=79.19,
                name='Sharon Ruecker',
            ),
            shared.BillWithholdingTax(
                amount=7639.37,
                name='Carl Breitenberg V',
            ),
            shared.BillWithholdingTax(
                amount=1917.24,
                name='Anita Dare III',
            ),
            shared.BillWithholdingTax(
                amount=5123.7,
                name='Mr. Armando Hermann',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=312690,
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
    query='esse',
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
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
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
        amount_due=6975.91,
        currency='EUR',
        currency_rate=5062.45,
        due_date='2022-10-23T00:00:00.000Z',
        id='5e320a31-9f4b-4adf-947c-9a867bc42426',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='5816ddca-8ef5-41fc-b4c5-93ec12cdaad0',
                    name='Clark Kohler',
                ),
                description='saepe',
                discount_amount=8139.75,
                discount_percentage=7487.23,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='d80df448-a47f-4939-8c58-880983dabf9e',
                    name='Jeffery Williamson',
                ),
                quantity=8301.49,
                sub_total=6077.42,
                tax_amount=9666.52,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4877.65,
                    id='f079af4d-3572-44cd-b0f4-d281187d5684',
                    name='Eloise Stoltenberg',
                ),
                total_amount=5057.99,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='a9065e62-8bdf-4c20-b2b6-c879923b7e13',
                            name='Leah Graham',
                        ),
                        shared.TrackingCategoryRef(
                            id='ae12c689-1f82-4ce1-9571-72305377dcfa',
                            name='Terrance Strosin',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quam',
                        id='5e356686-092e-49c3-9dc5-f111dea1026d',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='1a4d190f-eb21-4780-bccc-0dbbddb48470',
                        name='Dominick Purdy',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='91e6bc15-8c4c-44e5-8599-ea342260e9b2',
                        name='Elizabeth Rutherford',
                    ),
                ],
                unit_amount=5371.4,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='a1bd8fb7-a0a1-416c-a723-d4097fa30e9a',
                    name='Kurt Cronin',
                ),
                description='quia',
                discount_amount=6090.94,
                discount_percentage=1206.46,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='22030d83-f5ae-4b77-99d2-2e8c1f849382',
                    name='Marta Stanton',
                ),
                quantity=1663.24,
                sub_total=7639.28,
                tax_amount=5526.87,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4484.82,
                    id='6c2c2dfb-4cfc-41c7-a230-f841fb1bd23f',
                    name='Alton Bernhard',
                ),
                total_amount=7092.34,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='be5a6859-98e2-42ae-a0da-16fc2b271a28',
                            name='Clark Hermiston',
                        ),
                        shared.TrackingCategoryRef(
                            id='854e9043-9d22-4246-9694-62407084f7ab',
                            name='Nellie Ruecker',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='accusantium',
                        id='2225194d-b554-410a-9c66-9af90a26c7cd',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='81f06898-1d6b-4b33-8faa-348c31bf407e',
                        name='Francis Yundt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c42b78f1-5626-4398-a0dc-766324ccb06c',
                        name='Mr. Benny O'Reilly',
                    ),
                ],
                unit_amount=271.97,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='enim',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=4866.06,
                    total_amount=27.58,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b8d5722d-d895-4b8b-8f24-db959693352f',
                        name='Joanne Hermiston',
                    ),
                    currency='USD',
                    currency_rate=5812.69,
                    id='4d78de3b-6e93-489f-9abb-7f662550a283',
                    note='totam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='deserunt',
                    total_amount=7547.84,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='83afd231-5bba-4650-964e-06f5bf6ae591',
                purchase_order_number='expedita',
            ),
            shared.PurchaseOrderRef(
                id='c8bdef36-12b6-43c2-85fd-a840774a68a9',
                purchase_order_number='laborum',
            ),
        ],
        reference='dolor',
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.BillStatus.DRAFT,
        sub_total=229.66,
        supplemental_data=shared.BillSupplementalData(
            content={
                "voluptas": {
                    "voluptas": 'maiores',
                    "ea": 'vel',
                    "delectus": 'accusamus',
                },
                "reiciendis": {
                    "sed": 'accusantium',
                },
                "voluptates": {
                    "maiores": 'quaerat',
                    "numquam": 'non',
                    "cum": 'incidunt',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='257b992c-8dbd-4a6a-a1ef-a2198258fd0a',
            supplier_name='iste',
        ),
        tax_amount=9085.87,
        total_amount=7236.23,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=2889.07,
                name='Shari Konopelski',
            ),
            shared.BillWithholdingTax(
                amount=9156.53,
                name='Thomas Hahn',
            ),
            shared.BillWithholdingTax(
                amount=2946.5,
                name='Desiree Howell IV',
            ),
        ],
    ),
    bill_id='13d946f0-c5d5-42bc-b092-97ece17923ab',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=114588,
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
        content='quisquam'.encode(),
        request_body='atque',
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

