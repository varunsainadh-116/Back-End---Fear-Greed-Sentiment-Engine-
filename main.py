from data.ingest_twitter import fetch_recent_tweets
from data.ingest_reddit import fetch_hot_posts
from data.ingest_news import fetch_news_articles
from llm.groq_agent import get_trade_suggestion

def test_twitter():
    print("\n🐦 Twitter Feed:")
    tweets = fetch_recent_tweets("bitcoin", max_results=10) 
    for t in tweets:
        print("- ", t["text"][:100], "...")


def test_reddit():
    print("\n👽 Reddit Posts:")
    posts = fetch_hot_posts("cryptocurrency", limit=5)
    for p in posts:
        print("- ", p["title"])

def test_news():
    print("\n📰 News Headlines:")
    articles = fetch_news_articles("crypto")
    for a in articles[:5]:
        print("- ", a["title"])

def test_groq():
    print("\n🤖 Groq LLM Suggestion:")
    prompt = "There's a drop in BTC and ETH prices. What should an investor consider now?"
    suggestion = get_trade_suggestion(prompt)
    print("→", suggestion)

if __name__ == "__main__":
    test_twitter()
    test_reddit()
    test_news()
    test_groq()
