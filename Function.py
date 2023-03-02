from abc import abstractmethod, ABC
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class Function(ABC):
    @abstractmethod
    def CalculateValue(self, parameterA, parameterB):
        pass

class FifthOrderPolynomial(Function):

    def __init__(self):
        self.__a = 1
        self.__b = 1
        self.__c = 1
        self.__d = 1
        self.__e = 1
        self.__f = 1
        self.__g = 1
        self.__h = 1
        self.__i = 1
        self.__j = 1
        self.__k = 1

    def CalculateValue(self, parameterA, parameterB):
        return (parameterA**5*self.__a+parameterA**4*self.__b+parameterA**3*self.__c+parameterA**2*self.__d+parameterA**1*self.__e) + \
            (parameterB**5*self.__f+parameterB**4*self.__g+parameterB**3*self.__h+parameterB**2*self.__i+parameterB**1*self.__j) + self.__k

    def __CalculateValueForCurveFitting(self, x, a, b, c, d, e, f, g, h, i, j, k):
        x1,x2 = x
        return (x1**5*a+x1**4*b+x1**3*c+x1**2*d+x1**1*e) + (x2**5*f+x2**4*g+x2**3*h+x2**2*i+x2**1*j) + k

    def actualizeParameters(self, a, b, c, d, e, f, g, h, i, j, k):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        self.__g = g
        self.__h = h
        self.__i = i
        self.__j = j
        self.__k = k

    def plotHeatMap(self, parameterARange, parameterAStep, parameterBRange, parameterBStep):
        

        parametersA = range(parameterARange[0], parameterARange[1], parameterAStep)
        parametersB = range(parameterBRange[0], parameterBRange[1], parameterBStep)

        values = []
        for i in range(parameterARange[0], parameterARange[1], parameterAStep):
            col = []
            for j in range(parameterBRange[0], parameterBRange[1], parameterBStep):
                col.append(self.CalculateValue(i,j))
            values.append(col)


        fig, ax = plt.subplots()
        im = ax.imshow(values)

        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(parametersB)), labels=parametersB)
        ax.set_yticks(np.arange(len(parametersA)), labels=parametersA)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(parametersA)):
            for j in range(len(parametersB)):
                text = ax.text(j, i, round(values[i][j], 4),
                               ha="center", va="center", color="w")

        ax.set_title("Function aproximation")
        fig.tight_layout()
        plt.show()

    def GetParameters(self):
        return np.array([self.__a,
            self.__b,
            self.__c,
            self.__d,
            self.__e,
            self.__f,
            self.__g,
            self.__h,
            self.__i,
            self.__j,
            self.__k])

    def CurveFitting(self, x, y):
        oldParameters = self.GetParameters()
        functionParameters = curve_fit(self.__CalculateValueForCurveFitting, x, y, oldParameters)
        self.actualizeParameters(
            functionParameters[0][0],
            functionParameters[0][1],
            functionParameters[0][2],
            functionParameters[0][3],
            functionParameters[0][4],
            functionParameters[0][5],
            functionParameters[0][6],
            functionParameters[0][7],
            functionParameters[0][8],
            functionParameters[0][9],
            functionParameters[0][10]
            )