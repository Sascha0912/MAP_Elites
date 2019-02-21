from src.nicheCompete import nicheCompete
from src.updateMap import updateMap
def addToMap(map, newInd, fitness, behaviour, misc):
    replaced, replacement = nicheCompete(map, fitness, behaviour)
    map = updateMap(replaced, replacement, map, newInd, fitness, misc)

    improved = len(replaced)/len(newInd)

    return map, improved