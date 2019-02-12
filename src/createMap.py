import numpy as np
import math
def createMap(mapDims, sampleInd):
    class Map:
        def __init__(self):
            self.edges = []

    map = Map()
    for i in range(len(mapDims.res)):
        map.edges[i] = np.linspace(mapDims.min[i], mapDims.max[i], mapDims.res[i]+1)
        map.edges[i][0] = -np.inf
        map.edges[i][-1] = np.inf
    
    map.label = mapDims.label
    map.fitness = np.nan(mapDims.res)
    map.genomes = np.tile(sampleInd, mapDims.res)

    # Include additional values of interest per bin
    map.misc = mapDims.misc
    for iValues in range(len(map.misc)):
        eval('map.' + map.misc[iValues] + ' = np.nan(mapDims.res)')
