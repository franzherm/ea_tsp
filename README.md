# nic_ca1 
The first course assessment of the module "Nature-Inspired Computation" counting towards 40% of the final mark.
It consists of a programming task as well as a report.


### Experiment Operators / Parameters:

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
Combinatoricly that amounts to: 3 * 3 * 3 * 3 * 2 * 2 * 2 = 648 different experiments. 
Because each experiment will be carried out 10 times to ensure that random chance accounts for less variation in the outcome, 6480 runs will be performed for each of the two datasets.

Questions: 
	- is the optimal population size dependend on the solution space ?
	- for crossover and mutations: one parameter a popular one according to literature, the other one is towards the other end of the spectrum
