# company_info

## Overview

View company information fetched from the source platform.

### Available Operations

* [from_accounting_platform](#from_accounting_platform) - Get company info
* [from_commerce_platform](#from_commerce_platform) - Get company info

## from_accounting_platform

Gets the latest basic info for a company.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingCompanyInfoRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.company_info.from_accounting_platform(req)

if res.accounting_company_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetAccountingCompanyInfoRequest](../../models/operations/getaccountingcompanyinforequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |


### Response

**[operations.GetAccountingCompanyInfoResponse](../../models/operations/getaccountingcompanyinforesponse.md)**


## from_commerce_platform

Retrieve information about the company, as seen in the commerce platform.

This may include information like addresses, tax registration details and social media or website information.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCommerceCompanyInfoRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.company_info.from_commerce_platform(req)

if res.commerce_company_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetCommerceCompanyInfoRequest](../../models/operations/getcommercecompanyinforequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.GetCommerceCompanyInfoResponse](../../models/operations/getcommercecompanyinforesponse.md)**

