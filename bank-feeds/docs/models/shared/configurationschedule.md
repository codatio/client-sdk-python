# ConfigurationSchedule


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `frequency_options`                                       | List[*str*]                                               | :heavy_minus_sign:                                        | The available sync frequencies.                           |
| `selected_frequency`                                      | *Optional[str]*                                           | :heavy_minus_sign:                                        | The sync frequency.                                       |
| `start_date`                                              | *Optional[str]*                                           | :heavy_minus_sign:                                        | The datetime in UTC you want to start syncing from.       |
| `sync_hour_utc`                                           | *Optional[int]*                                           | :heavy_minus_sign:                                        | The hour in which the sync is initiated.                  |
| `time_zone_iana_id`                                       | *Optional[str]*                                           | :heavy_minus_sign:                                        | The [IANA](https://www.iana.org/time-zones) time zone ID. |