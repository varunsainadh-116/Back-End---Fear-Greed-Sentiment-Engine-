# utils/handlers.py

import re
from llm.groq_agent import get_trade_suggestion
from utils.twitter_utils import get_tweet_text_from_url
from utils.reddit_utils import get_reddit_post_content
from utils.sentiment_utils import get_sentiment_score
from utils.market_utils import get_price_change

# Simple regex-based ticker extractor
def extract_ticker(text: str) -> str:
    possible = re.findall(r"\b(BTC|ETH|SOL|XRP|DOGE|ADA|AVAX|MATIC|DOT|LTC)\b", text.upper())
    return possible[0] if possible else "BTC"

def handle_text_input(user_input: str) -> str:
    if "twitter.com" in user_input:
        return handle_tweet_url(user_input)
    elif "reddit.com" in user_input:
        return handle_reddit_url(user_input)
    else:
        return get_trade_suggestion(user_input)

def handle_tweet_url(url: str) -> str:
    tweet_text = get_tweet_text_from_url(url)
    if not tweet_text:
        return "⚠️ Unable to fetch tweet content."

    ticker = extract_ticker(tweet_text)
    price_change = get_price_change(ticker)
    sentiment_score = get_sentiment_score(tweet_text)

    prompt = f"""
    The following tweet discusses market opinion on {ticker}. Based on the extracted sentiment and current market data:
    Tweet: "{tweet_text}"
    {ticker} price change: {price_change}
    Sentiment score: {sentiment_score}
    Suggest what the user should be aware of and whether to take action.
    """
    return get_trade_suggestion(prompt)

def handle_reddit_url(url: str) -> str:
    post_text = get_reddit_post_content(url)
    if not post_text:
        return "⚠️ Unable to fetch Reddit post."

    ticker = extract_ticker(post_text)
    price_change = get_price_change(ticker)
    sentiment_score = get_sentiment_score(post_text)

    prompt = f"""
    The following Reddit post discusses market opinion on {ticker}. Based on the extracted sentiment and current market data:
    Post: "{post_text}"
    {ticker} price change: {price_change}
    Sentiment score: {sentiment_score}
    Suggest what the user should be aware of and whether to take action.
    """
    return get_trade_suggestion(prompt)
