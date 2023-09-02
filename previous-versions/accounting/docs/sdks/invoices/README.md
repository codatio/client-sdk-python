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
        additional_tax_amount=3808.53,
        additional_tax_percentage=3421.29,
        amount_due=5447.6,
        currency='USD',
        currency_rate=9462.07,
        customer_ref=shared.AccountingCustomerRef(
            company_name='consectetur',
            id='40414c5b-9ace-4e40-8ae9-f92caf1b025f',
        ),
        discount_percentage=1005.96,
        due_date='2022-10-23T00:00:00.000Z',
        id='14718c6f-a2fa-4d0c-86c5-d95472cdd14f',
        invoice_number='porro',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='b70bca88-fa70-4c43-b51c-3dd1eb8f7f75',
                    name='Miguel Weissnat',
                ),
                description='doloribus',
                discount_amount=949.91,
                discount_percentage=7688.46,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='0a586c3a-e7d7-4b67-beef-5e142d95b1db',
                    name='Guadalupe Weber',
                ),
                quantity=4809.57,
                sub_total=7789.75,
                tax_amount=2510.22,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7332.11,
                    id='156e9278-275e-4ea7-a817-468063f799b7',
                    name='Corey Jakubowski MD',
                ),
                total_amount=309.86,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='a0bb20a4-0e7c-44ae-a406-4272657b01a0',
                            name='Rachael Armstrong',
                        ),
                        shared.TrackingCategoryRef(
                            id='d3921c25-7930-4d6f-893a-3efa46d366df',
                            name='Mr. Walter Adams',
                        ),
                        shared.TrackingCategoryRef(
                            id='091b3ec8-b538-462d-a1a9-d14fe72e521f',
                            name='Mrs. Jeffrey Flatley',
                        ),
                        shared.TrackingCategoryRef(
                            id='fc338397-fffa-46d1-9320-90fc157ac9fe',
                            name='Miss Bobbie Jakubowski',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='perspiciatis',
                        id='be41c869-dd7d-4971-9d07-b200a58ffd29',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='df8fd882-a8e6-40be-a20c-d9c5afdd04c3',
                        name='Stacy Collins Sr.',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='accountTransaction',
                        id='eae1d87e-cc5f-4dce-a8e7-a88311662cda',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='d77c1d86-0662-437d-8227-866db8a749e3',
                        name='Everett Gottlieb Sr.',
                    ),
                    shared.TrackingCategoryRef(
                        id='cc75e4f0-c004-4b5b-b758-cc94562f0069',
                        name='Gwendolyn Hickle',
                    ),
                ],
                unit_amount=8194.9,
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='est',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=5137.33,
                    total_amount=2526.91,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='bbe24f29-834a-4fb0-b35c-b6285d4a29aa',
                        name='Mrs. Eric Toy',
                    ),
                    currency='GBP',
                    currency_rate=3678.44,
                    id='6f7d2ee2-0950-45bf-83a9-3e94480ca37f',
                    note='nam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ipsa',
                    total_amount=4957.89,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=542.66,
                    total_amount=1965.04,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='2ac33317-2e2d-4d79-ac74-ba7e88ddb36f',
                        name='Dennis Romaguera',
                    ),
                    currency='GBP',
                    currency_rate=2904.79,
                    id='1c865734-74f0-4a74-8fb4-ab441c3a09e7',
                    note='commodi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='perspiciatis',
                    total_amount=6094.27,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='vero',
                id='808bbe79-4455-4ebc-950a-1c426b59c836',
            ),
            shared.SalesOrderRef(
                data_type='ea',
                id='fdcc1355-82c1-4b85-9e88-9d9ef932e900',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.PARTIALLY_PAID,
        sub_total=1087.68,
        supplemental_data=shared.SupplementalData(
            content={
                "deserunt": {
                    "voluptatum": 'veritatis',
                    "consequuntur": 'dolore',
                    "fugit": 'alias',
                    "voluptatum": 'voluptates',
                },
            },
        ),
        total_amount=9590.06,
        total_discount=8707.38,
        total_tax_amount=1827.3,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=2591.29,
                name='Katherine Lesch',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=926770,
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
    invoice_id='quam',
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
    invoice_id='adipisci',
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
    invoice_id='praesentium',
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
    invoice_id='nihil',
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
    invoice_id='unde',
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
    query='eveniet',
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
    invoice_id='tenetur',
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
        additional_tax_amount=7082.83,
        additional_tax_percentage=9086.43,
        amount_due=5282.87,
        currency='EUR',
        currency_rate=6393.07,
        customer_ref=shared.AccountingCustomerRef(
            company_name='saepe',
            id='babb7945-36e9-4035-9bb9-7631720b77a5',
        ),
        discount_percentage=6489.97,
        due_date='2022-10-23T00:00:00.000Z',
        id='365a79f1-5271-4f01-80d3-61fed8dc5eff',
        invoice_number='nobis',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='3e9089e8-71fd-4b4d-a97b-dd9c985e4373',
                    name='Sandy Hayes',
                ),
                description='odit',
                discount_amount=8435.01,
                discount_percentage=5849.49,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='edd785be-5e7a-4fe5-9297-ba6281f44e3a',
                    name='Carmen Feil',
                ),
                quantity=6602.4,
                sub_total=4293.32,
                tax_amount=5230.55,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=7569.98,
                    id='c80d30ff-7216-44d0-a91f-e9d96553b89e',
                    name='Elizabeth Batz',
                ),
                total_amount=4285.11,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='92de7b35-6220-41a6-aab4-ae7b1a5b908d',
                            name='Mrs. Silvia Feil',
                        ),
                        shared.TrackingCategoryRef(
                            id='1aa35d4a-839f-403b-ab77-b918f0313984',
                            name='Nancy Kihn DVM',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='consectetur',
                        id='9c7e23ec-b060-4465-ae23-a3d6c657e9de',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.PROJECT,
                    project_ref=shared.ProjectRef(
                        id='7f002d19-86aa-499d-ba1d-32329e45837e',
                        name='Dominick Denesik',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='bb10e255-fdc4-480d-ae33-08675cbf1868',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='6a7e82cd-f9d0-4fc2-82c6-66af3c3f5589',
                        name='Sheldon Orn',
                    ),
                    shared.TrackingCategoryRef(
                        id='264e41e2-ca84-4822-a513-f6d9d2ad37c3',
                        name='Ms. Sabrina McCullough',
                    ),
                ],
                unit_amount=7504.07,
            ),
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='10b68792-163e-467d-8886-0543c0a3049c',
                    name='Traci Wolf',
                ),
                description='sit',
                discount_amount=1279.08,
                discount_percentage=4711.41,
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='6e7b21ba-d90d-4274-bfd6-c2a10e6c2978',
                    name='Salvatore Daugherty',
                ),
                quantity=6398.55,
                sub_total=3317.24,
                tax_amount=7368.46,
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=307.87,
                    id='9227fcc4-7996-4c97-bbbc-57f38928a860',
                    name='Roxanne Hammes',
                ),
                total_amount=4306.51,
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='d63e4aa5-6846-4457-9cfc-6c0e503f5683',
                            name='Johanna Bosco',
                        ),
                        shared.TrackingCategoryRef(
                            id='ed87b28e-8afa-4bc9-86e2-41e43b234241',
                            name='Angel Brown',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='nesciunt',
                        id='f62aa9ae-4ae8-4ab4-a9c4-92c5e8ba5d4a',
                    ),
                    is_billed_to=shared.BilledToType1.NOT_APPLICABLE,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='a508bd38-0c29-4aa8-9d71-bddaa30b7b91',
                        name='Emma Mohr',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='9c088d41-8bb7-4180-8f42-3d543935f377',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='c5c9b7e9-3b6a-43c5-a310-5e7c34cab0ec',
                        name='Bob Breitenberg',
                    ),
                    shared.TrackingCategoryRef(
                        id='66148944-a8e9-4085-875b-c2538253343f',
                        name='Ronald Murphy',
                    ),
                    shared.TrackingCategoryRef(
                        id='66ea4757-8d17-41e2-9418-18fc679b6b2f',
                        name='Lynn Effertz',
                    ),
                ],
                unit_amount=6957.24,
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
                    currency='GBP',
                    currency_rate=3240.28,
                    total_amount=6943.34,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='62c8b83a-38a8-4a88-8144-200c2caeb1ae',
                        name='Elvira Rutherford',
                    ),
                    currency='EUR',
                    currency_rate=2400.8,
                    id='4946bba7-a05a-48b4-a9ec-5b3688cca363',
                    note='magni',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='magni',
                    total_amount=4941.36,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=8973.52,
                    total_amount=5819.46,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='66e97e05-4103-4347-978f-f2491145fab9',
                        name='Jerome Mertz',
                    ),
                    currency='EUR',
                    currency_rate=9544.32,
                    id='336664ea-a6bf-42ff-94e8-c1b352acceda',
                    note='maxime',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='ad',
                    total_amount=1642.23,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='USD',
                    currency_rate=5437.75,
                    total_amount=1030.1,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='4eca016b-c41e-4a13-82d4-104a25ef71de',
                        name='Mr. Dora Ortiz',
                    ),
                    currency='USD',
                    currency_rate=1110.45,
                    id='4a431769-2ea4-4867-bd52-2b828a903066',
                    note='doloremque',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='doloremque',
                    total_amount=1474.89,
                ),
            ),
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=4891.43,
                    total_amount=5738.63,
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='b4cc64c2-b3a3-42c4-88ad-e62f6aa558a6',
                        name='Ms. Olive Daugherty',
                    ),
                    currency='GBP',
                    currency_rate=965.66,
                    id='6ca34bb8-7d4f-4621-a7a6-07d160629451',
                    note='magnam',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='neque',
                    total_amount=8634.15,
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='cupiditate',
                id='ca9f38bd-2be8-4787-8349-3f49aa8465a3',
            ),
            shared.SalesOrderRef(
                data_type='eos',
                id='83279b71-9d1c-4ea6-b3d8-6e3b35e49a31',
            ),
            shared.SalesOrderRef(
                data_type='consectetur',
                id='5778ce54-cacb-40e3-aa97-5045bacf63b2',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=1217.04,
        supplemental_data=shared.SupplementalData(
            content={
                "commodi": {
                    "nam": 'corporis',
                    "voluptates": 'amet',
                    "laborum": 'alias',
                },
                "eos": {
                    "autem": 'architecto',
                },
                "tempora": {
                    "ab": 'ad',
                },
            },
        ),
        total_amount=8257.86,
        total_discount=787.38,
        total_tax_amount=3435.3,
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=5176.62,
                name='Violet McClure',
            ),
            shared.WithholdingTaxitems(
                amount=1003.06,
                name='Boyd Sanford IV',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='suscipit',
    timeout_in_minutes=991467,
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
        content='voluptatibus'.encode(),
        request_body='dolores',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='alias',
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

