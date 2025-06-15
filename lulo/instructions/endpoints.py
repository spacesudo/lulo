from ..base import BaseClient
from typing import Optional

class Instructions(BaseClient):
    
    def __init__(self, api_key: str, base_url: str = "https://api.lulofi.com"):
        super().__init__(api_key, base_url)

    def initialize_referrer(self, payload: dict, params: Optional[dict] = None):
        """Initialize a referrer instruction for a new account.

        Args:
            payload (dict): the referrer details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
               
            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the referrer initialization instruction.
        """
        return self._post("generate.instructions.initializeReferrer", payload, params)

    def deposit_instruction(self, payload: dict, params: Optional[dict] = None):
        """Create a deposit instruction.

        Args:
            payload (dict): The instruction details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress : The mint address of the token to be deposited USDC on main net only.
                - regularAmount (optional): regular (boosted) amount to deposit
                - protectedAmount (optional): protected amount to deposit
                - referrer (optional): Optional referrer wallet using the same wallet that was created using initializeReferrer. Referrers are assigned during a new account only (first deposit)

            params (Optional[dict], optional):
                - priorityFee (optional): The priority fee for the transaction in lamports.


        Returns:
            JSON: A JSON response containing the deposit instruction.
        """
        
        return self._post("generate.instructions.deposit", payload, params)

    def withdraw_protected(self, payload: dict, params: Optional[dict] = None):

        """Create a withdraw protected instruction.

        Args:
            payload (dict): The instruction details:

                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress: The mint address of the token to be withdrawn USDC on main net only.
                - amount: Amount to withdraw

            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the withdraw protected instruction.
        """
        
        return self._post("generate.instructions.withdrawProtected", payload, params)

    def initiate_regular_withdraw(self, payload: dict, params: Optional[dict] = None):
        """Initiate a regular withdrawal instruction.
        This endpoint is used to initiate a regular withdrawal instruction.

        Args:
            payload (dict): The instruction details:
                - owner: Owner of the lulo account.
                - feePayer (optional): The public key of account that will pay the transaction fee.
                - mintAddress: The mint address of the token to be withdrawn. USDC on main net only.
                - amount: Amount to withdraw

            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the regular withdrawal initiation instruction.
        """
        
        return self._post("generate.instructions.initiateRegularWithdraw", payload, params)

    def complete_regular_withdrawal(self, payload: dict, params: Optional[dict] = None):
        """Complete a regular withdrawal instruction.

        Args:
            payload (dict): The instruction details:
                - owner: Owner of the lulo account.
                - pendingWithdrawalId: The ID of the pending withdrawal to complete.
                - feePayer (optional): The public key of account that will pay the transaction fee.
            params (Optional[dict], optional): 
                - priorityFee (optional): The priority fee for the transaction in lamports.

        Returns:
            JSON: A JSON response containing the regular withdrawal completion instruction.

        """
        return self._post("generate.instructions.completeRegularWithdrawal", payload, params)