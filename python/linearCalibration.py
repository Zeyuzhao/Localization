from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

calibMap = {}
NUM_POINTS = 10
for i in range(NUM_POINTS):
    input("Move the pi " + str((i + 1)) + " meters away from the beacon, then hit Enter")
    rssiVals = []
    for j in range(25):
        for dev in devices:
            print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            # for (adtype, desc, value) in dev.getScanData():
            #     print("  %s = %s" % (desc, value))
    sum = 0
    for k in rssiVals:
        sum += k
    average = sum / len(rssiVals)
    calibMap.update({i + 1 : average})

# Write to file to run regression in excel
f = open("calibFile.csv", "w+")
for key in calibMap.keys():
    f.write(str(key) + ",")
f.write("\n")
for val in calibMap.values():
    f.write(str(val) + ",")
f.close()

print("File created")
