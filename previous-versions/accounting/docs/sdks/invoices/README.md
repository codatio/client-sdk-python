# Invoices

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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=Decimal('263.21'),
        additional_tax_percentage=Decimal('8197.57'),
        amount_due=Decimal('7188.79'),
        currency='EUR',
        currency_rate=Decimal('8256.81'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='illum',
            id='b484708f-b4e3-491e-abc1-58c4c4e54599',
        ),
        discount_percentage=Decimal('9294.43'),
        due_date='2022-10-23T00:00:00.000Z',
        id='342260e9-b200-4ce7-8a1b-d8fb7a0a116c',
        invoice_number='officiis',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='23d4097f-a30e-49af-b25b-29122030d83f',
                    name='Rosie Waters',
                ),
                description='dignissimos',
                discount_amount=Decimal('5920.88'),
                discount_percentage=Decimal('5818.89'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='d22e8c1f-8493-4825-bdc4-2c876c2c2dfb',
                    name='Sheri Weissnat DDS',
                ),
                quantity=Decimal('4608.03'),
                sub_total=Decimal('3920.8'),
                tax_amount=Decimal('1296.19'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('1974.41'),
                    id='0f841fb1-bd23-4fdb-94db-6be5a685998e',
                    name='Wanda Osinski',
                ),
                total_amount=Decimal('276.53'),
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='da16fc2b-271a-4289-857e-854e90439d22',
                            name='Monica Johnson',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='cupiditate',
                        id='46240708-4f7a-4b37-8ef0-2225194db554',
                    ),
                    is_billed_to=shared.BilledToType1.UNKNOWN,
                    is_rebilled_to=shared.BilledToType1.UNKNOWN,
                    project_ref=shared.ProjectRef(
                        id='adc669af-90a2-46c7-8dc9-81f068981d6b',
                        name='Norman Ferry',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='accountTransaction',
                        id='a348c31b-f407-4ee4-bcf0-c42b78f15626',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='398a0dc7-6632-44cc-b06c-8ca12d025292',
                        name='Patricia Pouros',
                    ),
                ],
                unit_amount=Decimal('3689.76'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='fugit',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='EUR',
                    currency_rate=Decimal('5062.02'),
                    total_amount=Decimal('5749.9'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='5b8bcf24-db95-4969-b352-f74533994d78',
                        name='Elbert Fay',
                    ),
                    currency='EUR',
                    currency_rate=Decimal('6104.9'),
                    id='389f5abb-7f66-4255-8a28-382ac483afd2',
                    note='consectetur',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='minima',
                    total_amount=Decimal('7036.51'),
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='facilis',
                id='a650164e-06f5-4bf6-ae59-1bc8bdef3612',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=Decimal('2033.96'),
        supplemental_data=shared.SupplementalData(
            content={
                "quod": {
                    "eos": 'alias',
                },
            },
        ),
        total_amount=Decimal('3198.07'),
        total_discount=Decimal('9545.95'),
        total_tax_amount=Decimal('8168.25'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('6625.15'),
                name='Alex Bayer',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    timeout_in_minutes=264073,
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
    invoice_id='fuga',
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
    invoice_id='iure',
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
    invoice_id='deleniti',
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
    invoice_id='officia',
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
    invoice_id='sint',
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
    
### Useful queries

- Outstanding invoices - `query = amountDue > 0`
- Invoices due after a certain date: `query = dueDate > 2021-01-28`

[Read more about querying](https://docs.codat.io/using-the-api/querying).

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
    query='laborum',
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
    invoice_id='dolor',
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
from decimal import Decimal

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateInvoiceRequest(
    invoice=shared.Invoice(
        additional_tax_amount=Decimal('3227.73'),
        additional_tax_percentage=Decimal('8477.4'),
        amount_due=Decimal('229.66'),
        currency='USD',
        currency_rate=Decimal('3771.94'),
        customer_ref=shared.AccountingCustomerRef(
            company_name='expedita',
            id='6f66fef0-20e9-4f44-bb42-57b992c8dbda',
        ),
        discount_percentage=Decimal('4146.44'),
        due_date='2022-10-23T00:00:00.000Z',
        id='61efa219-8258-4fd0-a9eb-a47f7d3ef049',
        invoice_number='aliquid',
        issue_date='2022-10-23T00:00:00.000Z',
        line_items=[
            shared.InvoiceLineItem(
                account_ref=shared.AccountRef(
                    id='0d6a1831-c87a-4df5-96fd-f1ad837ae80c',
                    name='Blanca Brakus',
                ),
                description='occaecati',
                discount_amount=Decimal('3396.51'),
                discount_percentage=Decimal('7343.61'),
                is_direct_income=False,
                item_ref=shared.ItemRef(
                    id='a998678f-a3f6-4969-91af-388ce0361444',
                    name='Sylvester Kling',
                ),
                quantity=Decimal('4397.45'),
                sub_total=Decimal('6541.99'),
                tax_amount=Decimal('105.85'),
                tax_rate_ref=shared.TaxRateRef(
                    effective_tax_rate=Decimal('9164.86'),
                    id='f2f53602-8efe-4ef9-b415-2ed7e253f4c1',
                    name='Constance Stark',
                ),
                total_amount=Decimal('6687.83'),
                tracking=shared.Propertiestracking1(
                    category_refs=[
                        shared.TrackingCategoryRef(
                            id='7170f445-accf-4667-aaf9-bbad185fe431',
                            name='Rick Predovic',
                        ),
                    ],
                    customer_ref=shared.AccountingCustomerRef(
                        company_name='cumque',
                        id='838fbb8c-20cb-467f-84b4-25e99e6234c9',
                    ),
                    is_billed_to=shared.BilledToType1.PROJECT,
                    is_rebilled_to=shared.BilledToType1.NOT_APPLICABLE,
                    project_ref=shared.ProjectRef(
                        id='b79dfeb7-7a5c-438d-8baf-91e506ef890a',
                        name='Anita Reilly',
                    ),
                    record_ref=shared.InvoiceTo(
                        data_type='invoice',
                        id='f16f56d3-85a3-4c4a-8631-b99e26ced8f9',
                    ),
                ),
                tracking_category_refs=[
                    shared.TrackingCategoryRef(
                        id='fdb9410f-63bb-4f81-b837-b01afdd78862',
                        name='Katherine Kuvalis',
                    ),
                ],
                unit_amount=Decimal('7164.1'),
            ),
        ],
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date='2022-10-23T00:00:00.000Z',
        note='labore',
        paid_on_date='2022-10-23T00:00:00.000Z',
        payment_allocations=[
            shared.Items(
                allocation=shared.ItemsAllocation(
                    allocated_on_date='2022-10-23T00:00:00.000Z',
                    currency='GBP',
                    currency_rate=Decimal('9580.6'),
                    total_amount=Decimal('3371.49'),
                ),
                payment=shared.PaymentAllocationPayment(
                    account_ref=shared.AccountRef(
                        id='033f19db-f125-4ce4-952e-ab9cd7e5224a',
                        name='Jan Abbott Sr.',
                    ),
                    currency='GBP',
                    currency_rate=Decimal('7370.61'),
                    id='7847ec59-e1f6-47f3-84cc-e4b6d7696ff3',
                    note='eligendi',
                    paid_on_date='2022-10-23T00:00:00.000Z',
                    reference='nihil',
                    total_amount=Decimal('2628.91'),
                ),
            ),
        ],
        sales_order_refs=[
            shared.SalesOrderRef(
                data_type='dignissimos',
                id='501357e4-4f51-4f8b-884c-3197e193a245',
            ),
        ],
        source_modified_date='2022-10-23T00:00:00.000Z',
        status=shared.InvoiceStatus.SUBMITTED,
        sub_total=Decimal('4990.05'),
        supplemental_data=shared.SupplementalData(
            content={
                "tenetur": {
                    "excepturi": 'modi',
                },
            },
        ),
        total_amount=Decimal('5463.29'),
        total_discount=Decimal('4724.29'),
        total_tax_amount=Decimal('2600.46'),
        withholding_tax=[
            shared.WithholdingTaxitems(
                amount=Decimal('8113.8'),
                name='Mable Hills',
            ),
        ],
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    force_update=False,
    invoice_id='labore',
    timeout_in_minutes=596133,
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
        content='ducimus'.encode(),
        request_body='qui',
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    invoice_id='qui',
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

