
import re
from llm.groq_agent import get_trade_suggestion

def handle_text_input(user_input: str) -> str:
    if "twitter.com" in user_input:
        return handle_tweet_url(user_input)
    elif "reddit.com" in user_input:
        return handle_reddit_url(user_input)
    else:
        return get_trade_suggestion(user_input)

# Mock extraction for now (replace with actual API logic later)
def handle_tweet_url(url: str) -> str:
    tweet_text = "Bitcoin is crashing again! Worst timing ever."  # Example
    ticker = "BTC"
    price_change = "-2.5%"
    sentiment_score = "-0.6"

    prompt = f"""
    The following tweet discusses market opinion on {ticker}. Based on the extracted sentiment and current market data:
    Tweet: "{tweet_text}"
    BTC price change: {price_change}
    Sentiment score: {sentiment_score}
    Suggest what the user should be aware of and whether to take action.
    """
    return get_trade_suggestion(prompt)

def handle_reddit_url(url: str) -> str:
    post_text = "Ethereum is getting more traction with ETFs coming soon!"  # Example
    ticker = "ETH"
    price_change = "+1.5%"
    sentiment_score = "+0.4"

    prompt = f"""
    The following Reddit post discusses market opinion on {ticker}. Based on the extracted sentiment and current market data:
    Post: "{post_text}"
    ETH price change: {price_change}
    Sentiment score: {sentiment_score}
    Suggest what the user should be aware of and whether to take action.
    """
    return get_trade_suggestion(prompt)
