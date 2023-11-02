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
        p1,p2 = np.sort(np.random.randint(self.chromosome_size, size=2)) #determine crossover points
        children = np.zeros(shape=(2,self.chromosome_size), dtype=int) #initialise children

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

class OrderCrossover(CrossoverFunction):
    def perform_crossover(self, parents: np.ndarray) -> np.ndarray:
        p1,p2 = np.sort(np.random.randint(self.chromosome_size, size=2)) #determine crossover points
        children = np.zeros(shape=(2,self.chromosome_size), dtype=int) #initialise children

        #copy elements within crossover_points from parents to children
        children[:,p1:p2+1] = parents[:,p1:p2+1]
        
        #determine missing values for both children
        #shift parents so that the first index is the first element after the second crossover point that wasn't copied to the child
        values_to_insert = np.array([np.roll(parents[0],shift=-(p2+1)),
                                     np.roll(parents[1],shift=-(p2+1))])
        #trim values so that the ones copied to the children are excluded
        number_of_inserted_elements = (p2+1) - p1
        values_to_insert = values_to_insert[:,:(self.chromosome_size - number_of_inserted_elements)]
        #transform from numpy array to python list in order to easily remove elements
        values_to_insert = values_to_insert.tolist()

        #traverse through parents
        for i in range(2):
            parent_index = (p2+1)%self.chromosome_size
            child_index = (p2+1)%self.chromosome_size

            while child_index != p1:
                current_value = parents[i,parent_index]
                if(current_value in values_to_insert[(i+1)%2]):
                    children[(i+1)%2,child_index] = current_value #insert missing value into child
                    child_index = (child_index+1)%self.chromosome_size #increment child index
                    values_to_insert[(i+1)%2].remove(current_value)

                parent_index = (parent_index+1)%self.chromosome_size #increment parent value
                    
        return children


class CrossoverWithFix(CrossoverFunction):
    def perform_crossover(self, parents: np.ndarray) -> np.ndarray:
        crossover_point = np.random.randint(self.chromosome_size)
        children = np.copy(parents) #initialise children

        #perform one point crossover
        children[:,crossover_point:] = parents[::-1,crossover_point:]

        #determine missing elements
        all_elements = np.array([np.arange(start=1,stop=self.chromosome_size+1)]*2)
        missing_elements = [np.setdiff1d(all_elements[0],children[0]).tolist(),np.setdiff1d(all_elements[1],children[1]).tolist()]

        #replace duplicate elements with missing ones
        for i in range (2):
            j = 0
            while len(missing_elements[i]) != 0: #while there are still elements missing in the child
                current_element = children[i,j]
                if current_element in children[i,(j+1):]: #check if current element is a duplicate
                    children[i,j] = missing_elements[i][0] #replace duplicate with first element of missing list
                    missing_elements[i].pop(0)
                j+=1
        return children