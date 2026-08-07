from __future__ import annotations

from enum import Enum


class CompanyInformationSchemasType(str, Enum):
    """Speakeasy-name compat for CompanyInformationType (matched by value set)."""
    WEBSITE = 'Website'
    SOCIAL = 'Social'
    UNKNOWN = 'Unknown'
