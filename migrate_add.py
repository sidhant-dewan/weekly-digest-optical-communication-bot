# import sqlite3

# conn = sqlite3.connect("data/digest.db")
# cur = conn.cursor()

# # Add columns safely
# try:
#     cur.execute("ALTER TABLE articles ADD COLUMN keyword_score REAL")
# except sqlite3.OperationalError:
#     pass  # column already exists

# try:
#     cur.execute("ALTER TABLE articles ADD COLUMN relevance_score REAL")
# except sqlite3.OperationalError:
#     pass  # column already exists

# conn.commit()
# conn.close()

# print("Migration complete")
