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

            # MapDims = namedtuple('Mapdims','res label min max misc')
            # self.mapDims = MapDims([8,10], ['x-coord','y-coord'], [-2, -1], [2, 2], ['otherVal1','otherVal2'])
            
            # self.mapDims.res   = [8, 10]
            # self.mapDims.label = ['x-coord','y-coord']
            # self.mapDims.min   = [-2, -1]
            # self.mapDims.max   = [2, 2]
            # self.mapDims.misc  = ['otherVal1','otherVal2']

            # Genome
            # 

            self.sampleInd_genome = np.full((2,1),np.nan)

            # SampleInd = namedtuple('Sampleind','genome')
            # self.sampleInd = SampleInd(np.full((2,1),np.nan))
            
            # self.sampleInd.genome = np.full((2,1),np.nan)
            

            self.recombine_range = [-2, 2]
            self.recombine_mutSigma = [[1/8], [1/10]]
            self.recombine_parents = 1

            # Recombine = namedtuple('Recombine','range mutSigma parents')
            # self.recombine = Recombine([-2, 2], [[1/8],[1/10]], 1)
            # self.recombine.range    = [-2, 2]
            # self.recombine.mutSigma = [[1/8],[1/10]]
            # self.recombine.parents  = 1
    return Domain()

