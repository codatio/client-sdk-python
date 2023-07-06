# UpdateExpenseRequest


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `currency`                                                                    | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Currency the transaction was recorded in.                                     | GBP                                                                           |
| `issue_date`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | Date the transaction was recorded.                                            | 2022-06-28T00:00:00.000Z                                                      |
| `lines`                                                                       | list[[ExpenseTransactionLine](../../models/shared/expensetransactionline.md)] | :heavy_minus_sign:                                                            | Array of transaction lines.                                                   |                                                                               |
| `merchant_name`                                                               | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Name of the merchant where the purchase took place                            | Amazon UK                                                                     |
| `notes`                                                                       | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Any private, company notes about the transaction.                             | APPLE.COM/BILL - 09001077498 - Card Ending: 4590                              |
| `type`                                                                        | *Any*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |                                                                               |