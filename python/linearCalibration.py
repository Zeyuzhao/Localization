from bluepy.btle import Scanner, DefaultDelegate

calibMap = {}
NUM_POINTS = 10
for i in range(NUM_POINTS):
    input("Move the pi " + str((i + 1)) + " meters away from the beacon, then hit Enter")
    rssiVals = []
    for j in range(25):
        # Get RSSI value
        # Add RSSI to list
        pass
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