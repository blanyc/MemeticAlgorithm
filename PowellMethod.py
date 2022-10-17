import copy
import math


class PowellMethod():

    def __init__(self, maxStepWithoutImprovement, initialOptimizationStep = 0.5):
        self.__initialOptimizationStep = initialOptimizationStep
        self.__maxStepWithoutImprovement = maxStepWithoutImprovement
        self.__IterationPerSample = 0
        self.__directions = [[1,0],[0,1]]

    def Optimize2D(self, population):
        print("2D optimized")
        newPopulation = []
        for sample in population:
            oldSample = copy.deepcopy(sample)
            self.__SetInitialDirection()
            while self.__maxFinded() == False:
                sample = self.__OptimizeInEachDirection(sample, self.__directions)
                newDirection = self.__CalculateConjugateDirection(sample, oldSample)
                oldSample = copy.deepcopy(sample)
                self.__SwapDirection(newDirection)
            newPopulation.append(sample)
        return newPopulation

    def __SetInitialDirection(self):
        self.__directions = [[1,0],[0,1]]
        print("Initial direction seted")

    def __OptimizeInEachDirection(self, sample, directions):
        for direction in directions:
            sample = self.__Optimaze1D(sample, direction)
        print("Optimized in each direction")
        return sample

    def __SwapDirection(self, newDirection):
        if self.__directions[0] == [1,0]:
            self.__directions[0] = newDirection
        else:
            self.__directions[1] = newDirection
        print("Direction swaped")

    def __Optimaze1D(self, sample, direction):
        sampleToOptimize = copy.deepcopy(sample)
       
        currentValue = sampleToOptimize.GetValue()
        stepDirection = 1
        stepWithoutImprovement = 0
        optimizationStep = self.__initialOptimizationStep

        while stepWithoutImprovement<self.__maxStepWithoutImprovement:
            
            sampleToOptimize.SetParameterA(sample.GetParameterA() + optimizationStep*direction[0]*stepDirection)
            sampleToOptimize.SetParameterB(sample.GetParameterB() + optimizationStep*direction[1]*stepDirection)

            if sampleToOptimize.GetValue()<currentValue:
                stepDirection*=(-1)
                stepWithoutImprovement += 1
                optimizationStep *= 0.8
            else:
                sample = copy.deepcopy(sampleToOptimize)
                currentValue = sampleToOptimize.GetValue()
                stepWithoutImprovement = 0

        print("1D optimized")
        return sample

    def __CalculateConjugateDirection(self, sample, oldSample):
        parameterA = oldSample.GetParameterA() - sample.GetParameterA()
        parameterB = oldSample.GetParameterB() - sample.GetParameterB()
        if math.fabs(parameterA)>math.fabs(parameterB):
            denominator = math.fabs(parameterA)
        else:
            denominator = math.fabs(parameterB)

        if denominator ==0: 
            self.SetOptimizationToEnd()
            return [0,0]

        parameterA /= denominator
        parameterB /= denominator

        direction = [parameterA, parameterB]

        print("ConjugateDirection")

        return direction

    def SetOptimizationToEnd(self):
        self.__IterationPerSample = self.__maxStepWithoutImprovement-1


    def __maxFinded(self):
        self.__IterationPerSample += 1
        if self.__IterationPerSample == self.__maxStepWithoutImprovement:
            self.__IterationPerSample = 0
            return True
        else:
            return False