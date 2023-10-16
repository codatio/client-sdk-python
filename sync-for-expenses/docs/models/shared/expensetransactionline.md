# ExpenseTransactionLine


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `account_ref`                                           | [RecordRef](../../models/shared/recordref.md)           | :heavy_check_mark:                                      | N/A                                                     |                                                         |
| `net_amount`                                            | *Decimal*                                               | :heavy_check_mark:                                      | Amount of the line, exclusive of tax.                   | 110.42                                                  |
| `tax_amount`                                            | *Decimal*                                               | :heavy_check_mark:                                      | Amount of tax for the line.                             | 14.43                                                   |
| `tax_rate_ref`                                          | [Optional[RecordRef]](../../models/shared/recordref.md) | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `tracking_refs`                                         | list[[RecordRef](../../models/shared/recordref.md)]     | :heavy_minus_sign:                                      | N/A                                                     |                                                         |