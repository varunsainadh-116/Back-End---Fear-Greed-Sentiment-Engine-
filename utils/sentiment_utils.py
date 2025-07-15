from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_score(text: str) -> str:
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]
    return f"{score:+.2f}"
