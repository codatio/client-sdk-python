# PushFieldValidation


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `details`                                             | *str*                                                 | :heavy_check_mark:                                    | Details on the validation issue.                      |
| `field`                                               | *Optional[str]*                                       | :heavy_minus_sign:                                    | Field name that resulted in the validation issue.     |
| `ref`                                                 | *OptionalNullable[str]*                               | :heavy_minus_sign:                                    | Unique reference identifier for the validation issue. |