import re

def extract_ticker(text: str) -> str:
    tickers = re.findall(r"\b(BTC|ETH|SOL|XRP|DOGE|ADA|AVAX|MATIC|DOT|LTC)\b", text.upper())
    return tickers[0] if tickers else "BTC"
