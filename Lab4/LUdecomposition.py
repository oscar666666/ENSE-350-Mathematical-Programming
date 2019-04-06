import numpy as np
class LuDecomposition:
    #A = [[2, -1, -2],
    #     [-4, 6, 3],
    #     [-4, -2, 8]]
    def GaussianElimination(self, A):
        temp = np.zeros((3, 3))
        temp[0]=A[0]
        t=0
        for i in range(len(A)-1):
            for row in range(t, len(A)):
                for column in range(len(A[0])):
                    if(row>t):
                        temp[row][column] = A[row][column] - ((A[row][t]/A[0][0])*A[0][column])
            print(temp)
            t=t+1
        return(temp)



