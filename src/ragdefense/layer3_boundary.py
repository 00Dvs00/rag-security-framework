"""Instructionality and data-vs-instruction boundary detection."""

from __future__ import annotations

import re


def instructionality_score(text: str) -> float:
    """A simple instructionality heuristic in the range [0,1]."""
    value = text or ""
    instruction_markers = [
        "ignore",
        "override",
        "system",
        "developer",
        "reset",
        "act as",
        "pretend",
        "follow these steps",
    ]
    score = 0.2
    lowered = value.lower()
    for marker in instruction_markers:
        if marker in lowered:
            score += 0.15
    if re.search(r"(?:^|\s)(do|donot|never|always|must|ignore)\b", lowered):
        score += 0.2
    score = min(score, 1.0)
    return round(score, 3)
