import unittest
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def linearF(x, a, b):
    return a*x+b

def linear3D(x, a, b, c):
    x1,x2 = x
    return a * x1 + b * x2 + c

def linear3dArray(x, a, b, c):
    x1 = x[0]
    x2 = x[1]
    return a * x1 + b * x2 + c

class LeastSquareTest(unittest.TestCase):
    def test___twoDimensionExactMatchLinear(self):
        x_data = np.array([1, 2])
        y_data = np.array([1, 2])

        predictedFunctionParameters = [1, 0]

        functionParameters = curve_fit(linearF, x_data, y_data)

        self.assertAlmostEqual(functionParameters[0].tolist()[0], predictedFunctionParameters[0])
        self.assertAlmostEqual(functionParameters[0].tolist()[1], predictedFunctionParameters[1])


    def test___threeDimensionExactMatchLinear(self):
        x1_data = np.array([1,2,3, 4, 5, 6, 7, 8])
        x2_data = np.array([1,2,3, 4,5, 6, 7, 8])
        y_data = np.array([2, 4, 6, 8,10, 12, 14, 16])

        predictedFunctionParameters = [1, 1, 0]

        functionParameters = curve_fit(linear3D, (x1_data, x2_data), y_data)

        aParameter = functionParameters[0].tolist()[0]
        bParameter = functionParameters[0].tolist()[1]
        cParameter = functionParameters[0].tolist()[2]

        self.assertAlmostEqual(aParameter, predictedFunctionParameters[0], None , None ,0.2)
        self.assertAlmostEqual(bParameter, predictedFunctionParameters[1], None , None ,0.2)
        self.assertAlmostEqual(cParameter, predictedFunctionParameters[2], None , None ,0.2)

    def test___threeDimensionWithNan(self):
        x1_data = np.array([1,2,3, 4, 5, 6, 7, 8])
        x2_data = np.array([1,2,3, 4,5, 6, 7, 8])
        y_data = np.array([2, 4, np.NaN, 8, 10, 12, 14, 16])
        p0 = np.array([1,1,1])
        sigma = np.array([1,1,1, 1,1, 1, 1, 1])

        predictedFunctionParameters = [1, 1, 0]

        functionParameters = curve_fit(linear3D, (x1_data, x2_data), y_data, p0, sigma, False, False)

        aParameter = functionParameters[0].tolist()[0]
        bParameter = functionParameters[0].tolist()[1]
        cParameter = functionParameters[0].tolist()[2]

        self.assertAlmostEqual(aParameter, predictedFunctionParameters[0], None , None ,0.2)
        self.assertAlmostEqual(bParameter, predictedFunctionParameters[1], None , None ,0.2)
        self.assertAlmostEqual(cParameter, predictedFunctionParameters[2], None , None ,0.2)





