# hermai/explainers/base.py
from abc import ABC, abstractmethod

class BaseExplainer(ABC):
    """Abstract base class for all explainers."""
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def explain(self, *args, **kwargs):
        raise NotImplementedError