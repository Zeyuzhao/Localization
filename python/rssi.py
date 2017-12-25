#from bluepy.btle import Scanner, DefaultDelegate
#import numpy as np
import pickle
import os



NUM_SAMPLES = 1
NUM_BEACON = 4
# x and y are based on physical meters
# i and j are based on the number of sampling points
class RssiGrid:
    def __init__(self, numBeacons, l, w, metersDiff):
        self.grid = [[RssiPoint (numBeacons, i, j) for i in range(0, w + metersDiff, metersDiff)] for j in range (0, l + metersDiff, metersDiff)]
        # These numbers are based on the number of sampling points
        self.currentI = 0
        self.currentJ = 0
        self.sizeI = l / metersDiff
        self.sizeJ = w / metersDiff

        self.complete = False
        self.metersDiff = metersDiff
        self.__notSlide = True

    def addRssi(self, entry, val, x = 0, y = 0, useCustom = False):
        if (not useCustom):
            x = self.currentI
            y = self.currentJ
        p = self.grid[x][y]
        p.addRssi(entry, val)
        if p.isFull():
            self.increPoint()

    # Drawing on google doc for moving pattern
    # Check if code is ok
    def increPoint(self):
        i = self.currentI
        j = self.currentJ
        if self.grid[i][j].isFull():
            if (self.isComplete ()):
                self.complete = True
                return None
            elif (self.__notSlide and ((i >= self.sizeI) if (j % 2 == 0) else (i <= 0))):
                self.currentJ += 1
                self.__notSlide = False
            else:
                self.__notSlide = True
                self.currentI += (1) if (j % 2 == 0) else (-1)
            print("Current point is complete. Please move beacon to ({}, {})".format(self.currentI, self.currentJ))

    def isComplete(self):
        i = self.currentI
        j = self.currentJ
        if self.grid[i][j].isFull():
            if self.sizeJ % 2 == 0:
                self.complete = self.currentJ >= self.sizeJ and self.currentI >= self.sizeI
            else:
                self.complete = self.currentJ >= self.sizeJ and self.currentI <= 0
        return self.complete

    def getCurrentTileCoor(self):
        return (self.currentI * self.metersDiff, self.currentJ * self.metersDiff)


class RssiPoint:
    SAMPLES = NUM_SAMPLES

    def __init__(self, numBeacons, x, y):
        self.x = x
        self.y = y
        self.numBeacons = numBeacons
        self.resetEntries()
    def __repr__(self):
        return "<{}>".format(str(self.isFull()))
    def resetEntries(self):
        self.entries = [RssiEntry(i) for i in range (self.numBeacons)]

    def addRssi(self, entry, val):
        if (not self.entries[entry].isFull()):
            self.entries[entry].addRssi (val)

    def setAddress(self, entry, addr):
        self.entries[entry].setAddress(addr)

    def isFull(self):
        full = True
        for i in self.entries:
            if not i.isFull():
                return False
        return True


class RssiEntry:
    SAMPLES = NUM_SAMPLES

    def __init__(self, num):
        self.beaconNum = num
        self.rssiList = []
        self.address = ""
        self.average = 0

    def addRssi(self, val):
        #Fix error here
        self.rssiList.append(val)

    def setAddress(self, address):
        self.address = address

    def computeAvg(self):
        total = 0
        for i in self.rssiList:
            total += i
        self.average = total / len (self.rssiList)
        return self.average

    def isFull(self):
        if len(self.rssiList) >= RssiEntry.SAMPLES:
            self.computeAvg()
            return True
        return False

def addAll(grid):
    for x in range(NUM_SAMPLES):
        for y in range(NUM_BEACON):
            grid.addRssi(y, x)
"""
def print2D(A):
    print(np.array(A))
"""


'''
def calib(x , y):
    return (0, 1, 2, 3)
'''

if __name__ == "__main__":
    with open('grid.pckl', 'rb') as f:
        grid = pickle.load(f)











