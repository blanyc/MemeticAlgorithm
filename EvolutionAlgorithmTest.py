import unittest
import EvolutionAlgorithm
import Sample
import FunctionToSupportTests
import copy


class EvolutionAlgorithmTestSorted(unittest.TestCase):
    def test_MakeReproduction(self):
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        population = [Sample.Sample(0,0,function), 
                      Sample.Sample(1,2,function), 
                      Sample.Sample(2,4,function)]
        expectedPopulation = [Sample.Sample(0,0,function), 
                              Sample.Sample(1,2,function), 
                              Sample.Sample(2,4,function), 
                              Sample.Sample(0.5,1,function), 
                              Sample.Sample(1.5,3,function)]
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(5)
        evolution._EvolutionAlgorithm__Population = population

        evolution._EvolutionAlgorithm__MakeReproduction()

        self.assertListEqual(expectedPopulation, population)


    def test_MutateChild(self):
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        population = [Sample.Sample(0,0,function), 
                      Sample.Sample(1,2,function), 
                      Sample.Sample(2,4,function), 
                      Sample.Sample(0.5,1,function), 
                      Sample.Sample(1.5,3,function)]
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
        greatestSample = Sample.Sample(0,0,function)
        population = [Sample.Sample(1,2,function), 
                      Sample.Sample(4,4,function), 
                      Sample.Sample(5,5,function), 
                      Sample.Sample(6,6,function), 
                      Sample.Sample(7,7,function), 
                      Sample.Sample(8,8,function),
                      greatestSample]
        populationLenght = len(population)
        evolution = EvolutionAlgorithm.EvolutionAlgorithm(2)
        evolution._EvolutionAlgorithm__Population = population

        evolution._EvolutionAlgorithm__Selection()

        population = evolution._EvolutionAlgorithm__Population
        newPopulationLenght = len(population)
                  
        self.assertTrue(newPopulationLenght<populationLenght)
        self.assertEqual(population.count(greatestSample), 1)
