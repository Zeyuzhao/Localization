from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            pass
            #print ("Discovered device " + dev.addr)
        elif isNewData:
            pass
            #print("Received new data from " + dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
for x in range(10):
    devices = scanner.scan(1.0)
    for dev in devices:
        print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adType, desc, value) in dev.getScanData():
            print("  %s = %s" % (desc, value))
            