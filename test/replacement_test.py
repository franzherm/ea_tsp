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

#random test
pop = TspPermutationPopulation(10,13)

children = TspPermutationPopulation(2,13)
replacement_function = ReplaceFirstWeakest()

print("Population: \n",pop,"\n")
replacement_function.replace(pop.data, children.data, fitness_function.eval_fitness_ufunc(pop), fitness_function.eval_fitness_ufunc(children))
print("Children: \n",children,"\n")
print("New Pop: \n", pop)

# constructed test
pop = np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]) # population of ten elements
children = np.array([[10],[11],[12]]) # 3 children

cost_pop = np.array([[100],[75],[66],[1000],[24],[3],[111],[356],[647],[100]])
cost_children = np.array([[100],[1],[1001]])

print("\n")
print(pop,"\n")
print(children,"\n")
replaced_indexes = replacement_function.replace(pop,children,cost_pop,cost_children)
assert np.not_equal(pop, [[10],[11],[2],[3],[4],[5],[6],[7],[8],[9]]).sum() == 0
assert np.not_equal(replaced_indexes,[0,1]).sum() == 0

print(replaced_indexes,"\n")
print("pop")