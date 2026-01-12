from sentence_transformers import SentenceTransformer, util
from config import OPTICAL_CANONICAL_TEXT

_model = SentenceTransformer("all-MiniLM-L6-v2")
_canonical_embedding = _model.encode(OPTICAL_CANONICAL_TEXT, normalize_embeddings=True)


def semantic_score(text: str) -> float:
    if not text:
        return 0.0

    emb = _model.encode(text[:2000], normalize_embeddings=True)
    score = util.cos_sim(emb, _canonical_embedding).item()

    # cosine similarity typically ~0.2–0.8
    return max(min(score, 1.0), 0.0)
