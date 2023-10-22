import sys
import numpy as np
import timeit
sys.path.append('../src')

from mutation import SwapMutation

individuals = np.array([np.random.permutation(13) for _ in range(3)])
func = SwapMutation(1)
print("Individuals: \n",individuals,"\n")
swapped_indices = func.mutate(individuals)

print("Swapped Indices: \n", swapped_indices,"\n")
print("Mutated Individuals: \n", individuals)

time = timeit.Timer(lambda: func.mutate(individuals)).timeit(10000)
print("Time:",time)
