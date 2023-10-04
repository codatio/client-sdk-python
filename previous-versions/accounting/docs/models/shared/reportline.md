# ReportLine


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `account_id`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Identifier for the account, unique for the company in the accounting platform. |
| `items`                                                                        | list[[shared.ReportLine](undefined/models/shared/reportline.md)]               | :heavy_minus_sign:                                                             | An array of ReportLine items.                                                  |
| `name`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Name of the report line item.                                                  |
| `value`                                                                        | *Optional[Decimal]*                                                            | :heavy_check_mark:                                                             | Numerical value of the line item.                                              |