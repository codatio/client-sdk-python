# CustomDataTypeRecords

Resulting records pulled from the source platform for a specific custom data type.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `page_number`                                                                    | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | Current page number.                                                             |
| `page_size`                                                                      | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | Number of items to return in results array.                                      |
| `results`                                                                        | List[[shared.CustomDataTypeRecord](../../models/shared/customdatatyperecord.md)] | :heavy_minus_sign:                                                               | N/A                                                                              |
| `total_results`                                                                  | *Optional[int]*                                                                  | :heavy_minus_sign:                                                               | Total number of items.                                                           |