# ListBillPaymentsResponse


## Fields

| Field                                                                                                         | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `bill_payments`                                                                                               | [Optional[shared.BillPayments]](../../models/shared/billpayments.md)                                          | :heavy_minus_sign:                                                                                            | Success                                                                                                       |
| `content_type`                                                                                                | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `status_code`                                                                                                 | *int*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `raw_response`                                                                                                | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                         | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `list_bill_payments_409_application_json_object`                                                              | [Optional[ListBillPayments409ApplicationJSON]](../../models/operations/listbillpayments409applicationjson.md) | :heavy_minus_sign:                                                                                            | The data type's dataset has not been requested or is still syncing.                                           |
| `schema`                                                                                                      | [Optional[shared.Schema]](../../models/shared/schema.md)                                                      | :heavy_minus_sign:                                                                                            | Your `query` parameter was not correctly formed                                                               |