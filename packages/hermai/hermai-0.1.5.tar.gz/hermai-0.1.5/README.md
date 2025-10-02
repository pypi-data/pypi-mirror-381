# Hermai: A Hermeneutic Explainable AI Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Hermai is a Python library for explainable AI (XAI) that focuses on providing contextual, narrative, and actionable explanations for machine learning models. Inspired by hermeneutics, it aims to create a dialogue between the user and the model's decision-making process.

## Key Features

- **Contextual Perturbations:** Generates realistic "what-if" scenarios that respect the correlations in your data.
- **Local Explanations:** Explains individual predictions by identifying key feature contributions and generating counterfactuals.
- **General Explanations:** Approximates the overall behavior of a complex model with a simple, interpretable surrogate model (like a decision tree).
- **Narrative Summaries:** Presents explanations in human-readable text.

## Installation

You can install Hermai directly from GitHub:

```bash
pip install git+[https://github.com/](https://github.com/)bilgisayarkavramlari/hermai.git
```

## Quick Usage

Here's a quick example of how to get local and general explanations for a RandomForest model trained on the Titanic dataset.

```python
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from hermai.perturbations.tabular import TabularPerturbationGenerator
from hermai.explainers import LocalExplainer, GeneralExplainer

# Load and prepare data (assuming X_train, black_box_model are ready)
# ...

# --- Local Explanation ---
generator = TabularPerturbationGenerator(categorical_features=['pclass', 'sex', 'embarked'])
generator.fit(X_train)
local_explainer = LocalExplainer(black_box_model, generator)
instance = X_test.iloc[0]
local_explanation = local_explainer.explain(instance)
print(local_explanation.narrative())
local_explanation.plot()


# --- General Model Explanation ---
general_explainer = GeneralExplainer(black_box_model)
general_explanation = general_explainer.explain(X_train)
general_explanation.plot_feature_importance()
general_explanation.plot_surrogate_tree()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.