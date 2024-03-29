import Function
import matplotlib.pyplot as plt
import numpy as np

class Sample():
    def __init__(self, parameterA, parameterB, function, boudaryA, boudaryB):
        self.__parameterA = parameterA
        self.__parameterB = parameterB
        self.__value = 0
        self.function = function
        self.__isCalculated = False
        self.__boudaryA = boudaryA
        self.__boudaryB = boudaryB

    def GetParameterA(self):
        return self.__parameterA

    def SetParameterA(self, parameterA):
        if self.__boudaryA[0]<parameterA and parameterA<self.__boudaryA[1]:
            self.__isCalculated = False
            self.__parameterA = parameterA

    def GetParameterB(self):
        return self.__parameterB

    def SetParameterB(self, parameterB):
        if self.__boudaryB[0]<parameterB and parameterB<self.__boudaryB[1]:
            self.__isCalculated = False
            self.__parameterB = parameterB

    def GetValue(self):
        if self.__isCalculated == False:
            self.__CalculateValue()
        return self.__value

    def __CalculateValue(self):
        self.__value = self.function.CalculateValue(self.__parameterA, self.__parameterB)
        self.__isCalculated = True

    def __gt__(self, value):
        return self.GetValue()<value.GetValue()

    def __lt__(self, value):
        return self.GetValue()>value.GetValue()

    def __eq__(self, value):
        return self.GetValue()==value.GetValue()

def plotPopulationOfSamples(population):
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    n = 100

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for sample in population:
        xs = sample.GetParameterA()
        ys = sample.GetParameterB()
        zs = sample.GetValue()
        ax.scatter(xs, ys, zs)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()