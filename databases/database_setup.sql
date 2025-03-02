-- Create a table to store news articles
CREATE TABLE IF NOT EXISTS news_articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    published_date TEXT
);

-- Create a table to store MCQs generated from news articles
CREATE TABLE IF NOT EXISTS mcq_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER,
    question TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    FOREIGN KEY (article_id) REFERENCES news_articles(id) ON DELETE CASCADE
);
