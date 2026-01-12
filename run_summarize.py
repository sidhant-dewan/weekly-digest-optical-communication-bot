import sqlite3
import json
from llm.llm_client import run_llm
from llm.prompts import SUMMARY_PROMPT

DB_PATH = "data/digest.db"
RELEVANCE_THRESHOLD = 0.30
MIN_TEXT_CHARS = 500


def extract_json(text: str) -> dict:
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1 or end <= start:
        raise ValueError("No valid JSON boundaries found")

    return json.loads(text[start:end + 1])


def summarize_articles():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT a.id, a.title, a.source, a.raw_text
    FROM articles a
    LEFT JOIN summaries s ON a.id = s.article_id
    WHERE a.relevance_score >= ?
      AND s.article_id IS NULL
    """, (RELEVANCE_THRESHOLD,))

    rows = cur.fetchall()

    summarized = 0

    for article_id, title, source, text in rows:

        # --- text length gate ---
        if not text or len(text.strip()) < MIN_TEXT_CHARS:
            print(f"Skipping article {article_id}: insufficient text")
            continue

        prompt = SUMMARY_PROMPT.format(
            title=title,
            source=source,
            text=text[:3000]
        )

        try:
            response = run_llm(prompt)
            data = extract_json(response)

        except Exception:
            # retry once with stricter instruction
            hard_prompt = prompt + "\n\nIMPORTANT: Output JSON ONLY."
            try:
                response = run_llm(hard_prompt)
                data = extract_json(response)
            except Exception as e:
                print(f"Failed article {article_id}: {e}")
                continue

        cur.execute("""
        INSERT INTO summaries (article_id, category, summary, keywords)
        VALUES (?, ?, ?, ?)
        """, (
            article_id,
            data["category"],
            data["summary"],
            ", ".join(data["keywords"])
        ))

        conn.commit()
        summarized += 1

    conn.close()
    print(f"Summarized {summarized} articles")


if __name__ == "__main__":
    summarize_articles()
