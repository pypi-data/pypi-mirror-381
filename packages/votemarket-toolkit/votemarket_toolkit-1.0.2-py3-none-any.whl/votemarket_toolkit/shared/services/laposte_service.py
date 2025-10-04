"""Service for handling LaPoste wrapped tokens and their native counterparts."""

from typing import Dict, List, Optional

from eth_utils import to_checksum_address

from votemarket_toolkit.shared import registry
from votemarket_toolkit.shared.services.resource_manager import (
    resource_manager,
)
from votemarket_toolkit.shared.services.web3_service import Web3Service


class LaPosteService:
    """Handle LaPoste token wrapping/unwrapping operations."""

    def __init__(self):
        self.cache: Dict[str, Dict] = {}

    def get_token_factory_address(self) -> str:
        """Get TokenFactory address (same for all chains)."""
        return registry.get_token_factory_address()

    async def get_native_tokens(
        self, chain_id: int, wrapped_tokens: List[str]
    ) -> List[Optional[str]]:
        """
        Get native tokens for wrapped LaPoste tokens.

        Args:
            chain_id: Chain ID
            wrapped_tokens: List of wrapped token addresses

        Returns:
            List of native token addresses (None if not wrapped)
        """
        factory_address = self.get_token_factory_address()

        web3_service = Web3Service.get_instance(chain_id)
        bytecode_data = resource_manager.load_bytecode("GetTokensLaPoste")

        # Build constructor call with Mode.NATIVE (1)
        constructor_args = [
            factory_address,
            wrapped_tokens,
            1,
        ]  # Mode.NATIVE = 1

        # Get bytecode string from the bytecode data
        bytecode = (
            bytecode_data.get("bytecode", bytecode_data)
            if isinstance(bytecode_data, dict)
            else bytecode_data
        )

        tx = {
            "data": bytecode
            + web3_service.w3.codec.encode(
                ["address", "address[]", "uint8"], constructor_args
            ).hex()
        }

        try:
            result = web3_service.w3.eth.call(tx)
            # Decode the result
            native_tokens = web3_service.w3.codec.decode(
                ["address[]"], result
            )[0]

            # If native token is 0x0, it means the token is not wrapped
            return [
                native if native != "0x" + "0" * 40 else wrapped
                for native, wrapped in zip(native_tokens, wrapped_tokens)
            ]
        except Exception:
            # If TokenFactory doesn't exist or fails, assume tokens are not wrapped
            # This is common on chains without LaPoste
            return wrapped_tokens

    async def get_token_info(
        self,
        chain_id: int,
        token_address: str,
        is_native: bool = False,
        original_chain_id: int = None,
    ) -> Dict:
        # Fetch token info for all reward tokens

        """
        Get token information including metadata and price.

        Args:
            chain_id: Chain ID where to fetch the token info
            token_address: Token address
            is_native: Whether this is a native token (might be on different chain)
            original_chain_id: Original chain ID for context

        Returns:
            Dict with token information
        """
        token_address = to_checksum_address(token_address.lower())

        # For native tokens from LaPoste, they're usually on Ethereum mainnet
        if is_native and chain_id != 1:
            # Try mainnet first for native tokens
            fetch_chain_id = 1
        else:
            fetch_chain_id = chain_id

        cache_key = f"{fetch_chain_id}:{token_address}"

        if cache_key in self.cache:
            cached = self.cache[cache_key].copy()
            # Update chain_id to match requested chain for consistency
            cached["chain_id"] = original_chain_id or chain_id
            return cached

        # Try to fetch from the determined chain
        web3_service = Web3Service.get_instance(fetch_chain_id)

        try:
            # Get token metadata
            token_contract = web3_service.get_contract(token_address, "erc20")
            name = token_contract.functions.name().call()
            symbol = token_contract.functions.symbol().call()
            decimals = token_contract.functions.decimals().call()

            # Get price from DefiLlama
            import requests

            chain_names = {
                1: "ethereum",
                42161: "arbitrum",
                10: "optimism",
                137: "polygon",
                8453: "base",
            }
            chain_name = chain_names.get(fetch_chain_id, "ethereum")

            price_url = f"https://coins.llama.fi/prices/current/{chain_name}:{token_address}"
            response = requests.get(price_url, timeout=5)
            price = 0.0

            if response.status_code == 200:
                data = response.json()
                if (
                    "coins" in data
                    and f"{chain_name}:{token_address}" in data["coins"]
                ):
                    price = float(
                        data["coins"][f"{chain_name}:{token_address}"]["price"]
                    )

            token_info = {
                "name": name,
                "symbol": symbol,
                "address": token_address,
                "decimals": decimals,
                "chain_id": original_chain_id or chain_id,
                "price": price,
            }

            self.cache[cache_key] = token_info
            return token_info

        except Exception:
            # If native token fetch from mainnet failed and we're on L2, try the L2 chain
            if is_native and fetch_chain_id == 1 and chain_id != 1:
                try:
                    web3_service = Web3Service.get_instance(chain_id)
                    token_contract = web3_service.get_contract(
                        token_address, "erc20"
                    )
                    name = token_contract.functions.name().call()
                    symbol = token_contract.functions.symbol().call()
                    decimals = token_contract.functions.decimals().call()

                    token_info = {
                        "name": name,
                        "symbol": symbol,
                        "address": token_address,
                        "decimals": decimals,
                        "chain_id": original_chain_id or chain_id,
                        "price": 0.0,
                    }

                    self.cache[cache_key] = token_info
                    return token_info
                except Exception:
                    pass

            # Fallback to unknown
            return {
                "name": "Unknown",
                "symbol": "???",
                "address": token_address,
                "decimals": 18,
                "chain_id": original_chain_id or chain_id,
                "price": 0.0,
            }
            chain_name = chain_names.get(chain_id, "ethereum")

            price_url = f"https://coins.llama.fi/prices/current/{chain_name}:{token_address}"
            response = requests.get(price_url)
            price = 0.0

            if response.status_code == 200:
                data = response.json()
                if (
                    "coins" in data
                    and f"{chain_name}:{token_address}" in data["coins"]
                ):
                    price = float(
                        data["coins"][f"{chain_name}:{token_address}"]["price"]
                    )

            token_info = {
                "name": name,
                "symbol": symbol,
                "address": token_address,
                "decimals": decimals,
                "chainId": chain_id,
                "price": price,
            }

            self.cache[cache_key] = token_info
            return token_info

        except Exception:
            # Silently handle token info errors (common for non-standard tokens)
            return {
                "name": "Unknown",
                "symbol": "???",
                "address": token_address,
                "decimals": 18,
                "chainId": chain_id,
                "price": 0.0,
            }


# Singleton instance
laposte_service = LaPosteService()
