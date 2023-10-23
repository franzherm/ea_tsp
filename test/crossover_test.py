import sys
import numpy as np
import timeit
sys.path.append('../src')

from population import TspPermutationPopulation
from crossover import PmxCrossover

pop = TspPermutationPopulation(2,13)
func = PmxCrossover(pop.data.shape[1])

print("Population: \n", pop.data,"\n")

children = func.perform_crossover(pop.data)

print("Children: \n", children, "\n")

t = timeit.Timer(lambda: func.perform_crossover(pop.data)).timeit(10000)
print("Time: ",t)