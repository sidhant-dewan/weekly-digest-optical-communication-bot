import sqlite3

def init_db(db_path="data/digest.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT UNIQUE,
        source TEXT,
        published_at TEXT,
        first_seen_at TEXT,
        raw_text TEXT,
        keyword_score REAL,
        relevance_score REAL
    )
    """)

    conn.commit()
    conn.close()
