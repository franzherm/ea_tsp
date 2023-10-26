import sys
import numpy as np
import timeit
sys.path.append('../src')

from population import TspPermutationPopulation
from fitness import FitnessFunction
from replacement import ReplaceFirstWeakest
from city_xml_parser import get_distance_matrix_from_city_xml

distance_matrix = get_distance_matrix_from_city_xml("../xml/burma14.xml")
fitness_function = FitnessFunction(distance_matrix)
pop = TspPermutationPopulation(10,13)

children = TspPermutationPopulation(2,13)
replacement_function = ReplaceFirstWeakest()

print("Population: \n",pop,"\n")
replacement_function.replace(pop.data, children.data, fitness_function.eval_fitness_ufunc(pop), fitness_function.eval_fitness_ufunc(children))
print("Children: \n",children,"\n")
print("New Pop: \n", pop)
