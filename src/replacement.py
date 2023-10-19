from abc import ABC, abstractmethod
import numpy as np

class ReplacementFunction(ABC):

    @abstractmethod
    def replace(self, population: np.ndarray, children: np.ndarray) -> np.ndarray:
        pass