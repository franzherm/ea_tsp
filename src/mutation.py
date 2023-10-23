from abc import ABC, abstractmethod
import numpy as np


"""See 2015_Book_IntroductionToEvolutionaryComp"""

class MutationFunction(ABC):
    
    @abstractmethod
    def mutate(self, individuals: np.ndarray) -> np.ndarray:
        pass


class SwapMutation(MutationFunction):

    def __init__(self, number_of_swaps:int = 1) -> None:
        self.number_of_swaps:int = number_of_swaps

    def mutate(self, individuals: np.ndarray) -> np.ndarray:
        """ Performs n swap mutations for the given set of individuals, where n is the number specified during instantiation of the SwapMutation object.

        For each of the n swaps, 2 indices are chosen for each individual by using numpy.random.choice().
        The variable row_indices represents a matrix of two column vectors [0,...,g-1] where g is the number of genes
        in each individual. Both the swap_indices as well as the row_indices are then used to perform the swap using numpy's
        advanced indexing. The swaps are performed in place, which is why the swapped_indices are returned rather than the array of mutated individuals.

        ### Parameters: 
        individuals -- the chosen individuals the mutation should be applied to

        ### Returns:
        swap_indices -- an array of the indexes that were swapped during the mutation, 
                        where the first dimension is the number of the swap, the second dimension is the 
                        individual that was mutated and the third dimension are the swapped indices
        """
        assert individuals.ndim == 2
        number_of_individuals, number_of_genes = individuals.shape

        swap_indices = np.random.choice(number_of_genes, (self.number_of_swaps, number_of_individuals, 2))
        row_indices = np.tile(np.array([np.arange(number_of_individuals)]).T,(1,2))

        for swap in swap_indices:
            individuals[row_indices,swap] = individuals[row_indices,swap[:,::-1]]

        return swap_indices

class InversionMutation(MutationFunction):
    pass

class InsertMutation(MutationFunction):
    pass

class ScrambleMutation(MutationFunction):
    pass
