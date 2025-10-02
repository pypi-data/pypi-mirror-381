# hermai/explainers/general.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from .base import BaseExplainer
from ..core.explanation import GeneralExplanation

class GeneralExplainer(BaseExplainer):
    """Explains the general behavior of a model."""
    def __init__(self, model):
        super().__init__(model)

    def explain(self, X_train: pd.DataFrame, max_depth: int = 3) -> GeneralExplanation:
        """
        Trains a general surrogate model (Decision Tree) to approximate the black-box model.
        
        Args:
            X_train (pd.DataFrame): The training data to use for approximation.
            max_depth (int): The maximum depth of the surrogate decision tree.
        
        Returns:
            GeneralExplanation: An object containing the general explanation results.
        """
        black_box_predictions = self.model.predict(X_train)
        
        surrogate_model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        surrogate_model.fit(X_train, black_box_predictions)
        
        general_importances = pd.DataFrame({
            'feature': X_train.columns,
            'importance': surrogate_model.feature_importances_
        }).sort_values(by='importance', ascending=False).reset_index(drop=True)
        
        return GeneralExplanation(
            surrogate_model=surrogate_model,
            feature_importances=general_importances
        )