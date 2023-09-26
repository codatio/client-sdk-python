# Webhooks

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
        auth_header="",
    ),
)

req = shared.CreateRule(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    notifiers=shared.WebhookNotifier(
        emails=[
            'info@client.com',
        ],
        webhook='https://webhook.client.com',
    ),
    type='voluptatibus',
)

res = s.webhooks.create(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.CreateRule](../../models/shared/createrule.md)              | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.CreateRuleResponse](../../models/operations/createruleresponse.md)**


## get

Get a single webhook

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetWebhookRequest(
    rule_id='7318949f-c008-4936-a8ff-10d7ab563fa6',
)

res = s.webhooks.get(req)

if res.webhook is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetWebhookRequest](../../models/operations/getwebhookrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**


## list

List webhooks that you are subscribed to.

### Example Usage

```python
import codatplatform
from codatplatform.models import operations, shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.ListRulesRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='vero',
)

res = s.webhooks.list(req)

if res.webhooks is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListRulesRequest](../../models/operations/listrulesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.ListRulesResponse](../../models/operations/listrulesresponse.md)**

