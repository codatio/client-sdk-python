# CommerceOrders
(*commerce_orders*)

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get_commerce_order](#get_commerce_order) - Get order
* [list_commerce_orders](#list_commerce_orders) - List orders

## get_commerce_order

The *Get order* endpoint returns a single order for a given orderId.

[Orders](https://docs.codat.io/commerce-api#/schemas/Order) contain the transaction details for all products sold by the company.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-orders) for integrations that support getting a specific order.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-commerce-v1-api#/operations/refresh-company-data).


### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceOrderRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_id='string',
)

res = s.commerce_orders.get_commerce_order(req)

if res.commerce_order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCommerceOrderRequest](../../models/operations/getcommerceorderrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetCommerceOrderResponse](../../models/operations/getcommerceorderresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |

## list_commerce_orders

The *List orders* endpoint returns a list of [orders](https://docs.codat.io/commerce-api#/schemas/Order) for a given company's connection.

[Orders](https://docs.codat.io/commerce-api#/schemas/Order) contain the transaction details for all products sold by the company.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-commerce-v1-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListCommerceOrdersRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
)

res = s.commerce_orders.list_commerce_orders(req)

if res.commerce_orders is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListCommerceOrdersRequest](../../models/operations/listcommerceordersrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.ListCommerceOrdersResponse](../../models/operations/listcommerceordersresponse.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 400-600                             | */*                                 |
