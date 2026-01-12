import sqlite3
from datetime import date

DB_PATH = "data/digest.db"
MAX_ITEMS_PER_SECTION = 5


def fetch_summaries():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT
        a.title,
        a.url,
        a.source,
        a.relevance_score,
        s.category,
        s.summary
    FROM summaries s
    JOIN articles a ON a.id = s.article_id
    ORDER BY a.relevance_score DESC
    """)

    rows = cur.fetchall()
    conn.close()
    return rows


def group_by_category(rows):
    grouped = {}
    for title, url, source, score, category, summary in rows:
        grouped.setdefault(category, []).append({
            "title": title,
            "url": url,
            "source": source,
            "score": score,
            "summary": summary
        })
    return grouped


def build_digest(grouped):
    today = date.today().isoformat()
    lines = []

    lines.append(f"# Weekly Optical Communications Digest")
    lines.append(f"**Week of {today}**\n")

    section_order = [
        "Industry News",
        "Technical Trend",
        "Research",
        "Standards Update",
        "Jobs"
    ]

    for section in section_order:
        items = grouped.get(section, [])
        if not items:
            continue

        lines.append(f"## {section}")

        for item in items[:MAX_ITEMS_PER_SECTION]:
            lines.append(
                f"- **{item['title']}** ({item['source']}): "
                f"{item['summary']} "
                f"[link]({item['url']})"
            )

        lines.append("")  # blank line

    return "\n".join(lines)


def write_digest(text):
    filename = f"weekly_digest_{date.today().isoformat()}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Digest written to {filename}")


if __name__ == "__main__":
    rows = fetch_summaries()
    grouped = group_by_category(rows)
    digest_text = build_digest(grouped)
    write_digest(digest_text)
