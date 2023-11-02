import sys
import numpy as np
import timeit
sys.path.append('../src')

from population import TspPermutationPopulation
from crossover import *

pop = TspPermutationPopulation(2,7)
func = PmxCrossover(pop.data.shape[1])

##print("Population: \n", pop.data,"\n")

#children = func.perform_crossover(pop.data)

#print("Children: \n", children, "\n")

##t = timeit.Timer(lambda: func.perform_crossover(pop.data)).timeit(10000)
#print("Time: ",t)


#Order Crossover#
#print("Parents:\n",pop,"\n")
#func = OrderCrossover(pop.data.shape[1])
#children = func.perform_crossover(pop.data)

#print("Final children: \n", children)

#t2 = timeit.Timer(lambda: func.perform_crossover(pop.data)).timeit(10000)
#print("Time: ",t2)

#Crossover with fix
print("Parents:\n",pop,"\n")
func = CrossoverWithFix(pop.data.shape[1])
children = func.perform_crossover(pop.data)
print("Final children: \n", children)

t3 = timeit.Timer(lambda: func.perform_crossover(pop.data)).timeit(10000)
print("Time: ",t3)