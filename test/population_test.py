import sys
import numpy as np
sys.path.append('../src')

from population import TspPermutationPopulation

##Test for validity of population permutation

pop = TspPermutationPopulation(50,13)
print(pop,"\n")
assert TspPermutationPopulation.is_valid_population(pop.data), "Population is not a valid permutation!"

##Test if the random seed is working correctly

pop1 = TspPermutationPopulation(5,13,12345)
print(pop1,"\n")

pop2 = TspPermutationPopulation(5,13,12345)
print(pop2)

assert np.array_equal(pop1.data,pop2.data), "The populations are unequal even though the same random number seed was used!"