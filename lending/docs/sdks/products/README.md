# Sales.Products

## Overview

### Available Operations

* [get](#get) - Get product
* [list](#list) - List products

## get

The *Get product* endpoint returns a single product for a given productId.

[Products](https://docs.codat.io/lending-api#/schemas/Product) are items in the company's inventory that are available for sale.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).


### Example Usage

<!-- UsageSnippet language="python" operationID="get-commerce-product" method="get" path="/companies/{companyId}/connections/{connectionId}/data/commerce-products/{productId}" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.sales.products.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "product_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetCommerceProductRequest](../../models/operations/getcommerceproductrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[shared.CommerceProduct](../../models/shared/commerceproduct.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 401, 402, 403, 404, 409, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## list

The *List products* endpoint returns a list of [products](https://docs.codat.io/lending-api#/schemas/Product) for a given company's connection.

[Products](https://docs.codat.io/lending-api#/schemas/Product) are items in the company's inventory that are available for sale.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage

<!-- UsageSnippet language="python" operationID="list-commerce-products" method="get" path="/companies/{companyId}/connections/{connectionId}/data/commerce-products" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.sales.products.list(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "order_by": "-modifiedDate",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListCommerceProductsRequest](../../models/operations/listcommerceproductsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[shared.CommerceProducts](../../models/shared/commerceproducts.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 400, 401, 402, 403, 404, 409, 429 | application/json                  |
| errors.ErrorMessage               | 500, 503                          | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |