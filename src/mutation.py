from abc import ABC, abstractmethod
import numpy as np


"""See 2015_Book_IntroductionToEvolutionaryComp"""

class MutationFunction(ABC):
    
    @abstractmethod
    def mutate(self, individuals: np.ndarray):
        " Performs mutation operation on the individuals"
        pass


class SwapMutation(MutationFunction):

    def __init__(self, number_of_swaps:int = 1) -> None:
        self.number_of_swaps:int = number_of_swaps

    def mutate(self, individuals: np.ndarray) -> None:
        """ Performs n swap mutations for the given set of individuals, where n is the number specified during instantiation of the SwapMutation object.

        For each of the n swaps, 2 indices are chosen for each individual by using numpy.random.choice().
        The variable row_indices represents a matrix of two column vectors [0,...,g-1] where g is the number of genes
        in each individual. Both the swap_indices as well as the row_indices are then used to perform the swap using numpy's
        advanced indexing.

        ### Parameters: 
        individuals -- the chosen individuals the mutation should be applied to

        ### Returns:
        mutated_individuals
        """
        assert individuals.ndim == 2
        number_of_individuals, number_of_genes = individuals.shape

        swap_indices = np.random.choice(number_of_genes, size=(self.number_of_swaps, number_of_individuals, 2))
        row_indices = np.tile(np.array([np.arange(number_of_individuals)]).T,(1,2))

        for swap in swap_indices:
            individuals[row_indices,swap] = individuals[row_indices,swap[:,::-1]]
        
        return individuals

class InversionMutation(MutationFunction):
    def mutate(self, individuals: np.ndarray) -> None:
        assert individuals.ndim == 2
        number_of_individuals, number_of_genes = individuals.shape

        for i in range(number_of_individuals):
            p1,p2 = np.random.choice(number_of_genes, size=2, replace=False)
            slice_length = (p2 - p1 + 1) if p2 >= p1 else (number_of_genes - p1) + (p2 + 1)

            rolled_individual = np.roll(individuals[i],-p1) #shift so that p1 is at index 0
            inverted_slice = rolled_individual[:slice_length][::-1] #get the slice and invert
            rolled_individual[:slice_length] = inverted_slice #put inverted slice in individual
            individuals[i] = np.roll(rolled_individual,p1) #shift back
        
        return individuals

class InsertMutation(MutationFunction):
    def mutate(self, individuals: np.ndarray) -> None:
        assert individuals.ndim == 2
        number_of_individuals, number_of_genes = individuals.shape
        for i in range (number_of_individuals):
            p1, p2 = np.sort(np.random.choice(number_of_genes, size=2, replace=False))
            if p1 +1 == p2:
                continue

            moving_element = individuals[i,p2] #get element to be shifted next to p1
            individuals[i,p1+2:p2+1] = individuals[i,p1+1:p2] #shift all element between p1 and p2 one element to the right
            individuals[i,p1+1] = moving_element #place the moving element next to p1
        
        return individuals

