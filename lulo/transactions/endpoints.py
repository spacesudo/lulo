from ..base import BaseClient
from typing import Optional

class Transactions(BaseClient):
    
    def __init__(self, api_key: str, base_url: str = "https://api.lulofi.com"):
        super().__init__(api_key, base_url)

    def deposit_transaction(self, payload: dict, params: Optional[dict] = None):
        """Create a deposit transaction.

        Args:
            payload (dict): The transaction details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress : The mint address of the token to be deposited USDC on main net only.
                - regularAmount (optional): regular (boosted) amount to deposit
                - protectedAmount (optional): protected amount to deposit
                - referrer (optional): Optional referrer wallet using the same wallet that was created using initializeReferrer. Referrers are assigned during a new account only (first deposit)

            params (Optional[dict], optional):
                - priorityFee (optional): The priority fee for the transaction in lamports.
                

        Returns:
            JSON: A JSON response containing the deposit serialized transaction.
        """
        return self._post("generate.transactions.deposit", payload, params)

    def initialize_referrer(self, payload: dict, params: Optional[dict] = None):
        """Initialize a referrer for a new account.

        Args:
            payload (dict): the referrer details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.

            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the referrer initialization serialized transaction.
        """
        return self._post("generate.transaction.initializeReferrer", payload, params)

    def withdraw_protected(self, payload: dict, params: Optional[dict] = None):
        """Create a withdraw protected transaction.

        Args:
            payload (dict): The transaction details:
            
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress: The mint address of the token to be withdrawn USDC on main net only.
                - amount: Amount to withdraw

            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the withdraw protected serialized transaction.
        """
        return self._post("generate.transactions.withdrawProtected", payload, params)

    def initiate_regular_withdraw(self, payload: dict, params: Optional[dict] = None):
        """Initiate a regular withdrawal transaction.
        This endpoint is used to initiate a regular withdrawal transaction, which can be completed later using the `complete_regular_withdrawal` function.

        Args:
            payload (dict): The transaction details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress: The mint address of the token to be withdrawn. USDC on main net only.
                - amount: Amount to withdraw
            
            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the regular withdrawal initiation serialized transaction.
        """
        
        return self._post("generate.transactions.initiateRegularWithdraw", payload, params)

    def complete_regular_withdrawal(self, payload: dict, params: Optional[dict] = None):
        """Complete a regular withdrawal transaction.

        Args:
            payload (dict): The transaction details:
                - owner: Owner of the lulo account.
                - pendingWithdrawalId: The ID of the pending withdrawal to complete.
                - feePayer (optional): The public key of account that will pay the transaction fee.
            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the regular withdrawal completion serialized transaction.

        """
        return self._post("generate.transactions.completeRegularWithdrawal", payload, params)
