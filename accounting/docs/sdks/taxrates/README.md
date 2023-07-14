# tax_rates

## Overview

Tax rates

### Available Operations

* [get](#get) - Get tax rate
* [list](#list) - List all tax rates

## get

The *Get tax rate* endpoint returns a single tax rate for a given taxRateId.

[Tax rates](https://docs.codat.io/accounting-api#/schemas/TaxRate) are a set of taxes and associated rates within the SMB's accounting package.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=taxRates) for integrations that support getting a specific tax rate.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).


### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetTaxRateRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    tax_rate_id='asperiores',
)

res = s.tax_rates.get(req)

if res.tax_rate is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetTaxRateRequest](../../models/operations/gettaxraterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetTaxRateResponse](../../models/operations/gettaxrateresponse.md)**


## list

The *List tax rates* endpoint returns a list of [tax rates](https://docs.codat.io/accounting-api#/schemas/TaxRate) for a given company's connection.

[Tax rates](https://docs.codat.io/accounting-api#/schemas/TaxRate) are a set of taxes and associated rates within the SMB's accounting package.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
    

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListTaxRatesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='quisquam',
)

res = s.tax_rates.list(req)

if res.tax_rates is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListTaxRatesRequest](../../models/operations/listtaxratesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.ListTaxRatesResponse](../../models/operations/listtaxratesresponse.md)**

