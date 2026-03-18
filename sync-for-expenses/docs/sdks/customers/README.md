# Customers

## Overview

Get, create, and update customers.

### Available Operations

* [create](#create) - Create customer
* [get](#get) - Get customer
* [list](#list) - List customers
* [update](#update) - Update customer

## create

The *Create customer* endpoint creates a new [customer](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-customers-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="create-customer" method="post" path="/companies/{companyId}/connections/{connectionId}/push/customers" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.create(request={
        "customer": {
            "contacts": [
                {
                    "modified_date": "2022-10-23T00:00:00Z",
                    "phone": None,
                    "status": shared.CustomerStatus.UNKNOWN,
                },
            ],
            "default_currency": "GBP",
            "modified_date": "2022-10-23T00:00:00Z",
            "source_modified_date": "2022-10-23T00:00:00Z",
            "status": shared.CustomerStatus.UNKNOWN,
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateCustomerRequest](../../models/operations/createcustomerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.CreateCustomerResponse](../../models/shared/createcustomerresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get

The *Get customer* endpoint returns a single customer for a given customerId.

[Customers](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).


### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Clear Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Dynamics 365 Business Central" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Exact (Netherlands)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Exact (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="FreeAgent" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="FreshBooks" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="KashFlow" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Oracle NetSuite" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="QuickBooks Desktop" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="QuickBooks Online" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="QuickBooks Online Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Sage 200cloud" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Sage 50 (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Sage Business Cloud Accounting" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Wave

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Wave" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Xero" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/companies/{companyId}/data/customers/{customerId}" example="Zoho Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetCustomerRequest](../../models/operations/getcustomerrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[shared.Customer](../../models/shared/customer.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List customers* endpoint returns a list of [customers](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-expenses-api#/operations/refresh-company-data).
    

### Example Usage: Clear Books

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Clear Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Dynamics 365 Business Central

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Dynamics 365 Business Central" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (Netherlands)

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Exact (Netherlands)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Exact (UK)

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Exact (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreeAgent

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="FreeAgent" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: FreshBooks

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="FreshBooks" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: KashFlow

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="KashFlow" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Oracle NetSuite

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Oracle NetSuite" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Desktop

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="QuickBooks Desktop" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="QuickBooks Online" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: QuickBooks Online Sandbox

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="QuickBooks Online Sandbox" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 200cloud

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Sage 200cloud" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage 50 (UK)

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Sage 50 (UK)" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Business Cloud Accounting

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Sage Business Cloud Accounting" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Sage Intacct

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Sage Intacct" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Wave

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Wave" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Xero

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Xero" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```
### Example Usage: Zoho Books

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/companies/{companyId}/data/customers" example="Zoho Books" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCustomersRequest](../../models/operations/listcustomersrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.Customers](../../models/shared/customers.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |

## update

The *Update customer* endpoint updates an existing [customer](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) for a given company's connection.

[Customers](https://docs.codat.io/sync-for-expenses-api#/schemas/Customer) are people or organizations that buy goods or services from the SMB.

**Integration-specific behavior**

Required data may vary by integration. To see what data to post, first call [Get create/update customer model](https://docs.codat.io/sync-for-expenses-api#/operations/get-create-update-customers-model).

### Example Usage

<!-- UsageSnippet language="python" operationID="update-customer" method="put" path="/companies/{companyId}/connections/{connectionId}/push/customers/{customerId}" example="Malformed query" -->
```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared


with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_expenses:

    res = codat_sync_expenses.customers.update(request={
        "customer": {
            "contacts": [
                {
                    "modified_date": "2022-10-23T00:00:00Z",
                    "phone": [
                        {
                            "number": "+44 25691 154789",
                            "type": shared.Type.PRIMARY,
                        },
                    ],
                    "status": shared.CustomerStatus.UNKNOWN,
                },
            ],
            "default_currency": "GBP",
            "modified_date": "2022-10-23T00:00:00Z",
            "source_modified_date": "2022-10-23T00:00:00Z",
            "status": shared.CustomerStatus.ACTIVE,
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "customer_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateCustomerRequest](../../models/operations/updatecustomerrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.UpdateCustomerResponse](../../models/shared/updatecustomerresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |