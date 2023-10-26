from abc import ABC, abstractmethod
import numpy as np

class ReplacementFunction(ABC):

    @abstractmethod
    def replace(self, population: np.ndarray, children: np.ndarray, cost_population: np.ndarray, cost_children: np.ndarray) -> np.ndarray:
        pass

class ReplaceFirstWeakest(ReplacementFunction):

    def replace(self, population: np.ndarray, children: np.ndarray, cost_population: np.ndarray, cost_children: np.ndarray) -> np.ndarray:
        already_replaced_indexes = []
        for i in range(children.shape[0]): #traverse through all children
            weaker_individuals = np.argwhere(cost_population >= cost_children[i]) #get elements of population that are worse than particular child
            weaker_individuals = weaker_individuals[weaker_individuals not in already_replaced_indexes]
            if weaker_individuals.size != 0:
                population[weaker_individuals[0]] = children[i] #replace the first occurence of a weaker individual in the population with the child
                already_replaced_indexes.append(weaker_individuals[0]) #add index to list of already replaced indexes
        return population