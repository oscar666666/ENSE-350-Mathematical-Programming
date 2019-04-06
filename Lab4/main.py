from LUdecomposition import *


A = [[2, -1, -2],
     [-4, 6, 3],
     [-4, -2, 8]]

B = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

lud = LuDecomposition()
print(lud.GaussianElimination(A))