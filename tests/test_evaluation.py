from ragdefense.evaluation import build_benchmark_summary, compute_classification_metrics


def test_compute_classification_metrics():
    metrics = compute_classification_metrics(tp=19, fp=1, tn=80, fn=0)

    assert metrics["precision"] == 0.95
    assert metrics["recall"] == 1.0
    assert abs(metrics["f1"] - 0.9743589743589743) < 1e-9
    assert metrics["accuracy"] == 0.99


def test_build_benchmark_summary_contains_expected_rows():
    rows = build_benchmark_summary()
    labels = {row["label"] for row in rows}

    assert {"No Defense", "Keyword Filter", "This System (tuned)"}.issubset(labels)
    for row in rows:
        assert 0.0 <= row["precision"] <= 1.0
        assert 0.0 <= row["recall"] <= 1.0
        assert 0.0 <= row["f1"] <= 1.0
