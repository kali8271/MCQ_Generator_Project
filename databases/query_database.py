from database_manager import fetch_all_articles, fetch_mcqs_by_article

# Fetch and display all news articles
articles = fetch_all_articles()
print("News Articles:")
for article in articles:
    print(article)

# Fetch and display MCQs for the first article
mcqs = fetch_mcqs_by_article(1)
print("\nMCQs for Article 1:")
for mcq in mcqs:
    print(mcq)
