import numpy as np
import math
import pandas as pd
def rastrigin_FitnessFunc(pop):
    def rastr(x):
        return (20 + (x**2 - 10.0 * np.cos(2 * math.pi * x)))/40
    genes = []
    for i in range(len(pop)):
        genes.append(pop[i])
    # print(genes)
    df = pd.DataFrame(data=genes)
    df_fitness = pd.DataFrame(data=rastr(df))
    df_fitness = df_fitness.transpose()
    # print(df_fitness)
    return df_fitness