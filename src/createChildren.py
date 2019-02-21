import numpy as np
import math
from domain.rastrigin.rastrigin_Variation import rastrigin_Variation
def createChildren(map, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    mapIsTuple = isinstance(map,tuple)
    # Remove empty bins from parent pool

    # Because map is no tuple in first iteration
    if (mapIsTuple):
        # In next iteration its a tuple ((Map object, improved), Record object)
        if (isinstance(map[0], tuple)):
            parentPool = map[0][0].genomes
        else:
            parentPool = map[0].genomes
    else:
        parentPool = map.genomes
    parentPool_re = parentPool.reshape((parentPool.size,1),order='F')
    parentPool_re = parentPool_re[~np.isnan(parentPool_re)]

    # Uniform random selection of parents from parent pool
    selection = np.random.randint(0,high=len(parentPool_re)/2,size=[d.batchSize, d.recombine_parents])
    parents = []
    for sel in selection:
        parents.append(parentPool_re[sel*2])
        parents.append(parentPool_re[sel*2+1])
        
    # Create new population from parents
    children = feval(d.breedPop, parents, d.recombine_range, d.recombine_mutSigma)

    return children