import numpy as np
def rastrigin_Variation(parents, d_recombine_range, d_recombine_mutSigma):

    children = []
    for i in range(int(len(parents)/2)):
        # Mutate
        children.append(parents[2*i][0] + (np.random.randn()*d_recombine_mutSigma[0]))
        children.append(parents[2*i+1][0] + (np.random.randn()*d_recombine_mutSigma[1]))

        # Bind Values
        if (children[i] < d_recombine_range[0]):
            children[i] = d_recombine_range[0]
        elif (children[i] > d_recombine_range[1]):
            children[i] = d_recombine_range[1]
    
    children = np.array(children).reshape((2,len(children)//2),order='F').transpose()

    return children