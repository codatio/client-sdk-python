# AccountsReceivable.Payments

## Overview

### Available Operations

* [get](#get) - Get payment
* [list](#list) - List payments

## get

The *Get payment* endpoint returns a single payment for a given paymentId.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-accounting-payment" method="get" path="/companies/{companyId}/data/payments/{paymentId}" example="Zoho Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "payment_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingPaymentRequest](../../models/operations/getaccountingpaymentrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.AccountingPayment](../../models/shared/accountingpayment.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List payments* endpoint returns a list of [payments](https://docs.codat.io/lending-api#/schemas/Payment) for a given company's connection.

[Payments](https://docs.codat.io/lending-api#/schemas/Payment) represent an allocation of money within any customer accounts receivable account.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Clear Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Dynamics 365 Business Central" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Exact (Netherlands)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Exact (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="FreeAgent" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="FreshBooks" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="KashFlow" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Oracle NetSuite" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="QuickBooks Desktop" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="QuickBooks Online" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="QuickBooks Online Sandbox" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Sage 200cloud" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Sage 50 (UK)" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Sage Business Cloud Accounting" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Sage Intacct" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Xero" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="list-accounting-payments" method="get" path="/companies/{companyId}/data/payments" example="Zoho Books" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.accounts_receivable.payments.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListAccountingPaymentsRequest](../../models/operations/listaccountingpaymentsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.AccountingPayments](../../models/shared/accountingpayments.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |