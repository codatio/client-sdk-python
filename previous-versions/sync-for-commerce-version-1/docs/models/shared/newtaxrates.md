# NewTaxRates


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `accounting_tax_rate_options`                                            | list[[shared.Option](undefined/models/shared/option.md)]                 | :heavy_minus_sign:                                                       | Array of accounting tax rate options.                                    |
| `commerce_tax_rate_options`                                              | list[[shared.Option](undefined/models/shared/option.md)]                 | :heavy_minus_sign:                                                       | Array of tax component options.                                          |
| `default_zero_tax_rate_options`                                          | list[[shared.Option](undefined/models/shared/option.md)]                 | :heavy_minus_sign:                                                       | Default zero tax rate selected for sync.                                 |
| `selected_default_zero_tax_rate_id`                                      | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Default tax rate selected for sync.                                      |
| `tax_rate_mappings`                                                      | list[[shared.TaxRateMapping](undefined/models/shared/taxratemapping.md)] | :heavy_minus_sign:                                                       | Array of tax component to rate mapppings.                                |