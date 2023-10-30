from abc import ABC, abstractmethod
import numpy as np

"""See 2015_Book_IntroductionToEvolutionaryComp"""

class CrossoverFunction(ABC):
    
    def __init__(self, chromosome_size) -> None:
        self.chromosome_size = chromosome_size

    @abstractmethod
    def perform_crossover(self, parents: np.ndarray) -> np.ndarray:
        pass

class PmxCrossover(CrossoverFunction):
    
    def perform_crossover(self, parents: np.ndarray) -> np.ndarray:
        p1,p2 = np.sort(np.random.randint(self.chromosome_size, size=2))
        children = np.zeros(shape=(2,self.chromosome_size), dtype=int)

        #copy elements within crossover_points from parents to children
        children[:,p1:p2+1] = parents[:,p1:p2+1]
        
        #distribute elements within crossover_points of the other parent
        for other_parent_index in range(2):
            current_child = children[(other_parent_index+1)%2] # get child where elements shall be placed in
            for element_index in range(p1,p2+1):
                #check if element is already in child
                element = parents[other_parent_index, element_index]
                if element in current_child[p1:p2+1]:
                    continue
                
                #determine position in which to place the missing element from the other parent
                occupying_element = current_child[element_index] # get element within the child that is currently at the same index as the element to be placed
                desired_position = np.argwhere(parents[other_parent_index] == occupying_element)[0][0] # get the position of the occupying element within the other parent 
                
                #if the desired position is already occupied, repeat the two lines above until a free slot is found
                while current_child[desired_position] != 0:
                    occupying_element = current_child[desired_position]
                    desired_position = np.argwhere(parents[other_parent_index] == occupying_element)[0] # get the position of the occupying element within the other parent 

                current_child[desired_position] = element #put element in the free slot
        
        #fill empty slots in children with elements at respective index within the other parent.
        empty_slots = np.where(children == 0)
        children[empty_slots] = parents[::-1][empty_slots]

        return children

class EdgeCrossover(CrossoverFunction):
    pass

class OrderCrossover(CrossoverFunction):
    pass

class CycleCrossover(CrossoverFunction):
    pass