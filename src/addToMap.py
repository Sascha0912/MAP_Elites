from src.nicheCompete import nicheCompete
from src.updateMap import updateMap
def addToMap(map, newInd, fitness, behaviour, misc):
    # print(fitness)
    replaced, replacement = nicheCompete(map, fitness, behaviour)
    # print(map.genomes)
    map = updateMap(replaced, replacement, map, newInd, fitness, misc)

    # TEST: delete this
    improved = len(replaced)/len(newInd)

    return map, improved