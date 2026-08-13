"""Cross-chunk collusion analysis."""

from __future__ import annotations

from typing import Iterable, List, Tuple


def build_interaction_graph(chunks: Iterable[str]) -> List[Tuple[str, str, float]]:
    """Create a lightweight graph of chunk-to-chunk correlations."""
    chunk_list = list(chunks)
    edges: List[Tuple[str, str, float]] = []
    for i, left in enumerate(chunk_list):
        for j in range(i + 1, len(chunk_list)):
            right = chunk_list[j]
            overlap = len(set((left or "").lower().split()) & set((right or "").lower().split()))
            if overlap:
                edges.append((left, right, min(1.0, overlap / max(1, min(len(left.split()), len(right.split()))))))
    return edges


def collusion_risk(chunks: Iterable[str]) -> float:
    """Aggregate chunk-pair risk into a single risk score in [0,1]."""
    edges = build_interaction_graph(chunks)
    if not edges:
        return 0.0
    avg = sum(weight for _, _, weight in edges) / len(edges)
    return round(min(1.0, avg), 3)
