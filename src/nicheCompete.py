import numpy as np
import pandas as pd
def nicheCompete(map,fitness,behaviour):
    mapIsTuple = isinstance(map, tuple)
    # Get bin of each individual beased on behaviour
    print("behaviour")
    print(behaviour)
    nDims = np.shape(behaviour)[0]
    print("nDims")
    print(nDims)
    # Because map is no tuple in first iteration
    bin1 = [[] for i in range(nDims)]
    if (mapIsTuple):
        # TEST
        if (isinstance(map[0], tuple)):
            for iDim in range(nDims):
                bin1[iDim][:] = np.digitize(behaviour.iloc[iDim,:],map[0][0].edges[iDim])
        else:
            for iDim in range(nDims):
                bin1[iDim][:] = np.digitize(behaviour.iloc[iDim,:],map[0].edges[iDim])
    else:
        for iDim in range(nDims):
            bin1[iDim][:] = np.digitize(behaviour.iloc[iDim,:],map.edges[iDim])    
    
    # Get best in each bin
    # * First sort by bin then fitness (best fitness first)
    # * Then remove all but the first (highest fitness) for each bins combo
    
    df_bin1 = pd.DataFrame(data=bin1)
    # print(df_bin1)
    # print(fitness)
    # a = np.array([bin1],[fitness]).conj().transpose()
    # check fitness DataFrame index -> could be 0 or 1?
    a = df_bin1.append(fitness.iloc[0], ignore_index=True).transpose()
    # print(a)
    # indxSortOne = np.argsort(a[:][:])
    print(a)
    sortedByFeatureAndFitness = a.sort_values(by=[0,1,2])
    # print(sortedByFeatureAndFitness)
    indxSortOne = list(sortedByFeatureAndFitness.index.values)
    # print(indxSortOne)
    df_drop_dupl = sortedByFeatureAndFitness.drop_duplicates(subset=[0,1])
    indxSortTwo = list(df_drop_dupl.index.values)
    # print(indxSortTwo)
    bestIndex = indxSortTwo
    # print(bestIndex)
    bestBin = pd.DataFrame(data=df_bin1[bestIndex]) # bin1[:][bestIndex]
    # print(bestBin.iloc[0])
    # print(bestBin.iloc[1])
    # print(np.shape(map.fitness))
    # Because map is no tuple in first iteration
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map[0][0].fitness), order='F') # sub2ind(np.shape(map.fitness),bestBin.iloc[0],bestBin.iloc[1])
            mapfit_re = map[0][0].fitness.reshape((map[0][0].fitness.size, 1))
        else:
            mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map[0].fitness), order='F') # sub2ind(np.shape(map.fitness),bestBin.iloc[0],bestBin.iloc[1])
            mapfit_re = map[0].fitness.reshape((map[0].fitness.size, 1))
    else:
        mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map.fitness), order='F')
        mapfit_re = map.fitness.reshape((map.fitness.size, 1))
    # print(mapLinIndx)
    # Compare to already existing samples
    # print(fitness)
    # print(bestIndex)
    # check fitness index -> 0 or 1?
    # print(map.fitness)
    # list_idx = colIdx(mapLinIndx,map.fitness)
    # use reshape to access map only by column index

    #mapfit_re = map.fitness.reshape((map.fitness.size, 1))
    
    # print(mapfit_re)
    # print(fitness.iloc[0][bestIndex])
    # print(mapfit_re[mapLinIndx].transpose().ravel())
    improvement = ~np.greater_equal(fitness.iloc[0][bestIndex],mapfit_re[mapLinIndx].transpose().ravel())# False if fitness.iloc[0][bestIndex]>=mapfit_re[mapLinIndx].transpose() else True
    # print(np.isnan(fitness.iloc[0][bestIndex]))
    improvement[np.isnan(fitness.iloc[0][bestIndex])] = False
    
    # improvement = improvement*1 # convert true to 1 and false to 0
    # print("improvement")
    # print(improvement)
    # print(repl)
    # print("bestIndex")
    # print(bestIndex)
    replacement = [bestIndex[i] for i in range(len(bestIndex)) if improvement[improvement.index.values.tolist()[i]]]
    # print("replacement")
    # print(replacement)
    replaced = mapLinIndx[improvement.tolist()]
    # print("replaced")
    # print(replaced)

    return replaced, replacement


