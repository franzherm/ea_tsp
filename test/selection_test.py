import sys
import numpy as np
import timeit
sys.path.append('../src')

from population import TspPermutationPopulation
from fitness import FitnessFunction
from city_xml_parser import get_distance_matrix_from_city_xml
from selection import TournamentSelection

distance_matrix = get_distance_matrix_from_city_xml("../xml/burma14.xml")
fitfunc = FitnessFunction(distance_matrix)
pop = TspPermutationPopulation(20,13)

fitness = fitfunc.eval_fitness_ufunc(pop)

selfunc = TournamentSelection(5)
selfunc.select_from_population(pop, fitness, 2)