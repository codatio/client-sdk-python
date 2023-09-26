# Products

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get](#get) - Get product
* [get_category](#get_category) - Get product category
* [list](#list) - List products
* [list_categories](#list_categories) - List product categories

## get

The *Get product* endpoint returns a single product for a given productId.

[Products](https://docs.codat.io/commerce-api#/schemas/Product) are items in the company's inventory that are available for sale.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-products) for integrations that support getting a specific product.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetProductRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    product_id='suscipit',
)

res = s.products.get(req)

if res.product is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetProductRequest](../../models/operations/getproductrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetProductResponse](../../models/operations/getproductresponse.md)**


## get_category

The *Get product* endpoint returns a single product for a given productId.

[Product categories](https://docs.codat.io/commerce-api#/schemas/ProductCategory) are used to classify a group of products together, either by type (e.g. "Furniture"), or sometimes by tax profile.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-productCategories) for integrations that support getting a specific product.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetProductCategoryRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    product_id='iure',
)

res = s.products.get_category(req)

if res.product_category is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetProductCategoryRequest](../../models/operations/getproductcategoryrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.GetProductCategoryResponse](../../models/operations/getproductcategoryresponse.md)**


## list

The *List products* endpoint returns a list of [products](https://docs.codat.io/commerce-api#/schemas/Product) for a given company's connection.

[Products](https://docs.codat.io/commerce-api#/schemas/Product) are items in the company's inventory that are available for sale.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListProductsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='magnam',
)

res = s.products.list(req)

if res.products is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListProductsRequest](../../models/operations/listproductsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.ListProductsResponse](../../models/operations/listproductsresponse.md)**


## list_categories

The *List product categories* endpoint returns a list of [product categories](https://docs.codat.io/commerce-api#/schemas/ProductCategory) for a given company's connection.

[Product categories](https://docs.codat.io/commerce-api#/schemas/ProductCategory) are used to classify a group of products together, either by type (e.g. "Furniture"), or sometimes by tax profile.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatcommerce
from codatcommerce.models import operations, shared

s = codatcommerce.CodatCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListProductCategoriesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='debitis',
)

res = s.products.list_categories(req)

if res.product_categories is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListProductCategoriesRequest](../../models/operations/listproductcategoriesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.ListProductCategoriesResponse](../../models/operations/listproductcategoriesresponse.md)**

