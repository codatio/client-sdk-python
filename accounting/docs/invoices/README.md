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
        additional_tax_amount=3856.2,
        additional_tax_percentage=6970.56,
        amount_due=4400.63,
        currency='praesentium',
        currency_rate=5207.16,
        customer_ref=shared.CustomerRef(
            company_name='error',
            id='0a3fd3c8-1da1-40f8-823d-f931da3edb51',
        ),
        discount_percentage=9961.99,
        due_date='est',
        id='d94acc94-3513-4772-ad15-321b832a56d6',
        invoice_number='sint',
        issue_date='architecto',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='0ff60eb9-a665-48e6-9a4b-843d382dbec7',
                    name='Jacquelyn Jast',
                ),
                description='autem',
                discount_amount=163.03,
                discount_percentage=3914.99,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='59468ce3-04d8-4849-bf82-14c337f96bb0',
                    name='Cecil Mohr',
                ),
                quantity=4625.93,
                sub_total=1436.68,
                tax_amount=8176.23,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7291.09,
                    id='1344ba9f-78a5-4c0e-97aa-b62e97261fb0',
                    name='Jerome Lowe',
                ),
                total_amount=4514.48,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='51996b5b-4b50-4eef-b12b-7a7ab0344b17',
                            name='Nancy Johnson',
                        ),
                        shared.TrackingCategoryRef(
                            id='deebef89-7f3d-4d0c-8d33-f11b3e4e080a',
                            name='Terry Bednar IV',
                        ),
                        shared.TrackingCategoryRef(
                            id='6ec759e0-2f37-402c-9c8e-2d30ead3104f',
                            name='Theodore Gerlach IV',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='rerum',
                        id='f375b442-8282-41fd-b2f6-9e59267c71cc',
                    ),
                    is_billed_to=shared.BilledToTypeEnum1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToTypeEnum1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='3cd4258d-0358-4a82-8808-fe2751a2047c',
                        name='Marjorie Funk',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='43f9619b-b7d4-40d5-a11f-a436e6259233',
                        name='Luther Hane',
                    ),
                ],
                unit_amount=8428.91,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='237397c7-85b5-4db4-b500-183febdf676b',
                    name='Andrea Bashirian',
                ),
                description='deserunt',
                discount_amount=7054.18,
                discount_percentage=4503.12,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='50052a56-47ed-4c43-9ed8-c4320f41240d',
                    name='Eva Lebsack',
                ),
                quantity=7842.87,
                sub_total=3778.95,
                tax_amount=5909.98,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2042.83,
                    id='b94c3b9d-2488-4d79-9aa4-2fc405669f69',
                    name='Frank Batz',
                ),
                total_amount=1466.93,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='24945081-9d7c-43b1-b418-44060e00310d',
                            name='Norma Frami',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='error',
                        id='01f5afd2-a6c4-4484-aae9-d89253c8962f',
                    ),
                    is_billed_to=shared.BilledToTypeEnum1.UNKNOWN,
                    is_rebilled_to=shared.BilledToTypeEnum1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='96bf51e4-652d-43c3-83d6-1778af491247',
                        name='Anne Hamill',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1909e910-44a5-4de5-9ac7-706670cf1cf5',
                        name='Jeffery Dibbert II',
                    ),
                ],
                unit_amount=1280.87,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='51e66bb4-2689-47d9-9a2d-335670e93ee6',
                    name='Dominick Hammes',
                ),
                description='dolorem',
                discount_amount=3687.85,
                discount_percentage=5295.29,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='aaeacae3-23a3-41bf-bba1-cc97716c802c',
                    name='Dr. Kirk Veum',
                ),
                quantity=8218.96,
                sub_total=6105.84,
                tax_amount=8294.02,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2051.2,
                    id='23f1aa63-ed9c-4f1c-856b-cba51ef2454a',
                    name='Marlene Wolf',
                ),
                total_amount=9973.54,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='16cdd544-4a75-4628-b3c7-dd9efaf43dc6',
                            name='Victoria Jenkins DVM',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='nesciunt',
                        id='138f30df-3db0-422f-aa56-5fb8f652ebb9',
                    ),
                    is_billed_to=shared.BilledToTypeEnum1.PROJECT,
                    is_rebilled_to=shared.BilledToTypeEnum1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='83838790-243b-4293-9ab3-0e917f50fda0',
                        name='Francis Lesch MD',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='55a292b0-bc3b-4b74-8664-eb1d03388b0d',
                        name='Ms. Jeannette Price',
                    ),
                    shared.TrackingCategoryRef(
                        id='fee74b6f-eb94-457c-beda-f39d16fbf76f',
                        name='Andrew Kerluke',
                    ),
                    shared.TrackingCategoryRef(
                        id='303e3023-b93e-4343-96cf-55b4313553cc',
                        name='Justin Schaefer II',
                    ),
                ],
                unit_amount=8084.57,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='labore',
        note='culpa',
        paid_on_date='illum',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='minus',
                    currency='sint',
                    currency_rate=5786.36,
                    total_amount=286.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4c5195b8-648c-4efa-b8f1-e2d3b901e095',
                        name='Beulah Pouros',
                    ),
                    currency='minus',
                    currency_rate=6917.42,
                    id='b19f713d-95a4-4169-8138-7271e18ea9e4',
                    note='veniam',
                    paid_on_date='illo',
                    reference='illo',
                    total_amount=5361.81,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='quisquam',
                    currency='fugit',
                    currency_rate=7587.36,
                    total_amount=7784.03,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='57fbd60b-1a78-4ed2-9a9d-4eea85658c2d',
                        name='Dixie Hackett',
                    ),
                    currency='quas',
                    currency_rate=6955.11,
                    id='e4f278fd-9667-4e46-851d-2ffaa58dcef2',
                    note='ratione',
                    paid_on_date='quaerat',
                    reference='minus',
                    total_amount=6170.85,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='nostrum',
                    currency='veniam',
                    currency_rate=7312.33,
                    total_amount=6180.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='bdf2190a-bd9b-4bcc-a725-ec2659ce0280',
                        name='Jesus Abernathy',
                    ),
                    currency='excepturi',
                    currency_rate=9071.7,
                    id='f68e45c8-addf-4ac7-9450-0430c6632b43',
                    note='provident',
                    paid_on_date='inventore',
                    reference='sapiente',
                    total_amount=8387.98,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='sapiente',
                    currency='ipsa',
                    currency_rate=1140.37,
                    total_amount=7509.59,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='3e91e8f7-bc69-4d46-8a77-eceb26d10f1e',
                        name='Alan Howell DDS',
                    ),
                    currency='nihil',
                    currency_rate=7867.65,
                    id='0f0f873f-9d5c-425f-93e0-b4a4a4253c30',
                    note='consequuntur',
                    paid_on_date='ullam',
                    reference='molestiae',
                    total_amount=1037.45,
                ),
            ),
        ],
        sales_order_refs=[
            'maiores',
        ],
        source_modified_date='labore',
        status=shared.InvoiceStatusEnum.UNKNOWN,
        sub_total=8074.3,
        supplemental_data=shared.SupplementalData(
            content={
                "recusandae": {
                    "pariatur": 'porro',
                    "enim": 'tempora',
                },
                "voluptatum": {
                    "itaque": 'sit',
                    "excepturi": 'recusandae',
                    "numquam": 'architecto',
                },
            },
        ),
        total_amount=6845.98,
        total_discount=4808.29,
        total_tax_amount=6330.56,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=816.73,
                name='Mr. Leticia Nitzsche',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=289108,
)

res = s.invoices.create(req)

if res.create_invoice_response is not None:
    # handle response
```

## delete

Deletes an invoice from the accounting package for a given company.

> **Supported Integrations**
> 
> This functionality is currently only supported for our QuickBooks Online integration. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.

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

Download invoice attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadInvoiceAttachmentRequest(
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

Get invoice as PDF

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

Get invoice

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

Get invoice attachment

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

Get create/update invoice model. Returns the expected data for the request payload.

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

Gets the latest invoices for a company, with pagination

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
    query='harum',
)

res = s.invoices.list(req)

if res.invoices is not None:
    # handle response
```

## list_attachments

List invoice attachments

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

Posts an updated invoice to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support updating invoices.

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
        additional_tax_amount=6791.83,
        additional_tax_percentage=5932.05,
        amount_due=8445.45,
        currency='ipsam',
        currency_rate=5928.98,
        customer_ref=shared.CustomerRef(
            company_name='omnis',
            id='88192cfd-0c77-4c53-a7e7-d4ee6e8b90ba',
        ),
        discount_percentage=7821.55,
        due_date='consectetur',
        id='84e23967-03fe-4c31-8508-24d189a36a6b',
        invoice_number='sunt',
        issue_date='facere',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='7eb707aa-60c8-4fe4-ae61-77db9db3b70f',
                    name='Jonathon Quigley',
                ),
                description='ducimus',
                discount_amount=451.76,
                discount_percentage=9196.52,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='e770e360-97ef-47c2-86e6-1b0d308714c2',
                    name='Genevieve Erdman',
                ),
                quantity=5444.06,
                sub_total=4105.74,
                tax_amount=1937.94,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4604.15,
                    id='ca85c3fe-6557-44db-af94-a7c98f13af28',
                    name='Pete Crona',
                ),
                total_amount=1646.09,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='f4f3ded3-56d7-4e14-b21c-d98196d55af6',
                            name='Hubert Casper',
                        ),
                        shared.TrackingCategoryRef(
                            id='b79ae336-81c2-43c3-9a7c-0e17cb12c5ba',
                            name='Steve Herzog',
                        ),
                        shared.TrackingCategoryRef(
                            id='22cd5cba-6fbf-4ec9-b2af-6813d65bfece',
                            name='Fred Shields',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='provident',
                        id='16f7fc7d-da70-4ec6-8e60-75894d61c14c',
                    ),
                    is_billed_to=shared.BilledToTypeEnum1.PROJECT,
                    is_rebilled_to=shared.BilledToTypeEnum1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='0227e37c-0d97-47f1-a549-1abe9751b106',
                        name='Clarence Dicki I',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='69815aae-99fc-4de9-a729-c9d4f2d8a446',
                        name='Mary Schamberger',
                    ),
                    shared.TrackingCategoryRef(
                        id='0db73a2f-93f4-467d-80d8-da56122026ab',
                        name='Emmett Davis',
                    ),
                    shared.TrackingCategoryRef(
                        id='485c1976-af98-40da-ba08-9fc44db27453',
                        name='Rochelle Hermiston',
                    ),
                    shared.TrackingCategoryRef(
                        id='7c6d0cbc-fdcd-4334-b6f6-23bcecab50ae',
                        name='Dr. Alvin Weber',
                    ),
                ],
                unit_amount=5565.17,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='cum',
        note='sint',
        paid_on_date='laborum',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='nisi',
                    currency='id',
                    currency_rate=8611.66,
                    total_amount=202.23,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5486e7b4-13cb-4e2d-976d-c1c43d40f61d',
                        name='Mrs. Melinda Borer',
                    ),
                    currency='cumque',
                    currency_rate=7322.16,
                    id='e5ee4f72-1184-4077-af32-e3b49dbe0f23',
                    note='harum',
                    paid_on_date='voluptate',
                    reference='distinctio',
                    total_amount=3820.07,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='fugiat',
                    currency='perspiciatis',
                    currency_rate=5855.5,
                    total_amount=2959.58,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='8d6eded4-7768-40fc-ba17-a82e5e82fd28',
                        name='Albert Auer MD',
                    ),
                    currency='iusto',
                    currency_rate=8934.34,
                    id='91392ab4-4cb1-4835-808f-461ce53e9144',
                    note='perspiciatis',
                    paid_on_date='rem',
                    reference='animi',
                    total_amount=6129.79,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='libero',
                    currency='deserunt',
                    currency_rate=2957.26,
                    total_amount=3918.99,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='0addfde4-10c3-47da-a918-2a49d9625d3c',
                        name='Toby Wisoky V',
                    ),
                    currency='blanditiis',
                    currency_rate=9171.68,
                    id='ea445279-2bcd-4440-aa98-becce0486de0',
                    note='repellendus',
                    paid_on_date='ipsam',
                    reference='aliquid',
                    total_amount=8330.92,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='nihil',
                    currency='non',
                    currency_rate=7171.48,
                    total_amount=121.81,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='05503e8d-c626-4ff7-bc65-675f5b70e3e4',
                        name='Darrin Sawayn',
                    ),
                    currency='dolorum',
                    currency_rate=5828.22,
                    id='1ec52624-d000-414e-b45c-ea11ac53ebb6',
                    note='nostrum',
                    paid_on_date='corrupti',
                    reference='odio',
                    total_amount=9462.07,
                ),
            ),
        ],
        sales_order_refs=[
            'eius',
        ],
        source_modified_date='voluptatem',
        status=shared.InvoiceStatusEnum.DRAFT,
        sub_total=647.33,
        supplemental_data=shared.SupplementalData(
            content={
                "placeat": {
                    "cum": 'sint',
                    "est": 'quod',
                },
                "voluptates": {
                    "non": 'quae',
                    "perferendis": 'mollitia',
                    "voluptates": 'provident',
                    "doloribus": 'unde',
                },
            },
        ),
        total_amount=1671.44,
        total_discount=7933.34,
        total_tax_amount=6618.61,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=1012.53,
                name='Jose D'Amore',
            ),
            shared.WithholdingTaxitems(
                amount=1005.96,
                name='Justin Gusikowski IV',
            ),
            shared.WithholdingTaxitems(
                amount=8059.91,
                name='Dr. Tami O'Reilly',
            ),
            shared.WithholdingTaxitems(
                amount=8418.47,
                name='Erma Barton',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    timeout_in_minutes=329849,
)

res = s.invoices.update(req)

if res.update_invoice_response is not None:
    # handle response
```

## upload_attachment

Push invoice attachment

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
        content='facere'.encode(),
        request_body='excepturi',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```
