import sqlite3
import yaml
from collectors.rss_collector import fetch_rss
from db.schema import init_db

DB_PATH = "data/digest.db"


def load_sources():
    with open("sources/rss_sources.yaml") as f:
        return yaml.safe_load(f)


def store_articles(articles):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for a in articles:
        try:
            cur.execute("""
            INSERT INTO articles
            (title, url, source, published_at, first_seen_at, raw_text)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                a["title"],
                a["url"],
                a["source"],
                a["published_at"],
                a["first_seen_at"],
                a["raw_text"]
            ))
        except sqlite3.IntegrityError:
            pass  # duplicate URL, ignore



    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db(DB_PATH)
    sources = load_sources()

    all_articles = []
    for src in sources:
        all_articles.extend(fetch_rss(src))

    store_articles(all_articles)
    print(f"Ingested {len(all_articles)} articles")
