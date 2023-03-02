import Memetic
import Sample
import unittest
import FunctionToSupportTests
import PowellMethod
import EvolutionAlgorithm

class MemeticTest(unittest.TestCase):
    def test_Bohachevsky1Function(self):
        functionUnderTest = FunctionToSupportTests.Bohachevsky1Function() #maximum f(0,0) = 0 if x_i in <-10,10>
        boundaryA = [-10, 10]
        boundaryB = [-10, 10]
        initialPopulation = [Sample.Sample(-10, 10, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-8, 2, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-2, 7, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-1.23, 4.43, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(10, -10, functionUnderTest, boundaryA, boundaryB)]
        maxStepWithoutImprovement = 4
        powellMethod = PowellMethod.PowellMethod(maxStepWithoutImprovement)
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation)
        maxGenerationNumber = 1
        memetic = Memetic.MemeticAlgirithm(powellMethod, evolutionAlgorithm, initialPopulation, maxGenerationNumber)

        bestSpecimen = memetic.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.1
        self.assertGreater(expectedResult, result - acceptableDelta)
        self.assertLess(expectedResult, result + acceptableDelta)

    def test_BoothFunction(self):
        functionUnderTest = FunctionToSupportTests.BoothFunction() #maximum f(1,3) = 0 if x_i in <-10,10>
        boundaryA = [-10, 10]
        boundaryB = [-10, 10]
        initialPopulation = [Sample.Sample(-10, 10, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-8, 2, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-2, 7, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-1.23, 4.43, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(10, -10, functionUnderTest, boundaryA, boundaryB)]
        maxStepWithoutImprovement = 4
        powellMethod = PowellMethod.PowellMethod(maxStepWithoutImprovement)
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation)
        maxGenerationNumber = 1
        memetic = Memetic.MemeticAlgirithm(powellMethod, evolutionAlgorithm, initialPopulation, maxGenerationNumber)

        bestSpecimen = memetic.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.1
        self.assertGreater(expectedResult, result - acceptableDelta)
        self.assertLess(expectedResult, result + acceptableDelta)

    def test_Bukin4Function(self):
        functionUnderTest = FunctionToSupportTests.Bukin4Function()  #maximum f(-10,0) = 0 if x1 in <-15,-5> and x2 in <-3,3>
        boundaryA = [-15, -5]
        boundaryB = [-3, 3]
        initialPopulation = [Sample.Sample(-15, 3, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-8, 2, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-12, -2, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-6.23, 2.43, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-5, -3, functionUnderTest, boundaryA, boundaryB)]
        maxStepWithoutImprovement = 4
        powellMethod = PowellMethod.PowellMethod(maxStepWithoutImprovement)
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation)
        maxGenerationNumber = 1
        memetic = Memetic.MemeticAlgirithm(powellMethod, evolutionAlgorithm, initialPopulation, maxGenerationNumber)

        bestSpecimen = memetic.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.1
        self.assertGreater(expectedResult, result - acceptableDelta)
        self.assertLess(expectedResult, result + acceptableDelta)

    def test_HimmelblauFunction(self):

        functionUnderTest = FunctionToSupportTests.HimmelblauFunction() #maximum f(3,2) = 0 if x_i in <-5,5>
        boundaryA = [-5, 5]
        boundaryB = [-5, 5]
        initialPopulation = [Sample.Sample(-5, 5, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-4, 4, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-2, 3, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-1.23, 4.43, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(5, -5, functionUnderTest, boundaryA, boundaryB)]
        maxStepWithoutImprovement = 5
        powellMethod = PowellMethod.PowellMethod(maxStepWithoutImprovement)
        maxSizeOfPopulation = 9
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation)
        maxGenerationNumber = 300
        memetic = Memetic.MemeticAlgirithm(powellMethod, evolutionAlgorithm, initialPopulation, maxGenerationNumber)

        bestSpecimen = memetic.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.01
        self.assertGreater(expectedResult, result - acceptableDelta)
        self.assertLess(expectedResult, result + acceptableDelta)
