from LUdecomposition import *
import numpy as np
#np.seterr(divide='ignore', invalid='ignore')
A = np.array([[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]])

A2 = np.array([[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]])
L = np.array([[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]])
L2 =[[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
lud = LuDecomposition()
print("U", lud.GaussianElimination(A))
print("A", A2)
print("L", lud.FindL(A2, L))

#print("L", np.divide(A2,A))
print("LU",np.dot(L,A))
#lud.GaussianElimination(A)