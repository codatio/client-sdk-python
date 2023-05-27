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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateBillRequest(
    bill=shared.Bill(
        amount_due=7674.66,
        currency='doloremque',
        currency_rate=5168.33,
        due_date='iure',
        id='fa21e915-2cb3-4119-967b-8e3c8db03408',
        issue_date='repellendus',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='d364ffd4-5590-46d1-a63d-48e935c2c9e8',
                    name='Miss Jeannie Emmerich',
                ),
                description='sequi',
                discount_amount=9258.47,
                discount_percentage=2863.29,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='3202d721-6576-4506-a418-70d9d21f9ad0',
                    name='Sharon Ruecker',
                ),
                quantity=7639.37,
                sub_total=8061.24,
                tax_amount=922.64,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1073.01,
                    id='a0836429-068b-4850-aa55-e7f73bc845e3',
                    name='Helen O'Reilly V',
                ),
                total_amount=9738.94,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='badf947c-9a86-47bc-8242-6665816ddca8',
                            name='Dr. Emilio Hilll',
                        ),
                        shared.TrackingCategoryRef(
                            id='b4c593ec-12cd-4aad-8ec7-afedbd80df44',
                            name='Otis Greenholt',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='iste',
                        id='390c5888-0983-4dab-b9ef-3ffdd9f7f079',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='4d35724c-db0f-44d2-8118-7d56844eded8',
                        name='Ms. Madeline Miller',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='628bdfc2-032b-46c8-b992-3b7e13584f7a',
                        name='Carl Davis',
                    ),
                    shared.TrackingCategoryRef(
                        id='891f82ce-1157-4172-b053-77dcfa89df97',
                        name='Tasha Dickinson',
                    ),
                    shared.TrackingCategoryRef(
                        id='686092e9-c3dd-4c5f-911d-ea1026d541a4',
                        name='Dr. Terry Mohr',
                    ),
                    shared.TrackingCategoryRef(
                        id='b21780bc-cc0d-4bbd-9b48-4708fb4e391e',
                        name='Mrs. Susie Schowalter',
                    ),
                ],
                unit_amount=7803.7,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='4c4e5459-9ea3-4422-a0e9-b200ce78a1bd',
                    name='Cary Predovic',
                ),
                description='doloremque',
                discount_amount=6813.36,
                discount_percentage=1175.46,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='16ce723d-4097-4fa3-8e9a-f725b2912203',
                    name='Hope Lemke',
                ),
                quantity=3564.85,
                sub_total=6442.99,
                tax_amount=9319.53,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7143,
                    id='7799d22e-8c1f-4849-b825-fdc42c876c2c',
                    name='Marcella Windler',
                ),
                total_amount=7579.62,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c1c76230-f841-4fb1-bd23-fdb14db6be5a',
                            name='Lena Herzog',
                        ),
                        shared.TrackingCategoryRef(
                            id='8e22ae20-da16-4fc2-b271-a289c57e854e',
                            name='Jeffrey Gutmann',
                        ),
                        shared.TrackingCategoryRef(
                            id='d2224656-9462-4407-884f-7ab37cef0222',
                            name='Jean Mayert',
                        ),
                        shared.TrackingCategoryRef(
                            id='b55410ad-c669-4af9-8a26-c7cdc981f068',
                            name='Johnnie Berge',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='libero',
                        id='b33cfaa3-48c3-41bf-807e-e4fcf0c42b78',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='5626398a-0dc7-4663-a4cc-b06c8ca12d02',
                        name='Judy Mertz',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='b8d5722d-d895-4b8b-8f24-db959693352f',
                        name='Joanne Hermiston',
                    ),
                ],
                unit_amount=5831.38,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='occaecati',
        note='numquam',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='molestiae',
                    currency='quas',
                    currency_rate=8341.77,
                    total_amount=9065.24,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3b6e9389-f5ab-4b7f-a625-50a28382ac48',
                        name='Monique Wisoky',
                    ),
                    currency='consectetur',
                    currency_rate=809.98,
                    id='5bba6501-64e0-46f5-bf6a-e591bc8bdef3',
                    note='commodi',
                    paid_on_date='vitae',
                    reference='fugit',
                    total_amount=7240.73,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='ex',
                    currency='neque',
                    currency_rate=7977.12,
                    total_amount=1761.04,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='05fda840-774a-468a-9a35-d086b6f66fef',
                        name='Tammy Bartoletti',
                    ),
                    currency='maiores',
                    currency_rate=3114.49,
                    id='43b4257b-992c-48db-9a6a-61efa2198258',
                    note='doloribus',
                    paid_on_date='pariatur',
                    reference='aut',
                    total_amount=6302.86,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='iste',
                    currency='eveniet',
                    currency_rate=7236.23,
                    total_amount=6585.44,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='47f7d3ef-0496-440d-aa18-31c87adf596f',
                        name='Winston Bergstrom',
                    ),
                    currency='praesentium',
                    currency_rate=2053.9,
                    id='7ae80c1c-19c9-45ba-9986-78fa3f696991',
                    note='fuga',
                    paid_on_date='a',
                    reference='dolor',
                    total_amount=5280.82,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='molestias',
                    currency='quod',
                    currency_rate=9203.89,
                    total_amount=502.91,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3614448c-7977-4a0e-b2f5-36028efeef93',
                        name='Kathleen Harris',
                    ),
                    currency='possimus',
                    currency_rate=4917.84,
                    id='e253f4c1-57de-4aa7-970f-445accf667aa',
                    note='repellat',
                    paid_on_date='cupiditate',
                    reference='soluta',
                    total_amount=7332.26,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='d185fe43-1d6b-4f5c-838f-bb8c20cb67fc',
                purchase_order_number='ut',
            ),
            shared.PurchaseOrderRef(
                id='b425e99e-6234-4c9f-bb79-dfeb77a5c38d',
                purchase_order_number='dolore',
            ),
            shared.PurchaseOrderRef(
                id='baf91e50-6ef8-490a-94b4-75f16f56d385',
                purchase_order_number='fuga',
            ),
        ],
        reference='sequi',
        source_modified_date='maxime',
        status=shared.BillStatus.OPEN,
        sub_total=6714.28,
        supplemental_data=shared.BillSupplementalData(
            content={
                "autem": {
                    "sunt": 'rerum',
                },
                "occaecati": {
                    "necessitatibus": 'fugit',
                    "autem": 'optio',
                    "eveniet": 'fugiat',
                },
                "blanditiis": {
                    "natus": 'sapiente',
                    "repellendus": 'facilis',
                    "molestias": 'dolore',
                    "et": 'accusantium',
                },
                "maiores": {
                    "velit": 'tempore',
                    "expedita": 'hic',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='817837b0-1afd-4d78-8624-189eb44873f5',
            supplier_name='accusantium',
        ),
        tax_amount=1902.6,
        total_amount=2358.13,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=1030.53,
                name='Rufus Reynolds Sr.',
            ),
            shared.BillWithholdingTax(
                amount=3661.17,
                name='Mrs. Darrel Grant',
            ),
            shared.BillWithholdingTax(
                amount=9298.49,
                name='Damon Mueller',
            ),
            shared.BillWithholdingTax(
                amount=4547.61,
                name='Warren Conroy',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=625378,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteBillRequest(
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadBillAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBillRequest(
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetBillAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBillsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='vel',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListBillAttachmentsRequest(
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateBillRequest(
    bill=shared.Bill(
        amount_due=6798.35,
        currency='alias',
        currency_rate=9303.98,
        due_date='ab',
        id='23b7847e-c59e-41f6-bf3c-4cce4b6d7696',
        issue_date='repellat',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='3c574750-1357-4e44-b51f-8b084c3197e1',
                    name='Glenn Nolan',
                ),
                description='corporis',
                discount_amount=3088.66,
                discount_percentage=3816.39,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='7f94874c-2d5c-4c49-b223-3e66bd8fe5d0',
                    name='Jeannette Mante',
                ),
                quantity=8874.22,
                sub_total=9615.76,
                tax_amount=1692.29,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=232.36,
                    id='38732059-0ccc-4109-a400-313b3e5044f6',
                    name='Shawna Trantow',
                ),
                total_amount=8248.61,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='4077d0cc-3f40-48ef-815c-eb4d6e1eae0f',
                            name='Sally Paucek',
                        ),
                        shared.TrackingCategoryRef(
                            id='f2acab58-b991-4c92-addb-589461e7421c',
                            name='Rolando Jerde',
                        ),
                        shared.TrackingCategoryRef(
                            id='502f0ea9-30b6-49f7-ac2f-72f885009049',
                            name='Ms. Carolyn Jacobson',
                        ),
                        shared.TrackingCategoryRef(
                            id='07888ec6-6183-4bfe-9659-eb40ec16faf7',
                            name='Olivia Auer',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='ratione',
                        id='2a4da37c-baaf-4445-ac48-42c9b2ad32da',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='81a88f44-4457-43fe-8d47-353f63c82093',
                        name='Geneva Oberbrunner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='cd5fbcf7-9da1-48a7-822b-f95894e6861a',
                        name='Marco Hermann',
                    ),
                    shared.TrackingCategoryRef(
                        id='9e5d751c-9fe8-4f75-82bf-dc3450841f17',
                        name='Eleanor Gibson',
                    ),
                    shared.TrackingCategoryRef(
                        id='379f3fb2-7e21-4f86-a657-b36fc6b9f587',
                        name='Bert Hand',
                    ),
                ],
                unit_amount=7934.02,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='67641a83-12e5-4047-b4c2-1ccb423abcdc',
                    name='Carl Weimann',
                ),
                description='distinctio',
                discount_amount=8546.46,
                discount_percentage=8621.67,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='88e71f6c-4825-42d7-b71e-7fd074009ef8',
                    name='Carlos Morissette',
                ),
                quantity=717.41,
                sub_total=8135.82,
                tax_amount=8536.25,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4986.39,
                    id='097b5da0-8c57-4fa6-878a-216e19bafeca',
                    name='Mrs. Kathleen McDermott',
                ),
                total_amount=5410.46,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='40b64ff8-ae17-40ef-83b5-f37e4aa86855',
                            name='Cora Jenkins',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='nesciunt',
                        id='2aa5dcb6-682c-4b70-b8cf-d5fb6e91b9a9',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='4846e2c3-309d-4b05-b6d9-e75ca006f539',
                        name='Miss Krista Bosco',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='a8bf92f9-7428-4ad9-a9f8-bf8221125359',
                        name='Joey Labadie',
                    ),
                    shared.TrackingCategoryRef(
                        id='7f7a79cd-72cd-4248-8da2-1729f2ac41ef',
                        name='Jackie Crist',
                    ),
                ],
                unit_amount=1168.07,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='169ac1e4-1d8a-423c-a3e3-4f2dfa4a197f',
                    name='Betsy Walter',
                ),
                description='aspernatur',
                discount_amount=911.36,
                discount_percentage=3687.61,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='1fe17120-9985-43e9-b543-d854439ee224',
                    name='Kristen Bashirian',
                ),
                quantity=2107.1,
                sub_total=7122.09,
                tax_amount=7711.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1027.34,
                    id='54188c2f-56e8-45da-b832-eabd617c3b0d',
                    name='Heather Nader',
                ),
                total_amount=6942.92,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='01bad870-6d46-4082-bfbd-c41ff5d4e2ae',
                            name='Ora Purdy',
                        ),
                        shared.TrackingCategoryRef(
                            id='b35d1763-8f1e-4db7-8359-ecc5cb860f8c',
                            name='Miss Dan Lakin',
                        ),
                        shared.TrackingCategoryRef(
                            id='73810e4f-e444-4729-bcd3-b1dd3bbce247',
                            name='Karl Jacobs',
                        ),
                        shared.TrackingCategoryRef(
                            id='eff50126-d71c-4ffb-90eb-74b8421953b4',
                            name='Melody Stoltenberg',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='labore',
                        id='3159d33e-5953-4c00-9139-863aa41e6c31',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='2f1fcb51-c9a4-41ff-be9c-bd795ee65e07',
                        name='Johnnie Schamberger',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f616ea5c-7164-4193-8b90-f2e09d19d2fc',
                        name='Faith Mosciski',
                    ),
                    shared.TrackingCategoryRef(
                        id='e105944b-935d-4237-a72f-90849d6aed4a',
                        name='Earnest Rogahn',
                    ),
                    shared.TrackingCategoryRef(
                        id='37cd9222-c9ff-4574-91aa-bfa2e761f0ca',
                        name='Meredith Green',
                    ),
                ],
                unit_amount=8757.66,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='f1031e68-99f0-4c20-81e2-2cd55cc0584a',
                    name='Lena Goyette',
                ),
                description='voluptas',
                discount_amount=8175.09,
                discount_percentage=6079.37,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='71fc820c-65b0-437b-b8e0-cc885187e4de',
                    name='Leslie Pacocha',
                ),
                quantity=5461.33,
                sub_total=8037.63,
                tax_amount=3236.14,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8450.13,
                    id='ddb46aa1-cfd6-4d82-8da0-131911296466',
                    name='Dr. Veronica Runte',
                ),
                total_amount=932.99,
                tracking=shared.Propertiestracking(
                    category_refs=[
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
                        shared.TrackingCategoryRef(
                            id='7764eef6-d0c6-4d6e-99c7-3dd634571509',
                            name='Nelson Walker',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='doloremque',
                        id='d3c5a1f9-c242-4c7b-a6a1-f30c73df5b67',
                    ),
                    is_billed_to=shared.BilledToType.UNKNOWN,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='890f42a4-bb43-48d8-9b26-0591d745e3c2',
                        name='Lorraine Marquardt',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3f567e0e-2527-465b-9d62-fcdace1f0121',
                        name='Bernadette Waelchi',
                    ),
                    shared.TrackingCategoryRef(
                        id='39e8f25c-d0d1-49d9-99f4-39e39266cbd9',
                        name='Marta Kreiger',
                    ),
                    shared.TrackingCategoryRef(
                        id='2b241136-95d1-4e66-98fc-c4596217c297',
                        name='Beth Klocko',
                    ),
                    shared.TrackingCategoryRef(
                        id='34254038-bfb5-4971-a981-90557389cedb',
                        name='Spencer Kirlin',
                    ),
                ],
                unit_amount=6340.91,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='dolor',
        note='occaecati',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='unde',
                    currency='labore',
                    currency_rate=8658.06,
                    total_amount=4269.42,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6bc2ae48-0632-4b99-94b6-fa2206369828',
                        name='Vivian Dietrich',
                    ),
                    currency='ab',
                    currency_rate=32.41,
                    id='006bef49-21ec-4205-bb74-9366ac8ee0f2',
                    note='libero',
                    paid_on_date='sapiente',
                    reference='veritatis',
                    total_amount=5927.91,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='veniam',
                    currency='quos',
                    currency_rate=5216.94,
                    total_amount=8135.44,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='40d03f3d-eba2-497b-a3e9-0bc40df868fd',
                        name='Mrs. Norma Greenholt',
                    ),
                    currency='libero',
                    currency_rate=2213.92,
                    id='31d492f4-f127-4fb0-a0bf-1f8217978d0a',
                    note='eligendi',
                    paid_on_date='impedit',
                    reference='officia',
                    total_amount=4850.97,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='aeb7b702-1a52-4046-b64e-99fb0e67e094',
                purchase_order_number='hic',
            ),
            shared.PurchaseOrderRef(
                id='dfed5540-ef53-4a34-a1b8-fe99731adc05',
                purchase_order_number='fugiat',
            ),
        ],
        reference='quas',
        source_modified_date='quis',
        status=shared.BillStatus.VOID,
        sub_total=9080.3,
        supplemental_data=shared.BillSupplementalData(
            content={
                "illum": {
                    "rerum": 'voluptate',
                    "perferendis": 'maiores',
                    "harum": 'ratione',
                    "molestias": 'odio',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='4290d336-561e-4ca1-aef8-9451bd76eeeb',
            supplier_name='nemo',
        ),
        tax_amount=841.54,
        total_amount=5623.39,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=2657.73,
                name='Dana Bradtke',
            ),
            shared.BillWithholdingTax(
                amount=8325.89,
                name='Mr. Vivian Harvey',
            ),
            shared.BillWithholdingTax(
                amount=437.97,
                name='Janis Greenholt',
            ),
            shared.BillWithholdingTax(
                amount=7217.73,
                name='Dr. Louise Will',
            ),
        ],
    ),
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=296127,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UploadBillAttachmentRequest(
    request_body=operations.UploadBillAttachmentRequestBody(
        content='corrupti'.encode(),
        request_body='exercitationem',
    ),
    bill_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
