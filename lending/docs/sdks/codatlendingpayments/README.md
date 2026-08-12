# LoanWriteback.Payments

## Overview

### Available Operations

* [create](#create) - Create payment
* [get_create_model](#get_create_model) - Get create payment model

## create

The *Create payment* endpoint creates a new [payment](https://docs.codat.io/lending-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create payment model](https://docs.codat.io/lending-api#/operations/get-create-payments-model).

### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" example="Malformed query" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "currency": "GBP",
            "date_": "2022-10-23T00:00:00Z",
            "lines": [],
            "modified_date": "2022-10-23T00:00:00Z",
            "payment_method_ref": {
                "id": "EILBDVJVNUAGVKRQ",
                "name": "AliPay",
            },
            "source_modified_date": "2022-10-23T00:00:00Z",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "account_ref": {
                "id": "8000002E-1675267199",
                "name": "Undeposited Funds",
            },
            "currency": "USD",
            "currency_rate": Decimal("1"),
            "customer_ref": {
                "company_name": "string",
                "id": "80000002-1674552702",
            },
            "date_": "2023-02-10T11:47:04.792Z",
            "lines": [],
            "note": "note 14/02 1147",
            "payment_method_ref": {
                "id": "string",
                "name": "string",
            },
            "reference": "ref 14/02 1147",
            "total_amount": Decimal("28"),
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "account_ref": {
                "id": "1200",
                "name": "Bank Current Account",
            },
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "customer_ref": {
                "id": "CUST1",
            },
            "date_": "2023-03-17T11:47:04.792Z",
            "lines": [],
            "note": "note 07/03 14.31",
            "payment_method_ref": {
                "id": "4405",
            },
            "reference": "ref",
            "total_amount": Decimal("4"),
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "account_ref": {
                "id": "9a25937b267a11e797950a57719b2edb",
                "name": "Current",
            },
            "currency": "GBP",
            "currency_rate": Decimal("1"),
            "customer_ref": {
                "company_name": "Stanley test customer",
                "id": "30444c5bd4964fd787c7f8e2e5301ce1",
            },
            "date_": "2023-03-20T11:47:04.792Z",
            "lines": [],
            "note": "Need to send products asap.",
            "reference": "normal payment 20/03 17.05",
            "total_amount": Decimal("0.17"),
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="create-payment" method="post" path="/companies/{companyId}/connections/{connectionId}/push/payments" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared
from decimal import Decimal


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.create(request={
        "accounting_payment": {
            "account_ref": {
                "id": "81",
            },
            "customer_ref": {
                "id": "19",
            },
            "date_": "2022-03-12T00:00:00",
            "lines": [],
            "total_amount": Decimal("0"),
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreatePaymentRequest](../../models/operations/createpaymentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.AccountingCreatePaymentResponse](../../models/shared/accountingcreatepaymentresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_create_model

The *Get create payment model* endpoint returns the expected data for the request payload when creating a [payment](https://docs.codat.io/lending-api#/schemas/Payment) for a given company and integration.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

**Integration-specific behavior**

See the *response examples* for integration-specific indicative models.

### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: MYOB AccountRight and Essentials

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="MYOB AccountRight and Essentials" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Sandbox

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-create-payment-model" method="get" path="/companies/{companyId}/connections/{connectionId}/options/payments" example="Zoho Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.loan_writeback.payments.get_create_model(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCreatePaymentModelRequest](../../models/operations/getcreatepaymentmodelrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[shared.PushOption](../../models/shared/pushoption.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |