"""Post-generation output toxicity filter."""

from __future__ import annotations


def output_toxicity_score(text: str) -> float:
    """A minimal lexical toxicity heuristic in [0,1]."""
    lowered = (text or "").lower()
    harmful_terms = ["bomb", "poison", "kill", "attack", "weapon", "explosive", "drug"]
    count = sum(1 for term in harmful_terms if term in lowered)
    return round(min(1.0, count / max(1, len(harmful_terms))), 3)
