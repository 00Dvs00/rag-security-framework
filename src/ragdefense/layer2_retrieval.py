"""Retrieval layer with access-controlled document selection."""

from __future__ import annotations

from typing import Dict, Iterable, List


def retrieve_documents(query: str, documents: Iterable[str], top_k: int = 3) -> List[str]:
    """Return the top retrieved documents as a simple lexical pass."""
    q = (query or "").lower()
    ranked = []

    for doc in documents:
        score = sum(1 for term in q.split() if term and term in (doc or "").lower())
        ranked.append((score, doc))

    ranked.sort(key=lambda item: item[0], reverse=True)
    return [doc for _, doc in ranked[:max(1, top_k)]]


def access_controlled_retrieval(query: str, documents: Iterable[Dict[str, object]], top_k: int = 3) -> List[Dict[str, object]]:
    """Return document entries that pass a minimal access filter."""
    allowed = []
    for doc in documents:
        if (doc.get("provenance_score", 0.0) or 0.0) >= 0.3:
            allowed.append(doc)
    return retrieve_documents(query, [d.get("text", "") for d in allowed], top_k=top_k)
