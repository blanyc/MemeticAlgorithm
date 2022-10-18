import PowellMethod
import unittest
import Sample
import FunctionToSupportTests



class PowellMethodTest(unittest.TestCase):
    def test___Optimaze1D_FirstDirection(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.OneFirstParameterSquare(-1,0,0)
        sample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        direction = [1, 0]
         
        optimizedSample = powell._PowellMethod__Optimaze1D(sample, direction)

        self.assertTrue(optimizedSample.GetValue() > -0.01)        
        self.assertTrue(optimizedSample.GetValue() < 0.01)

    def test___Optimaze1D_SecoundDirection(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.OneSecoundParameterSquare(-1,0,0)
        sample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        direction = [0, 1]

        optimizedSample = powell._PowellMethod__Optimaze1D(sample, direction)

        self.assertTrue(optimizedSample.GetValue() > -0.01)        
        self.assertTrue(optimizedSample.GetValue() < 0.01)


    def test___Optimaze1D_BothDirection(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.TwoParameterSquare(-1,0,0)
        sample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        direction = [1, 1]

        optimizedSample = powell._PowellMethod__Optimaze1D(sample, direction)

        self.assertTrue(optimizedSample.GetValue() > -0.01)        
        self.assertTrue(optimizedSample.GetValue() < 0.01)

    def test___OptimizeInEachDirection(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.TwoParameterSquare(-1,0,0)
        sample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        direction = [[1, 0], [0, 1]]

        optimizedSample = powell._PowellMethod__OptimizeInEachDirection(sample, direction)

        self.assertTrue(optimizedSample.GetValue() > -0.01)        
        self.assertTrue(optimizedSample.GetValue() < 0.01)

    def test___CalculateConjugateDirection(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.FunctionMock(0,0,0)
        oldSample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        newSample = Sample.Sample(3,5, function, [-10, 10], [-10,10])
        expectedDirection = [0.5, 1]

        newDirection = powell._PowellMethod__CalculateConjugateDirection(oldSample, newSample)
        self.assertListEqual(newDirection, expectedDirection)

    def test___CalculateConjugateDirectionOpposite(self):
        powell = PowellMethod.PowellMethod(4)
        function = FunctionToSupportTests.FunctionMock(0,0,0)
        oldSample = Sample.Sample(3,5, function, [-10, 10], [-10,10])
        newSample = Sample.Sample(1,1, function, [-10, 10], [-10,10])
        expectedDirection = [-0.5, -1]

        newDirection = powell._PowellMethod__CalculateConjugateDirection(oldSample, newSample)
        self.assertListEqual(newDirection, expectedDirection)

    def test___SwapDirection(self):
        powell = PowellMethod.PowellMethod(4)
        initialDirections = [[1,0],[0,1]]
        newDirection = [0.5,1]
        expectedDirections = [[0.5,1],[0,1]]
        expectedDirectionsTwo = [[0.5,1],[0.5,1]]
        powell._PowellMethod__directions = initialDirections

        powell._PowellMethod__SwapDirection(newDirection)

        self.assertListEqual(powell._PowellMethod__directions, expectedDirections)

        powell._PowellMethod__SwapDirection(newDirection)

        self.assertListEqual(powell._PowellMethod__directions, expectedDirectionsTwo)

    def test___Optimaze2D_OneSample(self):
        powell = PowellMethod.PowellMethod(4, 0.4)
        function = FunctionToSupportTests.TwoParameterSquare(-1,0,0)
        sample = Sample.Sample(10.12,-3.87, function, [-10, 10], [-10,10])
        population = [sample]
         
        optimizedSamples = powell.Optimize2D(population)

        resultValue = optimizedSamples[0].GetValue()
        self.assertTrue(resultValue > -0.01)        
        self.assertTrue(resultValue < 0.01)


