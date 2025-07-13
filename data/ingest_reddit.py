import praw
from config.config_loader import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT

def fetch_hot_posts(subreddit_name="cryptocurrency", limit=10):
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
    subreddit = reddit.subreddit(subreddit_name)
    return [{"title": post.title, "score": post.score} for post in subreddit.hot(limit=limit)]
