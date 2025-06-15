from ..base import BaseClient

class Account(BaseClient):
    
    def __init__(self, api_key: str, base_url: str = "https://api.lulofi.com"):
        super().__init__(api_key, base_url)
    
    def get_account(self, params: dict):
        """
        Get account information.
        
        :param params: Dictionary containing parameters for the request. key should be "owner" with the public key of the account as value.
        
        :return: A JSON response containing account information.
        """
        return self._get("account.getAccount", params=params)
    
    def get_pending_withdrawals(self, params: dict):
        """
        Get pending withdrawals for the account.
        
        :param params: Dictionary containing parameters for the request. key should be "owner" with the public key of the account as value.
        
        :return: A JSON response containing pending withdrawals.
        """
        return self._get("account.withdrawals.listPendingWithdrawals", params=params)