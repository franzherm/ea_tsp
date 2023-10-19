from abc import ABC, abstractmethod
import numpy as np

class Population(ABC):

    data: np.ndarray

    def __init__(self, size: int, chromosome_length: int, random_seed: int =None):
        self.chromosome_length = chromosome_length
        self.size = size

    @abstractmethod
    def is_valid_population(self) -> bool:
        pass
    
    @abstractmethod
    def _generate_initial_population(size: int, chromosome_length: int, random_seed: int):
        pass

    def replace_individual(self, index: int, new_individual: np.ndarray):
        assert new_individual.shape == (1,self.chromosome_length), \
        f"The shape of the new individual should be {(1,self.chromosome_length)} but is {new_individual.shape}"

        self.data[index] = new_individual
        
    def __str__(self) -> str:
        return self.data.__str__()

class TspPermutationPopulation(Population):

    def __init__(self, size: int, chromosome_length: int, random_seed: int = None):
        super().__init__(size, chromosome_length, random_seed)
        self.data = TspPermutationPopulation._generate_initial_population(size, chromosome_length, random_seed)

    def is_valid_population(data: np.ndarray) -> bool:
        return np.apply_along_axis(lambda x: np.unique(x).size == data.shape[1],arr=data, axis=1).all()
    
    def _generate_initial_population(size: int, chromosome_length: int, random_seed: int):
        generator = np.random.default_rng(random_seed)
        return np.asarray([generator.permutation(chromosome_length) for _ in range(size)])