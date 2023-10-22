import sys
import numpy as np
sys.path.append('../src')

from mutation import SwapMutation

individuals = np.array([np.random.permutation(13) for _ in range(3)])
func = SwapMutation(1)
print("Individuals: \n",individuals,"\n")
mutated_individuals = func.mutate(individuals)

print("Mutated Individuals: \n", mutated_individuals)