# ListFilesResponse


## Fields

| Field                                                                                                                                                      | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                                                             | *str*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | N/A                                                                                                                                                        |
| `files`                                                                                                                                                    | list[[shared.File](../../models/shared/file.md)]                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Success                                                                                                                                                    |
| `status_code`                                                                                                                                              | *int*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                         | N/A                                                                                                                                                        |
| `raw_response`                                                                                                                                             | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                                                      | :heavy_minus_sign:                                                                                                                                         | N/A                                                                                                                                                        |
| `list_files_404_application_json_object`                                                                                                                   | [Optional[ListFiles404ApplicationJSON]](../../models/operations/listfiles404applicationjson.md)                                                            | :heavy_minus_sign:                                                                                                                                         | One or more of the resources you referenced could not be found.<br/>This might be because your company or data connection id is wrong, or was already deleted. |
| `schema`                                                                                                                                                   | [Optional[shared.Schema]](../../models/shared/schema.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                         | Your API request was not properly authorized.                                                                                                              |