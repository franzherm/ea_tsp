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
import pandas as pd
from tqdm import tqdm
import os

################ Auxiliary functions ################
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
####################################################
############## Program configuration ###############
tsp_config_real = {
    "distance_matrix_names": ["../xml/burma14.xml", "../xml/brazil58.xml"],
    "crossover_functions": [crossover.PmxCrossover, crossover.OrderCrossover, crossover.CrossoverWithFix],
    "mutation_functions":  [mutation.SwapMutation, mutation.InversionMutation, mutation.InsertMutation],
    "replacement_functions": [replacement.ReplaceWeakest, replacement.ReplaceFirstWeakest],
    "mutation_rates": [0.15, 0.5],
    "crossover_rates": [0.3, 0.8],
    "tournament_rates": [0.05, 0.10, 0.5],
    "population_sizes": [25,100,500]
}
tsp_config = {
    "distance_matrix_names": ["../xml/burma14.xml"],
    "crossover_functions": [crossover.PmxCrossover],
    "mutation_functions":  [mutation.SwapMutation],
    "replacement_functions": [replacement.ReplaceWeakest],
    "mutation_rates": [0.15],
    "crossover_rates": [0.3],
    "tournament_rates": [0.05],
    "population_sizes": [25,100,500]
}
runs_per_experiment = 1
iterations_per_run = 10000
####################################################
########### Compute auxiliary parameters ###########
distance_matrices = [get_distance_matrix_from_city_xml(x) for x in tsp_config["distance_matrix_names"]]
key_list = dict(zip(tsp_config.keys(),np.arange(len(tsp_config), dtype=int)))
index_to_key_dict = inv_map = {v: k for k, v in key_list.items()}
current_parameter_indices = np.zeros(len(tsp_config), dtype= int)
max_parameter_indices = np.array([len(x)-1 for x in tsp_config.values()], dtype=int)
num_of_experiments = np.cumprod(max_parameter_indices + 1)[-1]
column_headers = EvolutionaryAlgorithm.population_metrics_headers
column_header_length = len(column_headers)
####################################################
################### Data storage ###################
data_overview = np.empty(shape=(num_of_experiments,column_header_length))
data_detailed = np.empty(shape=(num_of_experiments,iterations_per_run, column_header_length))
data_parameter_values = []
####################################################
################ Program execution #################
for experiment_index in tqdm(range(num_of_experiments), desc="Experiments", position=0, leave=False):
    #retrieve config variables for experiment
    CrossoverFunctionClass = tsp_config["crossover_functions"][current_parameter_indices[key_list["crossover_functions"]]]
    MutationFunctionClass = tsp_config["mutation_functions"][current_parameter_indices[key_list["mutation_functions"]]]
    ReplacementFunctionClass = tsp_config["replacement_functions"][current_parameter_indices[key_list["replacement_functions"]]]
    mutation_rate = tsp_config["mutation_rates"][current_parameter_indices[key_list["mutation_rates"]]]
    crossover_rate = tsp_config["crossover_rates"][current_parameter_indices[key_list["crossover_rates"]]]
    tournament_rate= tsp_config["tournament_rates"][current_parameter_indices[key_list["tournament_rates"]]]
    pop_size = tsp_config["population_sizes"][current_parameter_indices[key_list["population_sizes"]]]
    distance_matrix_name = tsp_config["distance_matrix_names"][current_parameter_indices[key_list["distance_matrix_names"]]]
    distance_matrix = distance_matrices[current_parameter_indices[key_list["distance_matrix_names"]]]

    # deduce additional parameters from config variables
    chromosome_size = distance_matrix.shape[0]-1
    crossover_function = CrossoverFunctionClass(chromosome_size)
    mutation_function = MutationFunctionClass(chromosome_size)
    replacement_function = ReplacementFunctionClass()
    fitness_function = FitnessFunction(distance_matrix)
    selection_function = TournamentSelection(max(1,int(tournament_rate * pop_size)))

    #run experiment
    experiment_data = np.zeros(shape=(runs_per_experiment,iterations_per_run, column_header_length))
    for i in tqdm(range(runs_per_experiment), desc="Runs", position=1, leave=False, smoothing=1):
        pop = TspPermutationPopulation(pop_size, chromosome_size) # no seed specified, which means that a random one is fetched from the OS
        ea = EvolutionaryAlgorithm(pop, fitness_function, selection_function, crossover_function, mutation_function, replacement_function, mutation_rate, crossover_rate)
        experiment_data[i] = ea.run(iterations_per_run)

    #increment indices
    current_parameter_indices = increment_indices(current_parameter_indices, max_parameter_indices)

    #fetch experiment data
    #average data from the individual runs
    data_detailed[experiment_index] = np.average(experiment_data,axis=0)
    #configuration of experiment
    data_parameter_values.append([distance_matrix_name,
                                  CrossoverFunctionClass.__name__,
                                  MutationFunctionClass.__name__,
                                  ReplacementFunctionClass.__name__,
                                  mutation_rate, crossover_rate, tournament_rate, pop_size])

# populate data_overview array
data_overview[:,0] = data_detailed[:,-1,0]
data_overview[:,1] = data_detailed[:,-1,1]
data_overview[:,2] = data_detailed[:,-1,2]
####################################################
##################### Save Data ####################
if not os.path.exists("../csv"):
    os.makedirs("../csv")

configuration_frame = pd.DataFrame(data_parameter_values, columns=list(tsp_config.keys()))
result_frame = pd.DataFrame(data_overview, columns=column_headers)

overview_df = pd.concat([configuration_frame, result_frame], axis=1)
overview_df.to_csv("../csv/overview_df.csv")
pd.set_option('display.max_columns', None); 
print(overview_df)
#TODO: save top dataframe to file
#TODO: write code to display results (possibly in different file and use saved dataframe file for that so that the experiment doesn't have to run again)
