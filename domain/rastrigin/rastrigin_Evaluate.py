from math import *
import numpy as np
def rastrigin_Evaluate(pop, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
    # Get fitness of each individual
    fitness = feval(d.objFun, pop)

    # Get feature coordinates of each individual
    behaviour = feval(d.getBc, pop)

    # Get miscellaneous values of each individual
    miscVal = []
    miscVal[0] = np.random.rand(1,len(pop))
    miscVal[1] = np.zeros(1,len(pop))
       
    return fitness, behaviour, miscVal, pop
    # miscVal{1} = rand (1,length(pop));
    # miscVal{2} = zeros(1,length(pop));