from abc import ABC, abstractmethod
import numpy as np

class MutationFunction(ABC):
    
    @abstractmethod
    def mutate(self, individuals: np.ndarray) -> np.ndarray:
        pass

class SwapMutation(MutationFunction):
    
    def __init__(self, number_of_swaps:int = 1) -> None:
        self.number_of_swaps:int = number_of_swaps

    def mutate(self, individuals: np.ndarray) -> np.ndarray:
        assert individuals.ndim == 2
        number_of_individuals, number_of_genes = individuals.shape

        swap_indices = np.random.choice(number_of_genes, (self.number_of_swaps, number_of_individuals, 2))
        print("Swap indices: \n",swap_indices,"\n")
        row_indexes = np.tile(np.array([np.arange(number_of_individuals)]).T,(1,2))
        for swap in swap_indices:
            individuals[row_indexes,swap] = individuals[row_indexes,swap[:,::-1]]
        return individuals
