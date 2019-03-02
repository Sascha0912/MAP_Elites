import numpy as np
import numpy.matlib
import math
def createMap1(mapDims_res, mapDims_label, mapDims_min, mapDims_max, mapDims_misc, sampleInd_genome):
    class Map:
        def __init__(self):
            self.edges = []

    map = Map()
    for i in range(0,len(mapDims_res)):
        map.edges.insert(i,np.linspace(mapDims_min[i], mapDims_max[i], mapDims_res[i]+1))
        map.edges[i][0] = -np.inf
        map.edges[i][-1] = np.inf

    map.label = mapDims_label
    map.fitness = np.empty(mapDims_res)
    map.fitness[:] = np.nan

    map.genomes = np.empty(mapDims_res)

    map.genomes = numpy.matlib.repmat(sampleInd_genome, mapDims_res[0], mapDims_res[1])

    # Include additional values of interest per bin
    map.misc = mapDims_misc
    for iValues in range(len(map.misc)):
        exec('Map.'+map.misc[iValues]+'=property(np.full(mapDims_res, np.nan))')

    return map
