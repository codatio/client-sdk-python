# IntiateSyncResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `codat_error_message`                                                                 | [Optional[shared.CodatErrorMessage]](../../models/shared/codaterrormessage.md)        | :heavy_minus_sign:                                                                    | If model is incorrect                                                                 |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sync_initiated`                                                                      | [Optional[shared.SyncInitiated]](../../models/shared/syncinitiated.md)                | :heavy_minus_sign:                                                                    | Returns the newly created SyncId                                                      |