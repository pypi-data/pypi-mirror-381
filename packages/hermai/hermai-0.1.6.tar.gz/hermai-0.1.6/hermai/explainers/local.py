# hermai/explainers/local.py
import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

from .base import BaseExplainer
from ..perturbations.tabular import TabularPerturbationGenerator
from ..core.explanation import LocalExplanation

class LocalExplainer(BaseExplainer):
    """Explains a single prediction of a model."""
    def __init__(self, model, generator: TabularPerturbationGenerator):
        super().__init__(model)
        if not hasattr(model, 'predict_proba'):
            raise TypeError("Model must have a 'predict_proba' method for local explanations.")
        self.generator = generator

    def _find_counterfactual(self, instance, perturbations, original_pred, pred_probs, scaler):
        """Finds the closest perturbation that flips the prediction."""
        predictions = (pred_probs > 0.5).astype(int)
        flipped_indices = np.where(predictions != original_pred)[0]
        if len(flipped_indices) == 0:
            return None, None
        
        flipped_perturbations = perturbations.iloc[flipped_indices]
        instance_scaled = scaler.transform(instance.to_frame().T)
        flipped_scaled = scaler.transform(flipped_perturbations)
        
        distances = cdist(instance_scaled, flipped_scaled, metric='euclidean').flatten()
        closest_idx = flipped_indices[np.argmin(distances)]
        
        return perturbations.iloc[closest_idx], pred_probs[closest_idx]

    def explain(self, instance: pd.Series, n_samples: int = 3000) -> LocalExplanation:
        """Generates a local explanation for a single instance."""
        # 1. Generate perturbations
        perturbations = self.generator.perturb(instance, n_samples=n_samples)
        
        # 2. Get model predictions
        original_prob = self.model.predict_proba(instance.to_frame().T)[0, 1]
        pred_probs = self.model.predict_proba(perturbations)[:, 1]
        
        # 3. Train a local surrogate model (Lasso)
        scaler = StandardScaler().fit(perturbations)
        perturbations_scaled = scaler.transform(perturbations)
        instance_scaled = scaler.transform(instance.to_frame().T)
        
        distances = cdist(instance_scaled, perturbations_scaled, metric='euclidean').flatten()
        weights = np.exp(-distances**2 / np.median(distances)**2) # RBF kernel for weights
        
        surrogate = Lasso(alpha=0.01).fit(perturbations_scaled, pred_probs, sample_weight=weights)
        
        feature_importances = pd.DataFrame({
            'feature': self.generator.column_order,
            'importance': surrogate.coef_
        }).sort_values(by='importance', key=abs, ascending=False).reset_index(drop=True)

        # 4. Find counterfactual
        original_pred = (original_prob > 0.5).astype(int)
        counterfactual, cf_prob = self._find_counterfactual(
            instance, perturbations, original_pred, pred_probs, scaler
        )

        return LocalExplanation(
            instance=instance,
            prediction_prob=original_prob,
            feature_importances=feature_importances,
            counterfactual=counterfactual,
            counterfactual_prediction_prob=cf_prob
        )