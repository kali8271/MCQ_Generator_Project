import sqlite3
import logging
DATABASE_FILE = r"E:\MCQ_Generator_Project\databases\news_articles.db"

def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_FILE)
    return conn


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler and a stream handler
file_handler = logging.FileHandler('news_articles.log')
stream_handler = logging.StreamHandler()

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

DATABASE_FILE = r"E:\MCQ_Generator\databases\news_articles.db"

def create_connection():
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        logger.info('Connected to the database')
        return conn
    except sqlite3.Error as e:
        logger.error(f'Failed to connect to the database: {e}')

def insert_news_article(title, content, published_date):
    """Insert a new article into the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO news_articles (title, content, published_date) VALUES (?, ?, ?)",
            (title, content, published_date),
        )
        conn.commit()
        logger.info('Article inserted successfully')
    except sqlite3.Error as e:
        logger.error(f'Failed to insert article: {e}')
    finally:
        conn.close()

def fetch_all_articles():
    """Retrieve all news articles."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM news_articles")
        articles = cursor.fetchall()
        logger.info('Fetched all articles')
        return articles
    except sqlite3.Error as e:
        logger.error(f'Failed to fetch articles: {e}')
    finally:
        conn.close()

def insert_mcq(article_id, question, correct_answer, options):
    """Insert a generated MCQ for a given article."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mcq_questions (article_id, question, correct_answer, option_1, option_2, option_3) VALUES (?, ?, ?, ?, ?, ?)",
            (article_id, question, correct_answer, *options),
        )
        conn.commit()
        logger.info('MCQ inserted successfully')
    except sqlite3.Error as e:
        logger.error(f'Failed to insert MCQ: {e}')
    finally:
        conn.close()

def fetch_mcqs_by_article(article_id):
    """Retrieve all MCQs for a specific article."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mcq_questions WHERE article_id = ?", (article_id,))
        mcqs = cursor.fetchall()
        logger.info('Fetched MCQs for article')
        return mcqs
    except sqlite3.Error as e:
        logger.error(f'Failed to fetch MCQs: {e}')
    finally:
        conn.close()

def insert_news_article(title, content, published_date):
    """Insert a new article into the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO news_articles (title, content, published_date) VALUES (?, ?, ?)",
        (title, content, published_date),
    )
    conn.commit()
    conn.close()

def fetch_all_articles():
    """Retrieve all news articles."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news_articles")
    articles = cursor.fetchall()
    conn.close()
    return articles

def insert_mcq(article_id, question, correct_answer, options):
    """Insert a generated MCQ for a given article."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO mcq_questions (article_id, question, correct_answer, option_1, option_2, option_3) VALUES (?, ?, ?, ?, ?, ?)",
        (article_id, question, correct_answer, *options),
    )
    conn.commit()
    conn.close()

def fetch_mcqs_by_article(article_id):
    """Retrieve all MCQs for a specific article."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mcq_questions WHERE article_id = ?", (article_id,))
    mcqs = cursor.fetchall()
    conn.close()
    return mcqs
