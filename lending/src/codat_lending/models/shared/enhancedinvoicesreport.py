"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .enhancedinvoicereportitem import (
    EnhancedInvoiceReportItem,
    EnhancedInvoiceReportItemTypedDict,
)
from .reportinfo import ReportInfo, ReportInfoTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class EnhancedInvoicesReportTypedDict(TypedDict):
    r"""The enhanced invoices report takes the key elements of the Invoices report verifying those marked as paid in the accounting software have actually been paid by matching with the bank statement."""

    report_info: NotRequired[ReportInfoTypedDict]
    r"""Report additional information, which is specific to Lending API reports."""
    report_items: NotRequired[List[EnhancedInvoiceReportItemTypedDict]]


class EnhancedInvoicesReport(BaseModel):
    r"""The enhanced invoices report takes the key elements of the Invoices report verifying those marked as paid in the accounting software have actually been paid by matching with the bank statement."""

    report_info: Annotated[Optional[ReportInfo], pydantic.Field(alias="reportInfo")] = (
        None
    )
    r"""Report additional information, which is specific to Lending API reports."""

    report_items: Annotated[
        Optional[List[EnhancedInvoiceReportItem]], pydantic.Field(alias="reportItems")
    ] = None
