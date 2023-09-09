from web3 import Web3

from dotenv import dotenv_values

env_values = dotenv_values()
INFURA_API_KEY = env_values["INFURA_API_KEY"]
WALLET_ADDRESS = env_values["WALLET_ADDRESS"]
# Fill in your infura API key here
infura_url = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# get latest block number
print(web3.eth.block_number)

# get latest block
print(web3.eth.get_block('latest'))

# get latest 10 blocks
latest = web3.eth.block_number
for i in range(0, 10):
  print(web3.eth.get_block(latest - i))

# get transaction from specific block
hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
print(web3.eth.get_transaction_by_block(hash, 2))