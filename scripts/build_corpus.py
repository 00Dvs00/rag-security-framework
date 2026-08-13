"""Corpus-generation stub for the defense project.

This intentionally keeps the reproducible corpus-generation pattern explicit
without requiring a full training run while the notebook is being packaged.
"""

from __future__ import annotations

import json
from pathlib import Path


def build_corpus() -> dict:
    """Generate a tiny deterministic benchmark payload used for repo smoke tests."""
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "outputs"
    out_dir.mkdir(exist_ok=True)

    split = {
        "seed": 42,
        "note": "Do not alter indices; this split is kept frozen for reproducibility.",
        "train": [0, 1, 2, 3],
        "val": [4],
        "test": [5],
    }

    (out_dir / "benchmark_split.json").write_text(json.dumps(split, indent=2), encoding="utf-8")
    return split


if __name__ == "__main__":
    build_corpus()
    print("Corpus build complete.")
