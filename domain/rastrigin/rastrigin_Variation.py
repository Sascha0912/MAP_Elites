import numpy as np
def rastrigin_Variation(parents, d_recombine_range, d_recombine_mutSigma):
    # print("parents")
    # print(np.shape(parents))
    # print(parents)

    children = [] # children have same structure as parent with mutated values
    for i in range(int(len(parents)/2)):
        # Mutate
        # print(parents[i])
        children.append(parents[2*i][0] + (np.random.randn()*d_recombine_mutSigma[0]))
        children.append(parents[2*i+1][0] + (np.random.randn()*d_recombine_mutSigma[1]))
        # print(children[i])
        # print(children[i+1])

        # Bind Values
        
        if (children[i] < d_recombine_range[0]):
            children[i] = d_recombine_range[0]
        elif (children[i] > d_recombine_range[1]):
            children[i] = d_recombine_range[1]
        # children[np.where(children[i] < d_recombine_range[0])] = d_recombine_range[0]
        # children[np.where(children[i] > d_recombine_range[1])] = d_recombine_range[1]
        # print("bla")
    # print("children")
    # print(np.shape(children))
    
    children = np.array(children).reshape((2,len(children)//2),order='F').transpose()
    # print("children in variation")
    # print(children)
    return children