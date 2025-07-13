import tweepy
from config.config_loader import TWITTER_BEARER_TOKEN

def fetch_recent_tweets(query, max_results=10):
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    tweets = client.search_recent_tweets(query=query, tweet_fields=["text", "created_at", "lang"], max_results=max_results)
    return [{"text": tweet.text, "created_at": str(tweet.created_at)} for tweet in tweets.data if tweet.lang == "en"]
