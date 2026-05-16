from textblob import TextBlob


def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of a given text.

    Returns a dictionary with:
    - label: 'Positive', 'Negative', or 'Neutral'
    - polarity: float from -1.0 (most negative) to 1.0 (most positive)
    - subjectivity: float from 0.0 (objective) to 1.0 (subjective)
    - emoji: visual indicator
    """
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive"
        emoji = "😊"
    elif polarity < -0.1:
        label = "Negative"
        emoji = "😞"
    else:
        label = "Neutral"
        emoji = "😐"

    return {
        "label": label,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "emoji": emoji,
        "text": text,
    }


if __name__ == "__main__":
    # Quick CLI test — run: python analyzer.py
    test_sentences = [
        "I absolutely love this product! It's amazing.",
        "This is the worst experience I have ever had.",
        "The package arrived on Tuesday.",
    ]
    for sentence in test_sentences:
        result = analyze_sentiment(sentence)
        print(f"{result['emoji']} {result['label']:9} | Polarity: {result['polarity']:+.3f} | {sentence[:50]}")
