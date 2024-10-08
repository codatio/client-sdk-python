# BankFeedAccountMappingResponse

The result from POSTing a Bank Account mapping.


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `error`                                | *OptionalNullable[str]*                | :heavy_minus_sign:                     | Error returned during the post request |
| `status`                               | *OptionalNullable[str]*                | :heavy_minus_sign:                     | Status of the POST request.            |
| `source_account_id`                    | *Optional[str]*                        | :heavy_minus_sign:                     | Unique ID for the source account.      |
| `target_account_id`                    | *OptionalNullable[str]*                | :heavy_minus_sign:                     | Unique ID for the target account.      |