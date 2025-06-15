from ..base import BaseClient
from typing import Optional

class Pools(BaseClient):
    
    def __init__(self, api_key: str, base_url: str = "https://api.lulofi.com"):
        super().__init__(api_key, base_url)

    def get_pools(self, params: Optional[dict] = None):
        """
        Get a list of pools.
        
        :param params: (Optional) Dictionary containing parameters for the request. key should be "owner" with the public key of the account as value.
        
        :return: A JSON response containing the list of pools.
        
        """
        return self._get("pool.getPools", params=params)
    
    