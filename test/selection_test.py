import sys
import numpy as np
import timeit
sys.path.append('../src')

from city_xml_parser import get_distance_matrix_from_city_xml
from selection import TournamentSelection

distance_matrix = get_distance_matrix_from_city_xml("../xml/burma14.xml")

selfunc = TournamentSelection(tournament_size=5)

selection = np.zeros(100000)
for i in range(100000):
    selection[i] = selfunc.select_parent_from_population(np.arange(20), np.arange(20))

for i in range(20):
    print(f"Element {i} chosen: {np.sum(selection == i)}")