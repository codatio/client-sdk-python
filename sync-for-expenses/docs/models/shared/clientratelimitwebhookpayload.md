# ClientRateLimitWebhookPayload


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `daily_quota`                                        | *Optional[int]*                                      | :heavy_minus_sign:                                   | The number of available requests per day.            |
| `expiry_date`                                        | *Optional[str]*                                      | :heavy_minus_sign:                                   | The date time in UTC when your daily quota is reset. |
| `quota_remaining`                                    | *Optional[int]*                                      | :heavy_minus_sign:                                   | Total number of requests remaining for your client.  |