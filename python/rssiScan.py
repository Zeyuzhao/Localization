from python.rssi import *
from linearCalibration import calib
x_length = 4
y_length = 3
spacing = 1
grid = RssiGrid(NUM_BEACON, x_length, y_length, spacing)

while (not grid.isComplete()):
    rssiTuple = calib()
    for i in range(NUM_BEACON):
        print("Beacon: {}, Value: {}, Coord: ({}, {})".format(i, rssiTuple[i], grid.currentI, grid.currentJ))
        grid.addRssi(i, rssiTuple[i])
    input("Press Enter to Continue...")
    f = open('grid.pckl', 'wb')
    pickle.dump(grid, f)
    f.close()
    #print2D(grid)