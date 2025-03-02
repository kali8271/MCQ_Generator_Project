import sqlite3

# Connect to your database
conn = sqlite3.connect("news_articles.db")
cursor = conn.cursor()

# Read and execute SQL file
with open("database_setup.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database setup completed successfully!")
