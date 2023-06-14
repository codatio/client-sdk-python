# GetCreditNoteResponse


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `credit_note`                                                                                           | [Optional[shared.CreditNote]](../../models/shared/creditnote.md)                                        | :heavy_minus_sign:                                                                                      | Success                                                                                                 |
| `status_code`                                                                                           | *int*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `raw_response`                                                                                          | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                   | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `get_credit_note_409_application_json_object`                                                           | [Optional[GetCreditNote409ApplicationJSON]](../../models/operations/getcreditnote409applicationjson.md) | :heavy_minus_sign:                                                                                      | The data type's dataset has not been requested or is still syncing.                                     |
| `schema`                                                                                                | [Optional[shared.Schema]](../../models/shared/schema.md)                                                | :heavy_minus_sign:                                                                                      | Your API request was not properly authorized.                                                           |