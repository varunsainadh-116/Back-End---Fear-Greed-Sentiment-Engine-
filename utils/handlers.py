# utils/handlers.py

import re
from llm.groq_agent import get_trade_suggestion
from utils.twitter_utils import get_tweet_text_from_url
from utils.reddit_utils import get_reddit_post_content
from utils.sentiment_utils import get_sentiment_score
from utils.market_utils import get_price_change
from utils.helpers import extract_ticker


def handle_text_input(user_input: str) -> str:
    if "twitter.com" in user_input or "x.com" in user_input:
        return handle_tweet_url(user_input)
    elif "reddit.com" in user_input:
        return handle_reddit_url(user_input)
    else:
        ticker = extract_ticker(user_input)
        if not ticker:
            return (
                "⚠️ Sorry, I couldn't determine which cryptocurrency you're referring to.\n"
                "Could you please specify the asset (e.g. BTC, ETH, SOL)?"
            )

        price_change = get_price_change(ticker)
        sentiment_score = get_sentiment_score(user_input)

        prompt = f"""
        The user is asking about the outlook for {ticker}. 
        Based on current sentiment and price data:

        Query: "{user_input}"
        {ticker} price change: {price_change}
        Sentiment score: {sentiment_score}

        Suggest what the user should be aware of and whether to take action.
        """
        return get_trade_suggestion(prompt)

    
def handle_custom_text(text: str) -> str:
    ticker = extract_ticker(text)
    price_change = get_price_change(ticker)
    sentiment_score = get_sentiment_score(text)

    prompt = f"""
    The following message discusses market opinion on {ticker}. Based on the extracted sentiment and current market data:
    Post: "{text}"
    {ticker} price change: {price_change}
    Sentiment score: {sentiment_score}
    Suggest what the user should be aware of and whether to take action.
    """
    return get_trade_suggestion(prompt)

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
