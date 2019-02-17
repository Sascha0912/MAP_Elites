import numpy as np
def nicheCompete(map,fitness,behaviour):
    def sub2ind(array_shape, rows, cols):
        return rows * array_shape[1] + cols
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
    
    # print(bin1[:][:])
    print(fitness)
    a = np.array([bin1],[fitness]).conj().transpose()
    indxSortOne = np.argsort(a[:][:])
    sortedByFeatureAndFitness = a[indxSortOne,:]
    # print(sortedByFeatureAndFitness)

    u, indxSortTwo = np.unique(sortedByFeatureAndFitness[:][0,1], axis=0, return_index=True)
    bestIndex = indxSortOne[indxSortTwo]
    bestBin = bin1[:][bestIndex]
    mapLinIndx = sub2ind(np.shape(map.fitness),bestBin[0][:],bestBin[1][:])

    # Compare to already existing samples
    improvement = False if fitness[bestIndex]>=map.fitness[mapLinIndx] else True
    improvement[np.isnan[fitness[bestIndex]]] = False
    replacement = bestIndex[improvement]
    replaced = mapLinIndx[improvement]

    return replaced, replacement


