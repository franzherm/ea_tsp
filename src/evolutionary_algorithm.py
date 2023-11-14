import numpy as np
import pandas as pd
from replacement import ReplacementFunction
from selection import SelectionFunction
from mutation import MutationFunction
from fitness import FitnessFunction
from crossover import CrossoverFunction
from population import Population

class EvolutionaryAlgorithm:

    population_metrics_headers = ["LowestCost","HighestCost","AvgCost"]

    def __init__(self, initial_population: Population, fitness_function: FitnessFunction, selection_function: SelectionFunction,
                 crossover_function: CrossoverFunction, mutation_function: MutationFunction, replacement_function: ReplacementFunction,
                 mutation_rate: float = 0.15, crossover_rate: float = 0.8) -> None:
        
        self.population: Population = initial_population
        self.fitness_function: FitnessFunction = fitness_function
        self.selection_function: SelectionFunction = selection_function
        self.crossover_function: CrossoverFunction = crossover_function
        self.mutation_function: MutationFunction = mutation_function
        self.replacement_function: ReplacementFunction = replacement_function

        assert 0 <= mutation_rate <= 1 and 0 <= crossover_rate <= 1, "Both mutation and crossover rate must in the interval [0,1]"

        self.mutation_rate: float = mutation_rate
        self.crossover_rate: float = crossover_rate

    def run(self, number_of_iterations: int) -> np.ndarray:

        #initialise empty numpy array to populate during the run
        data = np.zeros((number_of_iterations, len(EvolutionaryAlgorithm.population_metrics_headers)))
        
        for iteration in range(number_of_iterations):
            #calculate fitness
            cost = self.fitness_function.eval_fitness(self.population.data)
            data[iteration] = [cost.min(), cost.max(), cost.mean()]

            #select two parents
            parent_indexes = np.array([self.selection_function.select_parent_from_population(self.population.size, cost),
                                self.selection_function.select_parent_from_population(self.population.size, cost)])
            parents = self.population.data[parent_indexes]

            #generate children and maybe perform crossover
            children = parents.copy()
            if self.crossover_rate >= np.random.random():
                children = self.crossover_function.perform_crossover(parents)

            #mutate children
            boolean_array = self.mutation_rate >= np.random.random(size=children.shape[0])
            children[boolean_array] = self.mutation_function.mutate(children[boolean_array])

            #substitute children into population
            self.replacement_function.replace(self.population.data, children, cost, self.fitness_function.eval_fitness(children))
        
        #return collected data
        return data
    