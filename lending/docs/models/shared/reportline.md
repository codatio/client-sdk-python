# ReportLine


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `value`                                                                        | *Decimal*                                                                      | :heavy_check_mark:                                                             | Numerical value of the line item.                                              |
| `account_id`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Identifier for the account, unique for the company in the accounting platform. |
| `items`                                                                        | List[[shared.ReportLine](../../models/shared/reportline.md)]                   | :heavy_minus_sign:                                                             | An array of ReportLine items.                                                  |
| `name`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Name of the report line item.                                                  |