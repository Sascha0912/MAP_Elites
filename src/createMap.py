import numpy as np
import math
def createMap1(mapDims, sampleInd):
    class Map:
        def __init__(self):
            self.edges = []

    map = Map()
    for i in range(0,len(mapDims.res)):
        map.edges.insert(i,np.linspace(mapDims.min[i], mapDims.max[i], mapDims.res[i]+1)) 
        map.edges[i][0] = -np.inf
        map.edges[i][-1] = np.inf
    
    map.label = mapDims.label
    map.fitness = np.empty(mapDims.res) #np.nan(mapDims.res)
    map.fitness[:] = np.nan
    print(sampleInd) # TODO: check MATLAB here for values
    map.genomes = np.tile(sampleInd, mapDims.res)
    print(map.genomes)
    # Include additional values of interest per bin
    map.misc = mapDims.misc
    for iValues in range(len(map.misc)):
        exec('Map.'+map.misc[iValues]+'=property(np.full(mapDims.res, np.nan))')
        # eval('map.'+map.misc[iValues]+'=np.empty(mapDims.res)')
        # exec('map.'+map.misc[iValues][:]+'=np.nan')
    return map