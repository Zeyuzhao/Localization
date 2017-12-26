import numpy as np
from sklearn import neighbors
from python.rssi import *

#load data for beacons
f = open("grid.pckl", "rb")
dataGrid = pickle.load(f)

#Constants
dimX = 3
dimY = 4
numBeacons = 4


gridBeacons = []

for beaconNum in range(numBeacons):
    currentGrid = np.zeros((dimX + 1, dimY + 1))

    for i, a in enumerate(dataGrid.grid):
        for j, b in enumerate(a):
            currentEntry = b.entries[beaconNum].average
            currentGrid[j][i] = currentEntry

    gridBeacons.append(currentGrid)
    # Make data
    X = np.linspace(0, dimX, dimX + 1, True)
    Y = np.linspace(0, dimY, dimY + 1, True)
    X, Y = np.meshgrid(X, Y, indexing='ij')
    Z = currentGrid

X = []
y = []
for i in range(dimX + 1):
    for j in range(dimY + 1):
        currentP = []
        for b in gridBeacons:
            currentP.append(b[i][j])
        X.append(currentP)
        y.append([i, j])
X = np.array(X)
y = np.array(y)


X_test = []
y_test = []



# Add noise to targets
#y[::5] += 1 * (0.5 - np.random.rand(8))

# #############################################################################
# Fit regression model

n_neighbors = 5
for i, weights in enumerate(['distance']):
    #Create kNN Regression Model
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    model = knn.fit(X, y)

    #Test Accuracy of Model
