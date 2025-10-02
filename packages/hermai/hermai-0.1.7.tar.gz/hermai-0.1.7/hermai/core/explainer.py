# hermai/core/explainer.py

import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

from ..perturbations import TabularPerturbationGenerator
from .explanation import Explanation

class HermaiExplainer:
    """
    The main Hermai explainer class.

    This class orchestrates the generation of explanations for machine learning model predictions
    by taking a model and a data generator.
    """
    def __init__(self, model, generator: TabularPerturbationGenerator):
        """
        Args:
            model: A machine learning model with a `predict_proba` method.
            generator (TabularPerturbationGenerator): The generator object that will be used
                                                       to create perturbations.
        """
        if not hasattr(model, 'predict_proba'):
            raise TypeError("The model must have a 'predict_proba' method.")
        self.model = model
        self.generator = generator

    def _find_counterfactual(self,
                             instance: pd.Series,
                             perturbed_data: pd.DataFrame,
                             original_prediction: int,
                             perturbed_predictions: np.ndarray,
                             scaler: StandardScaler) -> pd.Series:
        """Finds the closest perturbation that flips the prediction."""
        # Find indices where the prediction is different
        flipped_indices = np.where(perturbed_predictions != original_prediction)[0]

        if len(flipped_indices) == 0:
            return None # No counterfactual found

        # Filter to only the flipped perturbations
        flipped_perturbations = perturbed_data.iloc[flipped_indices]

        # Scale data to calculate meaningful distances
        instance_scaled = scaler.transform(instance.to_frame().T)
        flipped_scaled = scaler.transform(flipped_perturbations)

        # Calculate Euclidean distance
        distances = cdist(instance_scaled, flipped_scaled, metric='euclidean').flatten()

        # Find the index of the closest flipped perturbation
        closest_index = np.argmin(distances)
        return flipped_perturbations.iloc[closest_index]


    def explain_instance(self, instance: pd.Series, n_samples: int = 2000) -> Explanation:
        """
        Generates a full explanation for a single data instance.

        Args:
            instance (pd.Series): The data instance to explain.
            n_samples (int): The number of perturbations to generate for the explanation.

        Returns:
            Explanation: An object containing the full explanation results.
        """
        print("🔍 Starting explanation process for a single instance...")

        # === MODULE 1: Generate contextual perturbations ===
        perturbed_data = self.generator.perturb(instance, n_samples=n_samples)
        print(f"   - Step 1/4: Generated {n_samples} perturbed samples.")

        # === MODULE 2: Train a Surrogate Model ===
        # Get black-box model predictions for the original and perturbed data
        # We focus on the probability of the positive class (class 1)
        original_prob = self.model.predict_proba(instance.to_frame().T)[0, 1]
        perturbed_probs = self.model.predict_proba(perturbed_data)[:, 1]

        # Scale data for the linear model and distance calculations
        scaler = StandardScaler().fit(perturbed_data)
        perturbed_scaled = scaler.transform(perturbed_data)
        instance_scaled = scaler.transform(instance.to_frame().T)

        # Calculate distances to use as weights (closer points are more important)
        distances = cdist(instance_scaled, perturbed_scaled, metric='euclidean').flatten()
        weights = np.exp(-distances) # Simple kernel to weigh samples

        # Train a simple, interpretable surrogate model (Lasso)
        # Lasso is great because it pushes unimportant feature coefficients to zero
        surrogate_model = Lasso(alpha=0.01)
        surrogate_model.fit(perturbed_scaled, perturbed_probs, sample_weight=weights)
        print("   - Step 2/4: Trained a local surrogate model.")

        # Extract feature importances from the surrogate model
        importances = surrogate_model.coef_
        feature_names = perturbed_data.columns
        feature_importances_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values(by='importance', key=abs, ascending=False).reset_index(drop=True)


        # === MODULE 3: Find a Counterfactual Example ===
        original_prediction = (original_prob > 0.5).astype(int)
        perturbed_predictions = (perturbed_probs > 0.5).astype(int)

        counterfactual = self._find_counterfactual(instance, perturbed_data, original_prediction, perturbed_predictions, scaler)
        cf_prob = None
        if counterfactual is not None:
             cf_prob = self.model.predict_proba(counterfactual.to_frame().T)[0, 1]
        print("   - Step 3/4: Searched for a counterfactual example.")

        # === MODULE 4: Assemble the Explanation ===
        explanation = Explanation(
            instance=instance,
            prediction_prob=original_prob,
            feature_importances=feature_importances_df,
            counterfactual=counterfactual,
            counterfactual_prediction_prob=cf_prob
        )
        print("   - Step 4/4: Assembled the final explanation.")
        print("✅ Explanation complete.")

        return explanation