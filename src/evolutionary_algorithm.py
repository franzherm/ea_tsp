
import numpy as np
import pandas as pd
from replacement import ReplacementFunction
from selection import SelectionFunction
from mutation import MutationFunction
from fitness import FitnessFunction

class EvolutionaryAlgorithm:

    def __init__(self, selection_function: SelectionFunction, mutation_function: MutationFunction,
                fitness_function: FitnessFunction, replacement_function: ReplacementFunction, population_size: int) -> None:
        
        self.selection_function: SelectionFunction = selection_function
        self.mutation_function: MutationFunction = mutation_function
        self.fitness_function: FitnessFunction = fitness_function
        self.replacement_function: ReplacementFunction = replacement_function
        self.population: np.ndarray = generate_initial_population(population_size)

        self.current_iteration: int = 0

    def optimize() -> pd.DataFrame:
        pass

    
    