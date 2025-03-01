import requests
import json

# API Keys
NEWS_API_KEY = "your_newsapi_key"
GUARDIAN_API_KEY = "your_guardian_api_key"
NYT_API_KEY = "your_nytimes_api_key"

# API URLs
NEWS_SOURCES = {
    "NewsAPI": f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}",
    "NewYorkTimes": f"https://api.nytimes.com/svc/topstories/v2/world.json?api-key={NYT_API_KEY}",
    "Guardian": f"https://content.guardianapis.com/search?api-key={GUARDIAN_API_KEY}&show-fields=body"
}

# Function to Fetch News
def fetch_news():
    all_articles = []
    
    for source, url in NEWS_SOURCES.items():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            if source == "NewsAPI":
                articles = [article['content'] for article in data.get('articles', []) if article.get('content')]
            elif source == "NewYorkTimes":
                articles = [article['abstract'] for article in data.get('results', [])]
            elif source == "Guardian":
                articles = [article['fields']['body'][:500] for article in data['response']['results']]
                
            all_articles.extend(articles)

    return all_articles

if __name__ == "__main__":
    articles = fetch_news()
    with open("news_data.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4)
    print(f"Fetched {len(articles)} articles and saved to news_data.json")
