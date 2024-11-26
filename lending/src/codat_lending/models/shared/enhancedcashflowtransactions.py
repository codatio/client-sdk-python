"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .datasource import DataSource, DataSourceTypedDict
from .enhancedcashflowitem import EnhancedCashFlowItem, EnhancedCashFlowItemTypedDict
from .reportinfo import ReportInfo, ReportInfoTypedDict
from codat_lending.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EnhancedCashFlowTransactionsTypedDict(TypedDict):
    r"""> **Categorization engine**
    >
    > The categorization engine uses machine learning and has been fully trained against Plaid and TrueLayer banking data sources. It is not fully trained against the Basiq banking data source.

    The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.
    """

    data_sources: NotRequired[List[DataSourceTypedDict]]
    report_info: NotRequired[ReportInfoTypedDict]
    r"""Report additional information, which is specific to Lending API reports."""
    report_items: NotRequired[List[EnhancedCashFlowItemTypedDict]]


class EnhancedCashFlowTransactions(BaseModel):
    r"""> **Categorization engine**
    >
    > The categorization engine uses machine learning and has been fully trained against Plaid and TrueLayer banking data sources. It is not fully trained against the Basiq banking data source.

    The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.
    """

    data_sources: Annotated[
        Optional[List[DataSource]], pydantic.Field(alias="dataSources")
    ] = None

    report_info: Annotated[Optional[ReportInfo], pydantic.Field(alias="reportInfo")] = (
        None
    )
    r"""Report additional information, which is specific to Lending API reports."""

    report_items: Annotated[
        Optional[List[EnhancedCashFlowItem]], pydantic.Field(alias="reportItems")
    ] = None