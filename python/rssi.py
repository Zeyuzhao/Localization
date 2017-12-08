from bluepy.btle import Scanner, DefaultDelegate
import numpy as np

NUM_SAMPLES = 10


# x and y are based on physical meters
# i and j are based on the number of sampling points
class RssiGrid:
    def __init__(self, numBeacons, l, w, beaconPerM):
        self.grid = [[RssiPoint (numBeacons, i, j) for i in range (0, l, beaconPerM)] for j in range (0, w, beaconPerM)]
        # These numbers are based on the number of sampling points
        self.currentI = 0
        self.currentJ = 0
        self.sizeI = l * beaconPerM
        self.sizeJ = w * beaconPerM

        self.complete = False
        self.beaconPerM = beaconPerM
        self.__notSlide = True

    def addRssi(self, x, y, entry, val):
        p = self.grid[x][y]
        p.addRssi (entry, val)

    def addRssi(self, entry, val):
        self.addRssi (self.currentI, self.currentJ, entry, val)

    # Drawing on google doc for moving pattern
    # Check if code is ok
    def increPoint(self):
        i = self.currentI
        j = self.currentJ
        if self.grid[i][j].isFull ():
            if (self.__isComplete ()):
                self.complete = True
            elif (self.__notSlide and ((i >= self.sizeI) if (j % 2 == 0) else (i <= 0))):
                self.currentJ += 1
                self.__notSlide = False
            else:
                self.__notSlide = True
                self.currentI += (1) if (j % 2 == 0) else (-1)

    def __isComplete(self):
        if self.sizeJ % 2 == 0:
            self.complete = self.currentJ >= self.sizeJ and self.currentI >= self.sizeI
        else:
            self.complete = self.currentJ <= 0 and self.currentI <= 0
        return self.complete

    def getCurrentTileCoor(self):
        return (self.currentI / self.beaconPerM, self.currentJ / self.beaconPerM)


class RssiPoint:
    SAMPLES = NUM_SAMPLES

    def __init__(self, numBeacons, x, y):
        self.x = x
        self.y = y
        self.numBeacons = numBeacons
        self.resetEntries ()
        pass

    def resetEntries(self):
        self.entries = [RssiEntry (i) for i in range (self.numBeacons)]

    def addRssi(self, entry, val):
        if (not self.entries[entry].isFull ()):
            self.entries[entry].addRssi (val)

    def setAddress(self, entry, addr):
        self.entries[entry].setAddress (addr)

    def isFull(self):
        full = True
        for i in self.entries:
            if not i.isFull ():
                return False
        return True


class RssiEntry:
    SAMPLES = NUM_SAMPLES

    def __init__(self, num):
        self.beaconNum = num
        self.rssiList = []
        self.address = ""
        self.average = -1

    def addRssi(self, val):
        self.rssiList.append (val)

    def setAddress(self, address):
        self.address = address

    def computeAvg(self):
        total = 0
        for i in self.rssiList:
            total += i
        return total / len (self.rssiList)

    def isFull(self):
        return self.rssiList > RssiEntry.SAMPLES

