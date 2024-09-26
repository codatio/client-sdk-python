"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .reportline import ReportLine, ReportLineTypedDict
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BalanceSheetTypedDict(TypedDict):
    net_assets: Decimal
    r"""Value of net assets for a company in their base currency."""
    assets: NotRequired[ReportLineTypedDict]
    date_: NotRequired[str]
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """
    equity: NotRequired[ReportLineTypedDict]
    liabilities: NotRequired[ReportLineTypedDict]


class BalanceSheet(BaseModel):
    net_assets: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="netAssets"),
    ]
    r"""Value of net assets for a company in their base currency."""

    assets: Optional[ReportLine] = None

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```



    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:

    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`

    > Time zones
    >
    > Not all dates from Codat will contain information about time zones.
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """

    equity: Optional[ReportLine] = None

    liabilities: Optional[ReportLine] = None
