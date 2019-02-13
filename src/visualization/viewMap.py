import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axs
def viewMap(map, value='fitness'):
    eval('mapMat = map.' + value)

    mapRes = np.shape(mapMat)
    edges  = map.edges

    # Plot map values
    # TESTING
    # fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))
    # ax1.imshow(np.flipud(np.rot90(mapMat)))
    # ax1.set()
    imgHandle = plt.matshow(np.flipud(np.rot90(mapMat)))
    

    # Set labels on bin borders instead of centers
    fitPlot = plt.gca()
    plt.xticks(np.linspace(0.5,mapRes[0]+0.5,num=mapRes[0]+1),labels=edges[0])
    plt.yticks(np.linspace(0.5,mapRes[1]+0.5,num=mapRes[1]+1),labels=edges[1][range(-1,1,-1)])
    plt.grid(linestyle='-', linewidth=2)

    # Label Axis
    plt.xlabel(map.label[0])
    plt.ylabel(map.label[1])

    # axs.Axes.set_xticklabels(edges[0])
    # axs.Axes.set_yticklabels(edges[1])
    hcb = plt.colorbar()
    hcb.set_label(value)
    plt.show() 

    # Output handles to graphics objects
    handle = []
    handle[0] = fitPlot
    handle[1] = imgHandle
    handle[2] = hcb

    return handle
