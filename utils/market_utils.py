import requests

def get_price_change(ticker: str) -> str:
    symbol_map = {
        "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
        "XRP": "ripple", "DOGE": "dogecoin", "ADA": "cardano",
        "AVAX": "avalanche-2", "MATIC": "matic-network",
        "DOT": "polkadot", "LTC": "litecoin"
    }

    # Fallback if ticker is None or empty
    if not ticker:
        ticker = "BTC"

    coin_id = symbol_map.get(ticker.upper(), "bitcoin")
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        change = data[coin_id]["usd_24h_change"]
        return f"{change:+.2f}%"
    except Exception as e:
        print("❌ Price API error:", e)
        return "N/A"
