import sqlite3

conn = sqlite3.connect("data/digest.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM articles")
count = cur.fetchone()[0]

print("Article count:", count)

conn.close()
