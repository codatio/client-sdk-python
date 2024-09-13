# GetSupplementalDataConfigurationRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `data_type`                                                        | [models.PathParamDataType](../models/pathparamdatatype.md)         | :heavy_check_mark:                                                 | Supported supplemental data data type.                             | invoices                                                           |
| `platform_key`                                                     | *str*                                                              | :heavy_check_mark:                                                 | A unique 4-letter key to represent a platform in each integration. | gbol                                                               |