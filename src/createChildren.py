import numpy as np
import math
from domain.rastrigin.rastrigin_Variation import rastrigin_Variation
def createChildren(map, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    # Remove empty bins from parent pool
    # print("map")
    # print(map)
    parentPool = map[0].genomes
    # print("parentPool")
    # print(parentPool)
    # print(parentPool)
    basic_shape = parentPool.shape
    parentPool_re = parentPool.reshape((parentPool.size,1),order='F')

    # print("parentPool_re Before")
    # print(parentPool_re)
    parentPool_re = parentPool_re[~np.isnan(parentPool_re)]
    # parentPool_re is now row vector and not column vector anymore
    # print("parentPool_re After")
    # print(parentPool_re)

    # parentPool[np.isnan(map[0].fitness)] = []

    # Uniform random selection of parents from parent pool
    # !! parentPool is always =0 mod 2
    selection = np.random.randint(0,high=len(parentPool_re)/2,size=[d.batchSize, d.recombine_parents])
    parents = []#parentPool_re[selection]
    for sel in selection:
        parents.append(parentPool_re[sel*2])
        parents.append(parentPool_re[sel*2+1])
    # print("selction")
    # print(selection)
    # print("parents")
    # print(parents)
    # Create new population from parents
    children = feval(d.breedPop, parents, d.recombine_range, d.recombine_mutSigma)

    return children