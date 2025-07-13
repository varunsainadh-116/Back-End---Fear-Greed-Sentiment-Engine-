import tweepy
import re
from config.config_loader import TWITTER_BEARER_TOKEN

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def get_tweet_text_from_url(url: str) -> str:
    # Match both x.com and twitter.com
    match = re.search(r"(?:twitter\.com|x\.com)/\w+/status/(\d+)", url)
    if not match:
        return None
    tweet_id = match.group(1)
    try:
        tweet = client.get_tweet(tweet_id, tweet_fields=["text"])
        return tweet.data["text"]
    except Exception as e:
        print(f"❌ Error fetching tweet: {e}")
        return None
