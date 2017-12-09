from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            # print("Discovered device", dev.addr)
            pass
        elif isNewData:
            # print("Received new data from", dev.addr)
            pass

scanner = Scanner().withDelegate(ScanDelegate())

def getRSSIVals():
    rssiVals = []
    devices = scanner.scan(3.0)
    for dev in devices:
        rssiVals.append((dev.addr, dev.rssi))
    return rssiVals

def getBeaconToVal(lookupTableFile):
    lookupTable = {}
    rssiInOrder = []
    f = open(lookupTableFile, "r")
    for line in f.readlines():
        lineArray = line.split(",")
        lookupTable.update({lineArray[1] : lineArray[0]})
    for i in getRSSIVals():
        if lookupTable.keys().__contains__(i[0]):
            rssiInOrder.append((lookupTable.get(i[0]), i[1]))
    bubbleSort(rssiInOrder)
    return rssiInOrder

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][0]>alist[i+1][0]:
                temp = alist[i][0]
                alist[i][0] = alist[i+1][0]
                alist[i+1][0] = temp