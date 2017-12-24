from rssiToMeters import rssiToMeters as rtm
def rssiListToMeters(vals):
    meterVals = []
    for val in vals:
        newVal = []
        for v in val:
            newVal.append(rtm(v))
        meterVals.append(newVal)
    return meterVals