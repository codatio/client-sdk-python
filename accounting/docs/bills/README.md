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
        amount_due=4620.97,
        currency='atque',
        currency_rate=6383.63,
        due_date='ex',
        id='1fa1cf20-688f-477c-9ffc-71dca163f2a3',
        issue_date='eligendi',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='0a97ff33-4cdd-4f85-ba9e-61876c6ab21d',
                    name='Ada Stark',
                ),
                description='unde',
                discount_amount=2814.54,
                discount_percentage=8145.85,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='6fecd799-3900-466a-ad2d-000355338cec',
                    name='Lena Kerluke',
                ),
                quantity=1440.58,
                sub_total=842.07,
                tax_amount=8996.52,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6119.7,
                    id='152cb311-9167-4b8e-bc8d-b03408d6d364',
                    name='Irvin Shields',
                ),
                total_amount=3539.04,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='06d1263d-48e9-435c-ac9e-81f30be3e432',
                            name='Wanda Stanton',
                        ),
                        shared.TrackingCategoryRef(
                            id='16576506-6418-470d-9d21-f9ad030c4ecc',
                            name='Ms. Teresa Ondricka',
                        ),
                        shared.TrackingCategoryRef(
                            id='6429068b-8502-4a55-a7f7-3bc845e320a3',
                            name='Natasha Wiza',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dolorum',
                        id='df947c9a-867b-4c42-8266-65816ddca8ef',
                    ),
                    is_billed_to=shared.BilledToType.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='fcb4c593-ec12-4cda-ad0e-c7afedbd80df',
                        name='Marjorie Lockman',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='f9390c58-8809-483d-abf9-ef3ffdd9f7f0',
                        name='Guadalupe Murazik',
                    ),
                    shared.TrackingCategoryRef(
                        id='d35724cd-b0f4-4d28-9187-d56844eded85',
                        name='Wade Berge',
                    ),
                ],
                unit_amount=9090.93,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='628bdfc2-032b-46c8-b992-3b7e13584f7a',
                    name='Carl Davis',
                ),
                description='praesentium',
                discount_amount=6155.97,
                discount_percentage=1120.14,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='f82ce115-7172-4305-b77d-cfa89df975e3',
                    name='Gertrude Kautzer',
                ),
                quantity=444.43,
                sub_total=5968.2,
                tax_amount=1458.41,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9320.57,
                    id='9c3ddc5f-111d-4ea1-826d-541a4d190feb',
                    name='Evelyn Kuhlman MD',
                ),
                total_amount=8119.03,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c0dbbddb-4847-408f-b4e3-91e6bc158c4c',
                            name='Lila Hermiston',
                        ),
                        shared.TrackingCategoryRef(
                            id='99ea3422-60e9-4b20-8ce7-8a1bd8fb7a0a',
                            name='Julie Homenick',
                        ),
                        shared.TrackingCategoryRef(
                            id='723d4097-fa30-4e9a-b725-b29122030d83',
                            name='Dan Nolan',
                        ),
                        shared.TrackingCategoryRef(
                            id='7799d22e-8c1f-4849-b825-fdc42c876c2c',
                            name='Marcella Windler',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eligendi',
                        id='fc1c7623-0f84-41fb-9bd2-3fdb14db6be5',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='85998e22-ae20-4da1-afc2-b271a289c57e',
                        name='Maurice Friesen',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='439d2224-6569-4462-8070-84f7ab37cef0',
                        name='Lois Crooks V',
                    ),
                ],
                unit_amount=2907.61,
            ),
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='db55410a-dc66-49af-90a2-6c7cdc981f06',
                    name='Dr. Austin Little',
                ),
                description='libero',
                discount_amount=7225,
                discount_percentage=2253.83,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='3cfaa348-c31b-4f40-bee4-fcf0c42b78f1',
                    name='Sue Cronin',
                ),
                quantity=5681.62,
                sub_total=5493.48,
                tax_amount=6679.77,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=217.01,
                    id='dc766324-ccb0-46c8-8a12-d02529270b8d',
                    name='Courtney Conroy',
                ),
                total_amount=8506.28,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='95b8bcf2-4db9-4596-9335-2f74533994d7',
                            name='Gustavo Ullrich',
                        ),
                        shared.TrackingCategoryRef(
                            id='6e9389f5-abb7-4f66-a550-a28382ac483a',
                            name='Rufus Conn II',
                        ),
                        shared.TrackingCategoryRef(
                            id='bba65016-4e06-4f5b-b6ae-591bc8bdef36',
                            name='Denise Reilly',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quod',
                        id='205fda84-0774-4a68-a9a3-5d086b6f66fe',
                    ),
                    is_billed_to=shared.BilledToType.PROJECT,
                    is_rebilled_to=shared.BilledToType.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='20e9f443-b425-47b9-92c8-dbda6a61efa2',
                        name='Sheryl Littel',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fd0a9eba-47f7-4d3e-b049-640d6a1831c8',
                        name='Harriet Smitham',
                    ),
                    shared.TrackingCategoryRef(
                        id='96fdf1ad-837a-4e80-81c1-9c95ba998678',
                        name='Doug Ernser',
                    ),
                    shared.TrackingCategoryRef(
                        id='96991af3-88ce-4036-9444-8c7977a0ef2f',
                        name='Mr. Edna Howe',
                    ),
                ],
                unit_amount=8905.05,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='a',
        note='itaque',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='repellat',
                    currency='cupiditate',
                    currency_rate=2372.08,
                    total_amount=3035.49,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='152ed7e2-53f4-4c15-bdea-a7170f445acc',
                        name='Rick Howell',
                    ),
                    currency='officia',
                    currency_rate=9949.02,
                    id='9bbad185-fe43-41d6-bf5c-838fbb8c20cb',
                    note='ex',
                    paid_on_date='odio',
                    reference='delectus',
                    total_amount=7949.27,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='ut',
                    currency='distinctio',
                    currency_rate=2630.79,
                    total_amount=1764.18,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5e99e623-4c9f-47b7-9dfe-b77a5c38d4ba',
                        name='Kent Blanda',
                    ),
                    currency='eaque',
                    currency_rate=4064.62,
                    id='ef890a54-b475-4f16-b56d-385a3c4ac631',
                    note='rerum',
                    paid_on_date='occaecati',
                    reference='provident',
                    total_amount=8974.34,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='fugit',
                    currency='autem',
                    currency_rate=7637.09,
                    total_amount=9107.26,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='d8f9fdb9-410f-463b-bf81-7837b01afdd7',
                        name='Jordan Kassulke',
                    ),
                    currency='sunt',
                    currency_rate=5015.91,
                    id='9eb44873-f503-43f1-9dbf-125ce4152eab',
                    note='error',
                    paid_on_date='placeat',
                    reference='temporibus',
                    total_amount=4547.61,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='earum',
                    currency='minima',
                    currency_rate=1419.86,
                    total_amount=1383.06,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4a6a0e12-3b78-447e-859e-1f67f3c4cce4',
                        name='Ricardo Stanton',
                    ),
                    currency='sint',
                    currency_rate=4001.45,
                    id='ff3c5747-5013-457e-84f5-1f8b084c3197',
                    note='officiis',
                    paid_on_date='dicta',
                    reference='excepturi',
                    total_amount=2336.18,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='245467f9-4874-4c2d-9cc4-972233e66bd8',
                purchase_order_number='voluptatibus',
            ),
            shared.PurchaseOrderRef(
                id='e5d00b97-9ef2-4038-b320-590ccc109640',
                purchase_order_number='voluptatem',
            ),
            shared.PurchaseOrderRef(
                id='313b3e50-44f6-45fe-b2dc-4077d0cc3f40',
                purchase_order_number='corrupti',
            ),
        ],
        reference='itaque',
        source_modified_date='earum',
        status=shared.BillStatus.VOID,
        sub_total=1199.28,
        supplemental_data=shared.BillSupplementalData(
            content={
                "impedit": {
                    "cum": 'dolore',
                    "illum": 'ea',
                    "officiis": 'quasi',
                    "accusamus": 'animi',
                },
                "necessitatibus": {
                    "maiores": 'odio',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='5aedf2ac-ab58-4b99-9c92-6ddb589461e7',
            supplier_name='numquam',
        ),
        tax_amount=1446.21,
        total_amount=788.02,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=7486.56,
                name='Rafael Schuster',
            ),
            shared.BillWithholdingTax(
                amount=263.89,
                name='Elsa Adams',
            ),
            shared.BillWithholdingTax(
                amount=6238.68,
                name='Margaret Rau',
            ),
            shared.BillWithholdingTax(
                amount=9787.97,
                name='Lee Runte',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=460597,
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
    bill_id='explicabo',
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
    bill_id='delectus',
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
    bill_id='quos',
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
    bill_id='deleniti',
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
    query='enim',
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
    bill_id='sit',
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
        amount_due=279.55,
        currency='natus',
        currency_rate=293.46,
        due_date='tempora',
        id='91160820-7888-4ec6-a183-bfe9659eb40e',
        issue_date='quod',
        line_items=[
            shared.BillLineItem(
                account_ref=shared.AccountRef(
                    id='6faf75b0-b532-4a4d-a37c-baaf4452c484',
                    name='Sheri McGlynn',
                ),
                description='est',
                discount_amount=8687.09,
                discount_percentage=2163.79,
                is_direct_cost=False,
                item_ref=shared.ItemRef(
                    id='2dafe81a-88f4-4444-973f-ecd47353f63c',
                    name='Aaron Becker',
                ),
                quantity=4722.9,
                sub_total=6040.27,
                tax_amount=6463.21,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6621.84,
                    id='69cd5fbc-f79d-4a18-a782-2bf95894e686',
                    name='Lynda Schuppe',
                ),
                total_amount=3129.53,
                tracking=shared.Propertiestracking(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='9e5d751c-9fe8-4f75-82bf-dc3450841f17',
                            name='Eleanor Gibson',
                        ),
                        shared.TrackingCategoryRef(
                            id='379f3fb2-7e21-4f86-a657-b36fc6b9f587',
                            name='Bert Hand',
                        ),
                        shared.TrackingCategoryRef(
                            id='c67641a8-312e-4504-bb4c-21ccb423abcd',
                            name='Arturo Bosco',
                        ),
                        shared.TrackingCategoryRef(
                            id='abdd88e7-1f6c-4482-92d7-771e7fd07400',
                            name='Tomas Zieme',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='consequuntur',
                        id='9de1dd70-97b5-4da0-8c57-fa6c78a216e1',
                    ),
                    is_billed_to=shared.BilledToType.CUSTOMER,
                    is_rebilled_to=shared.BilledToType.CUSTOMER,
                    project_ref=shared.ProjectRef(
                        id='afeca619-1498-4140-b64f-f8ae170ef03b',
                        name='Josefina Durgan',
                    ),
                ),
                tracking_category_refs=[
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
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='quis',
        note='dolorem',
        payment_allocations=[
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='sed',
                    currency='quo',
                    currency_rate=917.36,
                    total_amount=761.45,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='a25a8bf9-2f97-4428-ad9a-9f8bf8221125',
                        name='Marion Medhurst',
                    ),
                    currency='blanditiis',
                    currency_rate=2326.02,
                    id='87f7a79c-d72c-4d24-84da-21729f2ac41e',
                    note='tenetur',
                    paid_on_date='exercitationem',
                    reference='nihil',
                    total_amount=1547.23,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='quis',
                    currency='maiores',
                    currency_rate=1168.07,
                    total_amount=1158.49,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='69ac1e41-d8a2-43c2-be34-f2dfa4a197f6',
                        name='Clay Monahan',
                    ),
                    currency='et',
                    currency_rate=3687.61,
                    id='1fe17120-9985-43e9-b543-d854439ee224',
                    note='non',
                    paid_on_date='laboriosam',
                    reference='accusantium',
                    total_amount=2736.38,
                ),
            ),
            shared.BillPaymentAllocation(
                allocation=shared.BillPaymentAllocationAllocation(
                    allocated_on_date='aliquam',
                    currency='dolorem',
                    currency_rate=7122.09,
                    total_amount=7711.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='154188c2-f56e-485d-a783-2eabd617c3b0',
                        name='Leon Braun',
                    ),
                    currency='ut',
                    currency_rate=6942.92,
                    id='f01bad87-06d4-4608-abfb-dc41ff5d4e2a',
                    note='saepe',
                    paid_on_date='labore',
                    reference='doloribus',
                    total_amount=7040.54,
                ),
            ),
        ],
        purchase_order_refs=[
            shared.PurchaseOrderRef(
                id='cb35d176-38f1-4edb-b835-9ecc5cb860f8',
                purchase_order_number='impedit',
            ),
            shared.PurchaseOrderRef(
                id='d580ba73-810e-44fe-8447-297cd3b1dd3b',
                purchase_order_number='libero',
            ),
        ],
        reference='impedit',
        source_modified_date='repudiandae',
        status=shared.BillStatus.OPEN,
        sub_total=2814.16,
        supplemental_data=shared.BillSupplementalData(
            content={
                "harum": {
                    "aliquid": 'blanditiis',
                    "labore": 'repudiandae',
                },
                "reiciendis": {
                    "exercitationem": 'voluptatem',
                    "beatae": 'qui',
                    "laboriosam": 'temporibus',
                    "in": 'veritatis',
                },
            },
        ),
        supplier_ref=shared.SupplierRef(
            id='cffbd0eb-74b8-4421-953b-44bd3c43159d',
            supplier_name='adipisci',
        ),
        tax_amount=2439.38,
        total_amount=8815.49,
        withholding_tax=[
            shared.BillWithholdingTax(
                amount=5913.67,
                name='Mr. Carmen Schmidt Jr.',
            ),
            shared.BillWithholdingTax(
                amount=2305.3,
                name='Isaac Hyatt',
            ),
        ],
    ),
    bill_id='fuga',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    timeout_in_minutes=266461,
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
        content='et'.encode(),
        request_body='eveniet',
    ),
    bill_id='aliquid',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.bills.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
