"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .agedcreditor import AgedCreditor
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingAgedCreditorReport:
    r"""The Aged Creditors report shows the total balance owed by a business to its suppliers over time.

    You can generate it for a company based on recently synced data from your customers' accounting platforms. The report is available in the **Reports** tab in the Codat portal.

    Total assets or liabilities are grouped into 30-day periods for each supplier, up to the current date. You can adjust the report date, period length, and number of periods to show on each report. The data can be grouped by customer or currency.

    > It is not guaranteed that write-offs are included in the Aged Creditors report.

    ## Underlying data

    The Aged Creditors report is generated from a set of required data types: [Suppliers](https://docs.codat.io/lending-api#/schemas/Supplier), [Bills](https://docs.codat.io/lending-api#/schemas/Bill), [Bill credit notes](https://docs.codat.io/lending-api#/schemas/BillCreditNote), and [Bill payments](https://docs.codat.io/lending-api#/schemas/BillPayment).

    To generate the report, the underlying data types must have been synced within 24 hours of each other. Otherwise an error is displayed when you try to run the report. Sync the required data types by clicking the link in the error, and then run the report again.

    > The Aged Creditor report runs based on the **issue dates** of the underlying data types rather than the due date.

    ## Accessing the Aged Creditors report in Portal

    Apart from returning the report via the API as JSON and query, you can also return the Aged Creditors report in the Codat portal.

    1. In the navigation bar, click **Companies**.
    2. Click the name of the company you want to generate the report for. The company's data page is displayed.
    3. Click the **Accounting** tab then click **Reports**.
    4. Select **Aged Creditors**.
    5. _(Optional)_ Edit the default reporting parameters.
       a. You can change the report date in the **Date** box. By default, the report includes transactions that occurred up to, but not including, today's date. To include transactions for today, enter tomorrow's date. 
       b. In the **Period Length Days** box, select the default period length for each column (the default is 30 days).
       b. In the **Number of Periods** box, enter the number of periods to show as columns in the report (the default is 4 periods).
    6. To run the report, click **Load aged creditors**.
    7. The report is generated and displayed at the bottom of the page.

    The report will be grouped per supplier and depending on the periods requested. The details indicates whether the amounts owed come from outstanding bills or bill credit notes.
    """
    data: Optional[List[AgedCreditor]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""Array of aged creditor."""
    generated: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generated'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    report_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportDate'), 'exclude': lambda f: f is None }})
    r"""In Codat's data model, dates and times are represented using the <a class=\\"external\\" href=\\"https://en.wikipedia.org/wiki/ISO_8601\\" target=\\"_blank\\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:

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
    

