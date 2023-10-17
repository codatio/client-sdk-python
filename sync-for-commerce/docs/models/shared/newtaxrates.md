# NewTaxRates


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `accounting_tax_rate_options`                                 | List[[Option](../../models/shared/option.md)]                 | :heavy_minus_sign:                                            | Array of accounting tax rate options.                         |
| `commerce_tax_rate_options`                                   | List[[Option](../../models/shared/option.md)]                 | :heavy_minus_sign:                                            | Array of tax component options.                               |
| `default_zero_tax_rate_options`                               | List[[Option](../../models/shared/option.md)]                 | :heavy_minus_sign:                                            | Default zero tax rate selected for sync.                      |
| `selected_default_zero_tax_rate_id`                           | *Optional[str]*                                               | :heavy_minus_sign:                                            | Default tax rate selected for sync.                           |
| `tax_rate_mappings`                                           | List[[TaxRateMapping](../../models/shared/taxratemapping.md)] | :heavy_minus_sign:                                            | Array of tax component to rate mapppings.                     |