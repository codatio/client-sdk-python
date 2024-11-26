# Address


## Fields

| Field                                                                                                                                                   | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                                                                  | [Optional[shared.AddressType]](../../models/shared/addresstype.md)                                                                                      | :heavy_minus_sign:                                                                                                                                      | The type of the address                                                                                                                                 |
| `line1`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Line 1 of the customer address.                                                                                                                         |
| `line2`                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Line 2 of the customer address.                                                                                                                         |
| `city`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | City of the customer address.                                                                                                                           |
| `region`                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Region of the customer address.                                                                                                                         |
| `country`                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Country of the customer's address. For NetSuite, use the 2-digit [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country code. |
| `postal_code`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                      | Postal code or zip code.                                                                                                                                |