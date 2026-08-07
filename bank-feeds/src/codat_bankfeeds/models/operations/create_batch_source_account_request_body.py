from __future__ import annotations
from typing import Union, List
from typing_extensions import TypeAliasType
from codat_bankfeeds.models.shared.sourceaccountv2prototype import SourceAccountV2Prototype
from codat_bankfeeds.models.shared.sourceaccountprototype import SourceAccountPrototype

CreateBatchSourceAccountRequestBody = TypeAliasType("CreateBatchSourceAccountRequestBody", Union[List[SourceAccountV2Prototype], List[SourceAccountPrototype]])
