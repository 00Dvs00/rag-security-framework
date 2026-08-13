"""Ingestion sanitization and provenance handling."""

from __future__ import annotations

import re
from typing import Dict


def sanitize_chunk(text: str) -> str:
    """Strip obvious attack markers and normalize spacing."""
    cleaned = text or ""
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.replace("\u200b", "")
    cleaned = re.sub(r"(?:ignore previous instructions|system prompt|developer message)", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


def provenance_score(source: str) -> float:
    """Simple source-trust heuristic, normalized to [0, 1]."""
    source_lower = (source or "").lower()
    trusted = ["official", "internal", "verified", "policy", "documentation"]
    score = 0.35
    for token in trusted:
        if token in source_lower:
            score += 0.15
    score = min(score, 1.0)
    return round(score, 3)


def ingest_document(doc: Dict[str, str]) -> Dict[str, object]:
    """Normalize a document entry for downstream defense layers."""
    text = sanitize_chunk(doc.get("text", ""))
    return {
        "source": doc.get("source", "unknown"),
        "text": text,
        "provenance_score": provenance_score(doc.get("source", "unknown")),
        "sanitized": bool(text),
    }
