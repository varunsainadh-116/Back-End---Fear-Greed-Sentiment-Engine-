
def generate_signal(sentiment_score: float, price_change_percent: float) -> dict:
    signal = "HOLD"
    confidence = 0.5
    holding_period = "1-3 days"

    if sentiment_score > 0.5 and price_change_percent > 1.0:
        signal = "BUY"
        confidence = min(1.0, (sentiment_score + (price_change_percent / 100)) / 2)
        holding_period = "3-7 days"
    elif sentiment_score < -0.5 and price_change_percent < -1.0:
        signal = "SELL"
        confidence = min(1.0, (abs(sentiment_score) + abs(price_change_percent / 100)) / 2)
        holding_period = "1-2 days"

    return {
        "signal": signal,
        "confidence": f"{confidence:.2f}",
        "holding_period": holding_period
    }
