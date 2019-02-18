import numpy as np
import pandas as pd
def nicheCompete(map,fitness,behaviour):
    def sub2ind(array_shape, rows, cols):
        return rows * array_shape[1] + cols
    # def colIdx(list_colnr,mapfit):
    #     list_idx = []
    #     mapfit_t = mapfit.transpose()
    #     for li in list_colnr: # for each column_nr
    #         idx = 0
    #         for i in range(0,len(mapfit_t)):
    #             for j in range(0,len(mapfit_t[i])):
    #                 if idx==li:
    #                     list_idx.append([i,j])
    #                 idx = idx + 1
    #     return list_idx

    # Get bin of each individual beased on behaviour
    nDims = np.shape(behaviour)[0]
    # print(behaviour)
    bin1 = [[] for i in range(nDims)]
    for iDim in range(nDims):
        # print(behaviour.iloc[iDim,:])
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
    mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map.fitness), order='F') # sub2ind(np.shape(map.fitness),bestBin.iloc[0],bestBin.iloc[1])
    # print(mapLinIndx)
    # Compare to already existing samples
    # print(fitness)
    # print(bestIndex)
    # check fitness index -> 0 or 1?
    # print(map.fitness)
    # list_idx = colIdx(mapLinIndx,map.fitness)
    # use reshape to access map only by column index
    mapfit_re = map.fitness.reshape((map.fitness.size, 1))
    # print(mapfit_re)
    # print(fitness.iloc[0][bestIndex])
    # print(mapfit_re[mapLinIndx].transpose().ravel())
    improvement = ~np.greater_equal(fitness.iloc[0][bestIndex],mapfit_re[mapLinIndx].transpose().ravel())# False if fitness.iloc[0][bestIndex]>=mapfit_re[mapLinIndx].transpose() else True
    # print(np.isnan(fitness.iloc[0][bestIndex]))
    improvement[np.isnan(fitness.iloc[0][bestIndex])] = False

    improvement = improvement*1 # convert true to 1 and false to 0
    print(improvement)
    replacement = bestIndex[improvement]
    replaced = mapLinIndx[improvement]

    return replaced, replacement


