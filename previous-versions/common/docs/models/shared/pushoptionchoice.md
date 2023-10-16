# PushOptionChoice


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `description`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | A description of the property.                                    |
| `display_name`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The property's display name.                                      |
| `required`                                                        | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | The property is required if `True`.                               |
| `type`                                                            | [Optional[PushOptionType]](../../models/shared/pushoptiontype.md) | :heavy_minus_sign:                                                | The option type.                                                  |
| `value`                                                           | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Allowed value for field.                                          |