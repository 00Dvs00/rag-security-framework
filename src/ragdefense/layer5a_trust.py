"""Trust scoring for retrieved chunks."""

from __future__ import annotations


def trust_score(instructionality: float, provenance: float, collusion: float) -> float:
    """Combine trust signals into a single score on [0,1]."""
    score = 0.5 * provenance + 0.3 * (1.0 - instructionality) + 0.2 * (1.0 - collusion)
    return round(min(1.0, max(0.0, score)), 3)
