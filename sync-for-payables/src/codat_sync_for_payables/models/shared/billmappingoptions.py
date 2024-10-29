"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountmappingoption import AccountMappingOption, AccountMappingOptionTypedDict
from .pagination import Pagination, PaginationTypedDict
from .taxratemappingoption import TaxRateMappingOption, TaxRateMappingOptionTypedDict
from codat_sync_for_payables.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BillMappingOptionsTypedDict(TypedDict):
    r"""The bill mapping options for a company's accounting software."""

    accounts: NotRequired[List[AccountMappingOptionTypedDict]]
    tax_rates: NotRequired[List[TaxRateMappingOptionTypedDict]]
    pagination: NotRequired[PaginationTypedDict]


class BillMappingOptions(BaseModel):
    r"""The bill mapping options for a company's accounting software."""

    accounts: Optional[List[AccountMappingOption]] = None

    tax_rates: Annotated[
        Optional[List[TaxRateMappingOption]], pydantic.Field(alias="taxRates")
    ] = None

    pagination: Optional[Pagination] = None
