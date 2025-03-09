from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def detect_bias(text):
    sentiment = sia.polarity_scores(text)
    polarity = TextBlob(text).sentiment.polarity

    if sentiment['compound'] >= 0.05:
        return "Positive Bias"
    elif sentiment['compound'] <= -0.05:
        return "Negative Bias"
    else:
        return "Neutral"

# 🔹 Get user input for analysis
user_text = input("Enter text to analyze for bias: ")
bias_result = detect_bias(user_text)

print(f"\n🔍 Bias Detection Result: {bias_result}")
