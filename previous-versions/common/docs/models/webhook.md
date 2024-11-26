# Webhook

Configuration to provide an event notification to a URL or list of email addresses based on the given type or condition.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `notifiers`                                            | [models.WebhookNotifier](../models/webhooknotifier.md) | :heavy_check_mark:                                     | N/A                                                    |                                                        |
| `type`                                                 | *str*                                                  | :heavy_check_mark:                                     | The type of webhook.                                   |                                                        |
| `company_id`                                           | *Optional[str]*                                        | :heavy_minus_sign:                                     | Unique identifier for your SMB in Codat.               | 8a210b68-6988-11ed-a1eb-0242ac120002                   |
| `id`                                                   | *Optional[str]*                                        | :heavy_minus_sign:                                     | Unique identifier for the configured notification.     | ff89c50e-a719-4ef5-a182-9917e53927b6                   |