from population import TspPermutationPopulation
from evolutionary_algorithm import EvolutionaryAlgorithm
from fitness import FitnessFunction
from city_xml_parser import get_distance_matrix_from_city_xml
from matplotlib import pyplot as plt
from selection import TournamentSelection
import crossover
import mutation
import replacement
import numpy as np
from tqdm import tqdm

########### Auxiliary functions ###########
def increment_indices(current_indices, max_indices):
    current_indices[-1] += 1
    for i in reversed(range(len(current_indices))):
        if current_indices[i] > max_indices[i]:
            current_indices[i] = 0
            if i != 0:
                current_indices[i-1] +=1
        else:
            break
    return current_indices
#############################################

########### Program configuration ###########
tsp_config = {
    "distance_matrices": [get_distance_matrix_from_city_xml("../xml/burma14.xml"), get_distance_matrix_from_city_xml("../xml/brazil58.xml")],
    "crossover_functions": [crossover.PmxCrossover, crossover.OrderCrossover, crossover.CrossoverWithFix],
    "mutation_functions":  [mutation.SwapMutation, mutation.InversionMutation, mutation.InsertMutation],
    "replacement_functions": [replacement.ReplaceWeakest, replacement.ReplaceFirstWeakest],
    "mutation_rates": [0.15, 0.5],
    "crossover_rates": [0.3, 0.8],
    "tournament_rates": [0.05, 0.10, 0.5],
    "population_sizes": [25,100,500]
}
runs_per_experiment = 5
iterations_per_run = 10000
#############################################


########### Program execution ###########
key_list = dict(zip(tsp_config.keys(),np.arange(len(tsp_config), dtype=int)))
current_parameter_indices = np.zeros(len(tsp_config), dtype= int)
max_parameter_indices = np.array([len(x)-1 for x in tsp_config.values()], dtype=int)
num_of_experiments = np.cumprod(max_parameter_indices + 1)[-1]

#TODO: top dataframe
for _ in tqdm(range(num_of_experiments), desc="Experiments", position=0, leave=False):
    #retrieve config variables for experiment
    CrossoverFunctionClass = tsp_config["crossover_functions"][current_parameter_indices[key_list["crossover_functions"]]]
    MutationFunctionClass = tsp_config["mutation_functions"][current_parameter_indices[key_list["mutation_functions"]]]
    ReplacementFunctionClass = tsp_config["replacement_functions"][current_parameter_indices[key_list["replacement_functions"]]]
    mutation_rate = tsp_config["mutation_rates"][current_parameter_indices[key_list["mutation_rates"]]]
    crossover_rate = tsp_config["crossover_rates"][current_parameter_indices[key_list["crossover_rates"]]]
    tournament_rate= tsp_config["tournament_rates"][current_parameter_indices[key_list["tournament_rates"]]]
    pop_size = tsp_config["population_sizes"][current_parameter_indices[key_list["population_sizes"]]]
    distance_matrix = tsp_config["distance_matrices"][current_parameter_indices[key_list["distance_matrices"]]]

    # deduce additional parameters from config variables
    chromosome_size = distance_matrix.shape[0]-1
    crossover_function = CrossoverFunctionClass(chromosome_size)
    mutation_function = MutationFunctionClass(chromosome_size)
    replacement_function = ReplacementFunctionClass()
    fitness_function = FitnessFunction(distance_matrix)
    selection_function = TournamentSelection(max(1,int(tournament_rate * pop_size)))

    #run experiment
    dataframes = []
    for i in tqdm(range(runs_per_experiment), desc="Runs", position=1, leave=False, smoothing=1):
        pop = TspPermutationPopulation(pop_size, chromosome_size) # no seed specified, which means that a random one is fetched from the OS
        ea = EvolutionaryAlgorithm(pop, fitness_function, selection_function, crossover_function, mutation_function, replacement_function, mutation_rate, crossover_rate)
        df = ea.run(iterations_per_run)
        #dataframes.append(df)

    current_parameter_indices = increment_indices(current_parameter_indices, max_parameter_indices)

    # TODO: compute averages of all dataframes from the same experiment in auxiliary function
    # TODO: append mean dataframe to top dataframe

#TODO: save top dataframe to file
#TODO: write code to display results (possibly in different file and use saved dataframe file for that so that the experiment doesn't have to run again)
