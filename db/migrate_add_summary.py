import sqlite3

conn = sqlite3.connect("data/digest.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS summaries (
    article_id INTEGER PRIMARY KEY,
    category TEXT,
    summary TEXT,
    keywords TEXT,
    FOREIGN KEY(article_id) REFERENCES articles(id)
)
""")

conn.commit()
conn.close()

print("Summaries table ready")
