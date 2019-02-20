import numpy as np
def rastrigin_Variation(parents, d_recombine_range, d_recombine_mutSigma):
    print("parents")
    print(parents)
    children = []
    for i in range(len(parents)):
        # Mutate
        children[i].genome = parents[i].genome + (np.random.randn(2,1)*d_recombine_mutSigma)

        # Bind Values
        children[i].genome[children[i].genome < d_recombine_range[0]] = d_recombine_range[0]
        children[i].genome[children[i].genome > d_recombine_range[1]] = d_recombine_range[1]
    
    return children