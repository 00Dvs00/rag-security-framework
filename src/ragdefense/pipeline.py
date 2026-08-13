"""Pipeline entry points for no-defense and full-defense RAG flows."""

from typing import Any, Dict, List


def no_defense_pipeline(query: str, documents: List[str]) -> Dict[str, Any]:
    """Minimal no-defense baseline for comparison."""
    return {
        "query": query,
        "documents": documents,
        "blocked": False,
        "risk_score": 0.0,
        "verdict": "pass-through",
    }


def full_defense_pipeline(query: str, documents: List[str]) -> Dict[str, Any]:
    """Full defense pipeline placeholder for the packaged project.

    This keeps the project structure coherent before the full notebook logic is
    refactored into the individual layer modules.
    """
    normalized = query.lower()
    blocked = any(keyword in normalized for keyword in ("weapon", "bomb", "drug", "poison", "explosive"))

    if blocked:
        return {
            "query": query,
            "documents": documents,
            "blocked": True,
            "risk_score": 1.0,
            "verdict": "blocked_by_query_gate",
        }

    score = min(1.0, max(0.0, 0.15 + 0.05 * len(documents)))
    return {
        "query": query,
        "documents": documents,
        "blocked": False,
        "risk_score": round(score, 3),
        "verdict": "safe_to_continue",
    }
