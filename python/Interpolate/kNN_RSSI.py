import numpy as np
from sklearn import neighbors
from python.rssi import *
import csv
import pandas as pd

#Constants
dimX = 3
dimY = 4
numBeacons = 4

testFile = "testPoints.csv"
pickleGrid = "grid.pckl"

###################################################################
# Process Data for Regression Model

f = open(pickleGrid, "rb")
dataGrid = pickle.load(f)
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

## save to xlsx file
df = pd.DataFrame (X)
filepath = 'Xvar.xlsx'
df.to_excel(filepath, index=False)
# #############################################################################
# Process Data for Testing Points

X_test = []
y_test = []

with open(testFile, "r") as g:
    reader = csv.reader(g)
    for i, row in enumerate(reader):
        if (i == 0):
            print(row)
        else:
            y_test.append([float(i) for i in row[0:2]])
            X_test.append([float(i) for i in row[2:]])
X_test = np.array(X_test)
y_test = np.array(y_test)
# #############################################################################
# Fit regression model

n_neighbors = 5
for i, weights in enumerate(['distance']):
    #Create kNN Regression Model
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    model = knn.fit(X, y)

    y_ = model.predict(X_test)

    accuracy = []
    for entry in range(len(y_test)):
        dist = np.linalg.norm(y_[entry] - y_test[entry])
        accuracy.append(dist)
    print(accuracy)
    print(np.mean(accuracy))
    #Test Accuracy of Model
