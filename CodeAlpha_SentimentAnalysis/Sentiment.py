import re
from collections import Counter

positive_words = {
    "good", "great", "excellent", "amazing", "awesome", "happy",
    "love", "best", "perfect", "satisfied", "useful", "recommend"
}

negative_words = {
    "bad", "poor", "terrible", "awful", "hate", "sad",
    "angry", "worst", "disappointed", "slow", "broken", "useless"
}

emotion_lexicon = {
    "joy": {"happy", "love", "amazing", "awesome", "perfect"},
    "anger": {"angry", "hate", "awful", "worst"},
    "sadness": {"sad", "disappointed", "poor", "bad"},
    "trust": {"good", "great", "excellent", "recommend", "satisfied"},
    "fear": {"broken", "problem", "slow"},
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()


def analyze_sentiment(text):
    words = clean_text(text)

    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, positive_score, negative_score


def detect_emotions(text):
    words = clean_text(text)
    emotions = Counter()

    for emotion, emotion_words in emotion_lexicon.items():
        emotions[emotion] = sum(1 for word in words if word in emotion_words)

    detected = {emotion: score for emotion, score in emotions.items() if score > 0}

    if not detected:
        return {"neutral": 0}

    return detected


text = input("Enter text for sentiment analysis: ")

sentiment, positive_score, negative_score = analyze_sentiment(text)
emotions = detect_emotions(text)

print("\nSentiment Analysis Result")
print("-------------------------")
print("Text:", text)
print("Sentiment:", sentiment)
print("Positive Score:", positive_score)
print("Negative Score:", negative_score)
print("Detected Emotions:", emotions)