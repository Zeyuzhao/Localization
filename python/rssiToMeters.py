from math import *

def rssiToMeters(rssi):
    if (rssi == 0):
        return -1
    else:
        return (1.04224 * pow(10, -13)) * pow((rssi * -1), 7.73395)

print(rssiToMeters(-48.68))