import math
import numpy as np
import matplotlib.pyplot as plt
def viewMap(map, value='fitness'):
    eval('mapMat = map.' + value)

    mapRes = np.shape(mapMat)
    edges  = map.edges

    # Plot map values
    # TESTING
    # fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))
    # ax1.imshow(np.flipud(np.rot90(mapMat)))
    # ax1.set()
    plt.matshow(np.flipud(np.rot90(mapMat)))
    plt.show()
# grid = np.random.random((10,10))
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))
# ax1.imshow(grid, extent=[0,100,0,1])
# ax1.set_title('Default')
# ax2.imshow(grid, extent=[0,100,0,1], aspect='auto')
# ax2.set_title('Auto-scaled Aspect')
# ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
# ax3.set_title('Manually Set Aspect')
# plt.tight_layout()
# plt.show()   
