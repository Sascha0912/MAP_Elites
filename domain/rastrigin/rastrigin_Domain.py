import numpy as np
from collections import namedtuple

def rastrigin_Domain():
    class Domain:
        def __init__(self):
            self.name = 'rastrigin'

            self.evaluate = 'rastrigin_Evaluate'
            self.objFun   = 'rastrigin_FitnessFunc'
            self.getBc    = 'rastrigin_GetBehaviour'
            self.breedPop = 'rastrigin_Variation'
            self.randInd  = 'rastrigin_RandInd'

            # MAP-Elites settings
            self.nInitial  = 2**6
            self.batchSize = 2**6
            self.nEvals    = 2**10

            # TESTING    
            self.mapDims_res = [8,10]
            self.mapDims_label = ['x-coord','y-coord'] 
            self.mapDims_min = [-2, -1]
            self.mapDims_max = [2, 2]
            self.mapDims_misc = ['otherVal1','otherVal2']               

            # Genome
            self.sampleInd_genome = np.full((2,1),np.nan)

            self.recombine_range = [-2, 2]
            self.recombine_mutSigma = [1.0/8, 1.0/10]
            self.recombine_parents = 1

    return Domain()

