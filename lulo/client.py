from .transactions.endpoints import Transactions
from .referrals.endpoints import Referrals
from .account.endpoints import Account
from .pool.endpoints import Pools
from .instructions.endpoints import Instructions
from .rates.endpoints import Rates


class LuloClient:
    def __init__(self, api_key: str, base_url: str = "https://api.lulo.fi/v1"):
        self.transactions = Transactions(api_key, base_url)
        self.referrals = Referrals(api_key, base_url)
        self.account = Account(api_key, base_url)
        self.pools = Pools(api_key, base_url)
        self.instructions = Instructions(api_key, base_url)
        self.rates = Rates(api_key, base_url)
        
    def __repr__(self):
        return f"LuloClient(api_key={self.api_key}, base_url={self.base_url})"
    
    def __str__(self):
        return f"LuloClient with API Key: {self.api_key} and Base URL: {self.base_url}"
    
    def __del__(self):
        #reminder!!!
        pass
    
