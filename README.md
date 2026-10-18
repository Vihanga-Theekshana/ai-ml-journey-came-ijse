# AI & ML Learning Journey

**Vihanga Theekshana · IJSE AI & ML coursework · Learning in progress**

I am studying AI and machine learning at IJSE and building a foundation in Python, data analysis, and machine learning. This repository organizes my course notebooks and practice exercises by learning day, with summaries and links to the code.

I am preparing for internship opportunities where I can apply these skills and continue learning from practical work.

## Start here

- [Day 12: regression](days/day-12/) — a first predictive modelling workflow.
- [Day 13: text classification](days/day-13/) — bag-of-words features and logistic regression.
- [Day 16: customer clustering](days/day-16/) — scaling, K-means, and cluster comparison.
- [Day 18: PyTorch](days/day-18/) — dense network architecture and training on synthetic data.

These are **coursework examples in progress**. They are not presented as independent production projects or independently verified model results. [Review notes](docs/REVIEW_NOTES.md) explain current limitations.

## Learning index

Day numbers preserve the original folder sequence; they are not calendar dates. Days 11, 14, and 17 had empty source notebooks.

| Day | Topic | Status |
| --- | --- | --- |
| 01 | [Python fundamentals](days/day-01/README.md) | Course practice |
| 02 | [Input, types, and collections](days/day-02/README.md) | Course practice |
| 03 | [Control flow and dictionaries](days/day-03/README.md) | Course practice |
| 04 | [Functions and OOP basics](days/day-04/README.md) | Course practice |
| 05 | [Inheritance and composition](days/day-05/README.md) | Course practice |
| 06 | [Python special methods](days/day-06/README.md) | Course practice |
| 07 | [NumPy fundamentals](days/day-07/README.md) | Course practice |
| 08 | [NumPy operations and linear algebra](days/day-08/README.md) | Course practice |
| 09 | [Pandas and introductory visualization](days/day-09/README.md) | Course practice |
| 10 | [Data visualization](days/day-10/README.md) | Course practice |
| 11 | [Notes pending](days/day-11/README.md) | Notes pending |
| 12 | [Simple linear regression](days/day-12/README.md) | Course practice |
| 13 | [Regression and text classification](days/day-13/README.md) | Course practice |
| 14 | [Notes pending](days/day-14/README.md) | Notes pending |
| 15 | [XGBoost classification](days/day-15/README.md) | Course practice |
| 16 | [Customer clustering and MLflow introduction](days/day-16/README.md) | Course practice |
| 17 | [Notes pending](days/day-17/README.md) | Notes pending |
| 18 | [Neural networks with PyTorch](days/day-18/README.md) | Course practice |

## Tools practised

Python · Jupyter · NumPy · Pandas · Matplotlib · Seaborn · scikit-learn · XGBoost · PyTorch

The MLflow notebook currently contains imports only.

## Run the notebooks

Create a virtual environment from the repository root. These commands use Windows PowerShell and call the environment's Python directly:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

For Day 15, install `requirements-xgboost.txt`; for Day 18, install `requirements-pytorch.txt`; for the Day 16 MLflow starter, install `requirements-mlflow.txt`, using the same `python.exe -m pip install -r` command.

Open a notebook in JupyterLab and run it from its own folder so that relative CSV paths resolve. Days 1–6 include Python-only exercises and may request input. Some learning cells contain errors; see the review notes before using Run All.

Dependencies are a starting specification derived from imports, not a fully tested environment lock. Datasets and trained model artifacts are excluded. Restore required files using [dataset setup](docs/DATASETS.md).

## More work

- [Assignments](assignments/README.md)
- [Additional practice](practice/README.md)
- [Daily update workflow](docs/DAILY_WORKFLOW.md)
- [Project development roadmap](docs/PROJECT_ROADMAP.md)
- [Original-to-organized file map](docs/FILE_MAP.md)

## Attribution

This repository contains materials from my learning during the IJSE AI & ML course. Guided examples and the Day 18 course walkthrough are learning references; their inclusion does not claim that I independently designed them. Original instructor and third-party rights remain with their owners. No blanket license is applied to mixed-origin course material. Dataset sources and permissions still need to be recorded where unknown.

Repository organization and summaries were prepared with AI assistance. Personal reflections are left for me to write in my own words.

[GitHub profile](https://github.com/Vihanga-Theekshana)
