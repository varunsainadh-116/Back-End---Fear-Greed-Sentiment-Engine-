from newsapi import NewsApiClient
from config.config_loader import NEWSAPI_KEY

# Function to fetch news articles based on a query

def fetch_news_articles(query, language="en"):
    newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
    articles = newsapi.get_everything(q=query, language=language, sort_by="publishedAt", page_size=10)
    return articles["articles"]
