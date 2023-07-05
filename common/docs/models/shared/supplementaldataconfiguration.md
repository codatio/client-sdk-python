# SupplementalDataConfiguration

The client's defined name for the object.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `data_source`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The underlying endpoint of the source system which the configuration is targeting.  |
| `pull_data`                                                                         | dict[str, *str*]                                                                    | :heavy_minus_sign:                                                                  | The additional properties that are required when pulling records.                   |
| `push_data`                                                                         | dict[str, *str*]                                                                    | :heavy_minus_sign:                                                                  | The additional properties that are required to create and/or update records.        |