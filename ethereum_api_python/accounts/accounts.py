from web3 import Web3
from dotenv import dotenv_values

env_values = dotenv_values()
INFURA_API_KEY = env_values["INFURA_API_KEY"]
WALLET_ADDRESS = env_values["WALLET_ADDRESS"]
# Fill in your infura API key here
infura_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.is_connected())

print(web3.eth.block_number)

# Fill in your account here
balance = web3.eth.get_balance(WALLET_ADDRESS)
print(web3.from_wei(balance, "ether"))