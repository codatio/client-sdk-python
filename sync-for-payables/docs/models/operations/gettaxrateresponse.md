# GetTaxRateResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `error_message`                                                                       | [Optional[shared.ErrorMessage]](../../models/shared/errormessage.md)                  | :heavy_minus_sign:                                                                    | Your API request was not properly authorized.                                         |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `tax_rate`                                                                            | [Optional[shared.TaxRate]](../../models/shared/taxrate.md)                            | :heavy_minus_sign:                                                                    | Success                                                                               |