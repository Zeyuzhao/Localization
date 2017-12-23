import numpy as np

def trilat(locs, radii):
    A = []
    b = []
    l1 = locs.pop(0)
    r1 = radii.pop(0)
    for loc, radius in zip(locs, radii):
        A.append([2*(loc[0] - l1[0]), 2*(loc[1] - l1[1])])
        b.append(r1 + (loc[0] - l1[0])**2 + (loc[1] - l1[1])**2 - radius)
    matrixA = np.matrix(A)
    matrixB = np.matrix(b).reshape(3,1)
    deltaX = np.matrix(l1).reshape(2,1)
    Ainv = np.linalg.pinv(matrixA)

    X = Ainv * matrixB
    return (X + deltaX)

if __name__ == "__main__":
    #Add test data here.
    print(trilat([[3,3],[13,3],[3,13],[13,13]],[80,80,80,70]))