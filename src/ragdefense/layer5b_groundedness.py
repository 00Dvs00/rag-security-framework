"""Groundedness validation against trusted context."""

from __future__ import annotations


def groundedness_score(answer: str, context: str) -> float:
    """Very simple lexical groundedness check."""
    if not answer or not context:
        return 0.0
    answer_terms = set((answer or "").lower().split())
    context_terms = set((context or "").lower().split())
    if not answer_terms:
        return 0.0
    match_ratio = len(answer_terms & context_terms) / len(answer_terms)
    return round(min(1.0, max(0.0, match_ratio)), 3)
