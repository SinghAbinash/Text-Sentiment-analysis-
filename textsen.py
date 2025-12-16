from textblob import TextBlob

def analyze_sentiment(text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
                return "Positive"
        elif sentiment_score < 0:
                return "Negative"
        else:
                return "Neutral" 
        
# example
post = "You are bad"
print("Sentiment", analyze_sentiment(post))