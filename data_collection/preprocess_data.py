import json
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)  # Remove special characters
    return text.strip()

def preprocess_articles():
    with open("news_data.json", "r", encoding="utf-8") as f:
        articles = json.load(f)

    processed_articles = []
    for article in articles:
        sentences = sent_tokenize(clean_text(article))
        words = [word_tokenize(sentence) for sentence in sentences]
        words = [[word.lower() for word in sentence if word.lower() not in STOPWORDS] for sentence in words]
        processed_articles.append(sentences)

    return processed_articles

if __name__ == "__main__":
    data = preprocess_articles()
    with open("processed_news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Preprocessed and saved news articles to processed_news.json")
