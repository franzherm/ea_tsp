from abc import ABC, abstractmethod
import numpy as np
from population import Population

class SelectionFunction(ABC):
    
    @abstractmethod
    def select_from_population(self, population: Population, fitness: np.ndarray, n: int) -> np.ndarray:
        pass

class TournamentSelection(SelectionFunction):

    def __init__(self, tournament_size: int) -> None:
        self.tournament_size = tournament_size

    def select_from_population(self, population: Population, cost: np.ndarray, n: int) -> np.ndarray:
        assert population.size != 0 #because selection is performed with replacement, the population size does not have to be >= tournament size
        assert n <= self.tournament_size
        
        selected_individuals = np.random.randint(population.size, size=self.tournament_size)
        ranked_indices = np.argsort(cost[selected_individuals]) #rank individuals to get those with the lowest cost
        parents = selected_individuals[ranked_indices[0:n]] #TODO: random selection when cost of multiple individuals is equal
        return parents



