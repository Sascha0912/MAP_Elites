import numpy as np
def rastrigin_Variation(parents, d):
    children = []
    for i in range(len(parents)):
        # Mutate
        children[i].genome = parents[i].genome + (np.random.randn(2,1)*d.mutSigma)

        # Bind Values
        children[i].genome[children[i].genome < d.range[0]] = d.range[0]
        children[i].genome[children[i].genome > d.range[1]] = d.range[1]
    
    return children