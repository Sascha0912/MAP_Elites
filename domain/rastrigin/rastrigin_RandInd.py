import numpy as np
def rastrigin_RandInd(nInds, d):
    # class RandIndsGenome:
    #     def __init__(self):
    #         self.genome = []
    unitRandom = np.random.rand(2,nInds)
    scaledRandom = (unitRandom*(d.range[1]-d.range[0])) + d.range[0]
    # print(scaledRandom)
    # print(scaledRandom[:][0])
    randInds = []
    for i in range(0,nInds):
        # print(np.array[scaledRandom[0][i],scaledRandom[1][i]])
        # TODO: fix subattribute problem here
        # .genome ??
        randInds.insert(i,[scaledRandom[0][i],scaledRandom[1][i]])
    return randInds