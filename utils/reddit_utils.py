import praw
from config.config_loader import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def get_reddit_post_content(url: str) -> str:
    try:
        submission = reddit.submission(url=url)
        return submission.title + " " + submission.selftext
    except Exception as e:
        print(f"❌ Error fetching Reddit post: {e}")
        return None
