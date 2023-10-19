from abc import ABC, abstractmethod
import numpy as np

class Population(ABC):

    def __init__(self, size: int, chromosome_length: int):
        self.chromosome_length = chromosome_length
        self.size = size
        self.data = Population.__generate_initial_population(size, chromosome_length)

    @abstractmethod
    def is_valid(self) -> bool:
        pass
    
    @abstractmethod
    def __generate_initial_population(size: int, chromosome_length: int):
        pass

    def replace_individual(self, index: int, new_individual: np.ndarray):
        assert new_individual.shape == (1,self.chromosome_length), \
        f"The shape of the new individual should be {(1,self.chromosome_length)} but is {new_individual.shape}"

        self.data[index] = new_individual
        



class TspPermutationPopulation(Population):

    def is_valid(self) -> bool:
        pass

    def __generate_initial_population(size: int, chromosome_length: int):
        pass