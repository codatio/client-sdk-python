# LocationsSDK
(*locations*)

## Overview

Retrieve standardized data from linked commerce software.

### Available Operations

* [get](#get) - Get location
* [list](#list) - List locations

## get

The *Get location* endpoint returns a single location for a given locationId.

[Locations](https://docs.codat.io/commerce-api#/schemas/Location) hold information on the geographic location at which stocks of [products](https://docs.codat.io/commerce-api#/schemas/Product) may be held or where [orders](https://docs.codat.io/commerce-api#/schemas/Order) were placed.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/commerce?view=tab-by-data-type&dataType=commerce-locations) for integrations that support getting a specific location.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.locations.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "location_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetLocationRequest](../../models/getlocationrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Location](../../models/location.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |


## list

The *List locations* endpoint returns a list of [locations](https://docs.codat.io/commerce-api#/schemas/Location) for a given company's connection.

[Locations](https://docs.codat.io/commerce-api#/schemas/Location) hold information on the geographic location at which stocks of [products](https://docs.codat.io/commerce-api#/schemas/Product) may be held or where [orders](https://docs.codat.io/commerce-api#/schemas/Order) were placed.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_commerce import CodatCommerce

s = CodatCommerce(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.locations.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListLocationsRequest](../../models/listlocationsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Locations](../../models/locations.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |
