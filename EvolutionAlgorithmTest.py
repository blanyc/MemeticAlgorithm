import unittest
import EvolutionAlgorithm
import Sample
import FunctionToSupportTests
import copy


class EvolutionAlgorithmTestSorted(unittest.TestCase):
    def test_MakeReproduction(self):
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        population = [Sample.Sample(0,0,function, [-10, 10], [-10,10]), 
                      Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(2,4,function, [-10, 10], [-10,10])]
        expectedPopulation = [Sample.Sample(0,0,function, [-10, 10], [-10,10]), 
                              Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                              Sample.Sample(2,4,function, [-10, 10], [-10,10]), 
                              Sample.Sample(0.5,1,function, [-10, 10], [-10,10]), 
                              Sample.Sample(1.5,3,function, [-10, 10], [-10,10])]
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(5)
        evolution._EvolutionAlgorithm__Population = population

        evolution._EvolutionAlgorithm__MakeReproduction()

        self.assertListEqual(expectedPopulation, population)


    def test_MutateChild(self):
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        population = [Sample.Sample(0,0,function, [-10, 10], [-10,10]), 
                      Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(2,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(0.5,1,function, [-10, 10], [-10,10]), 
                      Sample.Sample(1.5,3,function, [-10, 10], [-10,10])]
        newPopulation = copy.deepcopy(population)
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(2)
        evolution._EvolutionAlgorithm__Population = population

        evolution._EvolutionAlgorithm__MutateChild()

        for index in range(0,len(population),1):
            if index < evolution._EvolutionAlgorithm__maxSizeOfPopulation:
                self.assertTrue(population[index] == newPopulation[index])
            else:
                self.assertFalse(population[index] == newPopulation[index])

    def test_Selection(self):
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        greatestSample = Sample.Sample(0,0,function, [-10, 10], [-10,10])
        population = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10]),
                      greatestSample]
        populationLenght = len(population)
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(2)
        evolution._EvolutionAlgorithm__Population = population

        evolution._EvolutionAlgorithm__Selection()

        population = evolution._EvolutionAlgorithm__Population
        newPopulationLenght = len(population)
                  
        self.assertTrue(newPopulationLenght<populationLenght)
        self.assertEqual(evolution._EvolutionAlgorithm__bestSpecimen, greatestSample)

    def test_IsEndedFirstTime_NotEnded(self):
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(7)
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        greatestSample = Sample.Sample(0,0,function, [-10, 10], [-10,10])
        population = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10]),
                      greatestSample]
        evolution._EvolutionAlgorithm__Population = population
        evolution._EvolutionAlgorithm__ActualiseBestSolution()
        self.assertFalse(evolution._EvolutionAlgorithm__IsEnded())
        self.assertEqual(evolution._EvolutionAlgorithm__oldBestSpecimen, greatestSample)

    def test_IsEndedFirstTime_Ended(self):
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(7)
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        greatestSample = Sample.Sample(0,0,function, [-10, 10], [-10,10])
        population = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10]),
                      greatestSample]
        evolution._EvolutionAlgorithm__Population = population
        evolution._EvolutionAlgorithm__wasOldBestSpeciment = True
        evolution._EvolutionAlgorithm__oldBestSpecimen = greatestSample
        evolution._EvolutionAlgorithm__ActualiseBestSolution()
        self.assertTrue(evolution._EvolutionAlgorithm__IsEnded())

    def test_ActualiseBestSolution_FirstTime(self):
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(7)
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        greatestSample = Sample.Sample(0,0,function, [-10, 10], [-10,10])
        population = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10]),
                      greatestSample]
        evolution._EvolutionAlgorithm__Population = population
        evolution._EvolutionAlgorithm__ActualiseBestSolution()
        
        self.assertEqual(evolution._EvolutionAlgorithm__bestSpecimen, greatestSample)

    def test_ActualiseBestSolution(self):
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(7)
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        greatestSample = Sample.Sample(0,0,function, [-10, 10], [-10,10])
        populationWithoutBest = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10])]
        populationWithBest = [Sample.Sample(1,2,function, [-10, 10], [-10,10]), 
                      Sample.Sample(4,4,function, [-10, 10], [-10,10]), 
                      Sample.Sample(5,5,function, [-10, 10], [-10,10]), 
                      Sample.Sample(6,6,function, [-10, 10], [-10,10]), 
                      Sample.Sample(7,7,function, [-10, 10], [-10,10]), 
                      Sample.Sample(8,8,function, [-10, 10], [-10,10]),
                      greatestSample]
        evolution._EvolutionAlgorithm__Population = populationWithoutBest
        evolution._EvolutionAlgorithm__ActualiseBestSolution()
        evolution._EvolutionAlgorithm__Population = populationWithBest
        evolution._EvolutionAlgorithm__ActualiseBestSolution()
        
        self.assertEqual(evolution._EvolutionAlgorithm__bestSpecimen, greatestSample)

    def test_Bohachevsky1Function(self):
        functionUnderTest = FunctionToSupportTests.Bohachevsky1Function() #maximum f(0,0) = 0 if x_i in <-10,10>
        boundaryA = [-10, 10]
        boundaryB = [-10, 10]
        initialPopulation = [Sample.Sample(-10, 10, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-8, 2, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-2, 7, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(-1.23, 4.43, functionUnderTest, boundaryA, boundaryB),
                             Sample.Sample(10, -10, functionUnderTest, boundaryA, boundaryB)]
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation, initialPopulation)
        

        bestSpecimen = evolutionAlgorithm.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.01
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
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation, initialPopulation)

        bestSpecimen = evolutionAlgorithm.Optimize()

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
        maxSizeOfPopulation = 5
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation, initialPopulation)

        bestSpecimen = evolutionAlgorithm.Optimize()

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
        maxSizeOfPopulation = 9
        evolutionAlgorithm = EvolutionAlgorithm.EvolutionAlgorithm(maxSizeOfPopulation, initialPopulation)

        bestSpecimen = evolutionAlgorithm.Optimize()

        result = bestSpecimen.GetValue()
        expectedResult = 0
        acceptableDelta = 0.02
        self.assertGreater(expectedResult, result - acceptableDelta)
        self.assertLess(expectedResult, result + acceptableDelta)
