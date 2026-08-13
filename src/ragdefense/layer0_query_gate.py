"""Pre-retrieval query safety gate."""

from __future__ import annotations

from typing import Iterable, List


DEFAULT_HARMFUL_TERMS = (
    "weapon",
    "bomb",
    "explosive",
    "drug synthesis",
    "poison",
    "illegal",
    "self-harm",
)


def query_is_harmful(query: str, blocklist: Iterable[str] | None = None) -> bool:
    """Return True when a query appears to request harmful instructions."""
    text = (query or "").lower()
    terms = tuple(blocklist or DEFAULT_HARMFUL_TERMS)
    return any(term.lower() in text for term in terms)


def filter_harmful_queries(queries: List[str], blocklist: Iterable[str] | None = None) -> List[str]:
    """Keep only queries that pass the harmful-intent gate."""
    return [q for q in queries if not query_is_harmful(q, blocklist)]
