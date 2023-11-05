from abc import ABC, abstractmethod
import numpy as np

class ReplacementFunction(ABC):

    @abstractmethod
    def replace(self, population: np.ndarray, children: np.ndarray, cost_population: np.ndarray, cost_children: np.ndarray) -> np.ndarray:
        """Replaces individuals in the current population with the same number of children. The Population array is updated in place
        
        ### Parameters: 
        population -- the numpy array containing the current population
        children -- a numpy array with the new solutions that are to ne placed inside the population
        cost_population -- the numpy array containing the cost of each individual in the current population
        cost_children -- a numpy array containing the cost of the children

        ### Returns:
        replaced_indexes -- numpy array with the indexes of the individuals that were replaced by new child solutions

        """
        pass

class ReplaceFirstWeakest(ReplacementFunction):

    def replace(self, population: np.ndarray, children: np.ndarray, cost_population: np.ndarray, cost_children: np.ndarray) -> np.ndarray:
        """Replaces individuals in the current population with the same number of children. The Population array is updated in place
        
        The child array is traversed and each child is placed into the population array at the position 
        of the first individual in the current population whose cost is greater than or equal to that of the child.
        Elements of the children array cannot replace individuals that are also in the children array.
        
        ### Parameters: 
        population -- the numpy array containing the current population
        children -- a numpy array with the new solutions that are to ne placed inside the population
        cost_population -- the numpy array containing the cost of each individual in the current population
        cost_children -- a numpy array containing the cost of the children

        ### Returns:
        replaced_indexes -- numpy array with the indexes of the individuals that were replaced by new child solutions
        """
        
        replaced_indexes = []
        for i in range(children.shape[0]): #traverse through all children
            weaker_individuals = np.argwhere(cost_population >= cost_children[i]) #get elements of population that are worse than particular child
            weaker_individuals = weaker_individuals[~np.isin(weaker_individuals, replaced_indexes)] #exclude positions of children that already replaced a former individual this iteration
            if weaker_individuals.size != 0:
                population[weaker_individuals[0]] = children[i] #replace the first occurence of a weaker individual in the population with the child
                replaced_indexes.append(weaker_individuals[0]) #add index to list of already replaced indexes
        return replaced_indexes
    
class ReplaceWeakest(ReplacementFunction):

    def replace(self, population: np.ndarray, children: np.ndarray, cost_population: np.ndarray, cost_children: np.ndarray) -> np.ndarray:
        """Replaces individuals in the current population with the same number of children. The Population array is updated in place
            
            The children are put into the population array at the positions of the individuals with the highest cost if the children
            have a lower or equally high cost. If multiple individuals in the population have the highest cost, they are chosen randomly.
            
            ### Parameters: 
            population -- the numpy array containing the current population
            children -- a numpy array with the new solutions that are to ne placed inside the population
            cost_population -- the numpy array containing the cost of each individual in the current population
            cost_children -- a numpy array containing the cost of the children

            ### Returns:
            replaced_indexes -- numpy array with the indexes of the individuals that were replaced by new child solutions
            """
        
        replaced_indexes = []
        index_mask = np.zeros(population.shape[0], dtype=int)
        #sort children by ascending cost
        sorted_indexes = np.argsort(cost_children)
        children = children[sorted_indexes]
        cost_children = cost_children[sorted_indexes]

        for i in range(children.shape[0]): #traverse through all the children
            masked_cost_population = np.ma.masked_array(cost_population, mask=index_mask)
            highest_cost = np.max(masked_cost_population)
            
            if highest_cost < cost_children[i]:
                break #stop placing children in array if they are worse than the worst individuals in population

            weakest_individuals = np.argwhere(masked_cost_population == highest_cost).ravel()
            chosen_index = np.random.choice(weakest_individuals,1)[0]
            population[chosen_index] = children[i]
            replaced_indexes.append(chosen_index)
            index_mask[chosen_index] = 1 #remove already replaced indexes from consideration

        return replaced_indexes