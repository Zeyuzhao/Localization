import numpy as np

def trilat(locs, radii):
    A = []
    b = []
    l1 = locs.pop(0)
    r1 = radii.pop(0)
    for dist, radius in zip(locs, radii):
        A.append([dist[0] - l1[0], dist[1] - l1[1]])
        b.append(r1 + (l1[0] - dist[0])**2 + (l1[1] - dist[1])**2 - radius)
    matrixA = np.matrix(A)
    matrixB = np.matrix(b).reshape(3,1)
    deltaX = np.matrix(l1).reshape(2,1)
    Ainv = np.linalg.pinv(matrixA)

    X = Ainv * matrixB
    return (X + deltaX)

print(trilat([[0,0],[10,0],[10,10],[10,10]],[58,84,50,25]))