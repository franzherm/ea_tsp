import numpy as np

class FitnessFunction:
    
    def __init__(self, distance_matrix) -> None:
        self.distance_matrix = distance_matrix
    
    def eval_fitness(self, solution: np.ndarray) -> np.ndarray:
        assert solution.ndim == 1, "The solution parameter isn't 1-dimensional"
        cost = 0
        index = 1

        #traverse solution and add distance between cities to overall cost
        while index < solution.size:
            cost += self.distance_matrix[solution[index-1]][solution[index]]
            index += 1

        cost+= self.distance_matrix[solution[solution.size-1]][0] # add distance from last city to starting point (city 0)
        cost+= self.distance_matrix[0][solution[0]] # add distance from starting point (city 0) to first city in solution chromosome

        return cost