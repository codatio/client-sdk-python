# CompanyInfo
(*company_info*)

## Overview

View company information fetched from the source platform.

### Available Operations

* [get_accounting_profile](#get_accounting_profile) - Get company accounting profile

## get_accounting_profile

Gets the latest basic info for a company.

### Example Usage

```python
import codatsyncpayroll
from codatsyncpayroll.models import operations, shared

s = codatsyncpayroll.CodatSyncPayroll(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingProfileRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.company_info.get_accounting_profile(req)

if res.company_info is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingProfileRequest](../../models/operations/getaccountingprofilerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetAccountingProfileResponse](../../models/operations/getaccountingprofileresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 401,402,403,404,409,429,500,503 | application/json                |
| errors.SDKError                 | 400-600                         | */*                             |
