from __future__ import annotations

from enum import Enum


class CompanyInformationSchemasType(str, Enum):
    """Compat name for CompanyInformationType (matched by value set)."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'
