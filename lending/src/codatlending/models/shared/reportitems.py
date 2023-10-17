"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import definitionsitemref as shared_definitionsitemref
from ..shared import loanref as shared_loanref
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from enum import Enum
from typing import Optional

class ReportItemsLoanTransactionType(str, Enum):
    r"""The type of loan transaction."""
    INVESTMENT = 'Investment'
    REPAYMENT = 'Repayment'
    INTEREST = 'Interest'
    ACCURED_INTEREST = 'AccuredInterest'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportItems:
    amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""The loan transaction amount."""
    date_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
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
    item_ref: Optional[shared_definitionsitemref.DefinitionsitemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    lender_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lenderName'), 'exclude': lambda f: f is None }})
    r"""The name of lender providing the loan."""
    loan_ref: Optional[shared_loanref.LoanRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loanRef'), 'exclude': lambda f: f is None }})
    loan_transaction_type: Optional[ReportItemsLoanTransactionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('loanTransactionType'), 'exclude': lambda f: f is None }})
    r"""The type of loan transaction."""
    

