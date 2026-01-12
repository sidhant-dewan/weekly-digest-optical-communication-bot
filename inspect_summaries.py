import sqlite3

conn = sqlite3.connect("data/digest.db")
cur = conn.cursor()

cur.execute("""
SELECT a.title, s.category, s.summary
FROM summaries s
JOIN articles a ON a.id = s.article_id
ORDER BY a.relevance_score DESC
LIMIT 5
""")

for row in cur.fetchall():
    print("\n", row[1], "—", row[0])
    print(row[2])

conn.close()


