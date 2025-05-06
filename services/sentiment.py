from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using VADER.
    Returns a polarity score between 1 (very negative) and 10 (very positive).
    """
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']  # -1 (very negative) to 1 (very positive)

    # Scale compound score from -1 to 1 into 1 to 10
    sentiment_score = ((compound + 1) / 2) * 9 + 1
    return round(sentiment_score, 1)
