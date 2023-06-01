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

Posts a new bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) to see which integrations support this endpoint.


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
        amount_due=4486.01,
        currency='culpa',
        currency_rate=424.89,
        due_date='fuga',
        id='116ce723-d409-47fa-b0e9-af725b291220',
        issue_date='amet',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='d83f5aeb-7799-4d22-a8c1-f8493825fdc4',
                    name='Jacquelyn Lueilwitz',
                ),
                description='maxime',
                discount_amount=1514.86,
                discount_percentage=7915.38,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='2dfb4cfc-1c76-4230-b841-fb1bd23fdb14',
                    name='Malcolm Johnson',
                ),
                quantity=3422.26,
                sub_total=6422.79,
                tax_amount=3755.88,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5163.63,
                    id='5998e22a-e20d-4a16-bc2b-271a289c57e8',
                    name='Ellen Walter II',
                ),
                total_amount=2199.4,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d2224656-9462-4407-884f-7ab37cef0222',
                            name='Jean Mayert',
                        ),
                        shared.TrackingCategoryRef(
                            id='b55410ad-c669-4af9-8a26-c7cdc981f068',
                            name='Johnnie Berge',
                        ),
                        shared.TrackingCategoryRef(
                            id='bb33cfaa-348c-431b-b407-ee4fcf0c42b7',
                            name='Abel Buckridge',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='consequuntur',
                        id='6398a0dc-7663-424c-8b06-c8ca12d02529',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='0b8d5722-dd89-45b8-bcf2-4db959693352',
                        name='Clinton Greenholt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='994d78de-3b6e-4938-9f5a-bb7f662550a2',
                        name='Travis Leannon',
                    ),
                ],
                unit_amount=7547.84,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='incidunt',
        note='deleniti',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='est',
                    currency='reiciendis',
                    currency_rate=8204.62,
                    total_amount=1378.31,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='315bba65-0164-4e06-b5bf-6ae591bc8bde',
                        name='Mr. Dale Jenkins',
                    ),
                    currency='ex',
                    currency_rate=2033.96,
                    id='c205fda8-4077-44a6-8a9a-35d086b6f66f',
                    note='accusamus',
                    paid_on_date='reiciendis',
                    reference='consequatur',
                    total_amount=1487.14,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='e9f443b4-257b-4992-88db-da6a61efa219',
                purchase_order_number='atque',
            ),
        ],
        reference='explicabo',
        source_modified_date='ullam',
        status=shared.BillStatus.PAID,
        sub_total=9874.35,
        supplemental_data=shared.BillSupplementalData(
            content={
                "aut": {
                    "iste": 'eveniet',
                    "nam": 'animi',
                    "labore": 'voluptate',
                },
                "voluptatibus": {
                    "nulla": 'dolorem',
                    "voluptates": 'a',
                },
                "perferendis": {
                    "excepturi": 'aliquid',
                    "dolore": 'voluptatem',
                },
                "illum": {
                    "culpa": 'dicta',
                    "atque": 'ratione',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='1c87adf5-96fd-4f1a-9837-ae80c1c19c95',
            supplier_name='tempore',
        ),
        tax_amount=6379.69,
        total_amount=6105.63,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=5589.92,
                name='Dora Lemke',
            ),
            shared.BillWithholdingTax(
                amount=2212.4,
                name='Brad Mayer',
            ),
            shared.BillWithholdingTax(
                amount=5865.56,
                name='Kristine Wilderman',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=561858,
)

res = s.bills.create(req)

if res.create_bill_response is not None:
    # handle response
```

## delete

﻿The _Delete Bills_ endpoint allows you to delete a specified Bill from an accounting platform. 

### Process 
1. Pass the `{billId}` to the _Delete Bills_ endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the Bill object was deleted from the accounting platform.
3. (Optional) Check that the Bill was deleted from the accounting platform.

### Effect on related objects

Be aware that deleting a Bill from an accounting platform might cause related objects to be modified. For example, if you delete a paid Bill in QuickBooks Online, the bill is deleted but the bill payment against that bill is not. The bill payment is converted to a payment on account.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Delete | Details                                                                                                      |  
|-------------|-------------|--------------------------------------------------------------------------------------------------------------|
| QuickBooks Online | No          | -                                                                                                            |
| Oracle NetSuite   | No          | When deleting a Bill that's already linked to a Bill payment, you must delete the linked Bill payment first. |

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
    bill_id='quod',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## download_attachment

﻿Download bill attachment.

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
    bill_id='repudiandae',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.download_attachment(req)

if res.data is not None:
    # handle response
```

## get

﻿Get a bill.

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
    bill_id='eaque',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.bills.get(req)

if res.bill is not None:
    # handle response
```

## get_attachment

﻿Get bill attachment.

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
    bill_id='consectetur',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

﻿Get create/update bill model.

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support creating and updating a bill.

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

## list

﻿Gets the latest bills for a company, with pagination.

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
    query='autem',
)

res = s.bills.list(req)

if res.bills is not None:
    # handle response
```

## list_attachments

﻿List bill attachments.

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
    bill_id='vitae',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

﻿Posts an updated bill to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update bill model](https://docs.codat.io/accounting-api#/operations/get-create-update-bills-model).

> **Supported Integrations**
> 
> Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bills) for integrations that support updating a bill.

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
        amount_due=2569.75,
        currency='incidunt',
        currency_rate=2669.76,
        due_date='quos',
        id='c7977a0e-f2f5-4360-a8ef-eef934152ed7',
        issue_date='itaque',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='53f4c157-deaa-4717-8f44-5accf667aaf9',
                    name='Garry Nicolas IV',
                ),
                description='ad',
                discount_amount=9594.2,
                discount_percentage=9133.93,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='431d6bf5-c838-4fbb-8c20-cb67fc4b425e',
                    name='Sergio Tremblay',
                ),
                quantity=2277.06,
                sub_total=2796.79,
                tax_amount=7835.39,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5816.8,
                    id='f7b79dfe-b77a-45c3-8d4b-af91e506ef89',
                    name='Lee Hegmann',
                ),
                total_amount=2574.88,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='5f16f56d-385a-43c4-ac63-1b99e26ced8f',
                            name='Darrin Skiles',
                        ),
                        shared.TrackingCategoryRef(
                            id='410f63bb-f817-4837-b01a-fdd788624189',
                            name='Rudy Gorczany',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ducimus',
                        id='3f5033f1-9dbf-4125-8e41-52eab9cd7e52',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='a6a0e123-b784-47ec-99e1-f67f3c4cce4b',
                        name='Angel Kris',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='ff3c5747-5013-457e-84f5-1f8b084c3197',
                        name='Samuel Mann',
                    ),
                    shared.TrackingCategoryRef(
                        id='245467f9-4874-4c2d-9cc4-972233e66bd8',
                        name='Frankie Herzog Jr.',
                    ),
                ],
                unit_amount=7277.89,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='excepturi',
        note='odio',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='officiis',
                    currency='delectus',
                    currency_rate=1692.29,
                    total_amount=232.36,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='38732059-0ccc-4109-a400-313b3e5044f6',
                        name='Shawna Trantow',
                    ),
                    currency='assumenda',
                    currency_rate=7637.47,
                    id='4077d0cc-3f40-48ef-815c-eb4d6e1eae0f',
                    note='odio',
                    paid_on_date='veniam',
                    reference='fuga',
                    total_amount=9290.12,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='possimus',
                    currency='tenetur',
                    currency_rate=1499.41,
                    total_amount=6481.82,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='cab58b99-1c92-46dd-b589-461e7421cbe6',
                        name='Mr. Rene Harris',
                    ),
                    currency='consequatur',
                    currency_rate=8776.19,
                    id='a930b69f-7ac2-4f72-b885-009049116082',
                    note='perferendis',
                    paid_on_date='esse',
                    reference='quas',
                    total_amount=5007.68,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='laudantium',
                    currency='voluptates',
                    currency_rate=7939.09,
                    total_amount=4196.69,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6183bfe9-659e-4b40-ac16-faf75b0b532a',
                        name='Antonia Muller',
                    ),
                    currency='eligendi',
                    currency_rate=7363.13,
                    id='aaf4452c-4842-4c9b-aad3-2dafe81a88f4',
                    note='incidunt',
                    paid_on_date='labore',
                    reference='ut',
                    total_amount=3134.2,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='3fecd473-53f6-43c8-a093-79aa69cd5fbc',
                purchase_order_number='sapiente',
            ),
            shared.PurchaseOrderRef(
                id='79da18a7-822b-4f95-894e-6861adb55f9e',
                purchase_order_number='ipsam',
            ),
        ],
        reference='fugiat',
        source_modified_date='odio',
        status=shared.BillStatus.PARTIALLY_PAID,
        sub_total=819.17,
        supplemental_data=shared.BillSupplementalData(
            content={
                "occaecati": {
                    "necessitatibus": 'rem',
                    "a": 'nihil',
                    "veniam": 'aut',
                    "magni": 'rerum',
                },
                "voluptatibus": {
                    "quod": 'non',
                    "dolore": 'enim',
                    "alias": 'blanditiis',
                    "modi": 'illo',
                },
                "a": {
                    "molestiae": 'autem',
                },
                "dolore": {
                    "nostrum": 'ex',
                    "amet": 'voluptate',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='9f3fb27e-21f8-4626-97b3-6fc6b9f587ce',
            supplier_name='ad',
        ),
        tax_amount=1676.13,
        total_amount=3457.46,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=4005.1,
                name='Miss Terri Gerhold',
            ),
            shared.BillWithholdingTax(
                amount=2443.32,
                name='Jane Towne II',
            ),
            shared.BillWithholdingTax(
                amount=4496.94,
                name='Mario Runolfsson DDS',
            ),
            shared.BillWithholdingTax(
                amount=7678.8,
                name='Jesus Corkery',
            ),
        ],
    ),
    bill_id='facilis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=792555,
)

res = s.bills.update(req)

if res.update_bill_response is not None:
    # handle response
```

## upload_attachment

﻿Upload bill attachment.

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
        content='vero'.encode(),
        request_body='impedit',
    ),
    bill_id='omnis',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
