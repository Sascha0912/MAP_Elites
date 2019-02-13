import numpy as np
import math
def createChildren(map, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    # Remove empty bins from parent pool
    parentPool = map.genomes[:]
    parentPool[np.isnan(map.fitness)] = []

    # Uniform random selection of parents from parent pool
    parents = parentPool(np.random.randint(len(parentPool),[d.batchSize, d.recombine.parents]))

    # Create new population from parents
    children = feval(d.breedPop, parents, d.recombine)

    return children