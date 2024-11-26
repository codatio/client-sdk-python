# TransferTransactionRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `date_`                                           | *str*                                             | :heavy_check_mark:                                | N/A                                               | 2022-10-23 00:00:00 +0000 UTC                     |
| `from_`                                           | [shared.From](../../models/shared/from_.md)       | :heavy_check_mark:                                | N/A                                               |                                                   |
| `to`                                              | [shared.To](../../models/shared/to.md)            | :heavy_check_mark:                                | N/A                                               |                                                   |
| `description`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | Any private, company notes about the transaction. | Transfer from bank account Y to bank account Z    |