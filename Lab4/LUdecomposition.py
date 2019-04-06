import numpy as np
class LuDecomposition:
    #A = [[2, -1, -2],
    #     [-4, 6, 3],
    #     [-4, -2, 8]]
    def GaussianElimination(self, A):
        temp = np.zeros((3, 3))
        temp[0]=A[0]
        t=0
        for i in range(t, 10):
            for row in range(len(A)):
                for column in range(len(A[0])):
                    if(row>0):
                        temp[row][column] = A[row][column] - ((A[row][0]/A[0][0])*A[0][column])
        return(temp)



