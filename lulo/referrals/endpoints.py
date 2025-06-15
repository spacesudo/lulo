from ..base import BaseClient

class Referrals(BaseClient):
    
    def __init__(self, api_key: str, base_url: str = "https://api.lulofi.com"):
        super().__init__(api_key, base_url)

    def get_referrals(self, params: dict):
        """
        Get a list of referrals.
        
        :param params: Dictionary containing parameters for the request. key should be "owner" with the public key of the account as value.
        
        :return: A JSON response containing the list of referrals.
        """
        return self._get("referral.getReferrer", params=params)