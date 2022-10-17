import Sample
import random

class EvolutionAlgorithm():

	__maxSizeOfPopulation = 5
	__parameterMutator = 0.1

	def __init__(self, maxSizeOfPopulation, parameterMutator = 0.1):
		self.__Population = []
		self.__maxSizeOfPopulation = maxSizeOfPopulation
		self.__parameterMutator = parameterMutator

	def RunAlgorithm(self, population):
		self.__Population = population
		self.__MakeReproduction()
		self.__MutateChild()
		self.__Selection()
		print("Evolution optimized")
		return self.__Population

	def __MakeReproduction(self):
		self.__Population.sort()
		child = []
		for index in range(0,len(self.__Population)-1,1):
			parameterA = (self.__Population[index].GetParameterA() + self.__Population[index+1].GetParameterA())/2
			parameterB = (self.__Population[index].GetParameterB() + self.__Population[index+1].GetParameterB())/2
			child.append(Sample.Sample(parameterA, parameterB, self.__Population[index].function))
		print("Reproduction")
		self.__Population += child

	def __MutateChild(self):
		for index in range(self.__maxSizeOfPopulation, len(self.__Population),1):
			newParameterA = self.__Population[index].GetParameterA() + random.uniform(-self.__parameterMutator,self.__parameterMutator)
			self.__Population[index].SetParameterA(newParameterA) 

			newParameterB = self.__Population[index].GetParameterB() + random.uniform(-self.__parameterMutator,self.__parameterMutator)
			self.__Population[index].SetParameterB(newParameterB) 
		print("Mutated")

	def __Selection(self):
		self.__Population.sort()
		populationAfterSelection = []
		populationAfterSelection.append(self.__Population.pop(0))
		for populationStep in range(0,(self.__maxSizeOfPopulation - 1), 1):
			populationIndex = self.__randomFromPopulation(self.__Population)
			populationAfterSelection.append(self.__Population.pop(populationIndex))
		print("Selection performed")
		self.__Population = populationAfterSelection

	def __randomFromPopulation(self, population):
		denominator = 0
		for i in range(1, len(population)+1, 1):
		    denominator += i
		randomNumber = random.uniform(0,1)
		nominator = len(population)
		backwardCounting = nominator
		for sampleIndex in range(0, len(population), 1):
			if randomNumber < nominator/denominator:
				return sampleIndex
			else:
				backwardCounting -= 1
				nominator += backwardCounting
