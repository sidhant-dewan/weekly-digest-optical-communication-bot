from relevance.keyword_filter import keyword_score
from relevance.semantic_filter import semantic_score


def combined_relevance(text: str) -> tuple[float, float]:
    k = keyword_score(text)
    s = semantic_score(text)

    # weighted blend
    relevance = 0.4 * k + 0.6 * s
    return k, relevance
