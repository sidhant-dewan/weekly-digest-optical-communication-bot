import sqlite3
from relevance.scorer import combined_relevance

DB_PATH = "data/digest.db"


def score_articles():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT id, raw_text FROM articles
    WHERE relevance_score IS NULL
    """)

    rows = cur.fetchall()

    for article_id, text in rows:
        k, r = combined_relevance(text or "")
        cur.execute("""
        UPDATE articles
        SET keyword_score = ?, relevance_score = ?
        WHERE id = ?
        """, (k, r, article_id))

    conn.commit()
    conn.close()
    print(f"Scored {len(rows)} articles")


if __name__ == "__main__":
    score_articles()
