# invoices

## Overview

Invoices

### Available Operations

* [create](#create) - Create invoice
* [delete](#delete) - Delete invoice
* [download_attachment](#download_attachment) - Download invoice attachment
* [download_pdf](#download_pdf) - Get invoice as PDF
* [get](#get) - Get invoice
* [get_attachment](#get_attachment) - Get invoice attachment
* [get_create_update_model](#get_create_update_model) - Get create/update invoice model
* [list](#list) - List invoices
* [list_attachments](#list_attachments) - List invoice attachments
* [update](#update) - Update invoice
* [upload_attachment](#upload_attachment) - Push invoice attachment

## create

Posts a new invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) to see which integrations support this endpoint.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=50.37,
        additional_tax_percentage=162.33,
        amount_due=632.79,
        currency='tempora',
        currency_rate=9194.06,
        customer_ref=shared.CustomerRef(
            company_name='hic',
            id='45cea11a-c53e-4bb6-987f-340414c5b9ac',
        ),
        discount_percentage=9131.37,
        due_date='debitis',
        id='400ae9f9-2caf-41b0-a5f1-d14718c6fa2f',
        invoice_number='mollitia',
        issue_date='quibusdam',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='c06c5d95-472c-4dd1-8fc4-3b70bca88fa7',
                    name='Roxanne Green',
                ),
                description='exercitationem',
                discount_amount=817.93,
                discount_percentage=7886.47,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='3dd1eb8f-7f75-4f4f-a3f1-c0a586c3ae7d',
                    name='Patty Hoeger',
                ),
                quantity=8864.96,
                sub_total=9148.03,
                tax_amount=9451.88,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3338.68,
                    id='e142d95b-1dbe-4cef-b7c4-b156e9278275',
                    name='Grady Nitzsche',
                ),
                total_amount=5122.23,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7468063f-799b-4795-ac0b-0fa0bb20a40e',
                            name='Krista Goyette',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='aliquid',
                        id='40642726-57b0-41a0-bc08-fd3921c25793',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='6f093a3e-fa46-4d36-adfa-1011a091b3ec',
                        name='Garry Heller',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='2de1a9d1-4fe7-42e5-a1f9-0303dfc33839',
                        name='Lela Welch',
                    ),
                    shared.TrackingCategoryRef(
                        id='6d1d3209-0fc1-457a-89fe-1961ce9be41c',
                        name='Charlie Monahan',
                    ),
                ],
                unit_amount=4955.97,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='quibusdam',
        note='omnis',
        paid_on_date='molestiae',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='unde',
                    currency='repellendus',
                    currency_rate=78.52,
                    total_amount=4916.69,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b200a58f-fd29-467d-b8fd-882a8e60be62',
                        name='Lynne Schultz',
                    ),
                    currency='veniam',
                    currency_rate=6380.64,
                    id='fdd04c37-5251-42be-ae1d-87ecc5fdcea8',
                    note='eveniet',
                    paid_on_date='molestiae',
                    reference='laborum',
                    total_amount=5326.99,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='adipisci',
                id='11662cda-6d77-4c1d-8606-6237d4227866',
            ),
            shared.SalesOrderRef(
                data_type='quibusdam',
                id='b8a749e3-9845-411c-875e-4f0c004b5bb7',
            ),
            shared.SalesOrderRef(
                data_type='ipsam',
                id='8cc94562-f006-4968-9fcd-1a173d84bbe2',
            ),
        ],
        source_modified_date='modi',
        status=shared.InvoiceStatus.VOID,
        sub_total=1277.99,
        supplemental_data=shared.SupplementalData(
            content={
                "praesentium": {
                    "magnam": 'mollitia',
                },
                "doloribus": {
                    "doloremque": 'odio',
                    "ratione": 'corporis',
                    "eligendi": 'expedita',
                },
                "laboriosam": {
                    "molestias": 'corporis',
                },
            },
        ),
        total_amount=8154.52,
        total_discount=2900.44,
        total_tax_amount=6668.63,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=6035.51,
                name='Dr. Wilbur Orn III',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=607549,
)

res = s.invoices.create(req)

if res.create_invoice_response is not None:
    # handle response
```

## delete

﻿The _Delete Invoices_ endpoint allows you to delete a specified Invoice from an accounting platform.

### Process
1. Pass the `{invoiceId}` to the _Delete Invoices_ endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the Invoice object was deleted from the accounting platform.
3. (Optional) Check that the Invoice was deleted from the accounting platform.

### Effect on related objects

Be aware that deleting an Invoice from an accounting platform might cause related objects to be modified. For example, if you delete a paid invoice from QuickBooks Online, the invoice is deleted but the payment against that invoice is not. The payment is converted to a payment on account.

## Integration specifics
Integrations that support soft delete do not permanently delete the object in the accounting platform.

| Integration | Soft Deleted | 
|-------------|--------------|
| QuickBooks Online | Yes    |     

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.
> We're increasing support for object deletion across various accounting platforms and data types. You can check our [Accounting API Public Product Roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) for the latest status.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='veritatis',
)

res = s.invoices.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

## download_attachment

﻿Download invoice attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadInvoicesAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='nemo',
)

res = s.invoices.download_attachment(req)

if res.data is not None:
    # handle response
```

## download_pdf

﻿Download invoice as a pdf.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadInvoicePdfRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='nisi',
)

res = s.invoices.download_pdf(req)

if res.data is not None:
    # handle response
```

## get

﻿Get an invoice.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='repellat',
)

res = s.invoices.get(req)

if res.invoice is not None:
    # handle response
```

## get_attachment

﻿Get invoice attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetInvoiceAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='voluptate',
)

res = s.invoices.get_attachment(req)

if res.attachment is not None:
    # handle response
```

## get_create_update_model

﻿Get create/update invoice model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating and updating invoices.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCreateUpdateInvoicesModelRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.invoices.get_create_update_model(req)

if res.push_option is not None:
    # handle response
```

## list

﻿Gets the latest invoices for a company, with pagination.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListInvoicesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='possimus',
)

res = s.invoices.list(req)

if res.invoices is not None:
    # handle response
```

## list_attachments

﻿List invoice attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListInvoiceAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='aspernatur',
)

res = s.invoices.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## update

﻿Posts an updated invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices.
operationId: update-invoice

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=9264.79,
        additional_tax_percentage=9197.03,
        amount_due=1804.63,
        currency='perferendis',
        currency_rate=6247.3,
        customer_ref=shared.CustomerRef(
            company_name='ullam',
            id='05bf03a9-3e94-4480-8a37-fb10789032ac',
        ),
        discount_percentage=2261.31,
        due_date='amet',
        id='3172e2dd-79ec-474b-a7e8-8ddb36fd1ccc',
        invoice_number='nesciunt',
        issue_date='labore',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='c8657347-4f0a-4740-bb4a-b441c3a09e76',
                    name='Katrina Monahan',
                ),
                description='rem',
                discount_amount=313.05,
                discount_percentage=5480.08,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='bbe79445-5ebc-4550-a1c4-26b59c8366fd',
                    name='Kim Braun',
                ),
                quantity=3640.73,
                sub_total=5323.1,
                tax_amount=1563.13,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7881.7,
                    id='1b855e88-9d9e-4f93-ae90-00a13ad81242',
                    name='Jennie Veum',
                ),
                total_amount=1827.3,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='411898e7-3879-4efb-a8ba-ebabb794536e',
                            name='Jeffrey Frami MD',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quidem',
                        id='97631720-b77a-45a5-b65a-79f15271f01c',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='361fed8d-c5ef-4fb4-93e9-089e871fdb4d',
                        name='Katrina Krajcik',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='9c985e43-734a-45d7-ad9e-dd785be5e7af',
                        name='Derrick Hane',
                    ),
                    shared.TrackingCategoryRef(
                        id='7ba6281f-44e3-4a23-b94a-68cc80d30ff7',
                        name='Debra Jacobi',
                    ),
                    shared.TrackingCategoryRef(
                        id='0a91fe9d-9655-43b8-9e00-09c6692de7b3',
                        name='Loretta Collier Jr.',
                    ),
                    shared.TrackingCategoryRef(
                        id='a6aab4ae-7b1a-45b9-88d4-e30491aa35d4',
                        name='Alfredo Fahey',
                    ),
                ],
                unit_amount=98.84,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='ipsum',
        note='quidem',
        paid_on_date='dolorum',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='molestiae',
                    currency='reprehenderit',
                    currency_rate=7232.85,
                    total_amount=5807.71,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='18f03139-8450-47e0-a39c-7e23ecb06046',
                        name='Denise Walter',
                    ),
                    currency='similique',
                    currency_rate=2248.7,
                    id='d6c657e9-de8f-47f0-82d1-986aa99d3a1d',
                    note='ratione',
                    paid_on_date='odit',
                    reference='amet',
                    total_amount=1716.48,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='provident',
                    currency='repudiandae',
                    currency_rate=2826.23,
                    total_amount=3547.05,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='837e8f2a-d6bb-410e-a55f-dc480d6e3308',
                        name='Stella Herman',
                    ),
                    currency='sapiente',
                    currency_rate=632.04,
                    id='86856a7e-82cd-4f9d-8fc2-82c666af3c3f',
                    note='quis',
                    paid_on_date='nostrum',
                    reference='totam',
                    total_amount=5904.76,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='distinctio',
                    currency='accusamus',
                    currency_rate=6668.05,
                    total_amount=3319.44,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='d264e41e-2ca8-4482-ae51-3f6d9d2ad37c',
                        name='Shirley Mueller III',
                    ),
                    currency='esse',
                    currency_rate=7504.07,
                    id='10b68792-163e-467d-8886-0543c0a3049c',
                    note='ipsum',
                    paid_on_date='quod',
                    reference='voluptatibus',
                    total_amount=3769.3,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='sit',
                id='276e7b21-bad9-40d2-b43f-d6c2a10e6c29',
            ),
            shared.SalesOrderRef(
                data_type='quam',
                id='8ec256a5-b092-427f-8c47-996c977bbc57',
            ),
            shared.SalesOrderRef(
                data_type='sapiente',
                id='38928a86-00c5-48d6-bd63-e4aa56846457',
            ),
            shared.SalesOrderRef(
                data_type='omnis',
                id='cfc6c0e5-03f5-4683-9f1d-8ed87b28e8af',
            ),
        ],
        source_modified_date='culpa',
        status=shared.InvoiceStatus.PAID,
        sub_total=7973.76,
        supplemental_data=shared.SupplementalData(
            content={
                "laudantium": {
                    "necessitatibus": 'consequuntur',
                    "aliquam": 'dicta',
                },
                "earum": {
                    "dolorem": 'quidem',
                    "consequuntur": 'ratione',
                },
                "ut": {
                    "dolore": 'inventore',
                },
            },
        ),
        total_amount=4725.74,
        total_discount=8462.5,
        total_tax_amount=1103.98,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=8934.16,
                name='Miss Jeannie Hudson',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='cupiditate',
    timeout_in_minutes=633887,
)

res = s.invoices.update(req)

if res.update_invoice_response is not None:
    # handle response
```

## upload_attachment

﻿Upload invoice attachment.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadInvoiceAttachmentRequest(
    request_body=operations.UploadInvoiceAttachmentRequestBody(
        content='recusandae'.encode(),
        request_body='labore',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='fuga',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
