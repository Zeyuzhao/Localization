from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            # print("Discovered device", dev.addr)
            ...
        elif isNewData:
            # print("Received new data from", dev.addr)
            ...

scanner = Scanner().withDelegate(ScanDelegate())

VAL_NUM = 25
calibMap = {}
NUM_POINTS = 5
points = [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (3,1), (2,1), (1,1), (0,1), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3),
          (3,3), (2,3), (1,3), (0,3)]

pointsIt = iter(points)

f = open("calibFile.csv", "w+")

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
            elif dev.addr == "b8:27:eb:ba:6a:eb":
                rssiVals2.append(dev.rssi)
                print("RSSI = %ddB" % (dev.rssi))
            elif dev.addr == "b8:27:eb:28:b1:fe":
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
    allAverage = (average1, average2, average3, average4)
    f.write(str(allAverage) + ",")
    f.close()
    return allAverage

# Write to file to run regression in excel
# for key in calibMap.keys():
#     f.write(str(key) + ",")
# f.write("\n")
# for val in calibMap.values():
#     f.write(str(val) + ",")
# f.close()
#
# print("File created")