import numpy as np

class FitnessFunction:
    
    def __init__(self, distance_matrix) -> None:
        self.distance_matrix = distance_matrix
    
    def eval_fitness(self, population: np.ndarray) -> np.ndarray:
        city0 = np.zeros(population.shape[0], dtype=int)
        pop = np.column_stack((city0, population)) # add city 0 to the start of every solution
        pop_shifted = np.column_stack((population, city0)) # add city 0 to the end of every solution

        cost_array = self.distance_matrix[pop,pop_shifted] # retrieve costs for travel between cities at corresponding positions
        return np.sum(cost_array, axis=1) #sum up to get total cost and return