from __future__ import annotations
from typing import Union
from typing_extensions import TypeAliasType
from codat_bankfeeds.models.shared.sourceaccount import SourceAccount
from codat_bankfeeds.models.source_account_v2 import SourceAccountV2

CreateSourceAccountResponseBody = TypeAliasType("CreateSourceAccountResponseBody", Union[SourceAccount, SourceAccountV2])
