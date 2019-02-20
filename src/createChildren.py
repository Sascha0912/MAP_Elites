import numpy as np
import math
def createChildren(map, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    # Remove empty bins from parent pool
    # print("map")
    # print(map)
    # TODO: why is map a tuple? Index 0 is map object, index 1 a float?!
    parentPool = map[0].genomes
    # print("parentPool")
    # print(parentPool)
    # TODO: same here
    parentPool[np.isnan(map[0].fitness)] = []

    # Uniform random selection of parents from parent pool
    parents = parentPool(np.random.randint(len(parentPool),[d.batchSize, d.recombine_parents]))

    # Create new population from parents
    children = feval(d.breedPop, parents, d.recombine)

    return children