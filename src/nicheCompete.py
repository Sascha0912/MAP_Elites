import numpy as np
import pandas as pd
def nicheCompete(map,fitness,behaviour):
    mapIsTuple = isinstance(map, tuple)
    # Get bin of each individual based on behaviour
    nDims = np.shape(behaviour)[0]
    # Because map is no tuple in first iteration
    bin1 = [[] for i in range(nDims)]
    if (mapIsTuple):
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

    a = df_bin1.append(fitness.iloc[0], ignore_index=True).transpose()
    sortedByFeatureAndFitness = a.sort_values(by=[0,1,2])

    indxSortOne = list(sortedByFeatureAndFitness.index.values)
    df_drop_dupl = sortedByFeatureAndFitness.drop_duplicates(subset=[0,1])
    indxSortTwo = list(df_drop_dupl.index.values)

    bestIndex = indxSortTwo
    bestBin = pd.DataFrame(data=df_bin1[bestIndex])
    # Because map is no tuple in first iteration
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map[0][0].fitness), order='F')
            mapfit_re = map[0][0].fitness.reshape((map[0][0].fitness.size, 1))
        else:
            mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map[0].fitness), order='F')
            mapfit_re = map[0].fitness.reshape((map[0].fitness.size, 1))
    else:
        mapLinIndx = np.ravel_multi_index((bestBin.iloc[0]-1,bestBin.iloc[1]-1), dims=np.shape(map.fitness), order='F')
        mapfit_re = map.fitness.reshape((map.fitness.size, 1))

    # Compare to already existing samples
    improvement = ~np.greater_equal(fitness.iloc[0][bestIndex],mapfit_re[mapLinIndx].transpose().ravel())
    improvement[np.isnan(fitness.iloc[0][bestIndex])] = False

    replacement = [bestIndex[i] for i in range(len(bestIndex)) if improvement[improvement.index.values.tolist()[i]]]

    replaced = mapLinIndx[improvement.tolist()]

    return replaced, replacement
