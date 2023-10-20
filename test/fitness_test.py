import sys
import numpy as np
sys.path.append('../src')

from population import TspPermutationPopulation
from fitness import FitnessFunction
from city_xml_parser import get_distance_matrix_from_city_xml

distance_matrix = get_distance_matrix_from_city_xml("../xml/burma14.xml")
func = FitnessFunction(distance_matrix)
pop = TspPermutationPopulation(100,5)

print(distance_matrix,"\n")
fitness = np.apply_along_axis(func.eval_fitness,axis=1, arr=pop.data)
print(fitness,"\n")
print(pop)