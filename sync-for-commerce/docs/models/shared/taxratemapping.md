# TaxRateMapping


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `selected_accounting_tax_rate_id`                                                   | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | Selected tax rate id from the list of tax rates on the accounting software.         |
| `selected_commerce_tax_rate_ids`                                                    | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | Selected tax component id from the list of tax components on the commerce software. |