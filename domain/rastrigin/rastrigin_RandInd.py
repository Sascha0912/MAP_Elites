import numpy as np
def rastrigin_RandInd(nInds, recombine_range, recombine_mutSigma, recombine_parents):
    # class RandIndsGenome:
    #     def __init__(self):
    #         self.genome = []
    unitRandom = np.random.rand(2,nInds)
    scaledRandom = (unitRandom*(recombine_range[1]-recombine_range[0])) + recombine_range[0]
    # print(scaledRandom)
    # print(scaledRandom[:][0])
    randInds = []
    for i in range(0,nInds):
        # print(np.array[scaledRandom[0][i],scaledRandom[1][i]])
        # TODO: fix subattribute problem here
        # .genome ??
        genome = [scaledRandom[0][i],scaledRandom[1][i]] #changed from dict of list to list
        randInds.insert(i,genome)
    return randInds