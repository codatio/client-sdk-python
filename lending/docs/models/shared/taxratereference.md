# TaxRateReference

Data types that reference a tax rate, for example invoice and bill line items, use a taxRateRef that includes the ID and name of the linked tax rate.

Found on:

- Bill line items
- Bill Credit Note line items
- Credit Note line items
- Direct incomes line items
- Invoice line items
- Items


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `effective_tax_rate`                                           | *Optional[Decimal]*                                            | :heavy_minus_sign:                                             | Applicable tax rate.                                           |
| `id`                                                           | *Optional[str]*                                                | :heavy_minus_sign:                                             | Unique identifier for the tax rate in the accounting software. |
| `name`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Name of the tax rate in the accounting software.               |