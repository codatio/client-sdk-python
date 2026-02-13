# ValidationItem1


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `item_id`                                                     | *Optional[str]*                                               | :heavy_minus_sign:                                            | The unique identifier of the item that was validated.         |
| `message`                                                     | *Optional[str]*                                               | :heavy_minus_sign:                                            | The message that describes the validation warning or error.   |
| `rule_id`                                                     | *Optional[str]*                                               | :heavy_minus_sign:                                            | The unique identifier of the rule that wasn't met.            |
| `validator_name`                                              | *Optional[str]*                                               | :heavy_minus_sign:                                            | The name of the validator that was used to validate the item. |