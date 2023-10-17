# Sales


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `accounts`                                                        | Dict[str, [ConfigAccount](../../models/shared/configaccount.md)]  | :heavy_minus_sign:                                                | N/A                                                               |
| `grouping`                                                        | [Optional[Grouping]](../../models/shared/grouping.md)             | :heavy_minus_sign:                                                | N/A                                                               |
| `invoice_status`                                                  | [Optional[InvoiceStatus1]](../../models/shared/invoicestatus1.md) | :heavy_minus_sign:                                                | N/A                                                               |
| `new_tax_rates`                                                   | [Optional[NewTaxRates]](../../models/shared/newtaxrates.md)       | :heavy_minus_sign:                                                | N/A                                                               |
| `sales_customer`                                                  | [Optional[Customer]](../../models/shared/customer.md)             | :heavy_minus_sign:                                                | N/A                                                               |
| `sync_sales`                                                      | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | Boolean indicator for syncing sales.                              |
| `tax_rates`                                                       | Dict[str, [TaxRateAmount](../../models/shared/taxrateamount.md)]  | :heavy_minus_sign:                                                | N/A                                                               |