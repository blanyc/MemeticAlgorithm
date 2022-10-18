import unittest
import FunctionToSupportTests

class FunctionTest(unittest.TestCase):
    def test_Bohachevsky1Function(self):
        x1 = 0
        x2 = 0
        expectedResult = 0
        functionUnderTest = FunctionToSupportTests.Bohachevsky1Function()

        result = functionUnderTest.CalculateValue(x1, x2)

        self.assertEqual(expectedResult, result)

    def test_Bohachevsky1FunctionLess(self):
        x1 = -9
        x2 = 9
        resultLessFrom = 0
        functionUnderTest = FunctionToSupportTests.Bohachevsky1Function()

        result = functionUnderTest.CalculateValue(x1, x2)

        self.assertLess(result, resultLessFrom)

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



