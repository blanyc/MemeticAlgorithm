import Function

class Sample():
    def __init__(self, parameterA, parameterB, function):
        self.__parameterA = parameterA
        self.__parameterB = parameterB
        self.__value = 0
        self.function = function
        self.__isCalculated = False

    def GetParameterA(self):
        return self.__parameterA

    def SetParameterA(self, parameterA):
        self.__isCalculated = False
        self.__parameterA = parameterA

    def GetParameterB(self):
        return self.__parameterB

    def SetParameterB(self, parameterB):
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

    def __eq__(self, value):
        return self.GetValue()==value.GetValue()