import Function
import math

class OneFirstParameterSquare(Function.Function):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def CalculateValue(self, parameterA, parameterB):
        return self.__a*parameterA*parameterA + self.__b*parameterA + self.__c

class OneSecoundParameterSquare(Function.Function):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def CalculateValue(self, parameterA, parameterB):
        return self.__a*parameterB*parameterB + self.__b*parameterB + self.__c

class TwoParameterSquare(Function.Function):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def CalculateValue(self, parameterA, parameterB):
        return self.__a*parameterA*parameterA + self.__b*parameterA + self.__c + self.__a*parameterB*parameterB + self.__b*parameterB + self.__c 

class FunctionMock(Function.Function):
    def __init__(self, a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c

    def CalculateValue(self, parameterA, parameterB):
        return 0



class Bohachevsky1Function(Function.Function): #maximum f(0,0) = 0 if x_i in <-10,10>
    def CalculateValue(self, x1, x2):
        return -(x1*x1 + 2*x2*x2 - 0.3*math.cos(3*math.pi*x1) - 0.4*math.cos(4*math.pi*x2) + 0.7)

class BoothFunction(Function.Function): #maximum f(1,3) = 0 if x_i in <-10,10>
    def CalculateValue(self, x1, x2):
        return -(math.pow((x1 +2*x2 - 7),2) + pow((2*x1 + x2 -5), 2))

class Bukin4Function(Function.Function): #maximum f(-10,0) = 0 if x1 in <-15,-5> and x2 in <-3,3>
    def CalculateValue(self, x1, x2):
        return -(100*math.pow(x2,2) + 0.01* math.fabs(x1 + 10))

class HimmelblauFunction(Function.Function): #maximum f(3,2) = 0 if x_i in <-5,5>
    def CalculateValue(self, x1, x2):
        return -(math.pow((x1*x1 +x2 - 11),2) +pow((x1 + x2*x2 - 7), 2))