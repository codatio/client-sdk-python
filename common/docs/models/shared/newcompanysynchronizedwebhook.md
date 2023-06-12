# NewCompanySynchronizedWebhook

Webhook request body to notify that a new company has successfully synchronized at least one dataType for the first time.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `alert_id`                                  | *Optional[str]*                             | :heavy_minus_sign:                          | Unique identifier of the webhook event.     |                                             |
| `company_id`                                | *Optional[str]*                             | :heavy_minus_sign:                          | Unique identifier for your SMB in Codat.    | 8a210b68-6988-11ed-a1eb-0242ac120002        |
| `message`                                   | *Optional[str]*                             | :heavy_minus_sign:                          | A human readable message about the webhook. |                                             |
| `rule_id`                                   | *Optional[str]*                             | :heavy_minus_sign:                          | Unique identifier for the rule.             |                                             |
| `type`                                      | *Optional[str]*                             | :heavy_minus_sign:                          | The type of rule.                           |                                             |