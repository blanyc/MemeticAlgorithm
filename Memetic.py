import PowellMethod
import EvolutionAlgorithm

class MemeticAlgirithm():
    __Generation = 0

    def __init__(self, initialPopulation):
        self.__LocalSearchAlgorithm = PowellMethod.PowellMethod()
        self.__GlobalSearchAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm()
        self.__population = initialPopulation

    def Optimize(self):
        print("Optimization starter")
        while self.__IsEnded() == False:
            self.__LocalSearch()
            self.__GlobalSearch()
        self.__population.sort()
        return self.__population[0]

    def __LocalSearch(self):
        print("Local search starter")
        self.__population = self.__LocalSearchAlgorithm.Optimize2D(self.__population)

    def __GlobalSearch(self):
        print("Global search starter")
        self.__population = self.__GlobalSearchAlgorithm.RunAlgorithm(self.__population)

    def __IsEnded(self):
        print("End condition veryfied")
        self.__Generation+=1
        return (self.__Generation != 1)
