# nic_ca1 
The first course assessment of the module "Nature-Inspired Computation" counting towards 40% of the final mark.
It consists of a programming task as well as a report.


### Experiment Operators / Parameters:

##### Distance Matrix
    -Burma
    -Brazil

##### Mutation
    - Swap mutation
    - Inversion mutation
    - Insert mutation
##### Crossover
    - PMX Crossover
    - Order Crossover
    - Crossover with fix
##### Population Size
	- 25
    - 100
    - 500
##### Tournament Size / Ratio to Pop Size
    - 5%
    - 10%
    - 50%
##### Replacement Operator
    - Replace weakest
    - Replace first weakest
##### Crossover probability
    - 30%
    - 80%
##### Mutation probability
	- 15%
	- 50%
	
For each experiment, only one of the parameters / operators will be varied.
Combinatoricly that amounts to: 2 * 3 * 3 * 3 * 3 * 2 * 2 * 2 = 1296 different experiments. 
Because each experiment will be carried out 10 times to ensure that random chance accounts for less variation in the outcome, 12960 runs will be performed for the two datasets.

The configuration section of the main.py file looked as follows for the conducted experimets:

tsp_config = {
    "distance_matrix_names": ["../xml/burma14.xml", "../xml/brazil58.xml"],
    "crossover_functions": [crossover.PmxCrossover, crossover.OrderCrossover, crossover.CrossoverWithFix],
    "mutation_functions":  [mutation.SwapMutation, mutation.InversionMutation, mutation.InsertMutation],
    "replacement_functions": [replacement.ReplaceWeakest, replacement.ReplaceFirstWeakest],
    "mutation_rates": [0.15, 0.5],
    "crossover_rates": [0.3, 0.8],
    "tournament_rates": [0.05, 0.15, 0.5],
    "population_sizes": [25,100,500]
}
runs_per_experiment = 10
iterations_per_run = 10000
