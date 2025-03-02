import sqlite3
import json

# Connect to SQLite Database
conn = sqlite3.connect("mcq_database.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS NewsArticles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary TEXT,
    named_entities TEXT
)
""")

def save_to_db():
    with open("summarized_news.json", "r", encoding="utf-8") as f:
        summaries = json.load(f)

    with open("named_entities.json", "r", encoding="utf-8") as f:
        entities = json.load(f)

    for summary, entity in zip(summaries, entities):
        cursor.execute("INSERT INTO NewsArticles (summary, named_entities) VALUES (?, ?)", 
                       (summary, json.dumps(entity)))

    conn.commit()
    print("Data successfully saved to mcq_database.db")

if __name__ == "__main__":
    save_to_db()
    conn.close()
