import numpy as np
import pandas as pd
def updateMap(replaced,replacement,map,newInd,fitness,misc):
    # Replace individuals and fitness
    # print("map.fitness")
    # print(map.fitness)
    # print("fitness")
    # print(fitness.iloc[0])
    # print("replaced")
    # print(replaced)
    # print("replacement")
    # print(replacement)
    
    # print("fitness.iloc[0][replacement]")
    # print(fitness.iloc[0][replacement])
    mapfit_re = map.fitness.reshape((map.fitness.size, 1))
    # print("mapfit_re[replaced]")
    # print(mapfit_re[replaced])
    # check if fitness index is 0 or 1?
    mapfit_re[replaced] = fitness.iloc[0][replacement,np.newaxis]
    # print("test map.genomes")
    # print(map.genomes)
    # [unp_gen] = map.genomes # Delete unnecessary outer list TODO: Where does it come from?
    # df_map_genomes = pd.DataFrame(data=map.genomes)
    # print(df_map_genomes)
    # print(df_map_genomes.shape)


    # print("map.genomes")
    # print(map.genomes)
    # print("newInd")
    # print(np.shape(newInd))
    # print("df_map_genomes")
    # print(df_map_genomes)
    basic_shape = map.genomes.shape
    map_genomes_re = map.genomes.reshape((map.genomes.size, 1))
    # print("map_genomes_re")
    # print(map_genomes_re)
    # print("newInd")
    # print(newInd)
    # print("replaced")
    # print(replaced)
    # print("replacement")
    # print(replacement)
    for i in range(len(replaced)):
        pos = replaced[i]
        map_genomes_re[2*pos][0] = newInd[replacement[i]][0]
        map_genomes_re[2*pos+1][0] = newInd[replacement[i]][1]
        # print(i)
        # print(map_genomes_re)
    # map.genomes[replaced] = newInd[replacement]
    map.genomes = map_genomes_re.reshape(basic_shape,order='F')
    # Replace Miscellaneous Map values
    # for iValues in range(len(map.misc)):
        
    #     exec('map.' + map.misc[iValues] + '[replaced] = misc[' + str(iValues) + '][replacement]')

    return map #PROBLEM!!!