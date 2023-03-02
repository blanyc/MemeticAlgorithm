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

    def test_IsEndedFirstTime(self):
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
        self.assertFalse(evolution._EvolutionAlgorithm__IsEnded())
        self.assertEqual(evolution._EvolutionAlgorithm__oldBestSpecimen, greatestSample)