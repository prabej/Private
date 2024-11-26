import requests
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from web3 import Web3

# Function to download the pharsees.txt file from GitHub
def download_seed_file(github_url, save_path):
    response = requests.get(github_url)
    if response.status_code == 200:
        with open(save_path, 'w') as file:
            file.write(response.text)
        print(f"File downloaded and saved as {save_path}")
    else:
        print(f"Failed to download the file from {github_url}. Status code: {response.status_code}")

# Function to load wallet addresses from file
def load_wallet_addresses(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Check USDT balance using Etherscan or BscScan API
def check_usdt_balance(api_url, wallet_address, contract_address, api_key):
    url = f"{api_url}?module=account&action=tokenbalance"
    params = {
        "contractaddress": contract_address,
        "address": wallet_address,
        "tag": "latest",
        "apikey": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['status'] == '1':
        balance = int(data['result']) / (10 ** 6)  # USDT has 6 decimals
        return balance
    return None

# Function to save successful wallet addresses
def save_successful_wallet(wallet_address, eth_balance, bsc_balance):
    with open('successful_pharse_code.txt', 'a') as file:
        file.write(f"Wallet Address: {wallet_address}\n")
        file.write(f"Ethereum USDT: {eth_balance} USDT\n")
        file.write(f"Binance Smart Chain USDT: {bsc_balance} USDT\n")
        file.write("=" * 50 + "\n")

# Main function to check balances
def main():
    # URL of the raw file on GitHub
    github_url = "https://raw.githubusercontent.com/prabej/Private/main/pharsees.txt"
    seed_file = "pharsees.txt"  # Path to save the downloaded file locally

    # Download the pharsees.txt file
    download_seed_file(github_url, seed_file)

    api_key_etherscan = "IBJ6USVRFII3MQRERD5UJTUG9N2AZFPVJU"  # Replace with your Etherscan API key
    api_key_bscscan = "6F5JWC8YNGCMJ86ZX4TAICYGWQAFAG1ZJ6"  # Replace with your BscScan API key

    # API URLs and USDT contract addresses
    api_etherscan = "https://api.etherscan.io/api"
    api_bscscan = "https://api.bscscan.com/api"
    usdt_contract_eth = "0xdac17f958d2ee523a2206206994597c13d831ec7"  # USDT on Ethereum
    usdt_contract_bsc = "0x55d398326f99059fF775485246999027B3197955"  # USDT on BSC

    # Load wallet addresses from the downloaded file
    wallet_addresses = load_wallet_addresses(seed_file)

    # Iterate through the wallet addresses and check balances
    for wallet_address in wallet_addresses:
        print(f"\nChecking balances for wallet: {wallet_address}")
        
        # Check Ethereum USDT balance
        eth_balance = check_usdt_balance(api_etherscan, wallet_address, usdt_contract_eth, api_key_etherscan)
        if eth_balance is not None:
            print(f"USDT on Ethereum: {eth_balance} USDT")
        else:
            print("Failed to fetch USDT balance on Ethereum.")

        # Check BSC USDT balance
        bsc_balance = check_usdt_balance(api_bscscan, wallet_address, usdt_contract_bsc, api_key_bscscan)
        if bsc_balance is not None:
            print(f"USDT on Binance Smart Chain: {bsc_balance} USDT")
        else:
            print("Failed to fetch USDT balance on BSC.")

        # Save successful wallet addresses with balances
        if eth_balance is not None or bsc_balance is not None:
            save_successful_wallet(wallet_address, eth_balance or 0, bsc_balance or 0)

if __name__ == "__main__":
    main()