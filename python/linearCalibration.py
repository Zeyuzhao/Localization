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

VAL_NUM = 25
calibMap = {}
NUM_POINTS = 5

def calib():
    rssiVals1 = []
    rssiVals2 = []
    rssiVals3 = []
    rssiVals4 = []
    for j in range(VAL_NUM):
        devices = scanner.scan(3.0)
        for dev in devices:
            if dev.addr == "b8:27:eb:f4:45:e8":
                rssiVals1.append(dev.rssi)
                print("RSSI = %ddB" % (dev.rssi))
            elif dev.addr == "b8:27:eb:45:95:14":
                rssiVals2.append(dev.rssi)
                print("RSSI = %ddB" % (dev.rssi))
            elif dev.addr == "b8:27:eb:d7:4e:01":
                rssiVals3.append(dev.rssi)
                print("RSSI = %ddB" % (dev.rssi))
            elif dev.addr == "b8:27:eb:c9:80:30":
                rssiVals4.append(dev.rssi)
                print("RSSI = %ddB" % (dev.rssi))
    rssiVals1.sort()
    rssiVals2.sort()
    rssiVals3.sort()
    rssiVals4.sort()
    rssiVals1 = rssiVals1[int(VAL_NUM * .1):VAL_NUM - int(VAL_NUM * .1)]
    rssiVals2 = rssiVals2[int(VAL_NUM * .1):VAL_NUM - int(VAL_NUM * .1)]
    rssiVals3 = rssiVals3[int(VAL_NUM * .1):VAL_NUM - int(VAL_NUM * .1)]
    rssiVals4 = rssiVals4[int(VAL_NUM * .1):VAL_NUM - int(VAL_NUM * .1)]
    sum = 0
    for k in rssiVals1:
        sum += k
    average1 = sum / len(rssiVals1)
    sum = 0
    for k in rssiVals2:
        sum += k
    average2 = sum / len(rssiVals2)
    sum = 0
    for k in rssiVals3:
        sum += k
    average3 = sum / len(rssiVals3)
    sum = 0
    for k in rssiVals4:
        sum += k
    average4 = sum / len(rssiVals4)
    sum = 0
    allAverage = (average1, average2, average3, average4)
    # calibMap.update({i + 1 : allAverage})
    return allAverage

# Write to file to run regression in excel
f = open("calibFile.csv", "w+")
for key in calibMap.keys():
    f.write(str(key) + ",")
f.write("\n")
for val in calibMap.values():
    f.write(str(val) + ",")
f.close()

print("File created")