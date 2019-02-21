# demo - MAP-Elites demo usage script
from domain.rastrigin.rastrigin_Domain import rastrigin_Domain
# from domain.rastrigin.rastrigin_RandInd import rastrigin_RandInd
from src.mapElites import mapElites
import matplotlib.pyplot as plt
import numpy as np
from src.visualization.viewMap import viewMap

# Time Tracking
import time
current_milli_time = lambda: int(round(time.time() * 1000))

# Load problem domain
d = rastrigin_Domain()

# Run MAP-Elites with default parameters
map = mapElites(domain=d)
map = mapElites(domain=d, startMap=map)

# Increase resolution and number of children
d.mapDims_res = [20, 25] # Set resolution of map
d.nEvals      = 2**13    # Set evaluation budget
d.nInitial    = 2**7     # Set number of initial random samples
d.batchSize   = 2**8     # Set number of children to create at one time

# t1 = current_milli_time()
map = mapElites(domain=d)
# t2 = current_milli_time()
# print("mapElites(domain=d) took: " + str(t2-t1))

# Run at higher res
d.mapDims_res = [100, 100]
d.nEvals      = 2**16
d.nInitial    = 2**7
d.batchSize   = 2**9

map = mapElites(domain=d,genPerVis=0) # Don't watch every generation 

# Don't watch at all, just at end
map = mapElites(domain=d,genPerVis=2**3,gifMap='rastMap.gif')

## Save progress as data
map, record = mapElites(domain=d,genPerVis=0,genPerRecord=2**3)

## Display run details from record
plt.subplot(2,1,1)
plt.plot(record.evals,record.improved)
plt.title('Rate of Improvement')
plt.xlabel('Function Evaluations (log scale)')
plt.ylabel('Proportion of Newly Created\nChildren Entering Map')
plt.grid()

eights = np.arange(len(record.evals)/8,len(record.evals),len(record.evals)/8)
for i in range(8):
    plt.subplot(4,4,8+i)
    id = eights[i]
    h = viewMap(record.map[id]) # Alter graphics afterward
    # TODO: viewMap implementation and process returned obj
    plt.title('Eval ' + str(record.evals[id]))


