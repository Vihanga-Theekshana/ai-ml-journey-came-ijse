# Review notes

## What was checked

The preparation process parsed notebooks, validated their notebook structure, checked Python syntax, cleared notebook outputs/execution counts, preserved course code apart from the two corrections documented below, and checked the organized file inventory. The Day 15 XGBoost notebook and corrected Day 18 training notebook were executed successfully in the installed local environment on 2026-10-18. This checks those two workflows only; it does not verify the other notebooks or establish model quality. No scores are claimed in the main README.

## Items to revisit

- Days 11, 14, and 17: original notebooks are empty; README placeholders preserve the day sequence.
- Day 08: incompatible broadcasting, reshaping, and concatenation examples can raise errors. Label expected errors explicitly before presenting a Run All workflow.
- Day 13: the original multiple-regression filename contains a single-feature TV model; renamed to `regression-practice.ipynb` to avoid overstating the implementation.
- Day 13 sentiment classification: the code inspects missing review text but does not clearly clean it before vectorization. Verify the local dataset and handle missing/blank text explicitly.
- Day 16: MLflow is an import-only starter, not an implemented experiment-tracking workflow.
- Corrected Day 18 training: the intermediate evaluation cell now uses `model(x_test_t)` so predictions and test labels use the same split. The original used training inputs with test labels.
- Corrected Day 02: removed a duplicate comma from `list_A = [1,2,,9,0]` so the cell can parse.
- Day 18: synthetic classification features do not establish a real-world customer-purchase model.
- ML quiz Q01–Q05: hard-coded printed answers are retained as assessment history, not computational solutions.
- Course examples and assessment solutions have mixed or unverified authorship. Record your own changes and check course sharing rules; do not describe all examples as independently designed projects.
- Requirements were derived from imports. A clean environment, fresh kernel run, and verified dataset sources are still needed for full reproducibility.

## Packaging exclusions

Dataset/archive folders, PDFs, trained models, MLflow databases, notebook checkpoints, empty notebooks, a malformed temporary notebook, and trivial scratch test scripts are excluded. Two quiz notebooks duplicate the Day 13 notebooks and are represented by those Day 13 copies. Original files remain untouched.

## Static syntax check

All included Python scripts and notebook code cells passed Python syntax parsing after the two corrections above. This does not establish runtime correctness.

## Execution checks

- Day 15 `xgboost-classification.ipynb`: all cells completed, including training and save/load.
- Day 18 `neural-network-training.ipynb`: all cells completed after the evaluation correction, including training, checkpoint reload, and evaluation.
- Runs used temporary working directories. Generated models and execution outputs are excluded from the published source.
- Dependencies were already installed; the requirements files were not tested through a fresh installation.
