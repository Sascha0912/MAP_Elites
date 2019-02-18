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
    
    [unp_gen] = map.genomes # Delete unnecessary outer list TODO: Where does it come from?
    df_map_genomes = pd.DataFrame(data=unp_gen)
    # print(df_map_genomes)
    # print(df_map_genomes.shape)


    # print("map.genomes")
    # print(map.genomes)
    # print("newInd")
    # print(np.shape(newInd))
    
    df_map_genomes[replaced] = newInd[replacement]

    # Replace Miscellaneous Map values
    for iValues in range(len(map.misc)):
        eval('map.' + map.misc[iValues] + '[replaced] = misc[' + str(iValues) + '][replacement]')

    return map