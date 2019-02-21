import math
import numpy as np
from domain.rastrigin.rastrigin_FitnessFunc import rastrigin_FitnessFunc
from domain.rastrigin.rastrigin_GetBehaviour import rastrigin_GetBehaviour
def rastrigin_Evaluate(pop, d):
    def feval(funcName,*args):
        return eval(funcName)(*args)
        
    # Get fitness of each individual
    fitness = feval(d.objFun, pop)

    # Get feature coordinates of each individual
    behaviour = feval(d.getBc, pop)

    # Get miscellaneous values of each individual
    miscVal = []
    miscVal.append(np.random.rand(1,len(pop)))
    miscVal.append(np.zeros((1,len(pop))))
       
    return fitness, behaviour, miscVal, pop