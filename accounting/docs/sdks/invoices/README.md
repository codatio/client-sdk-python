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
        additional_tax_amount=4067.2,
        additional_tax_percentage=5272.66,
        amount_due=3638.91,
        currency='EUR',
        currency_rate=8024.04,
        customer_ref=shared.CustomerRef(
            company_name='possimus',
            id='1a173d84-bbe2-44f2-9834-afb0735cb628',
        ),
        discount_percentage=3619.78,
        due_date='2022-10-23T00:00:00.000Z',
        id='4a29aaa1-e169-4156-b7d2-ee209505bf03',
        invoice_number='laborum',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='e94480ca-37fb-4107-8903-2ac333172e2d',
                    name='Christian McLaughlin',
                ),
                description='in',
                discount_amount=2572.19,
                discount_percentage=7144.42,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='a7e88ddb-36fd-41cc-8341-c86573474f0a',
                    name='Eva Becker',
                ),
                quantity=2791.66,
                sub_total=6432.64,
                tax_amount=7196.52,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3005.14,
                    id='41c3a09e-7639-495d-808b-be794455ebc5',
                    name='Miss Elizabeth Ortiz',
                ),
                total_amount=1838.89,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='b59c8366-fdcc-4135-982c-1b855e889d9e',
                            name='Evan Feest',
                        ),
                        shared.TrackingCategoryRef(
                            id='9000a13a-d812-4420-8efd-23411898e738',
                            name='Lindsay Upton',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eveniet',
                        id='8baebabb-7945-436e-9035-1bb97631720b',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='a5a5365a-79f1-4527-9f01-c0d361fed8dc',
                        name='Silvia Wilkinson',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='53e9089e-871f-4db4-9697-bdd9c985e437',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='4a5d72d9-edd7-485b-a5e7-afe55297ba62',
                        name='Ralph Zulauf',
                    ),
                ],
                unit_amount=9076.5,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='laborum',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=2629.36,
                    total_amount=6602.4,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='68cc80d3-0ff7-4216-8d0a-91fe9d96553b',
                        name='Mr. Andy Tromp V',
                    ),
                    currency='EUR',
                    currency_rate=4285.11,
                    id='692de7b3-5622-401a-aaab-4ae7b1a5b908',
                    note='placeat',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='repudiandae',
                    total_amount=2357.58,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='aliquam',
                id='91aa35d4-a839-4f03-bab7-7b918f031398',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=223.74,
        supplemental_data=shared.SupplementalData(
            content={
                "officiis": {
                    "voluptates": 'consectetur',
                },
                "occaecati": {
                    "quam": 'saepe',
                    "odit": 'consectetur',
                    "itaque": 'impedit',
                    "quidem": 'voluptatem',
                },
            },
        ),
        total_amount=3782.32,
        total_discount=447.24,
        total_tax_amount=2556.89,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=3748.97,
                name='Kate Cummerata',
            ),
            shared.WithholdingTaxitems(
                amount=2248.7,
                name='Milton Satterfield',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=443801,
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
    invoice_id='vero',
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
    invoice_id='unde',
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
    invoice_id='quibusdam',
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
    invoice_id='debitis',
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
    invoice_id='rem',
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
    query='earum',
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
    invoice_id='molestiae',
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
        additional_tax_amount=9404.86,
        additional_tax_percentage=584.62,
        amount_due=55.44,
        currency='GBP',
        currency_rate=8563.28,
        customer_ref=shared.CustomerRef(
            company_name='veritatis',
            id='986aa99d-3a1d-4323-a9e4-5837e8f2ad6b',
        ),
        discount_percentage=6883.86,
        due_date='2022-10-23T00:00:00.000Z',
        id='0e255fdc-480d-46e3-b086-75cbf186856a',
        invoice_number='ducimus',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='2cdf9d0f-c282-4c66-aaf3-c3f5589bea5d',
                    name='Kristin Gislason',
                ),
                description='beatae',
                discount_amount=8996.64,
                discount_percentage=1872.03,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='ca84822e-513f-46d9-92ad-37c3099077c1',
                    name='Olivia Howe',
                ),
                quantity=6145.4,
                sub_total=1523.59,
                tax_amount=834.37,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=4147.2,
                    id='3e67d488-6054-43c0-a304-9c3cf6c0276e',
                    name='Miss Pam Deckow',
                ),
                total_amount=8413.79,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='0d2743fd-6c2a-410e-ac29-78ec256a5b09',
                            name='Anne Kessler',
                        ),
                        shared.TrackingCategoryRef(
                            id='c47996c9-77bb-4c57-b389-28a8600c58d6',
                            name='Mable Jaskolski',
                        ),
                        shared.TrackingCategoryRef(
                            id='4aa56846-4579-4cfc-ac0e-503f56831f1d',
                            name='Percy Strosin',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='nobis',
                        id='28e8afab-c986-4e24-9e43-b2342417d13e',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='62aa9ae4-ae8a-4b4a-9c49-2c5e8ba5d4aa',
                        name='Ms. Harriet Hartmann',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='380c29aa-8dd7-41bd-9aa3-0b7b91449ae6',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c088d418-bb71-4804-b423-d543935f377a',
                        name='Glen Russel',
                    ),
                    shared.TrackingCategoryRef(
                        id='7e93b6a3-c523-4105-a7c3-4cab0ecb812a',
                        name='Gertrude Brekke',
                    ),
                    shared.TrackingCategoryRef(
                        id='944a8e90-8507-45bc-a538-253343fb0a4e',
                        name='Stacey Watsica',
                    ),
                ],
                unit_amount=4685.4,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='578d171e-2941-4818-bc67-9b6b2f25359b',
                    name='Clyde Harber Jr.',
                ),
                description='ad',
                discount_amount=6943.34,
                discount_percentage=3983.03,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='2c8b83a3-8a8a-488c-9442-00c2caeb1ae1',
                    name='Edmund Zieme',
                ),
                quantity=2400.8,
                sub_total=2626.38,
                tax_amount=5865.8,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=2645.59,
                    id='6bba7a05-a8b4-4a9e-85b3-688cca363272',
                    name='Willie Bailey',
                ),
                total_amount=4250.9,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='e97e0541-0334-47d7-8ff2-491145fab9e5',
                            name='Cameron Gorczany',
                        ),
                        shared.TrackingCategoryRef(
                            id='336664ea-a6bf-42ff-94e8-c1b352acceda',
                            name='Kim Hammes',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='reprehenderit',
                        id='814eca01-6bc4-41ea-9342-d4104a25ef71',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='57a11d61-4a43-4176-92ea-48673d522b82',
                        name='Mrs. Donnie Mueller III',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='0f024c79-b4cc-464c-ab3a-32c488ade62f',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='aa558a65-e208-4301-aca3-4bb87d4f6212',
                        name='Ms. Kristi Jast',
                    ),
                    shared.TrackingCategoryRef(
                        id='16062945-14c3-4db9-8a9f-38bd2be87870',
                        name='Valerie Morissette',
                    ),
                ],
                unit_amount=2924.87,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='9aa8465a-3283-4279-b719-d1cea673d86e',
                    name='Yvette Donnelly',
                ),
                description='aliquam',
                discount_amount=5934.74,
                discount_percentage=6612.87,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='3135778c-e54c-4acb-8e3e-a975045bacf6',
                    name='Mrs. Juana Cremin V',
                ),
                quantity=4160.84,
                sub_total=6644.99,
                tax_amount=7240.48,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=3608.15,
                    id='e3a02261-4315-4d15-a829-9e61afc7186f',
                    name='Todd Abernathy',
                ),
                total_amount=6830.6,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='3df40ca0-d765-47c1-a41b-bf055271b251',
                            name='Nadine Shanahan III',
                        ),
                        shared.TrackingCategoryRef(
                            id='dd1b2827-2bc9-4c32-a169-7b1880fcbb2b',
                            name='Mrs. Luis Schneider',
                        ),
                    ],
                    customer_ref=shared.CustomerRef(
                        company_name='eum',
                        id='70bd1784-8316-453e-ab3b-6e241c310998',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='63c66dcb-b7df-46cb-89c8-b408e0713774',
                        name='Elias Friesen',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='transfer',
                        id='101d9780-a10c-447b-9504-0d6c8b2a5f00',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='207e4048-f900-409e-9290-278eb4ae9d64',
                        name='Vera Bernier',
                    ),
                ],
                unit_amount=1232.86,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='quae',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=6979.73,
                    total_amount=1793.89,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='c09b9247-71f5-4669-a5b7-ec7626649d84',
                        name='Randolph Medhurst',
                    ),
                    currency='EUR',
                    currency_rate=9525.87,
                    id='d2276e0b-88fb-487d-afa5-b6e8dbf812f8',
                    note='nesciunt',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='inventore',
                    total_amount=7530.97,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='autem',
                id='a9ffc561-929c-4ca9-960a-1395918da1d4',
            ),
            shared.SalesOrderRef(
                data_type='atque',
                id='e78e3cf8-e114-43da-9308-b27a08af2218',
            ),
            shared.SalesOrderRef(
                data_type='eius',
                id='439b3de8-756c-4cce-870c-d2147b6e6152',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.VOID,
        sub_total=556.06,
        supplemental_data=shared.SupplementalData(
            content={
                "quibusdam": {
                    "vero": 'voluptatum',
                },
            },
        ),
        total_amount=7572.73,
        total_discount=2244.11,
        total_tax_amount=6354.79,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=7069.06,
                name='Cameron Herman',
            ),
            shared.WithholdingTaxitems(
                amount=5656.18,
                name='Lynn Streich',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='provident',
    timeout_in_minutes=437586,
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
        content='incidunt'.encode(),
        request_body='repellat',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='similique',
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

