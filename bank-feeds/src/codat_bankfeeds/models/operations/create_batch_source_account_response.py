from __future__ import annotations
from typing import Union, List
from typing_extensions import TypeAliasType
from codat_bankfeeds.models.operations.response_body import ResponseBody
from codat_bankfeeds.models.operations.create_batch_source_account_response_body import CreateBatchSourceAccountResponseBody

CreateBatchSourceAccountResponse = TypeAliasType("CreateBatchSourceAccountResponse", Union[List[ResponseBody], List[CreateBatchSourceAccountResponseBody]])
