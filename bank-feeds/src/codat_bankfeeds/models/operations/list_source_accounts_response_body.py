from __future__ import annotations
from typing import Union, List
from typing_extensions import TypeAliasType
from codat_bankfeeds.models.source_account_v2 import SourceAccountV2
from codat_bankfeeds.models.shared.sourceaccount import SourceAccount

ListSourceAccountsResponseBody = TypeAliasType("ListSourceAccountsResponseBody", Union[List[SourceAccountV2], List[SourceAccount]])
