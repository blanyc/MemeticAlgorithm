import Memetic
import Sample
import unittest
import FunctionToSupportTests

class MemeticTest(unittest.TestCase):
    def test_Bohachevsky1Function(self):
        expectedX1 = 0
        expectedX2 = 0
        expectedResult = 0
        functionUnderTest = FunctionToSupportTests.Bohachevsky1Function() #maximum f(0,0) = 0 if x_i in <-10,10>
        initialPopulation = [Sample.Sample(-10, 10, functionUnderTest),
                             Sample.Sample(-8, 2, functionUnderTest),
                             Sample.Sample(-2, 7, functionUnderTest),
                             Sample.Sample(-1.23, 4.43, functionUnderTest),
                             Sample.Sample(10, -10, functionUnderTest)]
        memetic = Memetic.MemeticAlgirithm(initialPopulation)

        bestSpecimen = memetic.Optimize()

        self.assertEqual(expectedResult, result)

    def test_BoothFunction(self):
        x1 = 1
        x2 = 3
        expectedResult = 0
        functionUnderTest = FunctionToSupportTests.BoothFunction()

        result = functionUnderTest.CalculateValue(x1, x2)

        self.assertEqual(expectedResult, result)

    def test_Bukin4Function(self):
        x1 = -10
        x2 = 0
        expectedResult = 0
        functionUnderTest = FunctionToSupportTests.Bukin4Function()

        result = functionUnderTest.CalculateValue(x1, x2)

        self.assertEqual(expectedResult, result)

    def test_HimmelblauFunction(self):
        x1 = 3
        x2 = 2
        expectedResult = 0
        functionUnderTest = FunctionToSupportTests.HimmelblauFunction()

        result = functionUnderTest.CalculateValue(x1, x2)

        self.assertEqual(expectedResult, result)



