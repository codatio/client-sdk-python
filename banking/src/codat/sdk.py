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
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.5.1"
    _gen_version: str = "1.12.1"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
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
        
    