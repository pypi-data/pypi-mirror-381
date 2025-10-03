# Prestmit API Wrapper

A simple Python wrapper for the Prestmit crypto wallet balance API, with support for both synchronous and asynchronous clients. Fetches full balance details, including the complete transaction list.

## Installation

```bash
pip install prestmit
```

## Asynchronous Usage

```python
import asyncio
from prestmit import AsyncWalletClient, AddressNotFoundError

async def main():
    async with AsyncWalletClient() as client:
        try:
            btc_balance = await client.get_balance("btc", "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq")

            print(f"Address: {btc_balance.address}")
            print(f"Final Balance: {btc_balance.balance} BTC")
            print(f"Total Transactions: {btc_balance.n_tx}")

            print("\nRecent Transactions:")
            for tx in btc_balance.transactions[:5]: # Print first 5 transactions
                print(f"  - Hash: {tx.tx_hash[:10]}..., Value: {tx.value}, Confirmations: {tx.confirmations}")

        except AddressNotFoundError as e:
            print(e)

if __name__ == "__main__":
    asyncio.run(main())
```

## Synchronous Usage

```python
from prestmit import SyncWalletClient, AddressNotFoundError

def main():
    with SyncWalletClient() as client:
        try:
            eth_balance = client.get_balance("eth", "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe")
            print(f"ETH Balance: {eth_balance.balance} ETH")
            if eth_balance.transactions:
                print(f"First transaction hash: {eth_balance.transactions[0].tx_hash}")


        except AddressNotFoundError as e:
            print(e)

if __name__ == "__main__":
    main()
```

## Data Objects

A successful call returns a `WalletBalance` object containing a list of `Transaction` objects.

### `WalletBalance` Attributes
- `address` (str)
- `crypto_type` (str)
- `balance` (float)
- `total_received` (float)
- `total_sent` (float)
- `n_tx` (int)
- `transactions` (List[Transaction])

### `Transaction` Attributes
- `tx_hash` (str)
- `block_height` (int)
- `value` (float)
- `ref_balance` (float)
- `confirmations` (int)
- `confirmed_at` (str)
- `double_spend` (bool)
