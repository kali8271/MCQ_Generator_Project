from transformers import pipeline
import json

# Load Summarization Model
summarizer = pipeline("summarization")

def summarize_articles():
    with open("processed_news.json", "r", encoding="utf-8") as f:
        articles = json.load(f)

    summarized_articles = []
    for sentences in articles:
        text = " ".join(sentences[:5])  # Use first 5 sentences for summarization
        summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
        summarized_articles.append(summary[0]['summary_text'])

    return summarized_articles

if __name__ == "__main__":
    summaries = summarize_articles()
    with open("summarized_news.json", "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=4)
    print("Summarized news articles and saved to summarized_news.json")
