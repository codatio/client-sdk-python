# CodatSyncPayables SDK

## Overview

Sync for Payables: The API for Sync for Payables. 

Sync for Payables is an API and a set of supporting tools built to help integrate with your customers' accounting software, and keep their supplier information, invoices, and payments in sync.

[Read More...](https://docs.codat.io/payables/overview)

### Available Operations

* [get_accounting_profile](#get_accounting_profile) - Get company accounting profile

## get_accounting_profile

Gets the latest basic info for a company.

### Example Usage

```python
import codatsyncpayables
from codatsyncpayables.models import operations, shared

s = codatsyncpayables.CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingProfileRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.codat_sync_payables.get_accounting_profile(req)

if res.company_information is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetAccountingProfileRequest](../../models/operations/getaccountingprofilerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[operations.GetAccountingProfileResponse](../../models/operations/getaccountingprofileresponse.md)**

