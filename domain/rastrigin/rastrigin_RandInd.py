import numpy as np
def rastrigin_RandInd(nInds, recombine_range, recombine_mutSigma, recombine_parents):
    unitRandom = np.random.rand(2,nInds)
    scaledRandom = (unitRandom*(recombine_range[1]-recombine_range[0])) + recombine_range[0]

    randInds = []
    for i in range(0,nInds):
        genome = [scaledRandom[0][i],scaledRandom[1][i]]
        randInds.insert(i,genome)
    return randInds