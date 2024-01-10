# SyncAsBankFeeds


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `bank_account_options`                                                     | List[[shared.BankAccountOption](../../models/shared/bankaccountoption.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |
| `enable_sync`                                                              | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | True if bank feeds sync is enabled.                                        |
| `selected_bank_account_id`                                                 | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The bank account ID being synced.                                          |