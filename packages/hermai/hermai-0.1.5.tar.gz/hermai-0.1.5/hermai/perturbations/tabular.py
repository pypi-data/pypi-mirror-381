# hermai/perturbations/tabular.py
import pandas as pd
import numpy as np

class TabularPerturbationGenerator:
    """
    Generates context-aware perturbations for tabular data,
    respecting correlations between numerical features.
    """
    def __init__(self, categorical_features: list = None):
        self.categorical_features = categorical_features
        self._is_fitted = False
        self.stats = {}
        self.column_order = []
        self.numerical_features = []

    def fit(self, data: pd.DataFrame):
        """Learns the statistical properties, including covariance."""
        self.column_order = data.columns.tolist()
        if self.categorical_features is None:
            self.categorical_features = data.select_dtypes(include=['object', 'category']).columns.tolist()
        self.numerical_features = [c for c in self.column_order if c not in self.categorical_features]

        # Learn stats for numerical features (mean and covariance)
        if self.numerical_features:
            self.stats['numerical_mean'] = data[self.numerical_features].mean().values
            self.stats['numerical_cov'] = data[self.numerical_features].cov().values
        
        # Learn frequencies for categorical features
        self.stats['categorical_freqs'] = {
            col: data[col].value_counts(normalize=True).to_dict()
            for col in self.categorical_features
        }
        self._is_fitted = True

    def perturb(self, instance: pd.Series, n_samples: int = 1000) -> pd.DataFrame:
        """Generates realistic perturbations."""
        if not self._is_fitted:
            raise RuntimeError("Generator must be fitted first.")

        # Generate correlated numerical perturbations
        numerical_perturbations = pd.DataFrame()
        if self.numerical_features:
            perturbed_means = instance[self.numerical_features].values
            # Generate noise from multivariate normal, scaled down to be local
            noise = np.random.multivariate_normal(
                np.zeros(len(self.numerical_features)), 
                self.stats['numerical_cov'] / 4, # Scale covariance to keep perturbations local
                n_samples
            )
            numerical_data = perturbed_means + noise
            numerical_perturbations = pd.DataFrame(numerical_data, columns=self.numerical_features)
            
        # Generate categorical perturbations based on learned frequencies
        categorical_perturbations = pd.DataFrame()
        if self.categorical_features:
            for col in self.categorical_features:
                freqs = self.stats['categorical_freqs'][col]
                categories, p = zip(*freqs.items())
                categorical_perturbations[col] = np.random.choice(categories, size=n_samples, p=p)

        return pd.concat([numerical_perturbations, categorical_perturbations], axis=1)[self.column_order]