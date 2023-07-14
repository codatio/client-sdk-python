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

The *Create invoice* endpoint creates a new [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) for a given company's connection.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating an account.


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
        additional_tax_amount=6499.01,
        additional_tax_percentage=3702.19,
        amount_due=4227.22,
        currency='GBP',
        currency_rate=427.39,
        customer_ref=shared.CustomerRef(
            company_name='atque',
            id='91500970-19a4-48f8-8ece-7bf904e01105',
        ),
        discount_percentage=8370.8,
        due_date='2022-10-23T00:00:00.000Z',
        id='8908162c-6beb-468a-8f65-7b7d03a1480f',
        invoice_number='blanditiis',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='30f069d8-1061-48d9-be15-2297510da803',
                    name='Janice Cronin',
                ),
                description='nobis',
                discount_amount=7615.63,
                discount_percentage=3870.67,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='1c2a702b-b97e-4e10-ada2-de35f8e01bf3',
                    name='Silvia Murazik',
                ),
                quantity=2836.19,
                sub_total=3304.68,
                tax_amount=2609.08,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=619.54,
                    id='2ac1704b-f1cc-49fc-a1aa-e5eb5f0c492b',
                    name='Jackie Graham',
                ),
                total_amount=406.34,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='a2267aae-e79e-43c7-9ad3-1becb83d2378',
                            name='Rogelio Doyle',
                        ),
                        shared.TrackingCategoryRef(
                            id='c23d9450-a986-4a49-9bac-707f06b28ecc',
                            name='Raul Gerlach I',
                        ),
                        shared.TrackingCategoryRef(
                            id='86f62c96-9c4c-4c6b-b889-0a3fd3c81da1',
                            name='Tabitha Lesch',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='non',
                        id='df931da3-edb5-41fa-994a-cc9435137726',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='5321b832-a56d-4691-80ff-60eb9a6658e6',
                        name='Grant Fritsch',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='3d382dbe-c75c-468c-a065-9468ce304d88',
                        name='Shelly Quitzon',
                    ),
                    shared.TrackingCategoryRef(
                        id='214c337f-96bb-40c6-9e37-2db1344ba9f7',
                        name='Ernesto Heaney PhD',
                    ),
                ],
                unit_amount=8162.72,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='7aab62e9-7261-4fb0-858d-27b51996b5b4',
                    name='Jon Bashirian',
                ),
                description='sapiente',
                discount_amount=4822.43,
                discount_percentage=988.3,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='2b7a7ab0-344b-4171-8688-deebef897f3d',
                    name='Mark Schmidt',
                ),
                quantity=2232.35,
                sub_total=2259.45,
                tax_amount=9483.01,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=979.03,
                    id='1b3e4e08-0aa1-4041-86ec-759e02f3702c',
                    name='Blanca Langworth',
                ),
                total_amount=8570.75,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='0ead3104-fa44-4707-bf37-5b44282821fd',
                            name='Aaron Weimann',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eveniet',
                        id='59267c71-cc8d-43cd-8258-d0358a82c808',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='2751a204-7c04-449e-943f-9619bb7d40d5',
                        name='Eric Bergnaum',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='36e62592-33f9-45c9-9237-397c785b5db4',
                        name='Mr. Wesley Ankunding',
                    ),
                    shared.TrackingCategoryRef(
                        id='3febdf67-6b72-406d-ab75-0052a5647edc',
                        name='Annie Morissette',
                    ),
                ],
                unit_amount=5481.43,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='c4320f41-240d-4448-bac6-93b94c3b9d24',
                    name='Guy Spinka',
                ),
                description='ad',
                discount_amount=6383.23,
                discount_percentage=6864.21,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='42fc4056-69f6-49a0-86d2-1249450819d7',
                    name='Miss Nathan Ritchie',
                ),
                quantity=745.3,
                sub_total=5385.16,
                tax_amount=2986.57,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2793.53,
                    id='060e0031-0d02-43dc-901f-5afd2a6c4484',
                    name='Genevieve Waters',
                ),
                total_amount=5056.63,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='253c8962-f489-46bf-91e4-652d3c343d61',
                            name='Stella Littel',
                        ),
                        shared.TrackingCategoryRef(
                            id='49124772-5e62-4190-9e91-044a5de59ac7',
                            name='Jessica Hyatt',
                        ),
                        shared.TrackingCategoryRef(
                            id='0cf1cf59-3260-4525-9e66-bb426897d99a',
                            name='Christie Frami',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='suscipit',
                        id='70e93ee6-cf59-4f35-8aae-acae323a31bf',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='a1cc9771-6c80-42cc-9e0c-7d9d323f1aa6',
                        name='Cecelia Stoltenberg',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='1c856bcb-a51e-4f24-94a4-7facf116cdd5',
                        name='Jamie Funk',
                    ),
                    shared.TrackingCategoryRef(
                        id='562873c7-dd9e-4faf-83dc-623620f3138f',
                        name='Michelle Stroman',
                    ),
                    shared.TrackingCategoryRef(
                        id='db022faa-565f-4b8f-a52e-bb9d38383879',
                        name='Beverly Green',
                    ),
                    shared.TrackingCategoryRef(
                        id='293dab30-e917-4f50-bda0-4c8b1bb55a29',
                        name='Karla Armstrong',
                    ),
                ],
                unit_amount=2482.32,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='bb744664-eb1d-4033-88b0-d1bb17afee74',
                    name='Hector Willms',
                ),
                description='occaecati',
                discount_amount=2897.27,
                discount_percentage=3697.22,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='7c7edaf3-9d16-4fbf-b6fd-162b303e3023',
                    name='Andy Erdman',
                ),
                quantity=2724.93,
                sub_total=1973.88,
                tax_amount=893.2,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3986.87,
                    id='cf55b431-3553-4ccf-9c20-4c4adcc9904c',
                    name='Debra Medhurst',
                ),
                total_amount=5405.93,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='48cefa78-f1e2-4d3b-901e-0952bbb4cbb1',
                            name='Mrs. Courtney Kuhic',
                        ),
                        shared.TrackingCategoryRef(
                            id='95a4169c-1387-4271-a18e-a9e45118c2cc',
                            name='Dora White',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='aliquid',
                        id='0b1a78ed-29a9-4d4e-aa85-658c2d4f4c88',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='4f278fd9-667e-446c-91d2-ffaa58dcef23',
                        name='Alexandra Morissette',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='9bdf2190-abd9-4bbc-8272-5ec2659ce028',
                        name='Miss Priscilla Gerhold',
                    ),
                    shared.TrackingCategoryRef(
                        id='9ef68e45-c8ad-4dfa-8754-500430c6632b',
                        name='Dr. Carmen McKenzie',
                    ),
                    shared.TrackingCategoryRef(
                        id='f01c3e91-e8f7-4bc6-9d46-0a77eceb26d1',
                        name='Lorene Bosco',
                    ),
                ],
                unit_amount=1818.77,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='neque',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=461.37,
                    total_amount=9654.91,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='0f873f9d-5c25-4fd3-a0b4-a4a4253c3025',
                        name='Julie Bergstrom',
                    ),
                    currency='GBP',
                    currency_rate=8074.3,
                    id='7e7dc548-be09-4e41-a7a2-15ca12a4ba9d',
                    note='ipsam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='omnis',
                    total_amount=5229.85,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=5952.02,
                    total_amount=1465.4,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='cfd0c77c-53e7-4e7d-8ee6-e8b90bac384e',
                        name='Cindy Marquardt',
                    ),
                    currency='GBP',
                    currency_rate=1935.64,
                    id='fec31c50-824d-4189-a36a-6b2d27eb707a',
                    note='est',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='aut',
                    total_amount=8090.72,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=8853.36,
                    total_amount=2924.31,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='6e6177db-9db3-4b70-bfbb-6970ee770e36',
                        name='Violet Kshlerin',
                    ),
                    currency='USD',
                    currency_rate=8024.72,
                    id='206e61b0-d308-4714-820a-3d98637ca85c',
                    note='adipisci',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='repudiandae',
                    total_amount=4193.51,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=4780.21,
                    total_amount=2820.79,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='dbaf94a7-c98f-413a-b28d-b2cf2bf4f3de',
                        name='Vincent Hansen',
                    ),
                    currency='USD',
                    currency_rate=8883.28,
                    id='14b21cd9-8196-4d55-af69-a1c4b79ae336',
                    note='praesentium',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='eligendi',
                    total_amount=1805.44,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='eligendi',
                id='39a7c0e1-7cb1-42c5-ba82-5fe22cd5cba6',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.PAID,
        sub_total=9961.28,
        supplemental_data=shared.SupplementalData(
            content={
                "quisquam": {
                    "amet": 'consequuntur',
                    "fuga": 'a',
                    "aliquid": 'voluptatum',
                },
                "sunt": {
                    "illum": 'ea',
                },
                "veniam": {
                    "delectus": 'earum',
                    "placeat": 'saepe',
                    "quod": 'odit',
                },
                "assumenda": {
                    "ea": 'provident',
                    "inventore": 'ea',
                    "repellat": 'quam',
                    "delectus": 'minus',
                },
            },
        ),
        total_amount=4677.01,
        total_discount=8447.75,
        total_tax_amount=8284.89,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=4773.62,
                name='Kate Schowalter PhD',
            ),
            shared.WithholdingTaxitems(
                amount=3877.68,
                name='Melinda Heaney',
            ),
            shared.WithholdingTaxitems(
                amount=2559.53,
                name='Milton Bogisich I',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=787873,
)

res = s.invoices.create(req)

if res.create_invoice_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateInvoiceRequest](../../models/operations/createinvoicerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.CreateInvoiceResponse](../../models/operations/createinvoiceresponse.md)**


## delete

﻿The *Delete invoice* endpoint allows you to delete a specified invoice from an accounting platform.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

### Process
1. Pass the `{invoiceId}` to the *Delete invoice* endpoint and store the `pushOperationKey` returned.
2. Check the status of the delete operation by checking the status of push operation either via
    1. [Push operation webhook](https://docs.codat.io/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
    2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

   A `Success` status indicates that the invoice object was deleted from the accounting platform.
3. (Optional) Check that the invoice was deleted from the accounting platform.

### Effect on related objects

Be aware that deleting an invoice from an accounting platform might cause related objects to be modified. For example, if you delete a paid invoice from QuickBooks Online, the invoice is deleted but the payment against that invoice is not. The payment is converted to a payment on account.

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
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='facere',
)

res = s.invoices.delete(req)

if res.push_operation_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteInvoiceRequest](../../models/operations/deleteinvoicerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.DeleteInvoiceResponse](../../models/operations/deleteinvoiceresponse.md)**


## download_attachment

The *Download invoice attachment* endpoint downloads a specific attachment for a given `invoiceId` and `attachmentId`.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support downloading an invoice attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadInvoiceAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='excepturi',
)

res = s.invoices.download_attachment(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DownloadInvoiceAttachmentRequest](../../models/operations/downloadinvoiceattachmentrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.DownloadInvoiceAttachmentResponse](../../models/operations/downloadinvoiceattachmentresponse.md)**


## download_pdf

﻿Download invoice as a pdf.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadInvoicePdfRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='aut',
)

res = s.invoices.download_pdf(req)

if res.data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DownloadInvoicePdfRequest](../../models/operations/downloadinvoicepdfrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.DownloadInvoicePdfResponse](../../models/operations/downloadinvoicepdfresponse.md)**


## get

The *Get invoice* endpoint returns a single invoice for a given invoiceId.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support getting a specific invoice.

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

req = operations.GetInvoiceRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    invoice_id='aspernatur',
)

res = s.invoices.get(req)

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetInvoiceRequest](../../models/operations/getinvoicerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetInvoiceResponse](../../models/operations/getinvoiceresponse.md)**


## get_attachment

The *Get invoice attachment* endpoint returns a specific attachment for a given `invoiceId` and `attachmentId`.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support getting an invoice attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetInvoiceAttachmentRequest(
    attachment_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='odit',
)

res = s.invoices.get_attachment(req)

if res.attachment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetInvoiceAttachmentRequest](../../models/operations/getinvoiceattachmentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetInvoiceAttachmentResponse](../../models/operations/getinvoiceattachmentresponse.md)**


## get_create_update_model

The *Get create/update invoice model* endpoint returns the expected data for the request payload when creating and updating an [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) for a given company and integration.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

**Integration-specific behaviour**

See the *response examples* for integration-specific indicative models.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating and updating an invoice.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

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

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetCreateUpdateInvoicesModelRequest](../../models/operations/getcreateupdateinvoicesmodelrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.GetCreateUpdateInvoicesModelResponse](../../models/operations/getcreateupdateinvoicesmodelresponse.md)**


## list

The *List invoices* endpoint returns a list of [invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) for a given company's connection.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

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

req = operations.ListInvoicesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='molestiae',
)

res = s.invoices.list(req)

if res.invoices is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListInvoicesRequest](../../models/operations/listinvoicesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.ListInvoicesResponse](../../models/operations/listinvoicesresponse.md)**


## list_attachments

The *List invoice attachments* endpoint returns a list of attachments available to download for given `invoiceId`.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support listing invoice attachments.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListInvoiceAttachmentsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='recusandae',
)

res = s.invoices.list_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListInvoiceAttachmentsRequest](../../models/operations/listinvoiceattachmentsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.ListInvoiceAttachmentsResponse](../../models/operations/listinvoiceattachmentsresponse.md)**


## update

The *Update invoice* endpoint updates an existing [invoice](https://docs.codat.io/accounting-api#/schemas/Invoice) for a given company's connection.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

**Integration-specific behaviour**

Required data may vary by integration. To see what data to post, first call [Get create/update invoice model](https://docs.codat.io/accounting-api#/operations/get-create-update-invoices-model).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support creating an account.


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
        additional_tax_amount=2046.33,
        additional_tax_percentage=4704,
        amount_due=7513.92,
        currency='GBP',
        currency_rate=8156.07,
        customer_ref=shared.CustomerRef(
            company_name='iste',
            id='77f1a549-1abe-4975-9b10-6d23e03e6981',
        ),
        discount_percentage=3304.02,
        due_date='2022-10-23T00:00:00.000Z',
        id='ae99fcde-9e72-49c9-94f2-d8a44640ca60',
        invoice_number='illum',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='3a2f93f4-67dc-40d8-9a56-122026ab8f27',
                    name='Eleanor Lang',
                ),
                description='et',
                discount_amount=5825.69,
                discount_percentage=4501.13,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='6af980da-7a08-49fc-84db-274530e5cc7c',
                    name='Doreen Ankunding',
                ),
                quantity=7667.05,
                sub_total=9649.39,
                tax_amount=8335.9,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7785.2,
                    id='d334b6f6-23bc-4eca-b50a-ee5e0da8b9af',
                    name='Mrs. Alberta Stoltenberg',
                ),
                total_amount=5382.58,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e7b413cb-e2d1-476d-81c4-3d40f61d1711',
                            name='Joy Runolfsdottir',
                        ),
                        shared.TrackingCategoryRef(
                            id='5ee4f721-1840-4772-b32e-3b49dbe0f23b',
                            name='Lola Homenick',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='cupiditate',
                        id='48d6eded-4776-480f-87a1-7a82e5e82fd2',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='1040a7e9-1392-4ab4-8cb1-835008f461ce',
                        name='Robin Treutel I',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='98a9ba46-0add-4fde-810c-37daa9182a49',
                        name='Sergio Jacobi',
                    ),
                    shared.TrackingCategoryRef(
                        id='d3caffc1-98ee-4a44-9279-2bcd440ea98b',
                        name='Guadalupe Sawayn II',
                    ),
                ],
                unit_amount=5297.99,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='6de0d56d-73b0-4055-83e8-dc626ff77c65',
                    name='Courtney Hamill',
                ),
                description='harum',
                discount_amount=4443.84,
                discount_percentage=256.53,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='e3e4cfcc-6a91-4ec5-a624-d00014ef45ce',
                    name='Samuel Bruen',
                ),
                quantity=3285.77,
                sub_total=2073.91,
                tax_amount=8924.85,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=6954.27,
                    id='b6587f34-0414-4c5b-9ace-e400ae9f92ca',
                    name='Mr. Joe Rogahn',
                ),
                total_amount=9546.52,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d14718c6-fa2f-4ad0-806c-5d95472cdd14',
                            name='Sherman Gerlach',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='in',
                        id='0bca88fa-70c4-4335-9c3d-d1eb8f7f75f4',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='3f1c0a58-6c3a-4e7d-bb67-feef5e142d95',
                        name='Ralph Stracke',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='eff7c4b1-56e9-4278-a75e-ea7681746806',
                        name='Mandy Kutch',
                    ),
                    shared.TrackingCategoryRef(
                        id='b7956c0b-0fa0-4bb2-8a40-e7c4ae640642',
                        name='Janice Jones',
                    ),
                    shared.TrackingCategoryRef(
                        id='b01a07c0-8fd3-4921-8257-930d6f093a3e',
                        name='Lorenzo Gutmann',
                    ),
                    shared.TrackingCategoryRef(
                        id='366dfa10-11a0-491b-bec8-b53862de1a9d',
                        name='Alicia Ziemann',
                    ),
                ],
                unit_amount=1519.16,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='ipsam',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=593.03,
                    total_amount=2423.78,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='03dfc338-397f-4ffa-ad1d-32090fc157ac',
                        name='Ms. Aubrey Thiel',
                    ),
                    currency='GBP',
                    currency_rate=7529.61,
                    id='e9be41c8-69dd-47d9-b19d-07b200a58ffd',
                    note='consequuntur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='suscipit',
                    total_amount=4825.35,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='delectus',
                id='8fd882a8-e60b-4e62-8cd9-c5afdd04c375',
            ),
            shared.SalesOrderRef(
                data_type='aspernatur',
                id='512beae1-d87e-4cc5-bdce-a8e7a8831166',
            ),
            shared.SalesOrderRef(
                data_type='ratione',
                id='cda6d77c-1d86-4066-a37d-4227866db8a7',
            ),
            shared.SalesOrderRef(
                data_type='labore',
                id='9e398451-1cc7-45e4-b0c0-04b5bb758cc9',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=3765.76,
        supplemental_data=shared.SupplementalData(
            content={
                "delectus": {
                    "consequatur": 'suscipit',
                },
            },
        ),
        total_amount=5771.02,
        total_discount=4067.2,
        total_tax_amount=5272.66,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=9529.5,
                name='Owen Boyer IV',
            ),
            shared.WithholdingTaxitems(
                amount=2334.63,
                name='Dwight Fritsch',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='saepe',
    timeout_in_minutes=139567,
)

res = s.invoices.update(req)

if res.update_invoice_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateInvoiceRequest](../../models/operations/updateinvoicerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.UpdateInvoiceResponse](../../models/operations/updateinvoiceresponse.md)**


## upload_attachment

The *Upload invoice attachment* endpoint uploads an attachment and assigns it against a specific `invoiceId`.

[Invoices](https://docs.codat.io/accounting-api#/schemas/Invoice) are itemized records of goods sold or services provided to a customer.

**Integration-specific behaviour**

For more details on supported file types by integration see [Attachments](https://docs.codat.io/accounting-api#/schemas/Attachment).

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=invoices) for integrations that support uploading an invoice attachment.


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UploadInvoiceAttachmentRequest(
    request_body=operations.UploadInvoiceAttachmentRequestBody(
        content='modi'.encode(),
        request_body='tenetur',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='explicabo',
)

res = s.invoices.upload_attachment(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UploadInvoiceAttachmentRequest](../../models/operations/uploadinvoiceattachmentrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.UploadInvoiceAttachmentResponse](../../models/operations/uploadinvoiceattachmentresponse.md)**

