from abc import ABC, abstractmethod
import numpy as np
from population import Population

class SelectionFunction(ABC):
    
    @abstractmethod
    def select_parent_from_population(self, population: Population, fitness: np.ndarray) -> np.ndarray:
        pass

class TournamentSelection(SelectionFunction):

    def __init__(self, tournament_size: int) -> None:
        self.tournament_size = tournament_size

    def select_parent_from_population(self, population: Population, cost: np.ndarray) -> np.ndarray:
        assert population.size != 0 #because selection is performed with replacement, the population size does not have to be >= tournament size
        
        random_selection = np.random.randint(population.size, size=self.tournament_size) # select tournament_size numbers of solutions from population at random
        lowest_cost = np.min(cost[random_selection]) #determine lowest cost of the selected solutions
        lowest_cost_solutions = random_selection[cost[random_selection] == lowest_cost] # get all solutions with lowest cost
        
        return np.random.choice(lowest_cost_solutions) # choose randomly from selected solutions with lowest cost


