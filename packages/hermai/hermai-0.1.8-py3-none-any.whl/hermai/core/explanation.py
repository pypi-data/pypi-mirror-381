# hermai/core/explanation.py
import pandas as pd
from ..visualizations import plots

class LocalExplanation:
    # ... (Bu sınıfta değişiklik yok) ...
    def __init__(self, instance, prediction_prob, feature_importances, counterfactual, counterfactual_prediction_prob):
        self.instance = instance
        self.prediction_prob = prediction_prob
        self.feature_importances = feature_importances
        self.counterfactual = counterfactual
        self.counterfactual_prediction_prob = counterfactual_prediction_prob

    def plot(self):
        plots.plot_local_feature_importance(self)

    def narrative(self) -> str:
        pred_class = 1 if self.prediction_prob > 0.5 else 0
        narrative = f"Prediction Analysis for Instance:\n"
        narrative += f"---------------------------------\n"
        narrative += f"Model predicted class '{pred_class}' with {self.prediction_prob:.2%} confidence.\n"
        narrative += f"\nKey Feature Contributions (Local Importance):\n"
        for _, row in self.feature_importances.head(5).iterrows():
            direction = "increases" if row['importance'] > 0 else "decreases"
            narrative += f"- Feature '{row['feature']}' {direction} the probability.\n"
        
        if self.counterfactual is not None:
            cf_pred_class = 1 if self.counterfactual_prediction_prob > 0.5 else 0
            narrative += f"\nCounterfactual Analysis:\n"
            narrative += f"To flip the prediction to class '{cf_pred_class}', one of the closest possibilities found is:\n"
            # Using .compare() can fail if dtypes are different, a safer approach:
            changes = self.instance[self.instance != self.counterfactual]
            for feature, original_val in changes.items():
                 new_val = self.counterfactual[feature]
                 narrative += f"- Change '{feature}' from {original_val:.2f} to {new_val:.2f}\n"
        return narrative


class GeneralExplanation: # <-- DEĞİŞTİ
    """Container for a general model explanation."""
    def __init__(self, surrogate_model, feature_importances):
        self.surrogate_model = surrogate_model
        self.feature_importances = feature_importances

    def plot_feature_importance(self):
        """Visualizes the general feature importances."""
        plots.plot_general_feature_importance(self) # <-- DEĞİŞTİ

    def plot_surrogate_tree(self):
        """Visualizes the surrogate decision tree."""
        plots.plot_surrogate_tree(self)