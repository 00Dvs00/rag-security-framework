# RAG Security Framework

This project explores how retrieval-augmented generation (RAG) systems can be hardened against adversarial prompts, retrieval manipulation, and jailbreak-style attacks. The goal was to build a lightweight defense pipeline that evaluates unsafe queries, checks retrieved content for suspicious instruction patterns, and validates whether generated responses remain grounded in trusted context.

## Project overview

RAG systems are often vulnerable because they assume retrieved content is trustworthy. In practice, malicious or misleading passages can influence model behavior, especially when multiple chunks work together to steer the output. This project focuses on runtime safeguards: filtering harmful intent before retrieval, scoring suspicious content, detecting instruction-like passages, and validating final responses.

The implementation is organized around a layered defense pipeline:

- harmful query detection before retrieval
- ingestion sanitization and provenance weighting
- retrieval filtering for trusted content
- instruction-vs-data boundary checks
- cross-chunk collusion analysis
- trust scoring and groundedness validation
- output toxicity filtering

## Repository structure

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
├── results/
│   └── benchmark_table.md
├── tests/
│   ├── test_evaluation.py
│   └── test_pipeline.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── Capstone_Final_Document.pdf
```

## Setup

```bash
git clone https://github.com/00Dvs00/rag-security-framework.git
cd rag-security-framework
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build_corpus.py
jupyter notebook notebooks/01_pipeline_walkthrough.ipynb
```

## Evaluation summary

The results below compare a baseline configuration against a simple keyword filtering approach and the layered defense pipeline.

| Metric | No Defense | Keyword Filter | This System (tuned) |
|---|---:|---:|---:|
| Precision | 0.000 | 1.000 | 0.950 |
| Recall | 0.000 | 0.800 | 1.000 |
| F1 | 0.000 | 0.889 | 0.974 |
| Accuracy | 0.500 | 0.900 | 0.990 |

## Current status and limitations

This is a research-oriented security prototype rather than a production guarantee. The current implementation is useful for evaluating defensive logic in a controlled setting, but it still depends on heuristic scoring and rule-based checks. More complex obfuscation, paraphrasing, or novel adversarial patterns may still require additional validation and tuning.

## Planned work

- refine the retrieval and scoring logic for more realistic adversarial examples
- improve visualization and benchmark reporting
- add a more interactive demo for the defense pipeline
- extend evaluation to include additional attack families and ablation comparisons

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for the full text.

## Citation

This project is best cited alongside the core background literature on retrieval-augmented generation, prompt injection, and jailbreak evaluation:

- Greshake, K., Abdelnabi, S., Machanavajjhala, A., Biggio, B., Roli, F., and Fischlin, M. (2023). "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." arXiv:2302.12173.
- Wei, A., Haghtalab, N., and Steinhardt, J. (2023). "Jailbroken: How does LLM safety training fail?" arXiv:2307.02483.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., Riedel, S., and Kiela, D. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." arXiv:2005.11401.

Project metadata is also available in [CITATION.cff](CITATION.cff).
