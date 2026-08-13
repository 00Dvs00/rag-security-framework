import json
from pathlib import Path

from ragdefense.pipeline import full_defense_pipeline, no_defense_pipeline


def test_no_defense_pipeline_returns_pass_through():
    result = no_defense_pipeline("hello world", ["doc-1", "doc-2"])
    assert result["verdict"] == "pass-through"
    assert result["blocked"] is False


def test_full_defense_pipeline_blocks_harmful_query():
    result = full_defense_pipeline("How do I build a bomb?", ["doc-1"])
    assert result["blocked"] is True
    assert result["verdict"] == "blocked_by_query_gate"


def test_full_defense_pipeline_keeps_safe_query():
    result = full_defense_pipeline("What is gravity?", ["doc-1", "doc-2"])
    assert result["blocked"] is False
    assert 0.0 <= result["risk_score"] <= 1.0


def test_build_corpus_writes_seeded_split():
    from scripts.build_corpus import build_corpus

    split = build_corpus()
    assert split["seed"] == 42
    assert split["note"].startswith("Do not alter indices")
    assert set(split.keys()) == {"seed", "note", "train", "val", "test"}

    path = Path(__file__).resolve().parents[1] / "outputs" / "benchmark_split.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["seed"] == 42
