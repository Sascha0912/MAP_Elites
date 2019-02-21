import numpy as np
import pandas as pd
def updateMap(replaced,replacement,map,newInd,fitness,misc):
    mapIsTuple = isinstance(map, tuple)
    # Replace individuals and fitness
    
    # Because map is no tuple in first iteration
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            mapfit_re = map[0][0].fitness.reshape((map[0][0].fitness.size, 1))
        else:
            mapfit_re = map[0].fitness.reshape((map[0].fitness.size, 1))
    else:
        mapfit_re = map.fitness.reshape((map.fitness.size, 1))

    # check if fitness index is 0 or 1?
    mapfit_re[replaced] = fitness.iloc[0][replacement,np.newaxis]

    # Because map is no tuple in first iteration
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            basic_shape = map[0][0].genomes.shape
            map_genomes_re = map[0][0].genomes.reshape((map[0][0].genomes.size, 1))
        else:
            basic_shape = map[0].genomes.shape
            map_genomes_re = map[0].genomes.reshape((map[0].genomes.size, 1))
    else:
        basic_shape = map.genomes.shape
        map_genomes_re = map.genomes.reshape((map.genomes.size, 1))

    for i in range(len(replaced)):
        pos = replaced[i]
        map_genomes_re[2*pos][0] = newInd[replacement[i]][0]
        map_genomes_re[2*pos+1][0] = newInd[replacement[i]][1]

    # map.genomes[replaced] = newInd[replacement]

    # Because map is no tuple in first iteration
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            map[0][0].genomes = map_genomes_re.reshape(basic_shape,order='F')
        else:
            map[0].genomes = map_genomes_re.reshape(basic_shape,order='F')
    else:
        map.genomes = map_genomes_re.reshape(basic_shape,order='F')
    
    # Replace Miscellaneous Map values
    # for iValues in range(len(map.misc)):
        
    #     exec('map.' + map.misc[iValues] + '[replaced] = misc[' + str(iValues) + '][replacement]')

    return map