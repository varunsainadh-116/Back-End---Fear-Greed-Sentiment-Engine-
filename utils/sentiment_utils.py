
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(text: str) -> str:
    score = analyzer.polarity_scores(text)["compound"]
    return f"{score:+.2f}"  
