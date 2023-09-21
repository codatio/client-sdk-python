# CreateDirectCostRequest


## Fields

| Field                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accounting_direct_cost`                                                                                                                                                                                                                                                                                                      | [Optional[shared.AccountingDirectCost]](../../models/shared/accountingdirectcost.md)                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
| `allow_sync_on_push_complete`                                                                                                                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |
| `company_id`                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                           | 8a210b68-6988-11ed-a1eb-0242ac120002                                                                                                                                                                                                                                                                                          |
| `connection_id`                                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                           | 2e9d2c44-f675-40ba-8049-353bfcb5e171                                                                                                                                                                                                                                                                                          |
| `force_update`                                                                                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                            | When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check. |                                                                                                                                                                                                                                                                                                                               |
| `timeout_in_minutes`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                               |