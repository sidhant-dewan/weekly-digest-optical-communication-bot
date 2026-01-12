import sqlite3

# conn = sqlite3.connect("data/digest.db")
# cur = conn.cursor()

# cur.execute("""
# SELECT title, source, relevance_score
# FROM articles
# ORDER BY relevance_score DESC
# LIMIT 10
# """)

# for row in cur.fetchall():
#     print(f"{row[2]:.2f} | {row[1]} | {row[0]}")

# conn.close()

# import sqlite3

# conn = sqlite3.connect("data/digest.db")
# cur = conn.cursor()

# cur.execute("""
# SELECT COUNT(*)
# FROM articles
# WHERE relevance_score >= 0.45
# """)

# print("Relevant articles:", cur.fetchone()[0])
# conn.close()

import sqlite3

conn = sqlite3.connect("data/digest.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM summaries")
print("Summarized articles:", cur.fetchone()[0])

conn.close()


