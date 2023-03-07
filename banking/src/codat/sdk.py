__doc__ = """ SDK Documentation: Codat's Banking API allows you to access standardised data from over bank accounts via third party providers.

Standardize how you connect to your customers’ bank accounts. Retrieve bank account and bank transaction data in the same way via our partnerships with Plaid and TrueLayer.

[Read more...](https://docs.codat.io/banking-api/overview)

[See our OpenAPI spec](https://github.com/codatio/oas) """
import requests as requests_http
from . import utils
from .account_balances import AccountBalances
from .accounts import Accounts
from .transaction_categories import TransactionCategories
from .transactions import Transactions
from codat.models import shared

SERVERS = [
	"https://api.codat.io",
]

class Codat:
    r"""SDK Documentation: Codat's Banking API allows you to access standardised data from over bank accounts via third party providers.
    
    Standardize how you connect to your customers’ bank accounts. Retrieve bank account and bank transaction data in the same way via our partnerships with Plaid and TrueLayer.
    
    [Read more...](https://docs.codat.io/banking-api/overview)
    
    [See our OpenAPI spec](https://github.com/codatio/oas) """
    account_balances: AccountBalances
    accounts: Accounts
    transaction_categories: TransactionCategories
    transactions: Transactions
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.2.2"
    _gen_version: str = "1.8.5"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.account_balances = AccountBalances(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.accounts = Accounts(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transaction_categories = TransactionCategories(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.transactions = Transactions(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    