import EvolutionAlgorithm
import Function
import numpy as np

#Wstępne wyniki badań
initialRadiusRange = np.array([
    20,	                	            22,	            	        24,
    	                21,	            22,	           23,	        24,
    20,	                21,	            22,	           23,	        24,
    	                21,	            22,	           23,	        24,
    20,	                	            22,	           23,	        
    	                21,	            	           23,	        
    20,	                	            22	           
    ])
initialApexRange = np.array([
    20,                                 20,                         20,
                        25,             25,            25,          25,           
    30,                 30,             30,            30,          30,         
                        35,             35,            35,          35,                 
    40,                                 40,            40,                       
                        45,                            45,                       
    50,                                 50                                      
    ])
initialBatchPositions = np.array([
    31.4415507,	    	                30.10682839	,	            26.53418533,
    	                30.72797068	,   27.34780994	,25.96764919,   24.58748845,
    28.76574928,        27.38559208	,   27.36239007	,24.62527059,   22,
                        26.04321348	,   25.67847093	,24.52809642,   20.59249396,
    23.92317908,                        22.97442933	,20.3984732	                ,
                        24.39147735,                 21.29328106,   
    23.87283066,                        20.99491209		
    ])
initialMeltingEfficiency = np.array([
    0.004196197,		                0.004701806,		        0.006949654,
	                    0.004051376,    0.005916613,0.006509153,    0.006590666,
    0.00436076,         0.005379432,    0.007240125,0.004543789,    0.007956745,
	                    0.005597685,    0.005683771,0.006252878,    0.007867689,
    0.00543286,		                    0.006599733,0.007993233,
	                    0.005366741,	            0.006426038,	
    0.005334765,	                    0.007393509	
    ])

#Model dla położenia wsadu
batchPositionsModel = Function.FifthOrderPolynomial()
batchPositionsModel.CurveFitting((initialRadiusRange, initialApexRange),initialBatchPositions)
batchPositionsModel.plotHeatMap((20,25), 1, (20, 55), 5)

#Model dla efektywności topienia
meltingEfficiencyModel = Function.FifthOrderPolynomial()
meltingEfficiencyModel.CurveFitting((initialRadiusRange, initialApexRange),initialMeltingEfficiency)
meltingEfficiencyModel.plotHeatMap((20,30), 1, (20, 80), 5)

#Optymalizacja modelu
#Przeliczenie nowej populacji
    

