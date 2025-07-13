import re

def extract_ticker(text: str) -> str:
    possible = re.findall(r"\b(BTC|ETH|SOL|XRP|DOGE|ADA|AVAX|MATIC|DOT|LTC)\b", text.upper())
    return possible[0] if possible else "BTC"
