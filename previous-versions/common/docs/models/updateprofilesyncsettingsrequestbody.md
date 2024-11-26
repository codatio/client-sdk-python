# UpdateProfileSyncSettingsRequestBody

Include a `syncSetting` object for each data type.
`syncFromWindow`, `syncFromUTC` & `monthsToSync` only need to be included if you wish to set a value for them.


## Fields

| Field                                                                                                                       | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                 | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Unique identifier for your client in Codat.                                                                                 |
| `settings`                                                                                                                  | List[[models.SyncSetting](../models/syncsetting.md)]                                                                        | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `overrides_defaults`                                                                                                        | *Optional[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                          | Set to `True` if you want to override default [sync settings](https://docs.codat.io/knowledge-base/advanced-sync-settings). |