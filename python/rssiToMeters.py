from math import *

def rssiToMeters(rssi):
    if (rssi == 0):
        return -1
    else:
        return pow(0.966559, rssi) -3.4515

print(rssiToMeters(-48.68))
