import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axs
def viewMap(map, value='fitness'):
    # Because map is no tuple in first iteration
    mapIsTuple = isinstance(map, tuple)
    if (value=='fitness'):
        if (mapIsTuple):
            if (isinstance(map[0], tuple)):
                mapMat = map[0][0].fitness
                edges  = map[0][0].edges
            else:
                mapMat = map[0].fitness
                edges  = map[0].edges
        else:
            print("lal")
            mapMat = map.fitness
            edges  = map.edges
    else:
        raise Exception('Unknown value')
    mapRes = np.shape(mapMat)
    

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
    if (mapIsTuple):
        if (isinstance(map[0], tuple)):
            plt.xlabel(map[0][0].label[0])
            plt.ylabel(map[0][0].label[1])
        else:
            plt.xlabel(map[0].label[0])
            plt.ylabel(map[0].label[1])
    else:
        plt.xlabel(map.label[0])
        plt.ylabel(map.label[1])

    # axs.Axes.set_xticklabels(edges[0])
    # axs.Axes.set_yticklabels(edges[1])
    hcb = plt.colorbar()
    hcb.set_label(value)
    plt.show() 

    # Output handles to graphics objects
    handle = []
    handle.append(fitPlot)
    handle.append(imgHandle)
    handle.append(hcb)

    return handle
