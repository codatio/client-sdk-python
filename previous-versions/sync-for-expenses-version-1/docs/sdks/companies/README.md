# Companies
(*companies*)

## Overview

Create and manage your Codat companies.

### Available Operations

* [create_company](#create_company) - Create company
* [delete_company](#delete_company) - Delete a company
* [get_company](#get_company) - Get company
* [list_companies](#list_companies) - List companies
* [update_company](#update_company) - Update company

## create_company

﻿Use the *Create company* endpoint to create a new [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) that represents your customer in Codat. 

A [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

If forbidden characters (see `name` pattern) are present in the request, a company will be created with the forbidden characters removed. For example, `Company (Codat[1])` with be created as `Company Codat1`.

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CompanyRequestBody(
    name='Bank of Dave',
    description='Requested early access to the new financing scheme.',
)

res = s.companies.create_company(req)

if res.company is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CompanyRequestBody](../../models/shared/companyrequestbody.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |


### Response

**[operations.CreateCompanyResponse](../../models/operations/createcompanyresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## delete_company

﻿The *Delete company* endpoint permanently deletes a [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company), its [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) and any cached data. This operation is irreversible.

A [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DeleteCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.delete_company(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteCompanyRequest](../../models/operations/deletecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.DeleteCompanyResponse](../../models/operations/deletecompanyresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## get_company

﻿The *Get company* endpoint returns a single company for a given `companyId`.

A [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.


### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.get_company(req)

if res.company is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCompanyRequest](../../models/operations/getcompanyrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetCompanyResponse](../../models/operations/getcompanyresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## list_companies

﻿The *List companies* endpoint returns a list of [companies] associated to your instances.

A [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCompaniesRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
)

res = s.companies.list_companies(req)

if res.companies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCompaniesRequest](../../models/operations/listcompaniesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.ListCompaniesResponse](../../models/operations/listcompaniesresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4x-5xx                          | */*                             |

## update_company

﻿Use the *Update company* endpoint to update both the name and description of the company. 
If you use [groups](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Group) to manage a set of companies, use the [Add company](https://docs.codat.io/sync-for-expenses-v1-api#/operations/add-company-to-group) or [Remove company](https://docs.codat.io/sync-for-expenses-v1-api#/operations/remove-company-from-group) endpoints to add or remove a company from a group.

A [company](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/sync-for-expenses-v1-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.UpdateCompanyRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.companies.update_company(req)

if res.company is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCompanyRequest](../../models/operations/updatecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.UpdateCompanyResponse](../../models/operations/updatecompanyresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |
