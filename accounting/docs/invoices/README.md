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
        additional_tax_amount=7162.96,
        additional_tax_percentage=938.38,
        amount_due=1709.49,
        currency='EUR',
        currency_rate=3147.59,
        customer_ref=shared.CustomerRef(
            company_name='nam',
            id='a825fe22-cd5c-4ba6-bbfe-c932af6813d6',
        ),
        discount_percentage=3347.36,
        due_date='2022-10-23T00:00:00.000Z',
        id='fecec2dd-6916-4f7f-87dd-a70ec60e6075',
        invoice_number='praesentium',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='d61c14cd-9022-47e3-bc0d-977f1a5491ab',
                    name='Eduardo Kulas DDS',
                ),
                description='vitae',
                discount_amount=387.35,
                discount_percentage=4168.03,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='d23e03e6-9815-4aae-99fc-de9e729c9d4f',
                    name='Freda Leannon',
                ),
                quantity=2746.11,
                sub_total=3852.3,
                tax_amount=3114.5,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=16.63,
                    id='ca60db73-a2f9-43f4-a7dc-0d8da5612202',
                    name='Janie Roberts',
                ),
                total_amount=1810.16,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7485c197-6af9-480d-a7a0-89fc44db2745',
                            name='Brenda Torp',
                        ),
                        shared.TrackingCategoryRef(
                            id='c7c6d0cb-cfdc-4d33-8b6f-623bcecab50a',
                            name='Clay Hauck PhD',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='officia',
                        id='8b9af6ad-0548-46e7-b413-cbe2d176dc1c',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='d40f61d1-7115-47cb-a5ee-4f7211840772',
                        name='Chad Connelly',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='49dbe0f2-3b7b-46d9-948d-6eded477680f',
                        name='Ms. Brad Pacocha',
                    ),
                    shared.TrackingCategoryRef(
                        id='82e5e82f-d28d-4104-8a7e-91392ab44cb1',
                        name='Mr. Jeff Hilll',
                    ),
                    shared.TrackingCategoryRef(
                        id='f461ce53-e914-4498-a9ba-460addfde410',
                        name='Jeff Kuhic',
                    ),
                ],
                unit_amount=6589.17,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='9182a49d-9625-4d3c-affc-198eea445279',
                    name='Bridget Schneider',
                ),
                description='ut',
                discount_amount=588.2,
                discount_percentage=9020.01,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='a98becce-0486-4de0-956d-73b005503e8d',
                    name='Raul Christiansen',
                ),
                quantity=9794.26,
                sub_total=4671.12,
                tax_amount=4892.61,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7730.17,
                    id='65675f5b-70e3-4e4c-bcc6-a91ec52624d0',
                    name='Margaret Berge',
                ),
                total_amount=9411.74,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='5cea11ac-53eb-4b65-87f3-40414c5b9ace',
                            name='Miss Francis Beier',
                        ),
                        shared.TrackingCategoryRef(
                            id='9f92caf1-b025-4f1d-9471-8c6fa2fad0c0',
                            name='Francis Harris',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='exercitationem',
                        id='472cdd14-fc43-4b70-bca8-8fa70c43351c',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='d1eb8f7f-75f4-4f23-b1c0-a586c3ae7d7b',
                        name='Glenda Wisozk',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='5e142d95-b1db-4ece-bf7c-4b156e927827',
                        name='Raquel VonRueden',
                    ),
                    shared.TrackingCategoryRef(
                        id='68174680-63f7-499b-b956-c0b0fa0bb20a',
                        name='Jennifer Von',
                    ),
                    shared.TrackingCategoryRef(
                        id='4ae64064-2726-457b-81a0-7c08fd3921c2',
                        name='Delores Moore PhD',
                    ),
                    shared.TrackingCategoryRef(
                        id='6f093a3e-fa46-4d36-adfa-1011a091b3ec',
                        name='Garry Heller',
                    ),
                ],
                unit_amount=3904.23,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='nulla',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=8706.71,
                    total_amount=1150.28,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4fe72e52-1f90-4303-9fc3-38397fffa6d1',
                        name='Ms. Earl Collier DVM',
                    ),
                    currency='EUR',
                    currency_rate=956.45,
                    id='57ac9fe1-961c-4e9b-a41c-869dd7d9719d',
                    note='consequatur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='harum',
                    total_amount=1382.61,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='eaque',
                id='a58ffd29-67df-48fd-882a-8e60be620cd9',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.DRAFT,
        sub_total=6380.64,
        supplemental_data=shared.SupplementalData(
            content={
                "possimus": {
                    "doloremque": 'ut',
                    "eligendi": 'nesciunt',
                    "voluptate": 'corporis',
                    "aspernatur": 'veniam',
                },
                "quasi": {
                    "harum": 'earum',
                },
                "mollitia": {
                    "quasi": 'vero',
                    "atque": 'voluptate',
                    "itaque": 'quisquam',
                    "minus": 'corporis',
                },
                "delectus": {
                    "quod": 'saepe',
                    "animi": 'deleniti',
                    "eveniet": 'molestiae',
                    "laborum": 'voluptatum',
                },
            },
        ),
        total_amount=5002.48,
        total_discount=2381.22,
        total_tax_amount=921.66,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4150.3,
                name='Norma Sawayn',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=428284,
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
    invoice_id='quibusdam',
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
    invoice_id='iusto',
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
    invoice_id='voluptate',
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
    invoice_id='cumque',
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
    invoice_id='sunt',
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
    query='fugiat',
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
    invoice_id='rem',
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
        additional_tax_amount=3878.48,
        additional_tax_percentage=394.9,
        amount_due=3920.09,
        currency='USD',
        currency_rate=1404.57,
        customer_ref=shared.CustomerRef(
            company_name='nesciunt',
            id='7d422786-6db8-4a74-9e39-84511cc75e4f',
        ),
        discount_percentage=5.69,
        due_date='2022-10-23T00:00:00.000Z',
        id='004b5bb7-58cc-4945-a2f0-069685fcd1a1',
        invoice_number='nihil',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='84bbe24f-2983-44af-b073-5cb6285d4a29',
                    name='Dr. Wilbur Orn III',
                ),
                description='omnis',
                discount_amount=866.05,
                discount_percentage=3678.44,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='6f7d2ee2-0950-45bf-83a9-3e94480ca37f',
                    name='Andrew Bednar',
                ),
                quantity=6183.21,
                sub_total=542.66,
                tax_amount=1965.04,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1438.47,
                    id='ac333172-e2dd-479e-874b-a7e88ddb36fd',
                    name='Vicky Ruecker',
                ),
                total_amount=2904.79,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='c8657347-4f0a-4740-bb4a-b441c3a09e76',
                            name='Katrina Monahan',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='rem',
                        id='08bbe794-455e-4bc5-90a1-c426b59c8366',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='cc135582-c1b8-455e-889d-9ef932e9000a',
                        name='Peggy Nolan',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='24208efd-2341-4189-8e73-879efbe8baeb',
                        name='Pete Rice',
                    ),
                ],
                unit_amount=2814.76,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='536e9035-1bb9-4763-9720-b77a5a5365a7',
                    name='Timmy Bernier',
                ),
                description='voluptate',
                discount_amount=705.55,
                discount_percentage=9961.97,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='01c0d361-fed8-4dc5-affb-453e9089e871',
                    name='Jody Rogahn',
                ),
                quantity=3763.5,
                sub_total=5968.08,
                tax_amount=4751.53,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7361.58,
                    id='dd9c985e-4373-44a5-972d-9edd785be5e7',
                    name='Terrell Tillman',
                ),
                total_amount=1729.85,
                tracking=shared.Propertiestracking1(
                    category_refs=[
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
                    customer_ref=shared.CustomerRef(
                        company_name='consequatur',
                        id='3bab77b9-18f0-4313-9845-07e0e39c7e23',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='b0604652-e23a-43d6-8657-e9de8f7f002d',
                        name='Toni Legros',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='99d3a1d3-2329-4e45-837e-8f2ad6bb10e2',
                        name='Roberta Wisozk',
                    ),
                    shared.TrackingCategoryRef(
                        id='480d6e33-0867-45cb-b186-856a7e82cdf9',
                        name='Donald Wiegand',
                    ),
                    shared.TrackingCategoryRef(
                        id='82c666af-3c3f-4558-9bea-5d264e41e2ca',
                        name='Francis Lockman',
                    ),
                ],
                unit_amount=8864.94,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='513f6d9d-2ad3-47c3-8990-77c10b687921',
                    name='Cindy Vandervort',
                ),
                description='repellendus',
                discount_amount=2517.76,
                discount_percentage=5242.33,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='860543c0-a304-49c3-8f6c-0276e7b21bad',
                    name='Robert Stanton',
                ),
                quantity=2834.63,
                sub_total=2437.27,
                tax_amount=9841.11,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8573.88,
                    id='6c2a10e6-c297-48ec-a56a-5b09227fcc47',
                    name='Wendell Huels',
                ),
                total_amount=4585.85,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='bbc57f38-928a-4860-8c58-d67d63e4aa56',
                            name='Jay Kassulke',
                        ),
                        shared.TrackingCategoryRef(
                            id='79cfc6c0-e503-4f56-831f-1d8ed87b28e8',
                            name='Darnell Nader',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='excepturi',
                        id='86e241e4-3b23-4424-97d1-3e3f62aa9ae4',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='8ab4a9c4-92c5-4e8b-a5d4-aa4a508bd380',
                        name='Aaron Marks',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='dd71bdda-a30b-47b9-9449-ae69c088d418',
                        name='Ms. Wm Kohler II',
                    ),
                    shared.TrackingCategoryRef(
                        id='f423d543-935f-4377-ac5c-9b7e93b6a3c5',
                        name='Mrs. Grace Botsford',
                    ),
                    shared.TrackingCategoryRef(
                        id='7c34cab0-ecb8-412a-a614-8944a8e90850',
                        name='Annette Reilly',
                    ),
                ],
                unit_amount=3468.95,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='38253343-fb0a-44e6-aea4-7578d171e294',
                    name='Christy Bernhard',
                ),
                description='optio',
                discount_amount=3993.59,
                discount_percentage=4504.05,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='9b6b2f25-359b-4855-9015-b62c8b83a38a',
                    name='Angelo Langosh',
                ),
                quantity=1119.71,
                sub_total=2686.2,
                tax_amount=2857.2,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=1609.42,
                    id='00c2caeb-1ae1-4ecf-8c34-946bba7a05a8',
                    name='Oscar O'Connell',
                ),
                total_amount=7724.02,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b3688cca-3632-4727-a0e9-66e97e054103',
                            name='Michele Koelpin',
                        ),
                        shared.TrackingCategoryRef(
                            id='8ff24911-45fa-4b9e-99a4-af336664eaa6',
                            name='Timmy Daniel',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='quasi',
                        id='4e8c1b35-2acc-4eda-8c52-27814eca016b',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='1ea1342d-4104-4a25-af71-de57a11d614a',
                        name='Shannon Carter',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='2ea48673-d522-4b82-8a90-30660f024c79',
                        name='Alexander Rosenbaum',
                    ),
                    shared.TrackingCategoryRef(
                        id='4c2b3a32-c488-4ade-a2f6-aa558a65e208',
                        name='Susan Boyer',
                    ),
                    shared.TrackingCategoryRef(
                        id='a34bb87d-4f62-4127-a607-d1606294514c',
                        name='Freda Reichel',
                    ),
                ],
                unit_amount=6279.31,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='sapiente',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=1578.59,
                    total_amount=7272.94,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='e8787034-93f4-49aa-8465-a3283279b719',
                        name='Raymond Rosenbaum',
                    ),
                    currency='USD',
                    currency_rate=4429.32,
                    id='3d86e3b3-5e49-4a31-b577-8ce54cacb0e3',
                    note='vero',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='sint',
                    total_amount=4960.42,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=2892.81,
                    total_amount=3596.49,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='bacf63b2-1518-46ab-9e3a-022614315d15',
                        name='Lena Cummings',
                    ),
                    currency='EUR',
                    currency_rate=3778.77,
                    id='1afc7186-ff20-4b7a-b3df-40ca0d7657c1',
                    note='ex',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ab',
                    total_amount=7166.01,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=132.23,
                    total_amount=3450.21,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5271b251-1dd6-406d-91b2-8272bc9c3221',
                        name='Becky Kunde V',
                    ),
                    currency='USD',
                    currency_rate=276.89,
                    id='fcbb2b93-c15f-4670-bd17-84831653eeb3',
                    note='tempore',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='vero',
                    total_amount=1407.83,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='dicta',
                id='c3109983-663c-466d-8bb7-df6cb09c8b40',
            ),
            shared.SalesOrderRef(
                data_type='praesentium',
                id='e0713774-de4f-4ee1-81d9-780a10c47b95',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.DRAFT,
        sub_total=370.79,
        supplemental_data=shared.SupplementalData(
            content={
                "vel": {
                    "blanditiis": 'soluta',
                    "quia": 'similique',
                    "ipsam": 'a',
                    "alias": 'perferendis',
                },
                "aspernatur": {
                    "sit": 'esse',
                },
                "accusamus": {
                    "quae": 'dolore',
                    "molestias": 'maiores',
                },
                "cupiditate": {
                    "alias": 'sit',
                },
            },
        ),
        total_amount=6122.66,
        total_discount=9351.45,
        total_tax_amount=8479.43,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5771.16,
                name='Phyllis Koch',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='quidem',
    timeout_in_minutes=306065,
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
        content='fuga'.encode(),
        request_body='itaque',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='iste',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
