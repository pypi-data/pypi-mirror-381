import aiohttp
import requests
from dataclasses import dataclass
from typing import Optional, Literal, List

SUPPORTED_CRYPTOS = {"btc", "ltc", "eth", "doge"}

@dataclass
class Transaction:
    tx_hash: str
    block_height: int
    value: float
    ref_balance: float
    confirmations: int
    confirmed_at: str
    double_spend: bool

@dataclass
class WalletBalance:
    address: str
    crypto_type: str
    balance: float
    total_received: float
    total_sent: float
    n_tx: int
    transactions: List[Transaction]

class WalletError(Exception):
    pass

class InvalidCryptoError(WalletError):
    pass

class AddressNotFoundError(WalletError):
    pass

class BaseWalletClient:
    def _build_url(self, crypto: str, address: str) -> str:
        return f"https://prestmit.io/_next/data/FeCenzv5YKWUfPs6QYH3I/checker/{crypto}/{address}.json?crypto={crypto}&address={address}"

    def _validate_crypto(self, crypto: str):
        if crypto.lower() not in SUPPORTED_CRYPTOS:
            raise InvalidCryptoError(f"Unsupported crypto '{crypto}'. Must be one of {', '.join(SUPPORTED_CRYPTOS)}")

    def _parse_response(self, crypto: str, address: str, data: dict) -> Optional[WalletBalance]:
        transactions_data = data.get("pageProps", {}).get("transactions")

        if transactions_data is None:
            return WalletBalance(
                address=address, crypto_type=crypto,
                balance=0.0, total_received=0.0, total_sent=0.0, n_tx=0, transactions=[]
            )

        tx_list = []
        for tx_ref in transactions_data.get("txrefs", []):
            tx = Transaction(
                tx_hash=tx_ref.get("tx_hash", ""),
                block_height=tx_ref.get("block_height", 0),
                value=float(tx_ref.get("value", 0.0)),
                ref_balance=float(tx_ref.get("ref_balance", 0.0)),
                confirmations=tx_ref.get("confirmations", 0),
                confirmed_at=tx_ref.get("confirmed", ""),
                double_spend=tx_ref.get("double_spend", False)
            )
            tx_list.append(tx)

        return WalletBalance(
            address=transactions_data.get("address", address),
            crypto_type=crypto,
            balance=float(transactions_data.get("final_balance", 0.0)),
            total_received=float(transactions_data.get("total_received", 0.0)),
            total_sent=float(transactions_data.get("total_sent", 0.0)),
            n_tx=int(transactions_data.get("n_tx", 0)),
            transactions=tx_list
        )

class AsyncWalletClient(BaseWalletClient):
    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self._session = session
        self._owns_session = session is None

    async def __aenter__(self):
        if self._owns_session:
            self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._owns_session and self._session:
            await self._session.close()

    async def get_balance(self, crypto: Literal["btc", "ltc", "eth", "doge"], address: str) -> Optional[WalletBalance]:
        crypto = crypto.lower()
        self._validate_crypto(crypto)
        url = self._build_url(crypto, address)
        
        if not self._session:
            raise RuntimeError("Session not started. Use 'async with AsyncWalletClient() as client:'.")

        async with self._session.get(url) as resp:
            if resp.status == 404:
                raise AddressNotFoundError(f"Address '{address}' not found for crypto '{crypto}'. It may have no transaction history.")
            resp.raise_for_status()
            data = await resp.json()
            return self._parse_response(crypto, address, data)

class SyncWalletClient(BaseWalletClient):
    def __init__(self):
        self._session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def get_balance(self, crypto: Literal["btc", "ltc", "eth", "doge"], address: str) -> Optional[WalletBalance]:
        crypto = crypto.lower()
        self._validate_crypto(crypto)
        url = self._build_url(crypto, address)

        resp = self._session.get(url)
        if resp.status_code == 404:
            raise AddressNotFoundError(f"Address '{address}' not found for crypto '{crypto}'. It may have no transaction history.")
        resp.raise_for_status()
        return self._parse_response(crypto, address, resp.json())
