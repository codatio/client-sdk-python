from __future__ import annotations
from typing import Union, List
from typing_extensions import TypeAliasType
from codat_bankfeeds.models.source_account_v2 import SourceAccountV2TypedDict
from codat_bankfeeds.models.shared.sourceaccount import SourceAccountTypedDict

ListSourceAccountsResponseBodyTypedDict = TypeAliasType("ListSourceAccountsResponseBodyTypedDict", Union[List[SourceAccountV2TypedDict], List[SourceAccountTypedDict]])
