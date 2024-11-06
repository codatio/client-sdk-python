"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cashflowstatement import CashFlowStatement, CashFlowStatementTypedDict
from .reportbasis import ReportBasis
from .reportinput import ReportInput
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountingCashFlowStatementTypedDict(TypedDict):
    r"""> **Operating activities only**
    >
    > Currently, the cash flow statement shows cash that flows into and out of the company from operating activities *only*. Operating activities generate cash from the sale of goods or services.

    ## Overview

    A cash flow statement is a financial report that records all cash that is received or spent by a company during a given period. It gives you a clearer picture of the company’s performance, and their ability to pay creditors and finance growth.

    > **Cash flow statement or balance sheet?**
    >
    > Look at the cash flow statement to understand a company's ability to pay its bills. Although the balance sheet may show healthy earnings at a specific point in time, the cash flow statement allows you to see whether the company is meeting its financial commitments, such as paying creditors or its employees.
    """

    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    report_basis: ReportBasis
    r"""Accounting method used when aggregating the report data. In this case, `Cash`."""
    report_input: ReportInput
    r"""Accounting method used to prepare the cash flow statement."""
    reports: List[CashFlowStatementTypedDict]
    r"""Array of cash flow statements."""
    earliest_available_month: NotRequired[str]
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
    most_recent_available_month: NotRequired[str]
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


class AccountingCashFlowStatement(BaseModel):
    r"""> **Operating activities only**
    >
    > Currently, the cash flow statement shows cash that flows into and out of the company from operating activities *only*. Operating activities generate cash from the sale of goods or services.

    ## Overview

    A cash flow statement is a financial report that records all cash that is received or spent by a company during a given period. It gives you a clearer picture of the company’s performance, and their ability to pay creditors and finance growth.

    > **Cash flow statement or balance sheet?**
    >
    > Look at the cash flow statement to understand a company's ability to pay its bills. Although the balance sheet may show healthy earnings at a specific point in time, the cash flow statement allows you to see whether the company is meeting its financial commitments, such as paying creditors or its employees.
    """

    currency: str
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    report_basis: Annotated[ReportBasis, pydantic.Field(alias="reportBasis")]
    r"""Accounting method used when aggregating the report data. In this case, `Cash`."""

    report_input: Annotated[ReportInput, pydantic.Field(alias="reportInput")]
    r"""Accounting method used to prepare the cash flow statement."""

    reports: List[CashFlowStatement]
    r"""Array of cash flow statements."""

    earliest_available_month: Annotated[
        Optional[str], pydantic.Field(alias="earliestAvailableMonth")
    ] = None
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

    most_recent_available_month: Annotated[
        Optional[str], pydantic.Field(alias="mostRecentAvailableMonth")
    ] = None
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
