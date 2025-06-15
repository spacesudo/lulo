import json
from lulo import LuloClient
from dotenv import load_dotenv
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction
from solders import message
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Processed
from base64 import b64decode, b64encode
import os

load_dotenv()

api_key = os.getenv("API_KEY")

client = LuloClient(api_key=api_key)

rates = client.rates.get_rates()

pools = client.pools.get_pools()

print("Pools:", pools)

print("Rates:", rates)

# Example of creating a deposit transaction

signer = Keypair.from_base58_string("YOUR_PRIVATE_KEY_HERE") # Replace with your actual private key

payload = {
    "owner" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "feePayer" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "mintAddress" : "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", #USDC only supported
    "regularAmount" : 10,
} #will add a pydantic model for this later

params = {
    "priorityFee" : "5000", #in lamports
}

lulo_tx = client.transactions.deposit_transaction(
    payload=payload,
    params=params
)

print("Lulo Transaction:", lulo_tx)


# Create a Solana transaction

sol_client = Client("https://api.mainnet-beta.solana.com")

serialized_tx = lulo_tx['transaction'] #Serialized transaction

tx_bytes = b64decode(serialized_tx)

# sign and send the transaction

raw_transaction = VersionedTransaction.from_bytes(tx_bytes)

signature = signer.sign_message(message.to_bytes_versioned(raw_transaction.message))

signed_tx = VersionedTransaction.populate(raw_transaction.message, [signature])

opts = TxOpts(
    skip_preflight=False,
    preflight_commitment=Processed,
)
result = sol_client.send_raw_transaction(txn = bytes(signed_tx), opts=opts)
result_ = json.loads(result.to_json())
print("Transaction Signature:", result_['result'])
# Check transaction status
tx_status = sol_client.get_signature_status(result_['result'])
print("Transaction Status:", tx_status['result']['confirmationStatus']) 

""" this is a simple example of how to use the Lulo API to create a deposit transaction and send it to the Solana network.

You can edit this example to work with other endpoints like withdrawals, referrals, etc.

"""

# initiating a regular withdrawal transaction

payload = {
    "owner" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "feePayer" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "mintAddress" : "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", #USDC only supported
    "amount" : 10,
}

withdraw_tx = client.transactions.initiate_regular_withdraw(
    payload=payload,
    params=params
)

print("Withdraw Transaction:", withdraw_tx)

sol_client = Client("https://api.mainnet-beta.solana.com")

serialized_tx = withdraw_tx['transaction'] #Serialized transaction

tx_bytes = b64decode(serialized_tx)

# sign and send the transaction

raw_transaction = VersionedTransaction.from_bytes(tx_bytes)

signature = signer.sign_message(message.to_bytes_versioned(raw_transaction.message))

signed_tx = VersionedTransaction.populate(raw_transaction.message, [signature])

opts = TxOpts(
    skip_preflight=False,
    preflight_commitment=Processed,
)
result = sol_client.send_raw_transaction(txn = bytes(signed_tx), opts=opts)
result_ = json.loads(result.to_json())
print("Transaction Signature:", result_['result'])
# Check transaction status
tx_status = sol_client.get_signature_status(result_['result'])
print("Transaction Status:", tx_status['result']['confirmationStatus'])

# Get pending withdrawals for an account

account = client.account.get_pending_withdrawals(
    {"owner" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ"}
)

print("Pending Withdrawals:", account)

payload = {
    "owner" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "feePayer" : "6GEXA97VANiy4pSKgDXkoniuty8v91bVYuzRwZmzFPrQ",
    "pendingWithdrawalId" : 1
}


withdraw_completed = client.transactions.complete_regular_withdrawal(payload, params)

print("Completed Withdrawal Transaction:", withdraw_completed)

sol_client = Client("https://api.mainnet-beta.solana.com")

serialized_tx = withdraw_completed['transaction'] #Serialized transaction

tx_bytes = b64decode(serialized_tx)

# sign and send the transaction

raw_transaction = VersionedTransaction.from_bytes(tx_bytes)

signature = signer.sign_message(message.to_bytes_versioned(raw_transaction.message))

signed_tx = VersionedTransaction.populate(raw_transaction.message, [signature])

opts = TxOpts(
    skip_preflight=False,
    preflight_commitment=Processed,
)
result = sol_client.send_raw_transaction(txn = bytes(signed_tx), opts=opts)
result_ = json.loads(result.to_json())
print("Transaction Signature:", result_['result'])