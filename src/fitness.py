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
    
    def eval_fitness_ufunc(self, population: np.ndarray) -> np.ndarray:
        city0 = np.zeros(population.data.shape[0], dtype=int)
        pop = np.column_stack((city0, population.data)) # add city 0 to the start of every solution
        pop_shifted = np.column_stack((population.data, city0)) # add city 0 to the end of every solution

        cost_array = self.distance_matrix[pop,pop_shifted]
        fitness_array = np.sum(cost_array, axis=1)
        
        return fitness_array