# BillPayments


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `links`                                                        | [shared.Links](../../models/shared/links.md)                   | :heavy_check_mark:                                             | N/A                                                            |
| `page_number`                                                  | *int*                                                          | :heavy_check_mark:                                             | Current page number.                                           |
| `page_size`                                                    | *int*                                                          | :heavy_check_mark:                                             | Number of items to return in results array.                    |
| `results`                                                      | List[[shared.BillPayment](../../models/shared/billpayment.md)] | :heavy_minus_sign:                                             | N/A                                                            |
| `total_results`                                                | *int*                                                          | :heavy_check_mark:                                             | Total number of items.                                         |