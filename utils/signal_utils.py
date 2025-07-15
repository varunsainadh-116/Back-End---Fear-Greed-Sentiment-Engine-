def generate_signal(sentiment_score: float, price_change_percent: float, volatility: float = 0.0) -> dict:
    signal = "HOLD"
    confidence = 0.5
    holding_period = "1-3 days"

    if sentiment_score > 0.5 and price_change_percent > 1.0:
        signal = "BUY"
        confidence = min(1.0, sentiment_score + (price_change_percent / 100) + (volatility / 100))
    elif sentiment_score < -0.5 and price_change_percent < -1.0:
        signal = "SELL"
        confidence = min(1.0, abs(sentiment_score) + abs(price_change_percent / 100) + (volatility / 100))

    return {
        "signal": signal,
        "confidence": round(confidence, 2),
        "holding_period": holding_period
    }
