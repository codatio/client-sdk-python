# ListAccountingBillPaymentsResponse


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `accounting_bill_payments`                                                               | [Optional[shared.AccountingBillPayments]](../../models/shared/accountingbillpayments.md) | :heavy_minus_sign:                                                                       | Success                                                                                  |
| `content_type`                                                                           | *str*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `error_message`                                                                          | [Optional[shared.ErrorMessage]](../../models/shared/errormessage.md)                     | :heavy_minus_sign:                                                                       | Your `query` parameter was not correctly formed                                          |
| `status_code`                                                                            | *int*                                                                                    | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `raw_response`                                                                           | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)    | :heavy_minus_sign:                                                                       | N/A                                                                                      |