# hermai/perturbations/base_generator.py

from abc import ABC, abstractmethod
import pandas as pd

class BasePerturbationGenerator(ABC):
    """
    Abstract base class for all perturbation generators.

    Each generator must have a `fit` method to learn the data's structure and
    a `perturb` method to generate new samples around a specific data point.
    """
    def __init__(self, **kwargs):
        """
        A flexible constructor for future parameters.
        """
        pass

    @abstractmethod
    def fit(self, data: pd.DataFrame):
        """
        Learns the characteristics of the dataset (distributions, frequencies, etc.).
        This method should set the internal state of the generator.

        Args:
            data (pd.DataFrame): The training data used to learn the data structure.
        """
        raise NotImplementedError

    @abstractmethod
    def perturb(self, instance: pd.Series, n_samples: int = 1000) -> pd.DataFrame:
        """
        Generates perturbed new samples around a given instance.

        Args:
            instance (pd.Series): The original data point to perturb around.
            n_samples (int): The number of new samples to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the new, perturbed samples similar to the original instance.
        """
        raise NotImplementedError