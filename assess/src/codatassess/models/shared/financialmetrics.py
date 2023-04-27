"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import financialmetric as shared_financialmetric
from ..shared import financialmetricerror as shared_financialmetricerror
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class FinancialMetricsPeriodUnitEnum(str, Enum):
    MONTH = 'Month'
    WEEK = 'Week'
    DAY = 'Day'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FinancialMetrics:
    r"""OK"""
    
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})

    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.
    
    ## Unknown currencies
    
    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 
    
    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    errors: Optional[list[shared_financialmetricerror.FinancialMetricError]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})

    r"""If there are no errors, an empty array is returned."""
    metrics: Optional[list[shared_financialmetric.FinancialMetric]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics'), 'exclude': lambda f: f is None }})

    period_unit: Optional[FinancialMetricsPeriodUnitEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('periodUnit'), 'exclude': lambda f: f is None }})

    