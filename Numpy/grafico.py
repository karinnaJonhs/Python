import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([64,77,80,70,78,95,74,65,74,58,50,55])
ypoints = np.array([1.68,1.82,1.68,1.76,1.81,1.81,1.75,1.78,1.66,1.72,1.63,1.58])

xpoints.sort()
ypoints.sort()

plt.plot(xpoints,ypoints)
plt.show()