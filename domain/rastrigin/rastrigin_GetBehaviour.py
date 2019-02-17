import pandas as pd
def rastrigin_GetBehaviour(pop):
    # print(pop)
    # behaviour = [[] for i in range(64)]
    behaviour = []
    for i in range(len(pop)):
        behaviour.append(pop[i][i])
    # print(behaviour)
    df = pd.DataFrame(data=behaviour)
    df_t = df.transpose()
    # print(df_t)
    # behaviour = [pop.genome]
    return df_t