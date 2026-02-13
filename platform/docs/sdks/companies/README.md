# Companies

## Overview

Create and manage your SMB users' companies.

### Available Operations

* [add_product](#add_product) - Add product
* [create](#create) - Create company
* [delete](#delete) - Delete a company
* [get](#get) - Get company
* [get_access_token](#get_access_token) - Get company access token
* [get_company_sync_settings](#get_company_sync_settings) - Get company sync settings
* [list](#list) - List companies
* [refresh_product_data](#refresh_product_data) - Refresh product data
* [remove_product](#remove_product) - Remove product
* [replace](#replace) - Replace company
* [set_company_sync_settings](#set_company_sync_settings) - Set company sync settings
* [update](#update) - Update company

## add_product

Use the *Add product* endpoint to enable a product for the company specified by `companyId`.

> Note: This feature is currently in alpha and available only to participants in the development program.

### Example Usage

<!-- UsageSnippet language="python" operationID="add-product" method="put" path="/companies/{companyId}/products/{productIdentifier}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.companies.add_product(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "product_identifier": "bank-feeds",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.AddProductRequest](../../models/operations/addproductrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## create

﻿Use the *Create company* endpoint to create a new [company](https://docs.codat.io/platform-api#/schemas/Company) that represents your customer in Codat. 

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/platform-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

If forbidden characters (see `name` pattern) are present in the request, a company will be created with the forbidden characters removed. For example, `Company (Codat[1])` with be created as `Company Codat1`.

### Example Usage: Malformed query

<!-- UsageSnippet language="python" operationID="create-company" method="post" path="/companies" example="Malformed query" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.create(request={
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    })

    # Handle response
    print(res)

```
### Example Usage: With a description

<!-- UsageSnippet language="python" operationID="create-company" method="post" path="/companies" example="With a description" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.create(request={
        "description": "Technology services, including web and app design and development",
        "name": "Technicalium",
    })

    # Handle response
    print(res)

```
### Example Usage: With a tag

<!-- UsageSnippet language="python" operationID="create-company" method="post" path="/companies" example="With a tag" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.create(request={
        "description": "Requested early access to the new financing scheme.",
        "name": "Bank of Dave",
    })

    # Handle response
    print(res)

```
### Example Usage: With no description

<!-- UsageSnippet language="python" operationID="create-company" method="post" path="/companies" example="With no description" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.create(request={
        "name": "Technicalium",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.CompanyRequestBody](../../models/shared/companyrequestbody.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[shared.Company](../../models/shared/company.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 400, 401, 402, 403, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

﻿The *Delete company* endpoint permanently deletes a [company](https://docs.codat.io/platform-api#/schemas/Company), its [connections](https://docs.codat.io/platform-api#/schemas/Connection) and any cached data. This operation is irreversible.

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/platform-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.


### Example Usage

<!-- UsageSnippet language="python" operationID="delete-company" method="delete" path="/companies/{companyId}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.companies.delete(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteCompanyRequest](../../models/operations/deletecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get

﻿The *Get company* endpoint returns a single company for a given `companyId`.

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/platform-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.


### Example Usage: Parent multi-entity company

<!-- UsageSnippet language="python" operationID="get-company" method="get" path="/companies/{companyId}" example="Parent multi-entity company" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Simple company

<!-- UsageSnippet language="python" operationID="get-company" method="get" path="/companies/{companyId}" example="Simple company" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Subsidiary multi-entity company

<!-- UsageSnippet language="python" operationID="get-company" method="get" path="/companies/{companyId}" example="Subsidiary multi-entity company" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetCompanyRequest](../../models/operations/getcompanyrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[shared.Company](../../models/shared/company.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_access_token

Use the _Get company access token_ endpoint to return an access token for the specified company ID. The token is valid for one day. 

The token is required by Codat's embeddable UIs (such as [Connections SDK](https://docs.codat.io/auth-flow/optimize/connection-management) and [Link SDK](https://docs.codat.io/auth-flow/authorize-embedded-link)) to verify the identity of the user and improve the reliability of data provided by them.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-company-access-token" method="get" path="/companies/{companyId}/accessToken" example="Simple company" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.get_access_token(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCompanyAccessTokenRequest](../../models/operations/getcompanyaccesstokenrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[shared.CompanyAccessToken](../../models/shared/companyaccesstoken.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_company_sync_settings

Retrieve the [sync settings](https://docs.codat.io/knowledge-base/advanced-sync-settings) for a specific company. This includes how often data types should be queued to be updated, and how much history should be fetched.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-company-syncSettings" method="get" path="/companies/{companyId}/syncSettings" example="Example" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.get_company_sync_settings(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCompanySyncSettingsRequest](../../models/operations/getcompanysyncsettingsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.CompanySyncSettings](../../models/shared/companysyncsettings.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## list

﻿The *List companies* endpoint returns a list of [companies](https://docs.codat.io/platform-api#/schemas/Company) associated to your instances.

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/platform-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

## Filter by tags

The *List companies* endpoint supports the filtering of companies using [tags](https://docs.codat.io/using-the-api/managing-companies#add-metadata-to-a-company). It supports the following operators with [Codat’s query language](https://docs.codat.io/using-the-api/querying):

- equals (`=`)
- not equals (`!=`)
- contains (`~`)

For example, you can use the querying to filter companies tagged with a specific foreign key, region, or owning team: 
- Foreign key: `uid = {yourCustomerId}`
- Region: `region != uk`
- Owning team and region: `region = uk && owningTeam = invoice-finance`

### Example Usage: List of Companies

<!-- UsageSnippet language="python" operationID="list-companies" method="get" path="/companies" example="List of Companies" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)

```
### Example Usage: One company

<!-- UsageSnippet language="python" operationID="list-companies" method="get" path="/companies" example="One company" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.list(request={
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "tags": "region=uk && team=invoice-finance",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListCompaniesRequest](../../models/operations/listcompaniesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.Companies](../../models/shared/companies.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## refresh_product_data

Use the **Refresh product data** endpoint to manually refresh data for a custom product for a specific company.

### Tips and traps

- This endpoint only supports refreshing data for **custom products** and can't be used for Codat's standard solutions. Refer to [individual solutions' documentation](https://docs.codat.io/) instead.
- If a data sync is already in progress for a custom product, the refresh request will return a `Bad request (400)` response.
- If a company has multiple custom products enabled, you can refresh data for each product individually.
 - Optionally include a request body with `dataTypes` to refresh only selected data types for the specified product. If omitted, the product's scheduled refresh is triggered as usual.
 - When specifying `dataTypes`, each value must be a valid data type supported by the product. Invalid values will result in a `Bad request (400)` response listing valid options.

### Example Usage

<!-- UsageSnippet language="python" operationID="refresh-product-data" method="post" path="/companies/{companyId}/products/{productIdentifier}/refresh" example="Filter specific data types" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.companies.refresh_product_data(request={
        "request_body": {
            "data_types": [
                "invoices",
                "payments",
            ],
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "product_identifier": "bank-feeds",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.RefreshProductDataRequest](../../models/operations/refreshproductdatarequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## remove_product

Use the *Remove product* endpoint to disable a product for the company specified by `companyId`.

> Note: This feature is currently in alpha and available only to participants in the development program.

### Example Usage

<!-- UsageSnippet language="python" operationID="remove-product" method="delete" path="/companies/{companyId}/products/{productIdentifier}" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.companies.remove_product(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "product_identifier": "bank-feeds",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RemoveProductRequest](../../models/operations/removeproductrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## replace

﻿Use the *Replace company* endpoint to replace the existing name, description, and tags of the company. Calling the endpoint will replace existing values even if new values haven't been defined in the payload.

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.
Each company can have multiple [connections](https://docs.codat.io/platform-api#/schemas/Connection) to different data sources, such as one connection to Xero for accounting data, two connections to Plaid for two bank accounts, and a connection to Zettle for POS data.

### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="replace-company" method="put" path="/companies/{companyId}" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.replace(request={
        "company_request_body": {
            "description": "Requested early access to the new financing scheme.",
            "name": "Bank of Dave",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Update description

<!-- UsageSnippet language="python" operationID="replace-company" method="put" path="/companies/{companyId}" example="Update description" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.replace(request={
        "company_request_body": {
            "description": "Additional documents required",
            "name": "Same name",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Update name

<!-- UsageSnippet language="python" operationID="replace-company" method="put" path="/companies/{companyId}" example="Update name" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.replace(request={
        "company_request_body": {
            "name": "New Name",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ReplaceCompanyRequest](../../models/operations/replacecompanyrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[shared.Company](../../models/shared/company.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |

## set_company_sync_settings

Set the sync settings for a specific company.

### Example Usage

<!-- UsageSnippet language="python" operationID="set-company-syncSettings" method="post" path="/companies/{companyId}/syncSettings" example="Malformed query" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    cp_client.companies.set_company_sync_settings(request={
        "request_body": {
            "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
            "settings": [
                {
                    "data_type": shared.DataType.INVOICES,
                    "fetch_on_first_link": True,
                    "is_locked": True,
                    "months_to_sync": 24,
                    "sync_from_utc": "2020-01-01T12:00:00.000Z",
                    "sync_from_window": 24,
                    "sync_order": 0,
                    "sync_schedule": 24,
                },
            ],
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.SetCompanySyncSettingsRequest](../../models/operations/setcompanysyncsettingsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## update

﻿Use the *Update company* endpoint to update the name, description, or tags of the company.

The *Update company* endpoint doesn't have any required fields. If any of the fields provided are `null` or not provided, they won't be included in the update.  

A [company](https://docs.codat.io/platform-api#/schemas/Company) represents a business sharing access to their data.

### Example Usage: Unauthorized

<!-- UsageSnippet language="python" operationID="update-company" method="patch" path="/companies/{companyId}" example="Unauthorized" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.update(request={
        "company_update_request": {
            "description": "Requested early access to the new financing scheme.",
            "name": "Bank of Dave",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Update name

<!-- UsageSnippet language="python" operationID="update-company" method="patch" path="/companies/{companyId}" example="Update name" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.update(request={
        "company_update_request": {
            "name": "New Name",
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```
### Example Usage: Update tags

<!-- UsageSnippet language="python" operationID="update-company" method="patch" path="/companies/{companyId}" example="Update tags" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.update(request={
        "company_update_request": {
            "tags": {
                "refrence": "new reference",
            },
        },
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateCompanyRequest](../../models/operations/updatecompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[shared.Company](../../models/shared/company.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |