import re

def extract_ticker(text: str) -> str | None:
    alias_map = {
        "BITCOIN": "BTC",
        "BTC": "BTC",
        "ETHEREUM": "ETH",
        "ETH": "ETH",
        "SOLANA": "SOL",
        "SOL": "SOL",
        "RIPPLE": "XRP",
        "XRP": "XRP",
        "DOGECOIN": "DOGE",
        "DOGE": "DOGE",
        "AVALANCHE": "AVAX",
        "AVAX": "AVAX",
        "CARDANO": "ADA",
        "ADA": "ADA",
        "MATIC": "MATIC",
        "DOT": "DOT",
        "LITECOIN": "LTC",
        "LTC": "LTC"
    }

    for word in text.upper().split():
        clean_word = re.sub(r'[^\w]', '', word)  
        if clean_word in alias_map:
            return alias_map[clean_word]

    return None  # No known ticker found
