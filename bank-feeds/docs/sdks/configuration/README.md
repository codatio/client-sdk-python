# Configuration
(*configuration*)

## Overview

Configure bank feeds for a company.

### Available Operations

* [get](#get) - Get configuration
* [set](#set) - Set configuration

## get

﻿The *Get configuration* endpoint returns the current configuration for a given company ID.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get(req)

if res.configuration is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetConfigurationRequest](../../models/operations/getconfigurationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.GetConfigurationResponse](../../models/operations/getconfigurationresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## set

﻿Use *Set configuration* endpoint to configure a given company ID.

### Example Usage

```python
import codatbankfeeds
from codatbankfeeds.models import operations, shared

s = codatbankfeeds.CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.SetConfigurationRequest(
    configuration=shared.Configuration(
        company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
        configuration=shared.SyncConfiguration(
            sync_as_bank_feeds=shared.SyncAsBankFeeds(
                bank_account_options=[
                    shared.BankAccountOption(),
                ],
            ),
            sync_as_expenses=shared.SyncAsExpenses(
                bank_account_options=[
                    shared.BankAccountOption(),
                ],
                customer=shared.ConfigurationCustomer(
                    customer_options=[
                        shared.ConfigurationContactRef(),
                    ],
                ),
                supplier=shared.ConfigurationSupplier(
                    supplier_options=[
                        shared.ConfigurationContactRef(),
                    ],
                ),
            ),
        ),
        schedule=shared.ConfigurationSchedule(
            frequency_options=[
                'string',
            ],
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.set(req)

if res.configuration is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SetConfigurationRequest](../../models/operations/setconfigurationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.SetConfigurationResponse](../../models/operations/setconfigurationresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |
