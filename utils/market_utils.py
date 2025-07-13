# utils/market_utils.py

import requests

def get_price_change(ticker: str) -> str:
    symbol_map = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "SOL": "solana",
        "XRP": "ripple",
        "DOGE": "dogecoin",
        "ADA": "cardano",
        "AVAX": "avalanche-2",
        "MATIC": "matic-network",
        "DOT": "polkadot",
        "LTC": "litecoin"
    }
    coin_id = symbol_map.get(ticker.upper(), "bitcoin")

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
    try:
        res = requests.get(url).json()
        change = res[coin_id]["usd_24h_change"]
        return f"{change:.2f}%"
    except Exception as e:
        print("❌ Price API error:", e)
        return "0%"
