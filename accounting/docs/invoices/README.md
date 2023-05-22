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

﻿Posts a new invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating invoices.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.CreateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=7733.49,
        additional_tax_percentage=6927.98,
        amount_due=289.46,
        currency='voluptas',
        currency_rate=447.24,
        customer_ref=shared.CustomerRef(
            company_name='numquam',
            id='652e23a3-d6c6-457e-9de8-f7f002d1986a',
        ),
        discount_percentage=6416.3,
        due_date='natus',
        id='9d3a1d32-329e-4458-b7e8-f2ad6bb10e25',
        invoice_number='ipsam',
        issue_date='reiciendis',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='c480d6e3-3086-475c-bf18-6856a7e82cdf',
                    name='Sammy Barrows',
                ),
                description='fugit',
                discount_amount=5376.88,
                discount_percentage=1666.02,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='c666af3c-3f55-489b-aa5d-264e41e2ca84',
                    name='Bobby Crooks',
                ),
                quantity=684,
                sub_total=2081.12,
                tax_amount=9914.72,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4176.65,
                    id='d9d2ad37-c309-4907-bc10-b68792163e67',
                    name='Kyle Ledner',
                ),
                total_amount=608.42,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='43c0a304-9c3c-4f6c-8276-e7b21bad90d2',
                            name='April Frami',
                        ),
                        shared.TrackingCategoryRef(
                            id='6c2a10e6-c297-48ec-a56a-5b09227fcc47',
                            name='Wendell Huels',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='esse',
                        id='7bbc57f3-8928-4a86-80c5-8d67d63e4aa5',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='464579cf-c6c0-4e50-bf56-831f1d8ed87b',
                        name='Christy Walter',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='abc986e2-41e4-43b2-b424-17d13e3f62aa',
                        name='Shannon Walker',
                    ),
                    shared.TrackingCategoryRef(
                        id='e8ab4a9c-492c-45e8-ba5d-4aa4a508bd38',
                        name='Kara Cremin',
                    ),
                    shared.TrackingCategoryRef(
                        id='a8dd71bd-daa3-40b7-b914-49ae69c088d4',
                        name='Cassandra Rice',
                    ),
                    shared.TrackingCategoryRef(
                        id='1804f423-d543-4935-b377-ac5c9b7e93b6',
                        name='Earl Ruecker',
                    ),
                ],
                unit_amount=2263.68,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='105e7c34-cab0-4ecb-812a-66148944a8e9',
                    name='Ms. Jennie Hartmann',
                ),
                description='nam',
                discount_amount=7904.63,
                discount_percentage=1817.55,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='53825334-3fb0-4a4e-a6ea-47578d171e29',
                    name='Ms. Christine Leannon',
                ),
                quantity=7630.13,
                sub_total=3993.59,
                tax_amount=4504.05,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=5874.59,
                    id='b6b2f253-59b8-455d-815b-62c8b83a38a8',
                    name='Dwayne MacGyver I',
                ),
                total_amount=2857.2,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='00c2caeb-1ae1-4ecf-8c34-946bba7a05a8',
                            name='Oscar O'Connell',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='impedit',
                        id='5b3688cc-a363-4272-b60e-966e97e05410',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='47d78ff2-4911-445f-ab9e-59a4af336664',
                        name='Gerard O'Conner',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='2ff14e8c-1b35-42ac-8eda-cc5227814eca',
                        name='Alice Kautzer',
                    ),
                    shared.TrackingCategoryRef(
                        id='41ea1342-d410-44a2-9ef7-1de57a11d614',
                        name='Ms. Eddie Frami',
                    ),
                    shared.TrackingCategoryRef(
                        id='92ea4867-3d52-42b8-a8a9-030660f024c7',
                        name='Abraham Goyette',
                    ),
                    shared.TrackingCategoryRef(
                        id='64c2b3a3-2c48-48ad-a62f-6aa558a65e20',
                        name='Mrs. Marvin Armstrong',
                    ),
                ],
                unit_amount=6853.65,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='34bb87d4-f621-427a-a07d-1606294514c3',
                    name='Preston McCullough',
                ),
                description='omnis',
                discount_amount=9600.37,
                discount_percentage=2360.34,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='8bd2be87-8703-4493-b49a-a8465a328327',
                    name='Miss Cesar Konopelski',
                ),
                quantity=707.2,
                sub_total=7573.22,
                tax_amount=8840.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6422.68,
                    id='673d86e3-b35e-449a-b135-778ce54cacb0',
                    name='Chris Terry',
                ),
                total_amount=4960.42,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='045bacf6-3b21-4518-aab5-e3a022614315',
                            name='Dennis Heathcote',
                        ),
                        shared.TrackingCategoryRef(
                            id='299e61af-c718-46ff-a0b7-a73df40ca0d7',
                            name='Erin Kihn III',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eius',
                        id='1bbf0552-71b2-4511-9d60-6dd1b28272bc',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='3221697b-1880-4fcb-b2b9-3c15f670bd17',
                        name='Francis Labadie III',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3eeb3b6e-241c-4310-9983-663c66dcbb7d',
                        name='Gilbert Schaden V',
                    ),
                    shared.TrackingCategoryRef(
                        id='c8b408e0-7137-474d-a4fe-e101d9780a10',
                        name='Frederick Kub',
                    ),
                ],
                unit_amount=3444.01,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='040d6c8b-2a5f-4002-a07e-4048f90009ed',
                    name='Violet Baumbach',
                ),
                description='quos',
                discount_amount=8818.91,
                discount_percentage=6977.83,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='4ae9d641-61e9-4150-8323-b2c09b924771',
                    name='Herman Howe',
                ),
                quantity=9129.86,
                sub_total=3652.88,
                tax_amount=7053.17,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4498.47,
                    id='ec762664-9d84-4eb9-a4cf-d2276e0b88fb',
                    name='Brad Stoltenberg',
                ),
                total_amount=6278.38,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b6e8dbf8-12f8-43b1-8a6a-9ffc561929cc',
                            name='Tracy Hilll MD',
                        ),
                        shared.TrackingCategoryRef(
                            id='1395918d-a1d4-48e7-8e3c-f8e1143da930',
                            name='Robin Cummerata',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='aut',
                        id='8af22184-439b-43de-8756-ccce470cd214',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='6e6152cf-01d0-4d8c-ba4b-9a5bf935dfe9',
                        name='Debbie Zieme',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1e9c097e-da62-4344-ae1a-9237e9984c80',
                        name='Alexander Koss',
                    ),
                    shared.TrackingCategoryRef(
                        id='891923c1-8ca8-4d69-8568-9214fa20207e',
                        name='Marta Murphy I',
                    ),
                    shared.TrackingCategoryRef(
                        id='8cd7f1bc-2cab-4af7-bc2c-cba4bef0df68',
                        name='Shaun Swift',
                    ),
                ],
                unit_amount=1625.48,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='earum',
        note='necessitatibus',
        paid_on_date='quam',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='expedita',
                    currency='itaque',
                    currency_rate=40.87,
                    total_amount=4114.07,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='9fb36add-7040-480e-8a3f-c73a5a034b11',
                        name='Bobbie Mayer',
                    ),
                    currency='ratione',
                    currency_rate=6253.92,
                    id='fa6987a4-72b7-409a-953e-22301068539c',
                    note='saepe',
                    paid_on_date='ipsa',
                    reference='perspiciatis',
                    total_amount=2348.29,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='repellendus',
                id='10acd15d-8cc3-406b-b86b-3d37bd204a1f',
            ),
        ],
        source_modified_date='ipsum',
        status=shared.InvoiceStatus.DRAFT,
        sub_total=378.08,
        supplemental_data=shared.SupplementalData(
            content={
                "rerum": {
                    "ex": 'voluptatibus',
                },
                "voluptas": {
                    "odio": 'dolorum',
                    "eius": 'praesentium',
                },
                "corporis": {
                    "provident": 'quod',
                },
            },
        ),
        total_amount=2245.24,
        total_discount=2424.79,
        total_tax_amount=4619.68,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5749.23,
                name='Christina Luettgen',
            ),
            shared.WithholdingTaxitems(
                amount=5522.12,
                name='Vicki Reilly I',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=784316,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DeleteInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadInvoicesAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.DownloadInvoicePdfRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetInvoiceAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListInvoicesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='nihil',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListInvoiceAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UpdateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=9937.18,
        additional_tax_percentage=8210.46,
        amount_due=1600.93,
        currency='odit',
        currency_rate=3147.32,
        customer_ref=shared.CustomerRef(
            company_name='debitis',
            id='47871a88-ed72-4a2d-8af4-158ac2d0f0f5',
        ),
        discount_percentage=5522.56,
        due_date='optio',
        id='3b87b470-40d0-4d98-a9d8-2c5e306f5576',
        invoice_number='maiores',
        issue_date='nemo',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='deb0286d-0bc4-43b1-8ab3-78f2fcff81dd',
                    name='Ms. Lance Thiel',
                ),
                description='repellat',
                discount_amount=4819.23,
                discount_percentage=2892.95,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ef54c921-6e89-4263-93bb-6fc2c8d27010',
                    name='Duane Pouros',
                ),
                quantity=6641.93,
                sub_total=8554.62,
                tax_amount=3899.32,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8980.86,
                    id='3e1d9d3b-6603-434a-91aa-1d5d2247de9b',
                    name='Meredith Greenfelder IV',
                ),
                total_amount=514.52,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='768a96bb-3987-4883-98eb-a1bbf7143356',
                            name='Marc Fay',
                        ),
                        shared.TrackingCategoryRef(
                            id='a164249b-211c-4e46-b951-652b158ca914',
                            name='Johanna Bartoletti',
                        ),
                        shared.TrackingCategoryRef(
                            id='632b31ca-d692-4ffc-8745-005e9d3d934e',
                            name='Sheila Jerde',
                        ),
                        shared.TrackingCategoryRef(
                            id='c388664f-6985-4530-a2e2-aed6aaf863c2',
                            name='Clint Beatty DDS',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='vel',
                        id='9a3d906f-6ebd-45ad-bec7-394f25f634b3',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='0714e6be-8c3e-409c-a4d3-42ac299a6e5e',
                        name='Lee Weber I',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='02e945f5-3743-4efd-a119-8221f9b1f7d9',
                        name='Amos Wilkinson',
                    ),
                    shared.TrackingCategoryRef(
                        id='9682acee-fb04-4f8c-912c-aabea708ed57',
                        name='Wallace Schultz',
                    ),
                ],
                unit_amount=3304.22,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='d460599d-5c33-4495-b6d5-5209e9a2253b',
                    name='Elena Kreiger',
                ),
                description='praesentium',
                discount_amount=5156.7,
                discount_percentage=3967.41,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='eeae5fd4-b39f-48a1-8906-78f13c686d83',
                    name='Amos Roob',
                ),
                quantity=756.85,
                sub_total=4594.79,
                tax_amount=3137.17,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=9721.89,
                    id='fa906ae5-59b7-42eb-a746-030fe18376c2',
                    name='Merle Strosin',
                ),
                total_amount=4381.93,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='790ed0c1-6a7b-4a47-8404-489f6770ef04',
                            name='Miss Brian McCullough',
                        ),
                        shared.TrackingCategoryRef(
                            id='ba25ee6c-75af-48a6-8a7a-e346e0979e5a',
                            name='Miss Darrel Keeling',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='culpa',
                        id='ca645de9-8675-451a-9cce-61ec2c79a39a',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='a4d5a65b-4d55-462d-9b7d-9e2d6fcf5576',
                        name='Bobbie Stoltenberg',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5c3a8902-82a5-41f4-9cf6-796ed3d724c1',
                        name='Jerald Hand PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='98cce3f7-1660-40da-8e3a-a61c6fe09d85',
                        name='Shelia Hand',
                    ),
                ],
                unit_amount=2018.2,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='2c8c7c3c-710e-4167-bd90-5cb4bedef3c1',
                    name='Pearl Ruecker',
                ),
                description='aperiam',
                discount_amount=5631.81,
                discount_percentage=6128.99,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='5528250d-cbbc-4d3b-921b-88c1ee5e7a06',
                    name='Dr. Sherry Marks',
                ),
                quantity=5137.75,
                sub_total=9667.54,
                tax_amount=6470.68,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=140.4,
                    id='b7d17649-26b0-4cf5-a6cb-6ebabe5e0b99',
                    name='Mrs. Lee Rogahn',
                ),
                total_amount=5558.1,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='6a87bb7a-ecbe-4569-970c-b069907f9894',
                            name='Gloria Gottlieb V',
                        ),
                        shared.TrackingCategoryRef(
                            id='9f01f344-2c61-4be1-b3ba-cde532b6526f',
                            name='Sam Cole',
                        ),
                        shared.TrackingCategoryRef(
                            id='3fe2859c-e322-4231-be66-64c41d2fba5c',
                            name='Shannon Bahringer',
                        ),
                        shared.TrackingCategoryRef(
                            id='b8d291be-b810-4a2a-a874-9479edd4fcf7',
                            name='Dan Bechtelar',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='blanditiis',
                        id='7f08f392-7107-46a2-8b40-c8f08bff1081',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='8f86996c-8e22-4be0-a3cf-47893bd23f86',
                        name='Mary Beatty',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c7834273-caa9-4118-b38f-1b61a331a54d',
                        name='Stephen Bartell',
                    ),
                ],
                unit_amount=2674.45,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='f92fed93-9ba8-4f71-a299-2c20ee1228ac',
                    name='Alberta Shanahan',
                ),
                description='dolore',
                discount_amount=4824,
                discount_percentage=8600.36,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='240bc11e-a482-4824-8cc6-a2f0f5b9d3cb',
                    name='Doris Murray',
                ),
                quantity=5367.04,
                sub_total=4891.64,
                tax_amount=8210.12,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2214.66,
                    id='100e8e2b-9b0d-4746-92a7-c7d1ea0e79fa',
                    name='Robin Rau',
                ),
                total_amount=9824.77,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='79f650b1-e707-4e7e-8396-713bacce072a',
                            name='Ms. Taylor Jacobson IV',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='facere',
                        id='279c10c1-8516-4fd7-8be2-621272628fa5',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='962867e7-2b3a-4650-a4b1-57f9bb6ef72a',
                        name='Brenda Legros PhD',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='9b661a7d-ef16-48b6-8cb2-822b4a9850ed',
                        name='Ora Greenholt DVM',
                    ),
                    shared.TrackingCategoryRef(
                        id='9c4ae551-40e7-4572-ae00-3c2f02941925',
                        name='Kay Runolfsdottir',
                    ),
                    shared.TrackingCategoryRef(
                        id='41c999f4-69f6-4f1c-b1a3-f023c669e6a6',
                        name='Mr. Vicki Bartoletti',
                    ),
                ],
                unit_amount=7126.9,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='id',
        note='consequatur',
        paid_on_date='quis',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='unde',
                    currency='quos',
                    currency_rate=5264.74,
                    total_amount=8122.68,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6720c310-3f1a-440c-8f3e-c8688fd8ec6f',
                        name='Mr. Michael Feest',
                    ),
                    currency='voluptatibus',
                    currency_rate=42.61,
                    id='aaaeee00-4eba-47bf-8732-be509c508713',
                    note='quae',
                    paid_on_date='a',
                    reference='eaque',
                    total_amount=3967.4,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='maiores',
                    currency='voluptatem',
                    currency_rate=7324.85,
                    total_amount=7767.95,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='e55a8687-143c-4979-85ff-797a5da664b7',
                        name='Mitchell Kuhn',
                    ),
                    currency='nihil',
                    currency_rate=2955.37,
                    id='baaa2832-bb65-4862-92a3-1f9b14aa6bde',
                    note='quo',
                    paid_on_date='reprehenderit',
                    reference='repellat',
                    total_amount=2617.34,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='dolore',
                id='232e9a5d-ee1a-4cd7-aa89-981b58fe682e',
            ),
            shared.SalesOrderRef(
                data_type='sunt',
                id='c2dbe23d-58e8-4247-9122-c9f67678fa27',
            ),
        ],
        source_modified_date='occaecati',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=5416.5,
        supplemental_data=shared.SupplementalData(
            content={
                "commodi": {
                    "dolor": 'voluptas',
                    "dolor": 'facere',
                },
            },
        ),
        total_amount=6680.48,
        total_discount=152.97,
        total_tax_amount=4809.17,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=426.64,
                name='Brett Yundt',
            ),
            shared.WithholdingTaxitems(
                amount=7200.66,
                name='Ruben Green III',
            ),
            shared.WithholdingTaxitems(
                amount=2407.81,
                name='Angel Larkin',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    timeout_in_minutes=701054,
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
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.UploadInvoiceAttachmentRequest(
    request_body=operations.UploadInvoiceAttachmentRequestBody(
        content='rem'.encode(),
        request_body='unde',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
