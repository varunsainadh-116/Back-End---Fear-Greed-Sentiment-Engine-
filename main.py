from data.ingest_twitter import fetch_recent_tweets
from data.ingest_reddit import fetch_hot_posts
from data.ingest_news import fetch_news_articles
from llm.groq_agent import get_trade_suggestion


def test_twitter():
    print("\n🐦  Twitter Feed")
    print("────────────────────────────────")
    tweets = fetch_recent_tweets("bitcoin", max_results=10)
    for i, t in enumerate(tweets, 1):
        print(f"{i}. {t['text'][:120].strip()}...\n")


def test_reddit():
    print("\n👽  Reddit Posts")
    print("────────────────────────────────")
    posts = fetch_hot_posts("cryptocurrency", limit=5)
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']}\n")


def test_news():
    print("\n📰  News Headlines")
    print("────────────────────────────────")
    articles = fetch_news_articles("crypto")
    for i, article in enumerate(articles[:5], 1):
        print(f"{i}. {article['title']}\n")


def test_groq():
    print("\n🤖  Groq LLM Suggestion")
    print("────────────────────────────────")
    prompt = "There's a drop in BTC and ETH prices. What should an investor consider now?"
    response = get_trade_suggestion(prompt)
    print("Prompt:", prompt)
    print("\nLLM Response:")
    print(response)


if __name__ == "__main__":
    test_twitter()
    test_reddit()
    test_news()
    test_groq()
