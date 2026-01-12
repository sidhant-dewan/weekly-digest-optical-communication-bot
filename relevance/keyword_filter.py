from config import OPTICAL_KEYWORDS


def keyword_score(text: str) -> float:
    if not text:
        return 0.0

    text = text.lower()
    hits = sum(1 for kw in OPTICAL_KEYWORDS if kw in text)

    # normalize (cap at 1.0)
    return min(hits / 8.0, 1.0)
