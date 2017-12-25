from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pickle
from python.rssi import *

#load data for beacons
f = open("grid.pckl", "rb")
dataGrid = pickle.load(f)

dimX = 3
dimY = 4
numBeacons = 4
gridBeacons = [0 for x in range(numBeacons)]
fig = plt.figure()

for beaconNum in range(numBeacons):
    currentGrid = np.zeros((dimX + 1, dimY + 1))

    for i, a in enumerate(dataGrid.grid):
        for j, b in enumerate(a):
            currentEntry = b.entries[beaconNum].average
            currentGrid[j][i] = currentEntry

    gridBeacons[beaconNum] = currentGrid
    # Make data.
    X = np.linspace(0, dimX, dimX + 1, True)
    Y = np.linspace(0, dimY, dimY + 1, True)
    X, Y = np.meshgrid(X, Y, indexing='ij')
    Z = currentGrid

    # Plot the surface.
    ax = fig.add_subplot(2, 2, beaconNum + 1, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    plt.title("Beacon {} RSSI Signal".format(beaconNum))
    # Customize the z axis.
    ax.set_zlim(-70, 0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()




