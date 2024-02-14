# Webhooks
(*webhooks*)

## Overview

Manage webhooks, rules, and events.

### Available Operations

* [create](#create) - Create webhook
* [get](#get) - Get webhook
* [list](#list) - List webhooks

## create

Create a new webhook configuration

### Example Usage

```python
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.CreateRule(
    notifiers=shared.WebhookNotifier(
        emails=[
            'info@client.com',
        ],
        webhook='https://webhook.client.com',
    ),
    type='DataConnectionStatusChanged',
    company_id='39b73b17-cc2e-429e-915d-71654e9dcd1e',
)

res = s.webhooks.create(req)

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.CreateRule](../../models/shared/createrule.md)              | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.CreateRuleResponse](../../models/operations/createruleresponse.md)**
### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401,402,403,429,500,503 | application/json        |
| errors.SDKError         | 4x-5xx                  | */*                     |

## get

Get a single webhook

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.GetWebhookRequest(
    rule_id='7318949f-c008-4936-a8ff-10d7ab563fa6',
)

res = s.webhooks.get(req)

if res.webhook is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetWebhookRequest](../../models/operations/getwebhookrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4x-5xx                      | */*                         |

## list

List webhooks that you are subscribed to.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="<YOUR_API_KEY_HERE>",
    ),
)

req = operations.ListRulesRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
)

res = s.webhooks.list(req)

if res.webhooks is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListRulesRequest](../../models/operations/listrulesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListRulesResponse](../../models/operations/listrulesresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4x-5xx                          | */*                             |
