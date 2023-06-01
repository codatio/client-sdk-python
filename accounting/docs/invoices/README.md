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
        additional_tax_amount=4832.71,
        additional_tax_percentage=2115.84,
        amount_due=8116.96,
        currency='dignissimos',
        currency_rate=8445.24,
        customer_ref=shared.CustomerRef(
            company_name='placeat',
            id='9efaf43d-c623-4620-b313-8f30df3db022',
        ),
        discount_percentage=9381.13,
        due_date='similique',
        id='a565fb8f-652e-4bb9-9383-838790243b29',
        invoice_number='ratione',
        issue_date='facere',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='b30e917f-50fd-4a04-88b1-bb55a292b0bc',
                    name='Pam Quitzon',
                ),
                description='aliquam',
                discount_amount=3855.01,
                discount_percentage=3916.12,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='4eb1d033-88b0-4d1b-b17a-fee74b6feb94',
                    name='Colleen Schmidt',
                ),
                quantity=8490.45,
                sub_total=6734.93,
                tax_amount=9682.72,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2309.03,
                    id='9d16fbf7-6fd1-462b-b03e-3023b93e3431',
                    name='Nichole Williamson',
                ),
                total_amount=7436.12,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='313553cc-f1c2-404c-8adc-c9904c5195b8',
                            name='Leslie Langosh',
                        ),
                        shared.TrackingCategoryRef(
                            id='fa78f1e2-d3b9-401e-8952-bbb4cbb19f71',
                            name='Meredith Mante',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dolore',
                        id='169c1387-271e-418e-a9e4-5118c2cc57fb',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='0b1a78ed-29a9-4d4e-aa85-658c2d4f4c88',
                        name='Pat Grant',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='8fd9667e-46c5-41d2-bfaa-58dcef234c95',
                        name='Kelli Mosciski',
                    ),
                    shared.TrackingCategoryRef(
                        id='f2190abd-9bbc-4c27-a5ec-2659ce028084',
                        name='Sadie Huel',
                    ),
                ],
                unit_amount=9461.61,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='68e45c8a-ddfa-4c75-8500-430c6632b439',
                    name='Jeannie Smitham Sr.',
                ),
                description='nobis',
                discount_amount=2362.69,
                discount_percentage=9294.26,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='91e8f7bc-69d4-460a-b7ec-eb26d10f1ef2',
                    name='Crystal Bernier',
                ),
                quantity=7867.65,
                sub_total=461.37,
                tax_amount=9654.91,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=163.7,
                    id='f873f9d5-c25f-4d3e-8b4a-4a4253c30257',
                    name='Rebecca Wunsch',
                ),
                total_amount=8074.3,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e7dc548b-e09e-441a-ba21-5ca12a4ba9d5',
                            name='Fredrick Ledner V',
                        ),
                        shared.TrackingCategoryRef(
                            id='2cfd0c77-c53e-47e7-94ee-6e8b90bac384',
                            name='Shawn Fahey',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='in',
                        id='03fec31c-5082-44d1-89a3-6a6b2d27eb70',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='a60c8fe4-6e61-477d-b9db-3b70ffbb6970',
                        name='Phil Kuhlman DVM',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6097ef7c-206e-461b-8d30-8714c20a3d98',
                        name='Annie Koelpin',
                    ),
                ],
                unit_amount=5213.33,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='5c3fe655-74db-4af9-8a7c-98f13af28db2',
                    name='Timmy Cruickshank',
                ),
                description='eius',
                discount_amount=9761.21,
                discount_percentage=2074.59,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ded356d7-e14b-421c-9981-96d55af69a1c',
                    name='Shelley Kunze',
                ),
                quantity=9064.68,
                sub_total=2021.61,
                tax_amount=2477.82,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4269.64,
                    id='81c23c39-a7c0-4e17-8b12-c5ba825fe22c',
                    name='Lloyd Runolfsdottir',
                ),
                total_amount=4047.58,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='bfec932a-f681-43d6-9bfe-cec2dd6916f7',
                            name='Roosevelt Koss',
                        ),
                        shared.TrackingCategoryRef(
                            id='a70ec60e-6075-4894-961c-14cd90227e37',
                            name='Gary Schultz',
                        ),
                        shared.TrackingCategoryRef(
                            id='7f1a5491-abe9-4751-b106-d23e03e69815',
                            name='Rex Towne',
                        ),
                        shared.TrackingCategoryRef(
                            id='fcde9e72-9c9d-44f2-98a4-4640ca60db73',
                            name='Bobby Will',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='maiores',
                        id='467dc0d8-da56-4122-826a-b8f277485c19',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='af980da7-a089-4fc4-8db2-74530e5cc7c6',
                        name='Richard Schmeler',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='dcd334b6-f623-4bce-8ab5-0aee5e0da8b9',
                        name='Darrin Hudson',
                    ),
                    shared.TrackingCategoryRef(
                        id='05486e7b-413c-4be2-9176-dc1c43d40f61',
                        name='Mr. Dennis Kilback',
                    ),
                    shared.TrackingCategoryRef(
                        id='7cbe5ee4-f721-4184-8772-f32e3b49dbe0',
                        name='Billy Franey',
                    ),
                    shared.TrackingCategoryRef(
                        id='b6d9948d-6ede-4d47-b680-fc7a17a82e5e',
                        name='Craig Windler',
                    ),
                ],
                unit_amount=5097.39,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='fugiat',
        note='beatae',
        paid_on_date='perferendis',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='aperiam',
                    currency='harum',
                    currency_rate=4794.64,
                    total_amount=8934.34,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='91392ab4-4cb1-4835-808f-461ce53e9144',
                        name='Wallace O'Keefe',
                    ),
                    currency='deserunt',
                    currency_rate=2957.26,
                    id='60addfde-410c-437d-aa91-82a49d9625d3',
                    note='eligendi',
                    paid_on_date='laborum',
                    reference='delectus',
                    total_amount=9680.39,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='minus',
                    currency='inventore',
                    currency_rate=5825.21,
                    total_amount=5027.27,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='eea44527-92bc-4d44-8ea9-8becce0486de',
                        name='Dianna Hintz',
                    ),
                    currency='nihil',
                    currency_rate=2493.35,
                    id='b005503e-8dc6-426f-b77c-65675f5b70e3',
                    note='vero',
                    paid_on_date='eius',
                    reference='optio',
                    total_amount=9589.07,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='impedit',
                id='6a91ec52-624d-4000-94ef-45cea11ac53e',
            ),
            shared.SalesOrderRef(
                data_type='quidem',
                id='b6587f34-0414-4c5b-9ace-e400ae9f92ca',
            ),
            shared.SalesOrderRef(
                data_type='earum',
                id='1b025f1d-1471-48c6-ba2f-ad0c06c5d954',
            ),
            shared.SalesOrderRef(
                data_type='in',
                id='2cdd14fc-43b7-40bc-a88f-a70c43351c3d',
            ),
        ],
        source_modified_date='nulla',
        status=shared.InvoiceStatus.UNKNOWN,
        sub_total=8962.8,
        supplemental_data=shared.SupplementalData(
            content={
                "deleniti": {
                    "odio": 'tenetur',
                    "quam": 'nemo',
                    "sapiente": 'magnam',
                    "hic": 'aspernatur',
                },
                "ipsum": {
                    "quasi": 'cumque',
                    "eaque": 'error',
                    "corporis": 'totam',
                    "commodi": 'maxime',
                },
                "non": {
                    "repudiandae": 'odio',
                    "temporibus": 'reprehenderit',
                    "soluta": 'voluptas',
                },
            },
        ),
        total_amount=4838.96,
        total_discount=9698.61,
        total_tax_amount=8864.96,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9451.88,
                name='Gretchen Bergnaum',
            ),
            shared.WithholdingTaxitems(
                amount=8642.28,
                name='Dr. Dustin Reilly',
            ),
            shared.WithholdingTaxitems(
                amount=9097.17,
                name='Merle Yost',
            ),
            shared.WithholdingTaxitems(
                amount=7789.75,
                name='Hannah Bergnaum',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=928900,
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
    invoice_id='occaecati',
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
    invoice_id='odit',
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
    invoice_id='ducimus',
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
    invoice_id='corrupti',
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
    invoice_id='consequuntur',
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
    query='voluptate',
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
    invoice_id='ipsam',
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
        additional_tax_amount=8902.78,
        additional_tax_percentage=9179.07,
        amount_due=6424.25,
        currency='esse',
        currency_rate=3851.06,
        customer_ref=shared.CustomerRef(
            company_name='laudantium',
            id='17468063-f799-4b79-96c0-b0fa0bb20a40',
        ),
        discount_percentage=9171.02,
        due_date='reprehenderit',
        id='c4ae6406-4272-4657-b01a-07c08fd3921c',
        invoice_number='dolores',
        issue_date='exercitationem',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='930d6f09-3a3e-4fa4-ad36-6dfa1011a091',
                    name='Rodney Turcotte',
                ),
                description='tempore',
                discount_amount=3503.06,
                discount_percentage=2447.13,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='862de1a9-d14f-4e72-a521-f90303dfc338',
                    name='Faye Kozey',
                ),
                quantity=9437.98,
                sub_total=6258.87,
                tax_amount=4112.43,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=8325.3,
                    id='1d32090f-c157-4ac9-be19-61ce9be41c86',
                    name='Drew Schultz',
                ),
                total_amount=6057.59,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='19d07b20-0a58-4ffd-a967-df8fd882a8e6',
                            name='Hannah Thompson',
                        ),
                        shared.TrackingCategoryRef(
                            id='0cd9c5af-dd04-4c37-9251-2beae1d87ecc',
                            name='Lucia Stoltenberg',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='animi',
                        id='8e7a8831-1662-4cda-ad77-c1d86066237d',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='27866db8-a749-4e39-8451-1cc75e4f0c00',
                        name='Patty Harber',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='58cc9456-2f00-4696-85fc-d1a173d84bbe',
                        name='Miss Emma White',
                    ),
                    shared.TrackingCategoryRef(
                        id='34afb073-5cb6-4285-94a2-9aaa1e169156',
                        name='Adrian Schuster',
                    ),
                ],
                unit_amount=9197.03,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='209505bf-03a9-43e9-8480-ca37fb107890',
                    name='Theresa O'Connell',
                ),
                description='amet',
                discount_amount=1995.11,
                discount_percentage=933.23,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='72e2dd79-ec74-4ba7-a88d-db36fd1ccc34',
                    name='Francis Macejkovic',
                ),
                quantity=4958.43,
                sub_total=2225.2,
                tax_amount=2974.63,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4391.23,
                    id='4f0a740f-b4ab-4441-83a0-9e763995d808',
                    name='Preston Thompson',
                ),
                total_amount=2965.41,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='55ebc550-a1c4-426b-99c8-366fdcc13558',
                            name='Rosalie Borer',
                        ),
                        shared.TrackingCategoryRef(
                            id='55e889d9-ef93-42e9-800a-13ad8124208e',
                            name='Wilfred Deckow',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='dicta',
                        id='1898e738-79ef-4be8-baeb-abb794536e90',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='1bb97631-720b-477a-9a53-65a79f15271f',
                        name='Dr. Janet Sanford',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1fed8dc5-effb-4453-a908-9e871fdb4d69',
                        name='Bridget Schumm',
                    ),
                    shared.TrackingCategoryRef(
                        id='c985e437-34a5-4d72-99ed-d785be5e7afe',
                        name='Cathy D'Amore',
                    ),
                ],
                unit_amount=7352.56,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='mollitia',
        note='laboriosam',
        paid_on_date='explicabo',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sunt',
                    currency='repellat',
                    currency_rate=3036.95,
                    total_amount=2670.94,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='e3a23394-a68c-4c80-930f-f72164d0a91f',
                        name='Eduardo Stark',
                    ),
                    currency='minima',
                    currency_rate=3654.98,
                    id='3b89e000-9c66-492d-a7b3-562201a6aab4',
                    note='deserunt',
                    paid_on_date='voluptates',
                    reference='in',
                    total_amount=6889.51,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='vitae',
                    currency='fuga',
                    currency_rate=3711.71,
                    total_amount=6917.11,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='908d4e30-491a-4a35-94a8-39f03bab77b9',
                        name='Mrs. Mattie Wilderman I',
                    ),
                    currency='iste',
                    currency_rate=5540.29,
                    id='4507e0e3-9c7e-423e-8b06-04652e23a3d6',
                    note='quo',
                    paid_on_date='voluptas',
                    reference='quis',
                    total_amount=4438.01,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='vero',
                    currency='unde',
                    currency_rate=8413.46,
                    total_amount=8936.05,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8f7f002d-1986-4aa9-9d3a-1d32329e4583',
                        name='Alexis Lindgren',
                    ),
                    currency='officia',
                    currency_rate=8553.77,
                    id='6bb10e25-5fdc-4480-96e3-308675cbf186',
                    note='molestias',
                    paid_on_date='nostrum',
                    reference='vel',
                    total_amount=6468.22,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='officiis',
                id='82cdf9d0-fc28-42c6-a6af-3c3f5589bea5',
            ),
            shared.SalesOrderRef(
                data_type='possimus',
                id='264e41e2-ca84-4822-a513-f6d9d2ad37c3',
            ),
        ],
        source_modified_date='eaque',
        status=shared.InvoiceStatus.PARTIALLY_PAID,
        sub_total=5821.15,
        supplemental_data=shared.SupplementalData(
            content={
                "iure": {
                    "nobis": 'quae',
                    "sit": 'rerum',
                },
            },
        ),
        total_amount=3867.85,
        total_discount=5362.23,
        total_tax_amount=4770.94,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=1523.59,
                name='Lucy Fahey',
            ),
            shared.WithholdingTaxitems(
                amount=4686.34,
                name='Kyle Ledner',
            ),
            shared.WithholdingTaxitems(
                amount=608.42,
                name='Eleanor Feeney MD',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='adipisci',
    timeout_in_minutes=23984,
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
        content='labore'.encode(),
        request_body='excepturi',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='quisquam',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
