import xml.etree.ElementTree as ET
import numpy as np

def get_distance_matrix_from_city_xml(filepath: str) -> np.ndarray:
    """Parses TSPLib conforming xml file and returns city distance matrix

    Parameters:
    filepath (str) -- path to a TSPLib xml file

    Returns:
    np.ndarray: city distance matrix
    """
    root = ET.parse(filepath).getroot()
    nodes = root.find("graph").findall("vertex")
    num_of_cities = len(nodes[0])+1 #number of edges of a node + the node itself
    matrix = np.zeros((num_of_cities,num_of_cities)) #initialise distance matrix with all zeros

    #insert distances
    for row in range(num_of_cities):
        for column in range(num_of_cities):
            if(row == column): #edge case: distance from city to itself --> initial value of zero is correct
                continue
            matrix[row][column] = nodes[row][column if column < row else column-1].attrib["cost"]

    return matrix