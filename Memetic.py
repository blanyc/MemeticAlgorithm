class MemeticAlgirithm():

    def __init__(self, LocalSearchAlgorithm, GlobalSearchAlgorithm, initialPopulation, maxGenerationNumber):
        self.__LocalSearchAlgorithm = LocalSearchAlgorithm
        self.__GlobalSearchAlgorithm = GlobalSearchAlgorithm
        self.__population = initialPopulation
        self.__maxGenerationNumber = maxGenerationNumber
        self.__Generation = 0

    def Optimize(self):
        while self.__IsEnded() == False:
            self.__LocalSearch()
            self.__GlobalSearch()
        self.__population.sort()
        return self.__population[0]

    def __LocalSearch(self):
        self.__population = self.__LocalSearchAlgorithm.Optimize2D(self.__population)

    def __GlobalSearch(self):
        self.__population = self.__GlobalSearchAlgorithm.RunAlgorithm(self.__population)

    def __IsEnded(self):
        self.__Generation+=1
        return (self.__Generation == (self.__maxGenerationNumber+1))
