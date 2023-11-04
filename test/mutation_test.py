import sys
import numpy as np
import timeit
sys.path.append('../src')

from mutation import *
from population import TspPermutationPopulation

#individuals = np.array([np.random.permutation(13) for _ in range(3)])
##func = SwapMutation(1)
#print("Individuals: \n",individuals,"\n")
#swapped_indices = func.mutate(individuals)

#print("Swapped Indices: \n", swapped_indices,"\n")
#print("Mutated Individuals: \n", individuals)

#time = timeit.Timer(lambda: func.mutate(individuals)).timeit(10000)
#print("Time:",time)

#test inversion mutation
individuals = TspPermutationPopulation(3,13).data
func = InversionMutation()
print(individuals,"\n")
func.mutate(individuals)
print(individuals,"\n")
#adapt all mutations so that the same index cannot be selected twice
#test insert mutation
#individuals = TspPermutationPopulation(3,13).data
#func = InsertMutation()
#print(individuals,"\n")
#func.mutate(individuals)
#print(individuals)

