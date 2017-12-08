from math import pow

def rssiToMeters(rssi, txPower):
    if (rssi == 0):
        return -1
    else:
        return pow(10, (txPower - rssi) / 20)       # This formula will change based on the output of the calibration