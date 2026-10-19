from __future__ import annotations

from enum import Enum


class PeriodUnit(str, Enum):
    """Shared OAS parameter enum (lifted from components/parameters/periodUnit)."""
    DAY = 'Day'
    WEEK = 'Week'
    MONTH = 'Month'
    YEAR = 'Year'
