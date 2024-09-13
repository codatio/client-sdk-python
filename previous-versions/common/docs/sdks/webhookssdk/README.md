# WebhooksSDK
(*webhooks*)

## Overview

Create and manage webhooks that listen to Codat's events.

### Available Operations

* [~~create~~](#create) - Create webhook :warning: **Deprecated**
* [create_consumer](#create_consumer) - Create webhook consumer
* [delete_consumer](#delete_consumer) - Delete webhook consumer
* [~~get~~](#get) - Get webhook :warning: **Deprecated**
* [~~list~~](#list) - List webhooks :warning: **Deprecated**
* [list_consumers](#list_consumers) - List webhook consumers

## ~~create~~

Create a new webhook configuration

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.webhooks.create(request={
    "notifiers": {
        "emails": [
            "info@client.com",
        ],
        "webhook": "https://webhook.client.com",
    },
    "type": "DataConnectionStatusChanged",
    "company_id": "39b73b17-cc2e-429e-915d-71654e9dcd1e",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateRule](../../models/createrule.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Webhook](../../models/webhook.md)**

### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ErrorMessage     | 401,402,403,429,500,503 | application/json        |
| models.SDKError         | 4xx-5xx                 | */*                     |


## create_consumer

﻿Use the *Create webhook consumer* endpoint to create a new webhook consumer that will listen to messages we send you.

[Webhook consumer](https://docs.codat.io/platform-api#/schemas/WebhookConsumer) is an HTTP endpoint that you configure to subscribe to specific events. See our documentation for more details on [Codat's webhook service](https://docs.codat.io/using-the-api/webhooks/overview).

### Tips and traps
- The number of webhook consumers you can create is limited to 50. If you have reached the maximum number of consumers, use the [*Delete webhook consumer*](https://docs.codat.io/platform-api#/operations/delete-webhook-consumer) endpoint to delete an unused consumer first.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.webhooks.create_consumer(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "event_types": [
        "DataSyncCompleted",
        "Dataset data changed",
    ],
    "url": "https://example.com/webhoook-consumer",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.WebhookConsumerPrototype](../../models/webhookconsumerprototype.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.WebhookConsumer](../../models/webhookconsumer.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## delete_consumer

﻿Use the *Delete webhook consumer* endpoint to delete an existing webhoook consumer, providing its valid `id` as a parameter.

[Webhook consumer](https://docs.codat.io/platform-api#/schemas/WebhookConsumer) is an HTTP endpoint that you configure to subscribe to specific events. See our documentation for more details on [Codat's webhook service](https://docs.codat.io/using-the-api/webhooks/overview).

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.webhooks.delete_consumer(request={
    "webhook_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.DeleteWebhookConsumerRequest](../../models/deletewebhookconsumerrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## ~~get~~

Get a single webhook

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.webhooks.get(request={
    "rule_id": "7318949f-c008-4936-a8ff-10d7ab563fa6",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetWebhookRequest](../../models/getwebhookrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Webhook](../../models/webhook.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |


## ~~list~~

List webhooks that you are subscribed to.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.webhooks.list(request={
    "order_by": "-modifiedDate",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListRulesRequest](../../models/listrulesrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Webhooks](../../models/webhooks.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| models.SDKError                 | 4xx-5xx                         | */*                             |


## list_consumers

﻿Use the *List webhook consumers* endpoint to return a list of all webhook consumers that currently exist for your client.

[Webhook consumer](https://docs.codat.io/platform-api#/schemas/WebhookConsumer) is an HTTP endpoint that you configure to subscribe to specific events. See our documentation for more details on [Codat's webhook service](https://docs.codat.io/using-the-api/webhooks/overview).

### Example Usage

```python
from codat_common import CodatCommon

s = CodatCommon(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.webhooks.list_consumers()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookConsumers](../../models/webhookconsumers.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.ErrorMessage         | 400,401,402,403,429,500,503 | application/json            |
| models.SDKError             | 4xx-5xx                     | */*                         |
