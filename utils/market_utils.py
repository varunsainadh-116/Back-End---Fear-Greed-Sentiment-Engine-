import requests

def get_market_stats(ticker: str) -> dict:
    symbol_map = {
        "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
        "XRP": "ripple", "DOGE": "dogecoin", "ADA": "cardano"
    }
    coin_id = symbol_map.get(ticker.upper(), "bitcoin")

    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false&tickers=false&market_data=true"
        response = requests.get(url).json()
        market_data = response.get("market_data", {})

        current_price = market_data["current_price"]["usd"]
        volume = market_data["total_volume"]["usd"]
        high_24h = market_data["high_24h"]["usd"]
        low_24h = market_data["low_24h"]["usd"]

        volatility = ((high_24h - low_24h) / current_price) * 100

        return {
            "price": f'{market_data["price_change_percentage_24h"]:+.2f}%',
            "volume": f'${volume:,.0f}',
            "volatility": f'{volatility:.2f}%',
            "raw_volatility": volatility
        }

    except Exception as e:
        print("❌ Error in get_market_stats:", e)
        return {
            "price": "0%", "volume": "$0", "volatility": "0%", "raw_volatility": 0
        }
