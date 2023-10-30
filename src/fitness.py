import numpy as np

class FitnessFunction:
    
    def __init__(self, distance_matrix) -> None:
        self.distance_matrix = distance_matrix
    
    def eval_fitness(self, population: np.ndarray) -> np.ndarray:
        city0 = np.zeros(population.data.shape[0], dtype=int)
        pop = np.column_stack((city0, population.data)) # add city 0 to the start of every solution
        pop_shifted = np.column_stack((population.data, city0)) # add city 0 to the end of every solution

        cost_array = self.distance_matrix[pop,pop_shifted]
        return np.sum(cost_array, axis=1)