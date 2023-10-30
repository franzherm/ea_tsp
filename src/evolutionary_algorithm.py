
import numpy as np
import pandas as pd
from replacement import ReplacementFunction
from selection import SelectionFunction
from mutation import MutationFunction
from fitness import FitnessFunction
from crossover import CrossoverFunction
from population import Population
from progressbar import progressbar

class EvolutionaryAlgorithm:

    def __init__(self, initial_population: Population, fitness_function: FitnessFunction, selection_function: SelectionFunction,
                 crossover_function: CrossoverFunction, mutation_function: MutationFunction, replacement_function: ReplacementFunction) -> None:
        
        self.population: Population = initial_population
        self.fitness_function: FitnessFunction = fitness_function
        self.selection_function: SelectionFunction = selection_function
        self.crossover_function: CrossoverFunction = crossover_function
        self.mutation_function: MutationFunction = mutation_function
        self.replacement_function: ReplacementFunction = replacement_function

    def run(self, number_of_iterations: int) -> pd.DataFrame:

        #initialise empty numpy array to populate during the run
        column_headers = ["LowestCost","HighestCost","AvgCost"]
        data = np.empty(number_of_iterations,len(column_headers))
        
        with progressbar.ProgressBar(max_value=number_of_iterations) as progress_bar:
            for iteration in range(number_of_iterations):
                #update progress bar
                progress_bar.update(iteration)
                #calculate fitness
                cost = self.fitness_function.eval_fitness(self.population)
                data[iteration] = [cost.min(), cost.max(), cost.mean()]
                #select parents
                parents = np.array([self.selection_function.select_parent_from_population(self.population, cost),
                                    self.selection_function.select_parent_from_population(self.population, cost)])

                #generate children
                children = self.crossover_function.perform_crossover(parents)

                #mutate children
                self.mutation_function.mutate(children)

                #substitute children into population
                self.replacement_function.replace(self.population, children, cost, self.fitness_function.eval_fitness(children))
        #create pandas dataframe with collected data
        df = pd.DataFrame(data, columns=column_headers)
        return df
    