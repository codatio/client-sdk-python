# BankStatementUploadConfiguration

Configuration settings for uploading banking data to Codat


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `account_id`                                                 | *Optional[str]*                                              | :heavy_minus_sign:                                           | The ID of the account in the third-party platform            |
| `provider_id`                                                | *Optional[str]*                                              | :heavy_minus_sign:                                           | TrueLayer provider ID (only required if source is TrueLayer) |
| `source`                                                     | [Optional[shared.Source]](../../models/shared/source.md)     | :heavy_minus_sign:                                           | The source of the banking data that determines its format    |