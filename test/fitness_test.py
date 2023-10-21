import sys
import numpy as np
import timeit
sys.path.append('../src')

from population import TspPermutationPopulation
from fitness import FitnessFunction
from city_xml_parser import get_distance_matrix_from_city_xml

distance_matrix = get_distance_matrix_from_city_xml("../xml/burma14.xml")
func = FitnessFunction(distance_matrix)
pop = TspPermutationPopulation(1000,13)


fitness1 = np.apply_along_axis(func.eval_fitness,axis=1, arr=pop.data)
fitness2 = func.eval_fitness_ufunc(pop)

t1 = timeit.Timer(lambda: np.apply_along_axis(func.eval_fitness,axis=1, arr=pop.data)).timeit(number=1000)
t2 = timeit.Timer(lambda: func.eval_fitness_ufunc(pop)).timeit(number=1000)

print("Time 1: ",t1)
print("Time 2:", t2)