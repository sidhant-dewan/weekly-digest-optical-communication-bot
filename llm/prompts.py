SUMMARY_PROMPT = """
You are a technical analyst for optical communication systems.

Summarize the article faithfully. Do NOT speculate.
If information is missing, say "not specified".

Choose exactly ONE category from:
- Industry News
- Technical Trend
- Research
- Standards Update
- Jobs

Return ONLY valid JSON in this schema:

{{
  "category": "...",
  "summary": "2–3 sentence factual summary",
  "keywords": ["keyword1", "keyword2", "keyword3"]
}}

Article:
Title: {title}
Source: {source}
Text:
{text}
"""
