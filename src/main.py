from population import TspPermutationPopulation
from evolutionary_algorithm import EvolutionaryAlgorithm
from fitness import FitnessFunction
from city_xml_parser import get_distance_matrix_from_city_xml
from matplotlib import pyplot as plt
import selection
import crossover
import mutation
import replacement
pop = TspPermutationPopulation(100,13)
print(pop,"\n")

fitness_function = FitnessFunction(get_distance_matrix_from_city_xml("../xml/burma14.xml"))
selection_function = selection.TournamentSelection(10)
crossover_function = crossover.PmxCrossover(13)
mutation_function = mutation.SwapMutation(1)
replacement_function = replacement.ReplaceFirstWeakest()

ea = EvolutionaryAlgorithm(pop,fitness_function, selection_function, crossover_function, mutation_function, replacement_function)

data = ea.run(10000)
#print(data)

data.plot.line()
plt.show()