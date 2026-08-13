# Notebook overview

This folder holds the public-facing notebook materials used to demonstrate the defense pipeline and evaluate its behavior.

## 01_pipeline_walkthrough.ipynb
A shortened walkthrough of the full pipeline, showing how the corpus is generated, the defense layers operate, and the defense behavior is applied in a retrieval setting.

## 02_evaluation_and_ablation.ipynb
A more evaluation-focused notebook for ablations, guardrail metrics, and comparisons against a no-defense baseline.

## How to use

Open the notebook in Jupyter and run the cells in order. For a local setup, first install the project dependencies from the repository root:

```bash
pip install -r requirements.txt
```

If the project later adds a formal requirements file, this folder will be kept in sync with the package setup.
