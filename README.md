# rag-security-framework

Adversarial evaluation framework for RAG systems with corpus poisoning, retrieval manipulation, jailbreak simulations, and automated LLM security benchmarking.

## Overview

This project focuses on runtime defense and evaluation for retrieval-augmented generation (RAG) systems. It includes a layered defense pipeline for harmful-query detection, retrieval filtering, instructionality scoring, cross-chunk collusion checks, trust-based scoring, groundedness validation, and output toxicity filtering.

## What is included

- Seven-layer runtime defense concept
- Reproducible corpus-generation pattern
- Frozen benchmark split for evaluation consistency
- Minimal package layout for modular development
- Notebook walkthrough and evaluation notebooks
- Smoke-test validation for core behavior

## Project structure

```text
.
├── README.md
├── CITATION.cff
├── .gitignore
├── environment.yml
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── src/
│   └── ragdefense/
│       ├── __init__.py
│       ├── config.py
│       ├── evaluation.py
│       ├── layer0_query_gate.py
│       ├── layer1_ingestion.py
│       ├── layer2_retrieval.py
│       ├── layer3_boundary.py
│       ├── layer4_collusion.py
│       ├── layer5a_trust.py
│       ├── layer5b_groundedness.py
│       ├── layer5c_output_filter.py
│       └── pipeline.py
├── scripts/
│   └── build_corpus.py
├── notebooks/
│   ├── README.md
│   ├── 01_pipeline_walkthrough.ipynb
│   └── 02_evaluation_and_ablation.ipynb
├── outputs/
│   └── benchmark_split.json
├── docs/
│   └── index.md
├── results/
│   └── benchmark_table.md
├── tests/
│   ├── test_evaluation.py
│   └── test_pipeline.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Quickstart

```bash
git clone https://github.com/00Dvs00/rag-security-framework.git
cd rag-security-framework
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build_corpus.py
jupyter notebook notebooks/01_pipeline_walkthrough.ipynb
```

## Evaluation snapshot

| Metric | No Defense | Keyword Filter | This System (tuned) |
|---|---:|---:|---:|
| Precision | 0.000 | 1.000 | 0.950 |
| Recall | 0.000 | 0.800 | 1.000 |
| F1 | 0.000 | 0.889 | 0.974 |
| Accuracy | 0.500 | 0.900 | 0.990 |

## Limitations

This project is a practical security prototype and should be treated as a research and engineering artifact rather than a production guarantee. Heuristic filters and rule-based checks can still be bypassed by novel adversarial patterns, paraphrasing, or encoding-based obfuscation.

## Roadmap

- [x] Initial GitHub-ready repo scaffold
- [x] Package structure and layered defense modules
- [x] Reproducible corpus-generation logic and frozen split
- [x] Notebook walkthrough and evaluation notebooks
- [x] CI workflow for automated tests
- [ ] Add richer benchmark visuals and report exports
- [ ] Add a live demo UI or Gradio/Streamlit interface
- [ ] Publish a polished project landing page with case study details

## Citation

See [CITATION.cff](CITATION.cff).
