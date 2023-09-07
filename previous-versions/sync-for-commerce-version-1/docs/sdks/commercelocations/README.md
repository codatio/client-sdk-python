# commerce_locations

## Overview

Retrieve standardized data from linked commerce platforms.

### Available Operations

* [get_commerce_location](#get_commerce_location) - Get location
* [list_commerce_locations](#list_commerce_locations) - List locations

## get_commerce_location

The *Get location* endpoint returns a single location for a given locationId.

[Locations](https://docs.codat.io/commerce-api#/schemas/Location) hold information on the geographic location at which stocks of [products](https://docs.codat.io/commerce-api#/schemas/Product) may be held or where [orders](https://docs.codat.io/commerce-api#/schemas/Order) were placed.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-locations) for integrations that support getting a specific location.

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

req = operations.GetCommerceLocationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    location_id='expedita',
)

res = s.commerce_locations.get_commerce_location(req)

if res.commerce_location is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetCommerceLocationRequest](../../models/operations/getcommercelocationrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.GetCommerceLocationResponse](../../models/operations/getcommercelocationresponse.md)**


## list_commerce_locations

The *List locations* endpoint returns a list of [locations](https://docs.codat.io/commerce-api#/schemas/Location) for a given company's connection.

[Locations](https://docs.codat.io/commerce-api#/schemas/Location) hold information on the geographic location at which stocks of [products](https://docs.codat.io/commerce-api#/schemas/Product) may be held or where [orders](https://docs.codat.io/commerce-api#/schemas/Order) were placed.

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

req = operations.ListCommerceLocationsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.commerce_locations.list_commerce_locations(req)

if res.commerce_locations is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListCommerceLocationsRequest](../../models/operations/listcommercelocationsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.ListCommerceLocationsResponse](../../models/operations/listcommercelocationsresponse.md)**

