# Location

Reference to a configured dynamic key value pair that is unique to the accounting platform. This feature is in private beta, contact us if you would like to learn more.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `address`                                           | [Optional[Address]](../../models/shared/address.md) | :heavy_minus_sign:                                  | N/A                                                 |                                                     |
| `content`                                           | dict[str, dict[str, *Any*]]                         | :heavy_minus_sign:                                  | N/A                                                 |                                                     |
| `id`                                                | *str*                                               | :heavy_check_mark:                                  | A unique, persistent identifier for this record     | 13d946f0-c5d5-42bc-b092-97ece17923ab                |
| `modified_date`                                     | *Optional[str]*                                     | :heavy_minus_sign:                                  | N/A                                                 | 2022-10-23T00:00:00.000Z                            |
| `name`                                              | *Optional[str]*                                     | :heavy_minus_sign:                                  | Name of this location                               |                                                     |
| `source_modified_date`                              | *Optional[str]*                                     | :heavy_minus_sign:                                  | N/A                                                 | 2022-10-23T00:00:00.000Z                            |