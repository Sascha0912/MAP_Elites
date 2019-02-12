import numpy as np
def rastrigin_RandInd(nInds, d):
    unitRandom = np.random.rand(2,nInds)
    scaledRandom = (unitRandom*(d.range[1]-d.range[0])) + d.range[0]

    randInds = []
    for i in range(0,nInds):
        randInds[i].genome = scaledRandom[:][i]
    return randInds