from __future__ import annotations
from typing import Union, Any
from typing_extensions import TypeAliasType
from codat_lending.models.shared.bankingtransactions import BankingTransactions
from codat_lending.models.shared.bankingaccount import BankingAccount

UploadBankStatementDataRequestBody = TypeAliasType("UploadBankStatementDataRequestBody", Union[BankingTransactions, BankingAccount, Any])
