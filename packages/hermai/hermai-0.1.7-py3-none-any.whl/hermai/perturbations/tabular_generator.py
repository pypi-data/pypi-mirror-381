# hermai/perturbations/tabular_generator.py

import pandas as pd
import numpy as np
from .base_generator import BasePerturbationGenerator

class TabularPerturbationGenerator(BasePerturbationGenerator):
    """
    Generates contextual perturbations for tabular data.

    This class creates realistic "what-if" scenarios by using a normal distribution
    for numerical features and the frequency distribution from the training data
    for categorical features.
    """

    def __init__(self, categorical_features: list = None):
        """
        Args:
            categorical_features (list, optional): A list of names for categorical columns.
                                                   If None, columns with 'object' and 'category'
                                                   dtypes will be automatically detected.
        """
        super().__init__()
        self.categorical_features = categorical_features
        self._is_fitted = False

    def fit(self, data: pd.DataFrame):
        """
        Learns the statistical properties of the tabular data.

        Args:
            data (pd.DataFrame): The training data.
        """
        self.training_data_stats = {}
        self.column_order = data.columns.tolist()

        if self.categorical_features is None:
            self.categorical_features = data.select_dtypes(include=['object', 'category']).columns.tolist()

        self.numerical_features = [col for col in self.column_order if col not in self.categorical_features]

        # Calculate statistics for numerical features (used for perturbation scale)
        self.training_data_stats['numerical'] = data[self.numerical_features].describe().to_dict()

        # Calculate frequencies (probabilities) for categorical features
        self.training_data_stats['categorical'] = {}
        for col in self.categorical_features:
            counts = data[col].value_counts(normalize=True)
            self.training_data_stats['categorical'][col] = counts.to_dict()

        self._is_fitted = True
        print("✅ TabularPerturbationGenerator has been fitted to the data structure.")
        print(f"   - Numerical Features: {self.numerical_features}")
        print(f"   - Categorical Features: {self.categorical_features}")

    def perturb(self, instance: pd.Series, n_samples: int = 1000) -> pd.DataFrame:
        """
        Generates contextually meaningful perturbations around a given instance.

        Args:
            instance (pd.Series): The original data point to be explained.
            n_samples (int): The number of perturbations to generate.

        Returns:
            pd.DataFrame: The newly generated samples.
        """
        if not self._is_fitted:
            raise RuntimeError("Generator is not fitted yet. Call 'fit' with training data first.")

        perturbed_samples = []
        for _ in range(n_samples):
            new_sample = instance.copy()

            # Perturb numerical features
            # Add noise around the original value, scaled by the overall dataset's standard deviation
            for col in self.numerical_features:
                std = self.training_data_stats['numerical'][col]['std']
                noise = np.random.normal(0, std / 4) # Noise is 1/4th of the std deviation
                new_sample[col] += noise

            # Perturb categorical features
            # Resample based on the frequencies in the training data
            for col in self.categorical_features:
                frequencies = self.training_data_stats['categorical'][col]
                categories = list(frequencies.keys())
                probabilities = list(frequencies.values())
                new_sample[col] = np.random.choice(categories, p=probabilities)

            perturbed_samples.append(new_sample)

        return pd.DataFrame(perturbed_samples, columns=self.column_order)