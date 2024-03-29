from dydx3.constants import API_HOST_SEPOLIA, API_HOST_MAINNET
from decouple import config

# !!!!! SELECT MODE !!!!!
MODE = 'DEVELOPMENT'

# Close all open positions and orders
ABORT_AL_POSITIONS = True

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place Trades
PLACE_TRADES = True

# Manage Exits
MANAGE_EXITS = True

# Resolution
RESOLUTION = '1HOUR'

# Stats Window
WINDOW = 21

# Thresholds
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# Thresholds for closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum Address
ETHEREUM_ADDRESS = "0x35D2a50e268649EdC94D91e64f7d59C59F90006a"

# KEYS - PRODUCTION
# Must be on Mainnet ib DYDX
STARK_PRIVATE_KEY_MAINNET = config('STARK_PRIVATE_KEY_MAINNET')
DYDX_API_KEY_MAINNET = config('DYDX_API_KEY_MAINNET')
DYDX_API_SECRET_MAINNET = config('DYDX_API_SECRET_MAINNET')
DYDX_API_PASSPHRASE_MAINNET = config('DYDX_API_PASSPHRASE_MAINNET')

# KEYS - DEVELOPMENT
# Must be on Testnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config('STARK_PRIVATE_KEY_TESTNET')
DYDX_API_KEY_TESTNET = config('DYDX_API_KEY_TESTNET')
DYDX_API_SECRET_TESTNET = config('DYDX_API_SECRET_TESTNET')
DYDX_API_PASSPHRASE_TESTNET = config('DYDX_API_PASSPHRASE_TESTNET')

# Keys - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == 'PRODUCTION' else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == 'PRODUCTION' else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == 'PRODUCTION' else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == 'PRODUCTION' else DYDX_API_PASSPHRASE_TESTNET

# Host Export
HOST = API_HOST_MAINNET if MODE == 'PRODUCTION' else API_HOST_SEPOLIA

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = 'https://eth-mainnet.g.alchemy.com/v2/KDd3JU9qm_IAeDiNoalXmqS5yKNY2Y4N'
HTTP_PROVIDER_TESTNET = 'https://eth-sepolia.g.alchemy.com/v2/gQKrYsIrcppzTXp6R8crUvbd2yr9l5tv'
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == 'PRODUCTION' else HTTP_PROVIDER_TESTNET
