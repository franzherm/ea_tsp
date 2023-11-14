# nic_ca1 
This document describes how to execute the evolutionary algorithm developed over the course of the first coursework for the module Nature Inspired Computation.

### File description:
	- src/   contains the sourcecode of the evolutionary algorithm.
	- src/main.py   used to execute the algorithm with a specified set of configurations
	- src/data_analysis.ipynb  used to create plots based on the generated data from the execution of the EA
	- xml/   contains the TSP city trees that are to be optimised by the EA
	- csv/   contains data of the conducted experiments
	- csv/overview_df.csv   contains the used configuration as well as the lowest, average and highest cost of the population for the last iteration averaged over all runs for the specific experiement configuration
	- csv/detailed_df.csv   contains the lowest, average and highest cost of the population for every iteration and for each experiment averaged over all runs for the specific experiement configuration


### Experiment Operators / Parameters:
The following parameter values were explored over the course of the experiments.
##### Distance Matrix
    - Burma
    - Brazil

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
	
For each experiment, only one of the parameters / operators is varied.
Combinatoricly that amounts to: 2 * 3 * 3 * 3 * 3 * 2 * 2 * 2 = 1296 different experiments for the chosen parameter values.
Because each experiment will be carried out 10 times to ensure that random chance accounts for less variation in the outcome, 12960 runs will be performed for the two datasets.

The configuration section of the main.py file looked as follows for the conducted experiments used in the coursework report:

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

to conduct a different set of experiments, simply adjust the values within the tsp_config, runs_per_experiment and iterations_per_run variables to your liking. Each run should take about 2 to 4 seconds depending on the current configuration. An example configuration to try that your machine will be able to complete rather quickly, would be:

tsp_config = {
    "distance_matrix_names": ["../xml/burma14.xml", "../xml/brazil58.xml"],
    "crossover_functions": [crossover.PmxCrossover, crossover.OrderCrossover],
    "mutation_functions":  [mutation.SwapMutation, mutation.InversionMutation],
    "replacement_functions": [replacement.ReplaceFirstWeakest],
    "mutation_rates": [0.5],
    "crossover_rates": [0.8],
    "tournament_rates": [0.15, 0.5],
    "population_sizes": [25,100]
}
runs_per_experiment = 5
iterations_per_run = 10000

This should run a total of 16 experiments with five runs each.


### Running the algorithm:
This section explains how to run the algorithm with the current set of experiment configurations as described in the last section.
The Python version used is: Python 3.10.12.
	- First, install virtualenv if you havn't already using: pip install virtualenv
	- Secondly, create a new virtual python environment by running the command: virtualenv <NAME>
	- A new directory will be created in your current working directory
	- Activate the virtual environment with the command: source <NAME>/bin/activate
	- You should now see the name of your virtual environment surrounded by brackets being displayed at the beginning of the new line in your terminal
	- Install the required modules into the virtual environment by calling: pip install -r requirements.txt
	- Finally, execute the evolutionary algorithm by calling: python3 main.py
	- MAKE SURE THAT YOUR CURRENT WORKING DIRECTORY IS THE src FOLDER, OTHERWISE THE PROGRAM WILL NOT BE ABLE TO LOCATE THE XML FILES

Upon completion of the experiments, the program will create the csv files with the newly generated data, overwriting old csv files if they exist in the csv folder
To display the data, open the file data_analysis.ipynb either by installing jupyter notebook to your python environment or by using the VSCODE extentions
After that, execute the code cells one after the other.
Note that most plots will look very empty when only a few experiements have been conducted.

To show the plots generated by the extensive experiment dataset used for the coursework report, download the csv files from the following link and replace them with the ones that are currently in the csv folder: https://universityofexeteruk-my.sharepoint.com/:f:/g/personal/fh418_exeter_ac_uk/EmkV7TiaUOdApXuhfDicJo4Bj4vf3j4y7Sd8ViQKJr3cMw?e=y42Jgt

