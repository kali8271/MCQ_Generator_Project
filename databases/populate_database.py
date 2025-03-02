from database_manager import insert_news_article, insert_mcq

# Insert sample news articles
insert_news_article("AI Revolution in Healthcare", "AI is transforming the medical industry...", "2025-02-27")
insert_news_article("Climate Change Impact", "Recent studies show rising global temperatures...", "2025-02-26")

# Insert sample MCQs
insert_mcq(1, "What is AI transforming?", "Healthcare", ["Finance", "Education", "Manufacturing"])
insert_mcq(2, "What is the effect of climate change?", "Rising temperatures", ["More rainfall", "Lower CO2 levels", "Stable temperatures"])
