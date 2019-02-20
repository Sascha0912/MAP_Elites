from domain.rastrigin.rastrigin_RandInd import rastrigin_RandInd
from domain.rastrigin.rastrigin_Evaluate import rastrigin_Evaluate
from domain.rastrigin.rastrigin_GetBehaviour import rastrigin_GetBehaviour
from src.addToMap import addToMap
from src.createMap import createMap1
from src.createChildren import createChildren
from src.visualization.viewMap import viewMap
import numpy as np

# TEST
from pprint import pprint
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
        map = createMap1(d.mapDims_res, d.mapDims_label, d.mapDims_min, d.mapDims_max, d.mapDims_misc, d.sampleInd_genome)
        # map.genomes
        # Hier: 16x10 numpy Array -> in MATLAB 8x10 struct mit 2x1 Listen
        # In beiden Fällen sind an dieser Stelle alle Werte mit NaN belegt
        # map.genomes OK

        startPop = feval(d.randInd,d.nInitial, d.recombine_range, d.recombine_mutSigma, d.recombine_parents)

        # startPop
        # Hier: 64x2 numpy Array -> in MATLAB 1x64 struct mit 2x1 Listen
        # In beiden Fällen sind an dieser Stelle alle Werte mit Werten zw. -2 und +2 belegt
        # startPop OK


        # startPop
        # print("startPop")
        # print(startPop)
        # print(d.evaluate)
        # print(startPop)
        # print(d)
        fitness, behaviour, misc, startPop = feval(d.evaluate,startPop,d)
        # print(fitness)
        # VERMUTUNG: fitness values hat deshalb 2x64 format, weil startPop 64x2 ist
        # Hier: 2*64 DataFrame -> in MATLAB 1x64 Array
        # Gelöst erstmal durch fitness Access nur bei Index 0 -> gleiches Format, wie in MATLAB
        # fitness TESTOK

        # print(behaviour)
        # Hier: 2x64 DataFrame -> in MATLAB 2x64 Liste
        # behaviour OK


        # print(misc)
        # Hier: Liste mit 2 Arrays, die jeweils eine Matrix mit einer Zeile enthalten
        # Erstes Array: Werte zw. 0 und <1, Zweites Array: Nur Nullen
        # In MATLAB: Liste mit zwei Listen, die 1x64 Listen enthalten -> ähnliche Werte
        # misc OK
        
        # print(startPop)
        # startPop hat hier immer noch denselben Wert wie oben -> d.evaluate ändert offenbar nichts
        # in MATLAB genau so
        # startPop OK

        map = addToMap(map,startPop,fitness,behaviour,misc)
        # map besteht aus Map-Object und improved-Wert -> Nur Map-Object wird zu diesem Zeitpunkt benötigt
        # print("map")
        # pprint(vars(map[0]))
        # In der map fehlen: Die Attribute otherValue1 und 2 (TODO:wegen gestrichenem Part in updateMap)



    # print("map")
    
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