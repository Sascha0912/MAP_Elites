from domain.rastrigin.rastrigin_RandInd import rastrigin_RandInd
from src.addToMap import addToMap
from src.createMap import createMap1
from src.createChildren import createChildren
from src.visualization.viewMap import viewMap
import numpy as np
def mapElites(**kwargs):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    class Record:
        def __init__(self):
            self.evals    = []
            self.improved = []
            self.map      = []
            
    d        = None
    startMap = []
    visMod   = 2**0
    gifMap   = False
    recMod   = False   

    for key, value in kwargs.items():
        if key=="domain":
            d = value
            print(d)
        elif key=="startMap":
            startMap = value
            print(startMap)
        elif key=="genPerVis":
            visMod = value
            print(visMod)
        elif key=="gifMap":
            gifMap = value
            print(gifMap)
        elif key=="genPerRecord":
            recMod = value
            print(recMod)
    if d is None:
        raise ValueError('Domain is required!')
    
    # Fill initial map
    if len(startMap)!=0:
        map = startMap
    else:
        map = createMap1(d.mapDims,d.sampleInd)
        startPop = feval(d.randInd,d.nInitial,d.recombine)
        fitness, behaviour, misc, startPop = feval(d.evaluate,startPop,d)
        map = addToMap(map,startPop,fitness,behaviour,misc)

    # TODO: create gif

    # MAP-Elites
    nEvals = d.nInitial
    gen    = 1
    while (nEvals <= d.nEvals-d.batchSize):
        # Next three lines is the whole algorithm
        children = createChildren(map, d)
        fitness, behaviour, misc, children = feval(d.evaluate, children, d)
        map, improved = addToMap(map, children, fitness, behaviour, misc)

        # Visualization and Record Keeping
        nEvals = nEvals + len(children)
        gen = gen + 1
        if ~np.remainder(gen,visMod):
            viewMap(map)
            if gifMap:
                print("gif")
                # TODO: gif

        record = Record()
        recorded = []
        if ~np.remainder(gen,recMod):
            recorded[gen]        = True
            record.evals[gen]    = nEvals
            record.improved[gen] = improved
            record.map[gen]      = map
    
    # Clean up data struct
    if recMod:
        record.evals    = record.evals[recorded]
        record.improved = record.improved[recorded]
        record.map      = record.map[recorded]

    # Include method for inspecting individuals in map
    # TODO: implement

    return map, record