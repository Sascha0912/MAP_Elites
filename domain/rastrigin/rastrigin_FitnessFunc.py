import numpy as np
def rastrigin_FitnessFunc(pop):
    genes = [pop.genome]
    fitness = (20 + sum(genes**2 - 10.0 * np.cos(2 * np.pi * genes),2))/40
    fitness = fitness.transpose()