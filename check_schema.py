import sqlite3

conn = sqlite3.connect("data/digest.db")
cur = conn.cursor()

cur.execute("PRAGMA table_info(articles)")
for row in cur.fetchall():
    print(row)

conn.close()
